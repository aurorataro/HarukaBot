# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: locale.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0clocale.proto\x12\x18\x62ilibili.metadata.locale\"\x9a\x01\n\x06Locale\x12\x35\n\x08\x63_locale\x18\x01 \x01(\x0b\x32#.bilibili.metadata.locale.LocaleIds\x12\x35\n\x08s_locale\x18\x02 \x01(\x0b\x32#.bilibili.metadata.locale.LocaleIds\x12\x10\n\x08sim_code\x18\x03 \x01(\t\x12\x10\n\x08timezone\x18\x04 \x01(\t\"=\n\tLocaleIds\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x0e\n\x06script\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\tb\x06proto3')



_LOCALE = DESCRIPTOR.message_types_by_name['Locale']
_LOCALEIDS = DESCRIPTOR.message_types_by_name['LocaleIds']
Locale = _reflection.GeneratedProtocolMessageType('Locale', (_message.Message,), {
  'DESCRIPTOR' : _LOCALE,
  '__module__' : 'locale_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.metadata.locale.Locale)
  })
_sym_db.RegisterMessage(Locale)

LocaleIds = _reflection.GeneratedProtocolMessageType('LocaleIds', (_message.Message,), {
  'DESCRIPTOR' : _LOCALEIDS,
  '__module__' : 'locale_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.metadata.locale.LocaleIds)
  })
_sym_db.RegisterMessage(LocaleIds)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOCALE._serialized_start=43
  _LOCALE._serialized_end=197
  _LOCALEIDS._serialized_start=199
  _LOCALEIDS._serialized_end=260
# @@protoc_insertion_point(module_scope)
