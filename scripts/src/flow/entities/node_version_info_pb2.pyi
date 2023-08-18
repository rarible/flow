from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NodeVersionInfo(_message.Message):
    __slots__ = ["semver", "commit", "spork_id", "protocol_version"]
    SEMVER_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    SPORK_ID_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    semver: str
    commit: str
    spork_id: bytes
    protocol_version: int
    def __init__(self, semver: _Optional[str] = ..., commit: _Optional[str] = ..., spork_id: _Optional[bytes] = ..., protocol_version: _Optional[int] = ...) -> None: ...
