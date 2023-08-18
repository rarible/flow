from flow.entities import event_pb2 as _event_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN: _ClassVar[TransactionStatus]
    PENDING: _ClassVar[TransactionStatus]
    FINALIZED: _ClassVar[TransactionStatus]
    EXECUTED: _ClassVar[TransactionStatus]
    SEALED: _ClassVar[TransactionStatus]
    EXPIRED: _ClassVar[TransactionStatus]
UNKNOWN: TransactionStatus
PENDING: TransactionStatus
FINALIZED: TransactionStatus
EXECUTED: TransactionStatus
SEALED: TransactionStatus
EXPIRED: TransactionStatus

class Transaction(_message.Message):
    __slots__ = ["script", "arguments", "reference_block_id", "gas_limit", "proposal_key", "payer", "authorizers", "payload_signatures", "envelope_signatures"]
    class ProposalKey(_message.Message):
        __slots__ = ["address", "key_id", "sequence_number"]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        KEY_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        address: bytes
        key_id: int
        sequence_number: int
        def __init__(self, address: _Optional[bytes] = ..., key_id: _Optional[int] = ..., sequence_number: _Optional[int] = ...) -> None: ...
    class Signature(_message.Message):
        __slots__ = ["address", "key_id", "signature"]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        KEY_ID_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        address: bytes
        key_id: int
        signature: bytes
        def __init__(self, address: _Optional[bytes] = ..., key_id: _Optional[int] = ..., signature: _Optional[bytes] = ...) -> None: ...
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    GAS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_KEY_FIELD_NUMBER: _ClassVar[int]
    PAYER_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZERS_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    script: bytes
    arguments: _containers.RepeatedScalarFieldContainer[bytes]
    reference_block_id: bytes
    gas_limit: int
    proposal_key: Transaction.ProposalKey
    payer: bytes
    authorizers: _containers.RepeatedScalarFieldContainer[bytes]
    payload_signatures: _containers.RepeatedCompositeFieldContainer[Transaction.Signature]
    envelope_signatures: _containers.RepeatedCompositeFieldContainer[Transaction.Signature]
    def __init__(self, script: _Optional[bytes] = ..., arguments: _Optional[_Iterable[bytes]] = ..., reference_block_id: _Optional[bytes] = ..., gas_limit: _Optional[int] = ..., proposal_key: _Optional[_Union[Transaction.ProposalKey, _Mapping]] = ..., payer: _Optional[bytes] = ..., authorizers: _Optional[_Iterable[bytes]] = ..., payload_signatures: _Optional[_Iterable[_Union[Transaction.Signature, _Mapping]]] = ..., envelope_signatures: _Optional[_Iterable[_Union[Transaction.Signature, _Mapping]]] = ...) -> None: ...
