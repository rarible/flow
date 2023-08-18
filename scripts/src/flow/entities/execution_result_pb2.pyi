from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionResult(_message.Message):
    __slots__ = ["previous_result_id", "block_id", "chunks", "service_events", "execution_data_id"]
    PREVIOUS_RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_EVENTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_DATA_ID_FIELD_NUMBER: _ClassVar[int]
    previous_result_id: bytes
    block_id: bytes
    chunks: _containers.RepeatedCompositeFieldContainer[Chunk]
    service_events: _containers.RepeatedCompositeFieldContainer[ServiceEvent]
    execution_data_id: bytes
    def __init__(self, previous_result_id: _Optional[bytes] = ..., block_id: _Optional[bytes] = ..., chunks: _Optional[_Iterable[_Union[Chunk, _Mapping]]] = ..., service_events: _Optional[_Iterable[_Union[ServiceEvent, _Mapping]]] = ..., execution_data_id: _Optional[bytes] = ...) -> None: ...

class Chunk(_message.Message):
    __slots__ = ["CollectionIndex", "start_state", "event_collection", "block_id", "total_computation_used", "number_of_transactions", "index", "end_state", "execution_data_id", "state_delta_commitment"]
    COLLECTIONINDEX_FIELD_NUMBER: _ClassVar[int]
    START_STATE_FIELD_NUMBER: _ClassVar[int]
    EVENT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COMPUTATION_USED_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    END_STATE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_DATA_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_DELTA_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    CollectionIndex: int
    start_state: bytes
    event_collection: bytes
    block_id: bytes
    total_computation_used: int
    number_of_transactions: int
    index: int
    end_state: bytes
    execution_data_id: bytes
    state_delta_commitment: bytes
    def __init__(self, CollectionIndex: _Optional[int] = ..., start_state: _Optional[bytes] = ..., event_collection: _Optional[bytes] = ..., block_id: _Optional[bytes] = ..., total_computation_used: _Optional[int] = ..., number_of_transactions: _Optional[int] = ..., index: _Optional[int] = ..., end_state: _Optional[bytes] = ..., execution_data_id: _Optional[bytes] = ..., state_delta_commitment: _Optional[bytes] = ...) -> None: ...

class ServiceEvent(_message.Message):
    __slots__ = ["type", "payload"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    type: str
    payload: bytes
    def __init__(self, type: _Optional[str] = ..., payload: _Optional[bytes] = ...) -> None: ...

class ExecutionReceiptMeta(_message.Message):
    __slots__ = ["executor_id", "result_id", "spocks", "executor_signature"]
    EXECUTOR_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    SPOCKS_FIELD_NUMBER: _ClassVar[int]
    EXECUTOR_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    executor_id: bytes
    result_id: bytes
    spocks: _containers.RepeatedScalarFieldContainer[bytes]
    executor_signature: bytes
    def __init__(self, executor_id: _Optional[bytes] = ..., result_id: _Optional[bytes] = ..., spocks: _Optional[_Iterable[bytes]] = ..., executor_signature: _Optional[bytes] = ...) -> None: ...
