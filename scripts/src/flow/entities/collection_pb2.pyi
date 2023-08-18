from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Collection(_message.Message):
    __slots__ = ["id", "transaction_ids"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_IDS_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    transaction_ids: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, id: _Optional[bytes] = ..., transaction_ids: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CollectionGuarantee(_message.Message):
    __slots__ = ["collection_id", "signatures", "reference_block_id", "signature", "signer_ids", "signer_indices"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNER_IDS_FIELD_NUMBER: _ClassVar[int]
    SIGNER_INDICES_FIELD_NUMBER: _ClassVar[int]
    collection_id: bytes
    signatures: _containers.RepeatedScalarFieldContainer[bytes]
    reference_block_id: bytes
    signature: bytes
    signer_ids: _containers.RepeatedScalarFieldContainer[bytes]
    signer_indices: bytes
    def __init__(self, collection_id: _Optional[bytes] = ..., signatures: _Optional[_Iterable[bytes]] = ..., reference_block_id: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., signer_ids: _Optional[_Iterable[bytes]] = ..., signer_indices: _Optional[bytes] = ...) -> None: ...
