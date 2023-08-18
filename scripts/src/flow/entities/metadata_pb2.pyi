from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Metadata(_message.Message):
    __slots__ = ["latest_finalized_block_id", "latest_finalized_height", "node_id"]
    LATEST_FINALIZED_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_FINALIZED_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    latest_finalized_block_id: bytes
    latest_finalized_height: int
    node_id: bytes
    def __init__(self, latest_finalized_block_id: _Optional[bytes] = ..., latest_finalized_height: _Optional[int] = ..., node_id: _Optional[bytes] = ...) -> None: ...
