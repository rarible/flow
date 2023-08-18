from google.protobuf import timestamp_pb2 as _timestamp_pb2
from flow.entities import collection_pb2 as _collection_pb2
from flow.entities import block_seal_pb2 as _block_seal_pb2
from flow.entities import execution_result_pb2 as _execution_result_pb2
from flow.entities import block_header_pb2 as _block_header_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BLOCK_UNKNOWN: _ClassVar[BlockStatus]
    BLOCK_FINALIZED: _ClassVar[BlockStatus]
    BLOCK_SEALED: _ClassVar[BlockStatus]
BLOCK_UNKNOWN: BlockStatus
BLOCK_FINALIZED: BlockStatus
BLOCK_SEALED: BlockStatus

class Block(_message.Message):
    __slots__ = ["id", "parent_id", "height", "timestamp", "collection_guarantees", "block_seals", "signatures", "execution_receipt_metaList", "execution_result_list", "block_header"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_GUARANTEES_FIELD_NUMBER: _ClassVar[int]
    BLOCK_SEALS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_RECEIPT_METALIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_RESULT_LIST_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEADER_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    parent_id: bytes
    height: int
    timestamp: _timestamp_pb2.Timestamp
    collection_guarantees: _containers.RepeatedCompositeFieldContainer[_collection_pb2.CollectionGuarantee]
    block_seals: _containers.RepeatedCompositeFieldContainer[_block_seal_pb2.BlockSeal]
    signatures: _containers.RepeatedScalarFieldContainer[bytes]
    execution_receipt_metaList: _containers.RepeatedCompositeFieldContainer[_execution_result_pb2.ExecutionReceiptMeta]
    execution_result_list: _containers.RepeatedCompositeFieldContainer[_execution_result_pb2.ExecutionResult]
    block_header: _block_header_pb2.BlockHeader
    def __init__(self, id: _Optional[bytes] = ..., parent_id: _Optional[bytes] = ..., height: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., collection_guarantees: _Optional[_Iterable[_Union[_collection_pb2.CollectionGuarantee, _Mapping]]] = ..., block_seals: _Optional[_Iterable[_Union[_block_seal_pb2.BlockSeal, _Mapping]]] = ..., signatures: _Optional[_Iterable[bytes]] = ..., execution_receipt_metaList: _Optional[_Iterable[_Union[_execution_result_pb2.ExecutionReceiptMeta, _Mapping]]] = ..., execution_result_list: _Optional[_Iterable[_Union[_execution_result_pb2.ExecutionResult, _Mapping]]] = ..., block_header: _Optional[_Union[_block_header_pb2.BlockHeader, _Mapping]] = ...) -> None: ...
