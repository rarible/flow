from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockHeader(_message.Message):
    __slots__ = ["id", "parent_id", "height", "timestamp", "payload_hash", "view", "parent_voter_ids", "parent_voter_sig_data", "proposer_id", "proposer_sig_data", "chain_id", "parent_voter_indices", "last_view_tc", "parent_view"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_HASH_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PARENT_VOTER_IDS_FIELD_NUMBER: _ClassVar[int]
    PARENT_VOTER_SIG_DATA_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_ID_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_SIG_DATA_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_VOTER_INDICES_FIELD_NUMBER: _ClassVar[int]
    LAST_VIEW_TC_FIELD_NUMBER: _ClassVar[int]
    PARENT_VIEW_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    parent_id: bytes
    height: int
    timestamp: _timestamp_pb2.Timestamp
    payload_hash: bytes
    view: int
    parent_voter_ids: _containers.RepeatedScalarFieldContainer[bytes]
    parent_voter_sig_data: bytes
    proposer_id: bytes
    proposer_sig_data: bytes
    chain_id: str
    parent_voter_indices: bytes
    last_view_tc: TimeoutCertificate
    parent_view: int
    def __init__(self, id: _Optional[bytes] = ..., parent_id: _Optional[bytes] = ..., height: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., payload_hash: _Optional[bytes] = ..., view: _Optional[int] = ..., parent_voter_ids: _Optional[_Iterable[bytes]] = ..., parent_voter_sig_data: _Optional[bytes] = ..., proposer_id: _Optional[bytes] = ..., proposer_sig_data: _Optional[bytes] = ..., chain_id: _Optional[str] = ..., parent_voter_indices: _Optional[bytes] = ..., last_view_tc: _Optional[_Union[TimeoutCertificate, _Mapping]] = ..., parent_view: _Optional[int] = ...) -> None: ...

class TimeoutCertificate(_message.Message):
    __slots__ = ["view", "high_qc_views", "highest_qc", "signer_indices", "sig_data"]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    HIGH_QC_VIEWS_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_QC_FIELD_NUMBER: _ClassVar[int]
    SIGNER_INDICES_FIELD_NUMBER: _ClassVar[int]
    SIG_DATA_FIELD_NUMBER: _ClassVar[int]
    view: int
    high_qc_views: _containers.RepeatedScalarFieldContainer[int]
    highest_qc: QuorumCertificate
    signer_indices: bytes
    sig_data: bytes
    def __init__(self, view: _Optional[int] = ..., high_qc_views: _Optional[_Iterable[int]] = ..., highest_qc: _Optional[_Union[QuorumCertificate, _Mapping]] = ..., signer_indices: _Optional[bytes] = ..., sig_data: _Optional[bytes] = ...) -> None: ...

class QuorumCertificate(_message.Message):
    __slots__ = ["view", "block_id", "signer_indices", "sig_data"]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNER_INDICES_FIELD_NUMBER: _ClassVar[int]
    SIG_DATA_FIELD_NUMBER: _ClassVar[int]
    view: int
    block_id: bytes
    signer_indices: bytes
    sig_data: bytes
    def __init__(self, view: _Optional[int] = ..., block_id: _Optional[bytes] = ..., signer_indices: _Optional[bytes] = ..., sig_data: _Optional[bytes] = ...) -> None: ...
