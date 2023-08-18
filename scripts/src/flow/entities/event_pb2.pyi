from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ["type", "transaction_id", "transaction_index", "event_index", "payload"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_INDEX_FIELD_NUMBER: _ClassVar[int]
    EVENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    type: str
    transaction_id: bytes
    transaction_index: int
    event_index: int
    payload: bytes
    def __init__(self, type: _Optional[str] = ..., transaction_id: _Optional[bytes] = ..., transaction_index: _Optional[int] = ..., event_index: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...
