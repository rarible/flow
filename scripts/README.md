## Install
1. Install python3
2. Create venv ```python3 -m venv venv --clear```
3. Activate venv ```source venv/bin/activate```
3. Using python3 from venv, install requirements ```pip3 install -r requirements.txt```
4. If you need to regenerate grpc sources, call ```python3 -m grpc_tools.protoc -Iprotobuf/ --python_out=scripts/src --pyi_out=scripts/src --grpc_python_out=scripts/src protobuf/flow/access/access.proto protobuf/flow/entities/*```

## Launch
Uncomment interested block in main section and run script ```python3 scripts/src/flow_nodes_lags.py```

## Source code
Source code has 2 entry points: ```compare_nodes``` and ```compare_nodes_parallel```
```compare_nodes_parallel``` report latency for next block after latest (latest.height + 1) and skip block if txs of this block differs for different nodes.
```compare_nodes``` launches two async tasks: poller and sync. Poller asks node for new block and put in the sync queue. Sync queue ask its node when new block arrives in queue and compare with block provided by poller.
For each block we also request block transactions. If block not found or any of its collection guarantee or txs of any collection guarantee is not found, we assume that block is not synced and generally return that block not found.
We can request block transactions in two ways: using undocumented methods (undoc=True), or documented only (undoc=False)
undoc=True: request block (by height, by id, or just latest), for each block's collection guarantee request collection (by id), and finally for each tx in collection, request transactioon (by id)
undoc=False: use method GetTransactionResultsByBlockID
Please keep in mind, that latency comparision when one task uses undoc=True and another task uses undoc=False is not eligible because in case undoc=False we spent a lot more time for network jumps