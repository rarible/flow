# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flow/entities/block_header.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n flow/entities/block_header.proto\x12\rflow.entities\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf6\x02\n\x0b\x42lockHeader\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x11\n\tparent_id\x18\x02 \x01(\x0c\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cpayload_hash\x18\x05 \x01(\x0c\x12\x0c\n\x04view\x18\x06 \x01(\x04\x12\x18\n\x10parent_voter_ids\x18\x07 \x03(\x0c\x12\x1d\n\x15parent_voter_sig_data\x18\x08 \x01(\x0c\x12\x13\n\x0bproposer_id\x18\t \x01(\x0c\x12\x19\n\x11proposer_sig_data\x18\n \x01(\x0c\x12\x10\n\x08\x63hain_id\x18\x0b \x01(\t\x12\x1c\n\x14parent_voter_indices\x18\x0c \x01(\x0c\x12\x37\n\x0clast_view_tc\x18\r \x01(\x0b\x32!.flow.entities.TimeoutCertificate\x12\x13\n\x0bparent_view\x18\x0e \x01(\x04\"\x99\x01\n\x12TimeoutCertificate\x12\x0c\n\x04view\x18\x01 \x01(\x04\x12\x15\n\rhigh_qc_views\x18\x02 \x03(\x04\x12\x34\n\nhighest_qc\x18\x03 \x01(\x0b\x32 .flow.entities.QuorumCertificate\x12\x16\n\x0esigner_indices\x18\x04 \x01(\x0c\x12\x10\n\x08sig_data\x18\x05 \x01(\x0c\"]\n\x11QuorumCertificate\x12\x0c\n\x04view\x18\x01 \x01(\x04\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x0c\x12\x16\n\x0esigner_indices\x18\x03 \x01(\x0c\x12\x10\n\x08sig_data\x18\x04 \x01(\x0c\x42P\n\x1corg.onflow.protobuf.entitiesZ0github.com/onflow/flow/protobuf/go/flow/entitiesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flow.entities.block_header_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034org.onflow.protobuf.entitiesZ0github.com/onflow/flow/protobuf/go/flow/entities'
  _globals['_BLOCKHEADER']._serialized_start=85
  _globals['_BLOCKHEADER']._serialized_end=459
  _globals['_TIMEOUTCERTIFICATE']._serialized_start=462
  _globals['_TIMEOUTCERTIFICATE']._serialized_end=615
  _globals['_QUORUMCERTIFICATE']._serialized_start=617
  _globals['_QUORUMCERTIFICATE']._serialized_end=710
# @@protoc_insertion_point(module_scope)
