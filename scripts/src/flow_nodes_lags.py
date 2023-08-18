import asyncio
import itertools
import os
import logging
import time
from dataclasses import dataclass
from typing import List

import grpc
import numpy as np
from grpc.aio import AioRpcError

from flow.access import access_pb2_grpc
from flow.access.access_pb2 import GetLatestBlockRequest, BlockResponse, GetBlockByHeightRequest, GetBlockByIDRequest, \
    GetCollectionByIDRequest, CollectionResponse, GetTransactionRequest, GetTransactionsByBlockIDRequest, \
    TransactionResultsResponse
from flow.access.access_pb2_grpc import AccessAPI, AccessAPIStub
from flow.entities.block_pb2 import Block, BLOCK_FINALIZED, BLOCK_SEALED, BlockStatus
from flow.entities.event_pb2 import Event

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s")
log = logging.getLogger("my-logger")

onflow_access_url = "access.mainnet.nodes.onflow.org:9000"
quicknode_access_url = os.environ["QUICKNODE_ACCESS_URL"]


@dataclass
class BlockWithTransactions:
    block: Block
    block_status: BlockStatus
    transactions: List[Event]


async def transaction_by_id(api: AccessAPIStub, transaction_id) -> List[Event]:
    resp = await api.GetTransactionResult(GetTransactionRequest(id=transaction_id))
    return resp.events


async def transactions_by_collection_id(api: AccessAPIStub, collection_id):
    collection: CollectionResponse = await api.GetCollectionByID(GetCollectionByIDRequest(id=collection_id))
    transactions = await asyncio.gather(*[transaction_by_id(api, transaction_id)
                                          for transaction_id in collection.collection.transaction_ids])
    return itertools.chain(*transactions)


async def get_transactions_by_block_id(api: AccessAPIStub, block_id):
    resp: TransactionResultsResponse = await api.GetTransactionResultsByBlockID(
        GetTransactionsByBlockIDRequest(block_id=block_id))
    return [event for res in resp.transaction_results for event in res.events]


async def _get_block(api, handler, undoc=False):
    try:
        resp: BlockResponse = await handler()
        if resp is None or resp.block_status != BLOCK_SEALED:
            return None
        if undoc:
            transactions = await get_transactions_by_block_id(api, resp.block.id)
        else:
            collection_ids = map(lambda x: x.collection_id, resp.block.collection_guarantees)
            transactions = await asyncio.gather(*[transactions_by_collection_id(api, collection_id)
                                                  for collection_id in collection_ids])
            transactions = list(itertools.chain(*transactions))
        return BlockWithTransactions(resp.block, resp.block_status, transactions)
    except AioRpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            return None
        else:
            raise e


async def get_block_by_id(api: AccessAPIStub, id, undoc=False):
    async def handler():
        return await api.GetBlockByID(GetBlockByIDRequest(id=id))

    return await _get_block(api, handler, undoc)


async def get_block_by_height(api, height, undoc=False):
    async def handler():
        return await api.GetBlockByHeight(GetBlockByHeightRequest(height=height))

    return await _get_block(api, handler, undoc)


async def get_latest_block(api, undoc=False):
    async def handler():
        return await api.GetLatestBlock(GetLatestBlockRequest(is_sealed=True))

    return await _get_block(api, handler, undoc)


async def wait_until_block(api, height, undoc=False):
    start = time.perf_counter()
    while True:
        resp: BlockWithTransactions = await get_block_by_height(api, height, undoc)
        if resp is not None:
            return resp, 1000 * (time.perf_counter() - start)


def print_stats(native_ms, quicknode_ms):
    timings = zip(native_ms, quicknode_ms)
    diffs = list(map(lambda xy: xy[0] - xy[1], timings))
    print(
        f"timings diffs (native-quicknode): min={np.min(diffs):.2f}, max={np.max(diffs):.2f}, mean={np.mean(diffs):.2f}")
    print(f"native timings: min={np.min(native_ms):.2f}, "
          f"max={np.max(native_ms):.2f}, "
          f"mean={np.mean(native_ms):.2f}")
    print(f"quicknode timings: min={np.min(quicknode_ms):.2f}, "
          f"max={np.max(quicknode_ms):.2f}, "
          f"mean={np.mean(quicknode_ms):.2f}")


async def compare_nodes_parallel():
    native_api = access_pb2_grpc.AccessAPIStub(grpc.aio.insecure_channel(onflow_access_url))
    quicknode_api = access_pb2_grpc.AccessAPIStub(grpc.aio.insecure_channel(quicknode_access_url))
    last_height = (await native_api.GetLatestBlock(GetLatestBlockRequest(is_sealed=True,
                                                                         full_block_response=True))).block.height
    native_ms = []
    quicknode_ms = []
    while True:
        t1 = asyncio.create_task(wait_until_block(native_api, last_height + 1, undoc=True))
        t2 = asyncio.create_task(wait_until_block(quicknode_api, last_height + 1, undoc=True))
        native_block, native_elapsed = await t1
        quiknode_block, quicknode_elapsed = await t2
        if native_block == quiknode_block:
            native_ms.append(native_elapsed)
            quicknode_ms.append(quicknode_elapsed)
            print(f"{last_height}: "
                  f"native={native_elapsed:.2f}, quicknode={quicknode_elapsed:.2f} "
                  f"diff={native_elapsed - quicknode_elapsed :.2f}ms")
            last_height += 1
            if last_height % 1000 == 0:
                print_stats(native_ms, quicknode_ms)
                native_ms = []
                quicknode_ms = []


async def compare_nodes(poller_node_url, sync_node_url, poller_node_undoc, sync_node_undoc):
    poller_node_api = access_pb2_grpc.AccessAPIStub(grpc.aio.insecure_channel(poller_node_url))
    sync_node_api = access_pb2_grpc.AccessAPIStub(grpc.aio.insecure_channel(sync_node_url))
    event = asyncio.Event()
    queue = []
    mismatch_txs = set({})
    sync_time = []

    async def sync(poller_block):
        synced = False
        start = None
        while not synced:
            block = await get_block_by_id(sync_node_api, poller_block.block.id, undoc=sync_node_undoc)
            if block is None:
                log.warning(f"sync: missing block {poller_block.block.height}")
                if start is None:
                    start = time.perf_counter()
            elif poller_block.transactions != block.transactions:
                log.warning(f"sync: txs don't match for {poller_block.block.height}, "
                            f"poller has more transactions: {len(poller_block.transactions) > len(block.transactions)}, "
                            f"blocks statuses match: {poller_block.block_status == block.block_status}")

                mismatch_txs.add(poller_block.block.height)
                if len(poller_block.transactions) < len(block.transactions):
                    # infinite loop
                    return
                if start is None:
                    start = time.perf_counter()
            else:
                synced = True
                if start is not None:
                    elapsed = 1000 * (time.perf_counter() - start)
                    sync_time.append(elapsed)
                    log.info(f"sync: synced block {block.block.height} for {elapsed :.2f}ms")
                    start = None

    async def poller():
        init_block_height = (await get_latest_block(poller_node_api)).block.height
        last_block_height = init_block_height
        while last_block_height - init_block_height < 1000:
            latest_block = await get_block_by_height(poller_node_api, last_block_height + 1, undoc=poller_node_undoc)
            if latest_block is None:
                continue
            log.info(f"poller: new block {latest_block.block.height}")
            queue.append(asyncio.create_task(sync(latest_block)))
            last_block_height += 1
            event.set()
        log.info("poller: done")

    async def cleanup():
        while True:
            if len(queue) > 0:
                task = queue.pop(0)
                await task
                del task
                event.clear()
            else:
                log.info("cleanup: sync queue done")
                await event.wait()

    async def stats():
        while True:
            if len(sync_time) > 0:
                log.info(f"stats: min={np.min(sync_time):.2f}, max={np.max(sync_time):.2f}, "
                         f"mean={np.mean(sync_time):.2f}, size={len(sync_time)}")
                log.info(f"stats: mismatch_txs={len(mismatch_txs)}")
            await asyncio.sleep(60)

    await asyncio.gather(poller(), cleanup(), stats())


if __name__ == '__main__':
    # using base node in poller (1st argument) check that blocks in sync in target node (2nd argument)
    # 1. Check that nodes are in sync with themselves
    #
    # missing blocks delay
    # stats: min=308.41, max=3094.16, mean=720.86, size=95/1000
    # stats: mismatch_txs=215/1000
    # 1) test writes "poller has more transactions: False, blocks statuses match: True" - it means that second call for
    # that sealed block returned more transactions. We don't reevaluate poller txs, so in this test it will never be synced,
    # so we end syncing attempts here
    # 2) test writes "poller has more transactions: True, blocks statuses match: True" - it means that poller has more
    # transactions, first sync call returned block with less transactions, but second (or one of the following calls)
    # returned block with same txs like poller and at this moment block considered as synced
    # Keep in mind that in all calls this test demand that all block calls ask for sealed block and has extra check
    # for sealed block
    # poller_node_undoc=False, sync_node_undoc=True - effectively the same
    # poller_node_undoc=True, sync_node_undoc=False - has mismatch txs but always with "poller has more transactions: True",
    # so at second call (or at one of the following calls) it synced
    # asyncio.run(compare_nodes(poller_node_url=quicknode_access_url,
    #                           sync_node_url=quicknode_access_url,
    #                           poller_node_undoc=False,
    #                           sync_node_undoc=False))
    #
    # has missing blocks delay, no mismatch txs
    # stats: min=217.26, max=1624.48, mean=419.81, size=102/1000
    # asyncio.run(compare_nodes(poller_node_url=quicknode_access_url,
    #                           sync_node_url=quicknode_access_url,
    #                           poller_node_undoc=True,
    #                           sync_node_undoc=True))
    #
    # no missing blocks, no mismatch txs
    # asyncio.run(compare_nodes(poller_node_url=onflow_access_url,
    #                           sync_node_url=onflow_access_url,
    #                           poller_node_undoc=True|False,
    #                           sync_node_undoc=True|False))
    #
    # 2. Poller: onflow, sync: quicknode
    # delayed block stat:
    # stats: min=316.59, max=3748.11, mean=926.73, size=107/1000
    # stats: mismatch_txs=75/1000
    # In this test all mismatch txs have "poller has more transactions: True, blocks statuses match: True", in other words
    # poller always provide more txs than sync node, but after several calls sync node returns same txs
    # asyncio.run(compare_nodes(poller_node_url=onflow_access_url,
    #                           sync_node_url=quicknode_access_url,
    #                           poller_node_undoc=True,
    #                           sync_node_undoc=False))
    #
    # delayed block stat:
    # stats: min=217.36, max=1176.78, mean=371.02, size=64/1000
    # stats: mismatch_txs=0
    # asyncio.run(compare_nodes(poller_node_url=onflow_access_url,
    #                           sync_node_url=quicknode_access_url,
    #                           poller_node_undoc=True,
    #                           sync_node_undoc=True))
    #
    # 3. Poller: quicknode, sync: flow
    #
    # delayed block stat:
    # stats: min=352.55, max=10991.97, mean=2730.01, size=29/1000
    # stats: mismatch_txs=137/1000
    # asyncio.run(compare_nodes(poller_node_url=quicknode_access_url,
    #                           sync_node_url=onflow_access_url,
    #                           poller_node_undoc=False,
    #                           sync_node_undoc=False))
    #
    # delayed block stat:
    # stats: min=230.87, max=15838.18, mean=2535.99, size=94/1000
    # stats: mismatch_txs=0
    # asyncio.run(compare_nodes(poller_node_url=quicknode_access_url,
    #                           sync_node_url=onflow_access_url,
    #                           poller_node_undoc=True,
    #                           sync_node_undoc=True))
    #
    # delayed block stat:
    # stats:
    # stats:
    asyncio.run(compare_nodes(poller_node_url=quicknode_access_url,
                              sync_node_url=onflow_access_url,
                              poller_node_undoc=True,
                              sync_node_undoc=False))
    #
    # delayed block stat:
    # stats: min=348.14, max=10246.50, mean=2517.67, size=75
    # stats: mismatch_txs=0
    asyncio.run(compare_nodes(poller_node_url=quicknode_access_url,
                              sync_node_url=onflow_access_url,
                              poller_node_undoc=False,
                              sync_node_undoc=True))
    #
    # delayed block stat:
    # stats: min=345.47, max=23014.31, mean=4855.89, size=149
    # stats:  mismatch_txs=0
    asyncio.run(compare_nodes(poller_node_url=quicknode_access_url,
                              sync_node_url=onflow_access_url,
                              poller_node_undoc=True,
                              sync_node_undoc=False))
