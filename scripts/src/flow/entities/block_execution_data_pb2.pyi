from flow.entities import event_pb2 as _event_pb2
from flow.entities import transaction_pb2 as _transaction_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockExecutionData(_message.Message):
    __slots__ = ["block_id", "chunk_execution_data"]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_EXECUTION_DATA_FIELD_NUMBER: _ClassVar[int]
    block_id: bytes
    chunk_execution_data: _containers.RepeatedCompositeFieldContainer[ChunkExecutionData]
    def __init__(self, block_id: _Optional[bytes] = ..., chunk_execution_data: _Optional[_Iterable[_Union[ChunkExecutionData, _Mapping]]] = ...) -> None: ...

class ChunkExecutionData(_message.Message):
    __slots__ = ["collection", "events", "trieUpdate"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    TRIEUPDATE_FIELD_NUMBER: _ClassVar[int]
    collection: ExecutionDataCollection
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
    trieUpdate: TrieUpdate
    def __init__(self, collection: _Optional[_Union[ExecutionDataCollection, _Mapping]] = ..., events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]] = ..., trieUpdate: _Optional[_Union[TrieUpdate, _Mapping]] = ...) -> None: ...

class ExecutionDataCollection(_message.Message):
    __slots__ = ["transactions"]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[_transaction_pb2.Transaction]
    def __init__(self, transactions: _Optional[_Iterable[_Union[_transaction_pb2.Transaction, _Mapping]]] = ...) -> None: ...

class TrieUpdate(_message.Message):
    __slots__ = ["root_hash", "paths", "payloads"]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    root_hash: bytes
    paths: _containers.RepeatedScalarFieldContainer[bytes]
    payloads: _containers.RepeatedCompositeFieldContainer[Payload]
    def __init__(self, root_hash: _Optional[bytes] = ..., paths: _Optional[_Iterable[bytes]] = ..., payloads: _Optional[_Iterable[_Union[Payload, _Mapping]]] = ...) -> None: ...

class Payload(_message.Message):
    __slots__ = ["keyPart", "value"]
    KEYPART_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    keyPart: _containers.RepeatedCompositeFieldContainer[KeyPart]
    value: bytes
    def __init__(self, keyPart: _Optional[_Iterable[_Union[KeyPart, _Mapping]]] = ..., value: _Optional[bytes] = ...) -> None: ...

class KeyPart(_message.Message):
    __slots__ = ["type", "value"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: int
    value: bytes
    def __init__(self, type: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
