from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockSeal(_message.Message):
    __slots__ = ["block_id", "execution_receipt_id", "execution_receipt_signatures", "result_approval_signatures", "final_state", "result_id", "aggregated_approval_sigs"]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_RECEIPT_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_RECEIPT_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    RESULT_APPROVAL_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    FINAL_STATE_FIELD_NUMBER: _ClassVar[int]
    RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_APPROVAL_SIGS_FIELD_NUMBER: _ClassVar[int]
    block_id: bytes
    execution_receipt_id: bytes
    execution_receipt_signatures: _containers.RepeatedScalarFieldContainer[bytes]
    result_approval_signatures: _containers.RepeatedScalarFieldContainer[bytes]
    final_state: bytes
    result_id: bytes
    aggregated_approval_sigs: _containers.RepeatedCompositeFieldContainer[AggregatedSignature]
    def __init__(self, block_id: _Optional[bytes] = ..., execution_receipt_id: _Optional[bytes] = ..., execution_receipt_signatures: _Optional[_Iterable[bytes]] = ..., result_approval_signatures: _Optional[_Iterable[bytes]] = ..., final_state: _Optional[bytes] = ..., result_id: _Optional[bytes] = ..., aggregated_approval_sigs: _Optional[_Iterable[_Union[AggregatedSignature, _Mapping]]] = ...) -> None: ...

class AggregatedSignature(_message.Message):
    __slots__ = ["verifier_signatures", "signer_ids"]
    VERIFIER_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    SIGNER_IDS_FIELD_NUMBER: _ClassVar[int]
    verifier_signatures: _containers.RepeatedScalarFieldContainer[bytes]
    signer_ids: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, verifier_signatures: _Optional[_Iterable[bytes]] = ..., signer_ids: _Optional[_Iterable[bytes]] = ...) -> None: ...
