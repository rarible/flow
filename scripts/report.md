### Test strategy:

1. Sanity check. For each node check that sync return same result as poller request. In this case poller and sync tasks
   relate to the same node
   We also expect that transactions for sealed block is the same for poller and sync tasks
2. Compare nodes. For each case we also test all combinations undoc=False|True
   a) poller=onflow, sync=quicknode
   b) poller=quicknode, sync=onflow

### Results

1. Quicknode sanity check

```
asyncio.run(compare_nodes(poller_node_url=quicknode_access_url,
                          sync_node_url=quicknode_access_url,
                          poller_node_undoc=False,
                          sync_node_undoc=False))
```

Report:
stats: min=308.41, max=3094.16, mean=720.86, size=95/1000
stats: mismatch_txs=215/1000
Quicknode has a lot of missing transactions

1) test logs "poller has more transactions: False, blocks statuses match: True" - it means that second call for
   that sealed block returned more transactions. <br> We don't reevaluate poller txs, so in this test it will never be
   synced,
   so we end syncing attempts here
2) test logs "poller has more transactions: True, blocks statuses match: True" - it means that poller has more
   transactions, first sync call returned block with less transactions, but second (or one of the following calls)
   returned block with same txs like poller and at this moment block considered as synced
   <br> Keep in mind that in all calls this test demand that all block calls ask for sealed block and has extra check
   for sealed block

poller_node_undoc=False, sync_node_undoc=True - effectively the same
<br>poller_node_undoc=True, sync_node_undoc=False - has mismatch txs but always with "poller has more transactions:
<br>poller_node_undoc=True, sync_node_undoc=True - has delay, but no mismatch txs
```stats: min=217.26, max=1624.48, mean=419.81, size=102/1000```

2. Onflow sanity check

```
asyncio.run(compare_nodes(poller_node_url=onflow_access_url,
                          sync_node_url=onflow_access_url,
                          poller_node_undoc=True|False,
                          sync_node_undoc=True|False))
```

no missing blocks, no mismatch txs

> **_NOTE:_** From now on, let's assume that onflow has no inconsistency in any methods (undoc=False|True), but
> quicknode may add
(or remove) transactions after block is sealed using undoc=False and don't add (or remove) transactions using undoc=True

3. Compare nodes with each other. poller=onflow, sync=quicknode

run:<br>

```
asyncio.run(compare_nodes(poller_node_url=onflow_access_url,
                          sync_node_url=quicknode_access_url,
                          poller_node_undoc=False,
                          sync_node_undoc=False))
```

results:<br>
&nbsp;&nbsp;stats: min=368.02, max=4451.49, mean=1075.98, size=112/1000<br>
&nbsp;&nbsp;stats: mismatch_txs=81/1000<br>
&nbsp;&nbsp;poller_node_undoc=True - effectively the same mismatch txs

run:<br>

```
asyncio.run(compare_nodes(poller_node_url=onflow_access_url,
                          sync_node_url=quicknode_access_url,
                          poller_node_undoc=True,
                          sync_node_undoc=True))
``` 

results:<br>
&nbsp;&nbsp;stats: min=247.23, max=2089.68, mean=624.48, size=66/1000<br>
&nbsp;&nbsp;stats: mismatch_txs=0/1000<br>
&nbsp;&nbsp;poller_node_undoc=False - effectively the same mismatch txs

4. Compare nodes with each other. poller=quicknode, sync=onflow

run:<br>

```
asyncio.run(compare_nodes(poller_node_url=quicknode_access_url,
                          sync_node_url=onflow_access_url,
                          poller_node_undoc=False,
                          sync_node_undoc=False))
``` 

results:<br>
&nbsp;&nbsp;stats: min=384.21, max=7877.30, mean=2596.40, size=34/1000<br>
&nbsp;&nbsp;stats: mismatch_txs=97/1000<br>
&nbsp;&nbsp;sync_node_undoc=True - effectively the same mismatch txs

run:<br>

```
asyncio.run(compare_nodes(poller_node_url=quicknode_access_url,
                          sync_node_url=onflow_access_url,
                          poller_node_undoc=True,
                          sync_node_undoc=True))
``` 

results:<br>
&nbsp;&nbsp;stats: min=225.22, max=6969.85, mean=1922.84, size=53/1000<br>
&nbsp;&nbsp;stats: mismatch_txs=0<br>
&nbsp;&nbsp;sync_node_undoc=False - effectively the same mismatch txs

### Results

1. Seems like quicknode have some inconsistency in transactions in sealed block. Mostly it may got around using
   undocumented method ```GetTransactionResultsByBlockID```. Interesting that native node doesn't have such behaviour.
   Maybe this doesn't happen on blocks with finalized seal, but there is no api for requesting only such blocks.
2. Both nodes have blocks delays comparing with each other around 5-10%