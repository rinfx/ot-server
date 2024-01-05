# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trace.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import resource_pb2 as resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btrace.proto\x12\x1copentelemetry.proto.trace.v1\x1a\x0c\x63ommon.proto\x1a\x0eresource.proto\"Q\n\nTracesData\x12\x43\n\x0eresource_spans\x18\x01 \x03(\x0b\x32+.opentelemetry.proto.trace.v1.ResourceSpans\"\xa7\x01\n\rResourceSpans\x12;\n\x08resource\x18\x01 \x01(\x0b\x32).opentelemetry.proto.resource.v1.Resource\x12=\n\x0bscope_spans\x18\x02 \x03(\x0b\x32(.opentelemetry.proto.trace.v1.ScopeSpans\x12\x12\n\nschema_url\x18\x03 \x01(\tJ\x06\x08\xe8\x07\x10\xe9\x07\"\x97\x01\n\nScopeSpans\x12\x42\n\x05scope\x18\x01 \x01(\x0b\x32\x33.opentelemetry.proto.common.v1.InstrumentationScope\x12\x31\n\x05spans\x18\x02 \x03(\x0b\x32\".opentelemetry.proto.trace.v1.Span\x12\x12\n\nschema_url\x18\x03 \x01(\t\"\x84\x08\n\x04Span\x12\x10\n\x08trace_id\x18\x01 \x01(\x0c\x12\x0f\n\x07span_id\x18\x02 \x01(\x0c\x12\x13\n\x0btrace_state\x18\x03 \x01(\t\x12\x16\n\x0eparent_span_id\x18\x04 \x01(\x0c\x12\r\n\x05\x66lags\x18\x10 \x01(\x07\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x39\n\x04kind\x18\x06 \x01(\x0e\x32+.opentelemetry.proto.trace.v1.Span.SpanKind\x12\x1c\n\x14start_time_unix_nano\x18\x07 \x01(\x06\x12\x1a\n\x12\x65nd_time_unix_nano\x18\x08 \x01(\x06\x12;\n\nattributes\x18\t \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12 \n\x18\x64ropped_attributes_count\x18\n \x01(\r\x12\x38\n\x06\x65vents\x18\x0b \x03(\x0b\x32(.opentelemetry.proto.trace.v1.Span.Event\x12\x1c\n\x14\x64ropped_events_count\x18\x0c \x01(\r\x12\x36\n\x05links\x18\r \x03(\x0b\x32\'.opentelemetry.proto.trace.v1.Span.Link\x12\x1b\n\x13\x64ropped_links_count\x18\x0e \x01(\r\x12\x34\n\x06status\x18\x0f \x01(\x0b\x32$.opentelemetry.proto.trace.v1.Status\x1a\x8c\x01\n\x05\x45vent\x12\x16\n\x0etime_unix_nano\x18\x01 \x01(\x06\x12\x0c\n\x04name\x18\x02 \x01(\t\x12;\n\nattributes\x18\x03 \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12 \n\x18\x64ropped_attributes_count\x18\x04 \x01(\r\x1a\xac\x01\n\x04Link\x12\x10\n\x08trace_id\x18\x01 \x01(\x0c\x12\x0f\n\x07span_id\x18\x02 \x01(\x0c\x12\x13\n\x0btrace_state\x18\x03 \x01(\t\x12;\n\nattributes\x18\x04 \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12 \n\x18\x64ropped_attributes_count\x18\x05 \x01(\r\x12\r\n\x05\x66lags\x18\x06 \x01(\x07\"\x99\x01\n\x08SpanKind\x12\x19\n\x15SPAN_KIND_UNSPECIFIED\x10\x00\x12\x16\n\x12SPAN_KIND_INTERNAL\x10\x01\x12\x14\n\x10SPAN_KIND_SERVER\x10\x02\x12\x14\n\x10SPAN_KIND_CLIENT\x10\x03\x12\x16\n\x12SPAN_KIND_PRODUCER\x10\x04\x12\x16\n\x12SPAN_KIND_CONSUMER\x10\x05\"\xae\x01\n\x06Status\x12\x0f\n\x07message\x18\x02 \x01(\t\x12=\n\x04\x63ode\x18\x03 \x01(\x0e\x32/.opentelemetry.proto.trace.v1.Status.StatusCode\"N\n\nStatusCode\x12\x15\n\x11STATUS_CODE_UNSET\x10\x00\x12\x12\n\x0eSTATUS_CODE_OK\x10\x01\x12\x15\n\x11STATUS_CODE_ERROR\x10\x02J\x04\x08\x01\x10\x02*H\n\tSpanFlags\x12\x19\n\x15SPAN_FLAGS_DO_NOT_USE\x10\x00\x12 \n\x1bSPAN_FLAGS_TRACE_FLAGS_MASK\x10\xff\x01\x42w\n\x1fio.opentelemetry.proto.trace.v1B\nTraceProtoP\x01Z\'go.opentelemetry.io/proto/otlp/trace/v1\xaa\x02\x1cOpenTelemetry.Proto.Trace.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'trace_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037io.opentelemetry.proto.trace.v1B\nTraceProtoP\001Z\'go.opentelemetry.io/proto/otlp/trace/v1\252\002\034OpenTelemetry.Proto.Trace.V1'
  _globals['_SPANFLAGS']._serialized_start=1690
  _globals['_SPANFLAGS']._serialized_end=1762
  _globals['_TRACESDATA']._serialized_start=75
  _globals['_TRACESDATA']._serialized_end=156
  _globals['_RESOURCESPANS']._serialized_start=159
  _globals['_RESOURCESPANS']._serialized_end=326
  _globals['_SCOPESPANS']._serialized_start=329
  _globals['_SCOPESPANS']._serialized_end=480
  _globals['_SPAN']._serialized_start=483
  _globals['_SPAN']._serialized_end=1511
  _globals['_SPAN_EVENT']._serialized_start=1040
  _globals['_SPAN_EVENT']._serialized_end=1180
  _globals['_SPAN_LINK']._serialized_start=1183
  _globals['_SPAN_LINK']._serialized_end=1355
  _globals['_SPAN_SPANKIND']._serialized_start=1358
  _globals['_SPAN_SPANKIND']._serialized_end=1511
  _globals['_STATUS']._serialized_start=1514
  _globals['_STATUS']._serialized_end=1688
  _globals['_STATUS_STATUSCODE']._serialized_start=1604
  _globals['_STATUS_STATUSCODE']._serialized_end=1682
# @@protoc_insertion_point(module_scope)
