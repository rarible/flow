## Install
1. Install python3
2. Create venv ```python3 -m venv venv --clear```
3. Activate venv ```source venv/bin/activate```
3. Using python3 from venv, install requirements ```pip3 install -r requirements.txt```
4. If you need to regenerate grpc sources, call ```python3 -m grpc_tools.protoc -Iprotobuf/ --python_out=scripts/src --pyi_out=scripts/src --grpc_python_out=scripts/src protobuf/flow/access/access.proto protobuf/flow/entities/*```

## Launch
Uncomment interested block in main section and run script ```python3 scripts/src/flow_nodes_lags.py```