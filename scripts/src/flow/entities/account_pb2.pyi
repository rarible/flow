from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ["address", "balance", "code", "keys", "contracts"]
    class ContractsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    balance: int
    code: bytes
    keys: _containers.RepeatedCompositeFieldContainer[AccountKey]
    contracts: _containers.ScalarMap[str, bytes]
    def __init__(self, address: _Optional[bytes] = ..., balance: _Optional[int] = ..., code: _Optional[bytes] = ..., keys: _Optional[_Iterable[_Union[AccountKey, _Mapping]]] = ..., contracts: _Optional[_Mapping[str, bytes]] = ...) -> None: ...

class AccountKey(_message.Message):
    __slots__ = ["index", "public_key", "sign_algo", "hash_algo", "weight", "sequence_number", "revoked"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SIGN_ALGO_FIELD_NUMBER: _ClassVar[int]
    HASH_ALGO_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    index: int
    public_key: bytes
    sign_algo: int
    hash_algo: int
    weight: int
    sequence_number: int
    revoked: bool
    def __init__(self, index: _Optional[int] = ..., public_key: _Optional[bytes] = ..., sign_algo: _Optional[int] = ..., hash_algo: _Optional[int] = ..., weight: _Optional[int] = ..., sequence_number: _Optional[int] = ..., revoked: bool = ...) -> None: ...
