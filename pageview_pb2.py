# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pageview.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pageview.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0epageview.proto\"m\n\x08PSession\x12\x0c\n\x04guid\x18\x01 \x01(\t\x12\r\n\x05locId\x18\x02 \x01(\x05\x12\x14\n\x0clastActiveTs\x18\x03 \x01(\x03\x12\x0f\n\x07os_code\x18\x04 \x01(\x05\x12\x1d\n\tpageViews\x18\x05 \x03(\x0b\x32\n.PPageView\"T\n\tPPageView\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x12\n\ntimecreate\x18\x02 \x01(\x03\x12\x12\n\ntimeOnSite\x18\x03 \x01(\x03\x12\x12\n\ntimeOnRead\x18\x04 \x01(\x03\"\x1c\n\x0cPRequestInfo\x12\x0c\n\x04guid\x18\x01 \x01(\t\"\x1c\n\x0cPingResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\r\n\x0bPingRequest\"E\n\x0e\x41rticleContext\x12\x0e\n\x06newsId\x18\x01 \x01(\t\x12\x12\n\npopularity\x18\x02 \x01(\x05\x12\x0f\n\x07recency\x18\x03 \x01(\x01\" \n\x0e\x41rticleRequest\x12\x0e\n\x06newsId\x18\x01 \x01(\t\"\x1c\n\nLastNClick\x12\x0e\n\x06newsId\x18\x01 \x03(\t\"\x1e\n\x11LastNClickRequest\x12\t\n\x01n\x18\x01 \x01(\x05\x32]\n\x0eSessionService\x12&\n\nGetSession\x12\r.PRequestInfo\x1a\t.PSession\x12#\n\x04Ping\x12\x0c.PingRequest\x1a\r.PingResponse2\x80\x01\n\x15\x41rticleContextService\x12\x35\n\x11GetArticleContext\x12\x0f.ArticleRequest\x1a\x0f.ArticleContext\x12\x30\n\rGetLastNClick\x12\x12.LastNClickRequest\x1a\x0b.LastNClickb\x06proto3')
)




_PSESSION = _descriptor.Descriptor(
  name='PSession',
  full_name='PSession',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='guid', full_name='PSession.guid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locId', full_name='PSession.locId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastActiveTs', full_name='PSession.lastActiveTs', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os_code', full_name='PSession.os_code', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageViews', full_name='PSession.pageViews', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=127,
)


_PPAGEVIEW = _descriptor.Descriptor(
  name='PPageView',
  full_name='PPageView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='PPageView.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timecreate', full_name='PPageView.timecreate', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeOnSite', full_name='PPageView.timeOnSite', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeOnRead', full_name='PPageView.timeOnRead', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=213,
)


_PREQUESTINFO = _descriptor.Descriptor(
  name='PRequestInfo',
  full_name='PRequestInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='guid', full_name='PRequestInfo.guid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=243,
)


_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='PingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='PingResponse.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=273,
)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=288,
)


_ARTICLECONTEXT = _descriptor.Descriptor(
  name='ArticleContext',
  full_name='ArticleContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='newsId', full_name='ArticleContext.newsId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='popularity', full_name='ArticleContext.popularity', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recency', full_name='ArticleContext.recency', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=359,
)


_ARTICLEREQUEST = _descriptor.Descriptor(
  name='ArticleRequest',
  full_name='ArticleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='newsId', full_name='ArticleRequest.newsId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=393,
)


_LASTNCLICK = _descriptor.Descriptor(
  name='LastNClick',
  full_name='LastNClick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='newsId', full_name='LastNClick.newsId', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=423,
)


_LASTNCLICKREQUEST = _descriptor.Descriptor(
  name='LastNClickRequest',
  full_name='LastNClickRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='LastNClickRequest.n', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=455,
)

_PSESSION.fields_by_name['pageViews'].message_type = _PPAGEVIEW
DESCRIPTOR.message_types_by_name['PSession'] = _PSESSION
DESCRIPTOR.message_types_by_name['PPageView'] = _PPAGEVIEW
DESCRIPTOR.message_types_by_name['PRequestInfo'] = _PREQUESTINFO
DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['ArticleContext'] = _ARTICLECONTEXT
DESCRIPTOR.message_types_by_name['ArticleRequest'] = _ARTICLEREQUEST
DESCRIPTOR.message_types_by_name['LastNClick'] = _LASTNCLICK
DESCRIPTOR.message_types_by_name['LastNClickRequest'] = _LASTNCLICKREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PSession = _reflection.GeneratedProtocolMessageType('PSession', (_message.Message,), {
  'DESCRIPTOR' : _PSESSION,
  '__module__' : 'pageview_pb2'
  # @@protoc_insertion_point(class_scope:PSession)
  })
_sym_db.RegisterMessage(PSession)

PPageView = _reflection.GeneratedProtocolMessageType('PPageView', (_message.Message,), {
  'DESCRIPTOR' : _PPAGEVIEW,
  '__module__' : 'pageview_pb2'
  # @@protoc_insertion_point(class_scope:PPageView)
  })
_sym_db.RegisterMessage(PPageView)

PRequestInfo = _reflection.GeneratedProtocolMessageType('PRequestInfo', (_message.Message,), {
  'DESCRIPTOR' : _PREQUESTINFO,
  '__module__' : 'pageview_pb2'
  # @@protoc_insertion_point(class_scope:PRequestInfo)
  })
_sym_db.RegisterMessage(PRequestInfo)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), {
  'DESCRIPTOR' : _PINGRESPONSE,
  '__module__' : 'pageview_pb2'
  # @@protoc_insertion_point(class_scope:PingResponse)
  })
_sym_db.RegisterMessage(PingResponse)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'pageview_pb2'
  # @@protoc_insertion_point(class_scope:PingRequest)
  })
_sym_db.RegisterMessage(PingRequest)

ArticleContext = _reflection.GeneratedProtocolMessageType('ArticleContext', (_message.Message,), {
  'DESCRIPTOR' : _ARTICLECONTEXT,
  '__module__' : 'pageview_pb2'
  # @@protoc_insertion_point(class_scope:ArticleContext)
  })
_sym_db.RegisterMessage(ArticleContext)

ArticleRequest = _reflection.GeneratedProtocolMessageType('ArticleRequest', (_message.Message,), {
  'DESCRIPTOR' : _ARTICLEREQUEST,
  '__module__' : 'pageview_pb2'
  # @@protoc_insertion_point(class_scope:ArticleRequest)
  })
_sym_db.RegisterMessage(ArticleRequest)

LastNClick = _reflection.GeneratedProtocolMessageType('LastNClick', (_message.Message,), {
  'DESCRIPTOR' : _LASTNCLICK,
  '__module__' : 'pageview_pb2'
  # @@protoc_insertion_point(class_scope:LastNClick)
  })
_sym_db.RegisterMessage(LastNClick)

LastNClickRequest = _reflection.GeneratedProtocolMessageType('LastNClickRequest', (_message.Message,), {
  'DESCRIPTOR' : _LASTNCLICKREQUEST,
  '__module__' : 'pageview_pb2'
  # @@protoc_insertion_point(class_scope:LastNClickRequest)
  })
_sym_db.RegisterMessage(LastNClickRequest)



_SESSIONSERVICE = _descriptor.ServiceDescriptor(
  name='SessionService',
  full_name='SessionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=457,
  serialized_end=550,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSession',
    full_name='SessionService.GetSession',
    index=0,
    containing_service=None,
    input_type=_PREQUESTINFO,
    output_type=_PSESSION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='SessionService.Ping',
    index=1,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SESSIONSERVICE)

DESCRIPTOR.services_by_name['SessionService'] = _SESSIONSERVICE


_ARTICLECONTEXTSERVICE = _descriptor.ServiceDescriptor(
  name='ArticleContextService',
  full_name='ArticleContextService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=553,
  serialized_end=681,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetArticleContext',
    full_name='ArticleContextService.GetArticleContext',
    index=0,
    containing_service=None,
    input_type=_ARTICLEREQUEST,
    output_type=_ARTICLECONTEXT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLastNClick',
    full_name='ArticleContextService.GetLastNClick',
    index=1,
    containing_service=None,
    input_type=_LASTNCLICKREQUEST,
    output_type=_LASTNCLICK,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ARTICLECONTEXTSERVICE)

DESCRIPTOR.services_by_name['ArticleContextService'] = _ARTICLECONTEXTSERVICE

# @@protoc_insertion_point(module_scope)