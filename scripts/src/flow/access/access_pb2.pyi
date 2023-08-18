from flow.entities import account_pb2 as _account_pb2
from flow.entities import block_header_pb2 as _block_header_pb2
from flow.entities import block_pb2 as _block_pb2
from flow.entities import collection_pb2 as _collection_pb2
from flow.entities import event_pb2 as _event_pb2
from flow.entities import execution_result_pb2 as _execution_result_pb2
from flow.entities import metadata_pb2 as _metadata_pb2
from flow.entities import node_version_info_pb2 as _node_version_info_pb2
from flow.entities import transaction_pb2 as _transaction_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PingRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetNodeVersionInfoRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetNodeVersionInfoResponse(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _node_version_info_pb2.NodeVersionInfo
    def __init__(self, info: _Optional[_Union[_node_version_info_pb2.NodeVersionInfo, _Mapping]] = ...) -> None: ...

class GetLatestBlockHeaderRequest(_message.Message):
    __slots__ = ["is_sealed"]
    IS_SEALED_FIELD_NUMBER: _ClassVar[int]
    is_sealed: bool
    def __init__(self, is_sealed: bool = ...) -> None: ...

class GetBlockHeaderByIDRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetBlockHeaderByHeightRequest(_message.Message):
    __slots__ = ["height"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    height: int
    def __init__(self, height: _Optional[int] = ...) -> None: ...

class BlockHeaderResponse(_message.Message):
    __slots__ = ["block", "block_status", "metadata"]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    BLOCK_STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    block: _block_header_pb2.BlockHeader
    block_status: _block_pb2.BlockStatus
    metadata: _metadata_pb2.Metadata
    def __init__(self, block: _Optional[_Union[_block_header_pb2.BlockHeader, _Mapping]] = ..., block_status: _Optional[_Union[_block_pb2.BlockStatus, str]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class GetLatestBlockRequest(_message.Message):
    __slots__ = ["is_sealed", "full_block_response"]
    IS_SEALED_FIELD_NUMBER: _ClassVar[int]
    FULL_BLOCK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    is_sealed: bool
    full_block_response: bool
    def __init__(self, is_sealed: bool = ..., full_block_response: bool = ...) -> None: ...

class GetBlockByIDRequest(_message.Message):
    __slots__ = ["id", "full_block_response"]
    ID_FIELD_NUMBER: _ClassVar[int]
    FULL_BLOCK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    full_block_response: bool
    def __init__(self, id: _Optional[bytes] = ..., full_block_response: bool = ...) -> None: ...

class GetBlockByHeightRequest(_message.Message):
    __slots__ = ["height", "full_block_response"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FULL_BLOCK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    height: int
    full_block_response: bool
    def __init__(self, height: _Optional[int] = ..., full_block_response: bool = ...) -> None: ...

class BlockResponse(_message.Message):
    __slots__ = ["block", "block_status", "metadata"]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    BLOCK_STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    block: _block_pb2.Block
    block_status: _block_pb2.BlockStatus
    metadata: _metadata_pb2.Metadata
    def __init__(self, block: _Optional[_Union[_block_pb2.Block, _Mapping]] = ..., block_status: _Optional[_Union[_block_pb2.BlockStatus, str]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class GetCollectionByIDRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class CollectionResponse(_message.Message):
    __slots__ = ["collection", "metadata"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    collection: _collection_pb2.Collection
    metadata: _metadata_pb2.Metadata
    def __init__(self, collection: _Optional[_Union[_collection_pb2.Collection, _Mapping]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class SendTransactionRequest(_message.Message):
    __slots__ = ["transaction"]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _transaction_pb2.Transaction
    def __init__(self, transaction: _Optional[_Union[_transaction_pb2.Transaction, _Mapping]] = ...) -> None: ...

class SendTransactionResponse(_message.Message):
    __slots__ = ["id", "metadata"]
    ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    metadata: _metadata_pb2.Metadata
    def __init__(self, id: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class GetTransactionRequest(_message.Message):
    __slots__ = ["id", "block_id", "collection_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    block_id: bytes
    collection_id: bytes
    def __init__(self, id: _Optional[bytes] = ..., block_id: _Optional[bytes] = ..., collection_id: _Optional[bytes] = ...) -> None: ...

class GetTransactionByIndexRequest(_message.Message):
    __slots__ = ["block_id", "index"]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    block_id: bytes
    index: int
    def __init__(self, block_id: _Optional[bytes] = ..., index: _Optional[int] = ...) -> None: ...

class GetTransactionsByBlockIDRequest(_message.Message):
    __slots__ = ["block_id"]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    block_id: bytes
    def __init__(self, block_id: _Optional[bytes] = ...) -> None: ...

class TransactionResultsResponse(_message.Message):
    __slots__ = ["transaction_results", "metadata"]
    TRANSACTION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    transaction_results: _containers.RepeatedCompositeFieldContainer[TransactionResultResponse]
    metadata: _metadata_pb2.Metadata
    def __init__(self, transaction_results: _Optional[_Iterable[_Union[TransactionResultResponse, _Mapping]]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class TransactionsResponse(_message.Message):
    __slots__ = ["transactions", "metadata"]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[_transaction_pb2.Transaction]
    metadata: _metadata_pb2.Metadata
    def __init__(self, transactions: _Optional[_Iterable[_Union[_transaction_pb2.Transaction, _Mapping]]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ["transaction", "metadata"]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    transaction: _transaction_pb2.Transaction
    metadata: _metadata_pb2.Metadata
    def __init__(self, transaction: _Optional[_Union[_transaction_pb2.Transaction, _Mapping]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class TransactionResultResponse(_message.Message):
    __slots__ = ["status", "status_code", "error_message", "events", "block_id", "transaction_id", "collection_id", "block_height", "metadata"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    status: _transaction_pb2.TransactionStatus
    status_code: int
    error_message: str
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
    block_id: bytes
    transaction_id: bytes
    collection_id: bytes
    block_height: int
    metadata: _metadata_pb2.Metadata
    def __init__(self, status: _Optional[_Union[_transaction_pb2.TransactionStatus, str]] = ..., status_code: _Optional[int] = ..., error_message: _Optional[str] = ..., events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]] = ..., block_id: _Optional[bytes] = ..., transaction_id: _Optional[bytes] = ..., collection_id: _Optional[bytes] = ..., block_height: _Optional[int] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    def __init__(self, address: _Optional[bytes] = ...) -> None: ...

class GetAccountResponse(_message.Message):
    __slots__ = ["account", "metadata"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    account: _account_pb2.Account
    metadata: _metadata_pb2.Metadata
    def __init__(self, account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class GetAccountAtLatestBlockRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    def __init__(self, address: _Optional[bytes] = ...) -> None: ...

class AccountResponse(_message.Message):
    __slots__ = ["account", "metadata"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    account: _account_pb2.Account
    metadata: _metadata_pb2.Metadata
    def __init__(self, account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class GetAccountAtBlockHeightRequest(_message.Message):
    __slots__ = ["address", "block_height"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    block_height: int
    def __init__(self, address: _Optional[bytes] = ..., block_height: _Optional[int] = ...) -> None: ...

class ExecuteScriptAtLatestBlockRequest(_message.Message):
    __slots__ = ["script", "arguments"]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    script: bytes
    arguments: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, script: _Optional[bytes] = ..., arguments: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ExecuteScriptAtBlockIDRequest(_message.Message):
    __slots__ = ["block_id", "script", "arguments"]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    block_id: bytes
    script: bytes
    arguments: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, block_id: _Optional[bytes] = ..., script: _Optional[bytes] = ..., arguments: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ExecuteScriptAtBlockHeightRequest(_message.Message):
    __slots__ = ["block_height", "script", "arguments"]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    block_height: int
    script: bytes
    arguments: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, block_height: _Optional[int] = ..., script: _Optional[bytes] = ..., arguments: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ExecuteScriptResponse(_message.Message):
    __slots__ = ["value", "metadata"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    metadata: _metadata_pb2.Metadata
    def __init__(self, value: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class GetEventsForHeightRangeRequest(_message.Message):
    __slots__ = ["type", "start_height", "end_height"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    START_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    END_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    type: str
    start_height: int
    end_height: int
    def __init__(self, type: _Optional[str] = ..., start_height: _Optional[int] = ..., end_height: _Optional[int] = ...) -> None: ...

class GetEventsForBlockIDsRequest(_message.Message):
    __slots__ = ["type", "block_ids"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_IDS_FIELD_NUMBER: _ClassVar[int]
    type: str
    block_ids: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, type: _Optional[str] = ..., block_ids: _Optional[_Iterable[bytes]] = ...) -> None: ...

class EventsResponse(_message.Message):
    __slots__ = ["results", "metadata"]
    class Result(_message.Message):
        __slots__ = ["block_id", "block_height", "events", "block_timestamp"]
        BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
        BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        BLOCK_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        block_id: bytes
        block_height: int
        events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
        block_timestamp: _timestamp_pb2.Timestamp
        def __init__(self, block_id: _Optional[bytes] = ..., block_height: _Optional[int] = ..., events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]] = ..., block_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[EventsResponse.Result]
    metadata: _metadata_pb2.Metadata
    def __init__(self, results: _Optional[_Iterable[_Union[EventsResponse.Result, _Mapping]]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class GetNetworkParametersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetNetworkParametersResponse(_message.Message):
    __slots__ = ["chain_id"]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    chain_id: str
    def __init__(self, chain_id: _Optional[str] = ...) -> None: ...

class GetLatestProtocolStateSnapshotRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ProtocolStateSnapshotResponse(_message.Message):
    __slots__ = ["serializedSnapshot", "metadata"]
    SERIALIZEDSNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    serializedSnapshot: bytes
    metadata: _metadata_pb2.Metadata
    def __init__(self, serializedSnapshot: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class GetExecutionResultForBlockIDRequest(_message.Message):
    __slots__ = ["block_id"]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    block_id: bytes
    def __init__(self, block_id: _Optional[bytes] = ...) -> None: ...

class ExecutionResultForBlockIDResponse(_message.Message):
    __slots__ = ["execution_result", "metadata"]
    EXECUTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    execution_result: _execution_result_pb2.ExecutionResult
    metadata: _metadata_pb2.Metadata
    def __init__(self, execution_result: _Optional[_Union[_execution_result_pb2.ExecutionResult, _Mapping]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...

class GetExecutionResultByIDRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class ExecutionResultByIDResponse(_message.Message):
    __slots__ = ["execution_result", "metadata"]
    EXECUTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    execution_result: _execution_result_pb2.ExecutionResult
    metadata: _metadata_pb2.Metadata
    def __init__(self, execution_result: _Optional[_Union[_execution_result_pb2.ExecutionResult, _Mapping]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ...) -> None: ...
