# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cubic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cubic.proto',
  package='cobaltspeech.cubic',
  syntax='proto3',
  serialized_options=_b('Z\007cubicpb\252\002\022CobaltSpeech.Cubic'),
  serialized_pb=_b('\n\x0b\x63ubic.proto\x12\x12\x63obaltspeech.cubic\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x13\n\x11ListModelsRequest\"~\n\x10RecognizeRequest\x12\x35\n\x06\x63onfig\x18\x01 \x01(\x0b\x32%.cobaltspeech.cubic.RecognitionConfig\x12\x33\n\x05\x61udio\x18\x02 \x01(\x0b\x32$.cobaltspeech.cubic.RecognitionAudio\"\x96\x01\n\x19StreamingRecognizeRequest\x12\x37\n\x06\x63onfig\x18\x01 \x01(\x0b\x32%.cobaltspeech.cubic.RecognitionConfigH\x00\x12\x35\n\x05\x61udio\x18\x02 \x01(\x0b\x32$.cobaltspeech.cubic.RecognitionAudioH\x00\x42\t\n\x07request\"0\n\x0fVersionResponse\x12\r\n\x05\x63ubic\x18\x01 \x01(\t\x12\x0e\n\x06server\x18\x02 \x01(\t\"?\n\x12ListModelsResponse\x12)\n\x06models\x18\x01 \x03(\x0b\x32\x19.cobaltspeech.cubic.Model\"M\n\x13RecognitionResponse\x12\x36\n\x07results\x18\x01 \x03(\x0b\x32%.cobaltspeech.cubic.RecognitionResult\"\x8e\x03\n\x11RecognitionConfig\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x46\n\x0e\x61udio_encoding\x18\x02 \x01(\x0e\x32..cobaltspeech.cubic.RecognitionConfig.Encoding\x12/\n\x0cidle_timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12 \n\x18\x65nable_word_time_offsets\x18\x04 \x01(\x08\x12\x1e\n\x16\x65nable_word_confidence\x18\x05 \x01(\x08\x12\x1d\n\x15\x65nable_raw_transcript\x18\x06 \x01(\x08\x12 \n\x18\x65nable_confusion_network\x18\x07 \x01(\x08\x12\x16\n\x0e\x61udio_channels\x18\x08 \x03(\r\"S\n\x08\x45ncoding\x12\x10\n\x0cRAW_LINEAR16\x10\x00\x12\x07\n\x03WAV\x10\x01\x12\x07\n\x03MP3\x10\x02\x12\x08\n\x04\x46LAC\x10\x03\x12\x0b\n\x07VOX8000\x10\x04\x12\x0c\n\x08ULAW8000\x10\x05\" \n\x10RecognitionAudio\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"Z\n\x05Model\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x37\n\nattributes\x18\x03 \x01(\x0b\x32#.cobaltspeech.cubic.ModelAttributes\"&\n\x0fModelAttributes\x12\x13\n\x0bsample_rate\x18\x01 \x01(\r\"\xbf\x01\n\x11RecognitionResult\x12@\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32*.cobaltspeech.cubic.RecognitionAlternative\x12\x12\n\nis_partial\x18\x02 \x01(\x08\x12=\n\x04\x63net\x18\x03 \x01(\x0b\x32/.cobaltspeech.cubic.RecognitionConfusionNetwork\x12\x15\n\raudio_channel\x18\x04 \x01(\r\"\xe1\x01\n\x16RecognitionAlternative\x12\x12\n\ntranscript\x18\x01 \x01(\t\x12\x16\n\x0eraw_transcript\x18\x06 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x01\x12+\n\x05words\x18\x03 \x03(\x0b\x32\x1c.cobaltspeech.cubic.WordInfo\x12-\n\nstart_time\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x08\x64uration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x88\x01\n\x08WordInfo\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x01\x12-\n\nstart_time\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x08\x64uration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\"V\n\x1bRecognitionConfusionNetwork\x12\x37\n\x05links\x18\x01 \x03(\x0b\x32(.cobaltspeech.cubic.ConfusionNetworkLink\"\xa9\x01\n\x14\x43onfusionNetworkLink\x12-\n\nstart_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x35\n\x04\x61rcs\x18\x03 \x03(\x0b\x32\'.cobaltspeech.cubic.ConfusionNetworkArc\"7\n\x13\x43onfusionNetworkArc\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x01\x32\xda\x03\n\x05\x43ubic\x12\\\n\x07Version\x12\x16.google.protobuf.Empty\x1a#.cobaltspeech.cubic.VersionResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/api/version\x12t\n\nListModels\x12%.cobaltspeech.cubic.ListModelsRequest\x1a&.cobaltspeech.cubic.ListModelsResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/api/listmodels\x12u\n\tRecognize\x12$.cobaltspeech.cubic.RecognizeRequest\x1a\'.cobaltspeech.cubic.RecognitionResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/api/recognize:\x01*\x12\x85\x01\n\x12StreamingRecognize\x12-.cobaltspeech.cubic.StreamingRecognizeRequest\x1a\'.cobaltspeech.cubic.RecognitionResponse\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/api/stream(\x01\x30\x01\x42\x1eZ\x07\x63ubicpb\xaa\x02\x12\x43obaltSpeech.Cubicb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])



_RECOGNITIONCONFIG_ENCODING = _descriptor.EnumDescriptor(
  name='Encoding',
  full_name='cobaltspeech.cubic.RecognitionConfig.Encoding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RAW_LINEAR16', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAV', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MP3', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAC', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOX8000', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ULAW8000', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=938,
  serialized_end=1021,
)
_sym_db.RegisterEnumDescriptor(_RECOGNITIONCONFIG_ENCODING)


_LISTMODELSREQUEST = _descriptor.Descriptor(
  name='ListModelsRequest',
  full_name='cobaltspeech.cubic.ListModelsRequest',
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
  serialized_start=126,
  serialized_end=145,
)


_RECOGNIZEREQUEST = _descriptor.Descriptor(
  name='RecognizeRequest',
  full_name='cobaltspeech.cubic.RecognizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='cobaltspeech.cubic.RecognizeRequest.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audio', full_name='cobaltspeech.cubic.RecognizeRequest.audio', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=147,
  serialized_end=273,
)


_STREAMINGRECOGNIZEREQUEST = _descriptor.Descriptor(
  name='StreamingRecognizeRequest',
  full_name='cobaltspeech.cubic.StreamingRecognizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='cobaltspeech.cubic.StreamingRecognizeRequest.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audio', full_name='cobaltspeech.cubic.StreamingRecognizeRequest.audio', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='request', full_name='cobaltspeech.cubic.StreamingRecognizeRequest.request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=276,
  serialized_end=426,
)


_VERSIONRESPONSE = _descriptor.Descriptor(
  name='VersionResponse',
  full_name='cobaltspeech.cubic.VersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cubic', full_name='cobaltspeech.cubic.VersionResponse.cubic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server', full_name='cobaltspeech.cubic.VersionResponse.server', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=428,
  serialized_end=476,
)


_LISTMODELSRESPONSE = _descriptor.Descriptor(
  name='ListModelsResponse',
  full_name='cobaltspeech.cubic.ListModelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='models', full_name='cobaltspeech.cubic.ListModelsResponse.models', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=478,
  serialized_end=541,
)


_RECOGNITIONRESPONSE = _descriptor.Descriptor(
  name='RecognitionResponse',
  full_name='cobaltspeech.cubic.RecognitionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='cobaltspeech.cubic.RecognitionResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=543,
  serialized_end=620,
)


_RECOGNITIONCONFIG = _descriptor.Descriptor(
  name='RecognitionConfig',
  full_name='cobaltspeech.cubic.RecognitionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_id', full_name='cobaltspeech.cubic.RecognitionConfig.model_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audio_encoding', full_name='cobaltspeech.cubic.RecognitionConfig.audio_encoding', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='idle_timeout', full_name='cobaltspeech.cubic.RecognitionConfig.idle_timeout', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_word_time_offsets', full_name='cobaltspeech.cubic.RecognitionConfig.enable_word_time_offsets', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_word_confidence', full_name='cobaltspeech.cubic.RecognitionConfig.enable_word_confidence', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_raw_transcript', full_name='cobaltspeech.cubic.RecognitionConfig.enable_raw_transcript', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_confusion_network', full_name='cobaltspeech.cubic.RecognitionConfig.enable_confusion_network', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audio_channels', full_name='cobaltspeech.cubic.RecognitionConfig.audio_channels', index=7,
      number=8, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RECOGNITIONCONFIG_ENCODING,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=623,
  serialized_end=1021,
)


_RECOGNITIONAUDIO = _descriptor.Descriptor(
  name='RecognitionAudio',
  full_name='cobaltspeech.cubic.RecognitionAudio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='cobaltspeech.cubic.RecognitionAudio.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1023,
  serialized_end=1055,
)


_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='cobaltspeech.cubic.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cobaltspeech.cubic.Model.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cobaltspeech.cubic.Model.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='cobaltspeech.cubic.Model.attributes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1057,
  serialized_end=1147,
)


_MODELATTRIBUTES = _descriptor.Descriptor(
  name='ModelAttributes',
  full_name='cobaltspeech.cubic.ModelAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_rate', full_name='cobaltspeech.cubic.ModelAttributes.sample_rate', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=1149,
  serialized_end=1187,
)


_RECOGNITIONRESULT = _descriptor.Descriptor(
  name='RecognitionResult',
  full_name='cobaltspeech.cubic.RecognitionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alternatives', full_name='cobaltspeech.cubic.RecognitionResult.alternatives', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_partial', full_name='cobaltspeech.cubic.RecognitionResult.is_partial', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cnet', full_name='cobaltspeech.cubic.RecognitionResult.cnet', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audio_channel', full_name='cobaltspeech.cubic.RecognitionResult.audio_channel', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=1190,
  serialized_end=1381,
)


_RECOGNITIONALTERNATIVE = _descriptor.Descriptor(
  name='RecognitionAlternative',
  full_name='cobaltspeech.cubic.RecognitionAlternative',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transcript', full_name='cobaltspeech.cubic.RecognitionAlternative.transcript', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_transcript', full_name='cobaltspeech.cubic.RecognitionAlternative.raw_transcript', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='cobaltspeech.cubic.RecognitionAlternative.confidence', index=2,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='words', full_name='cobaltspeech.cubic.RecognitionAlternative.words', index=3,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='cobaltspeech.cubic.RecognitionAlternative.start_time', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='cobaltspeech.cubic.RecognitionAlternative.duration', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1384,
  serialized_end=1609,
)


_WORDINFO = _descriptor.Descriptor(
  name='WordInfo',
  full_name='cobaltspeech.cubic.WordInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='cobaltspeech.cubic.WordInfo.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='cobaltspeech.cubic.WordInfo.confidence', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='cobaltspeech.cubic.WordInfo.start_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='cobaltspeech.cubic.WordInfo.duration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1612,
  serialized_end=1748,
)


_RECOGNITIONCONFUSIONNETWORK = _descriptor.Descriptor(
  name='RecognitionConfusionNetwork',
  full_name='cobaltspeech.cubic.RecognitionConfusionNetwork',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='links', full_name='cobaltspeech.cubic.RecognitionConfusionNetwork.links', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1750,
  serialized_end=1836,
)


_CONFUSIONNETWORKLINK = _descriptor.Descriptor(
  name='ConfusionNetworkLink',
  full_name='cobaltspeech.cubic.ConfusionNetworkLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='cobaltspeech.cubic.ConfusionNetworkLink.start_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='cobaltspeech.cubic.ConfusionNetworkLink.duration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arcs', full_name='cobaltspeech.cubic.ConfusionNetworkLink.arcs', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=1839,
  serialized_end=2008,
)


_CONFUSIONNETWORKARC = _descriptor.Descriptor(
  name='ConfusionNetworkArc',
  full_name='cobaltspeech.cubic.ConfusionNetworkArc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='cobaltspeech.cubic.ConfusionNetworkArc.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='cobaltspeech.cubic.ConfusionNetworkArc.confidence', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=2010,
  serialized_end=2065,
)

_RECOGNIZEREQUEST.fields_by_name['config'].message_type = _RECOGNITIONCONFIG
_RECOGNIZEREQUEST.fields_by_name['audio'].message_type = _RECOGNITIONAUDIO
_STREAMINGRECOGNIZEREQUEST.fields_by_name['config'].message_type = _RECOGNITIONCONFIG
_STREAMINGRECOGNIZEREQUEST.fields_by_name['audio'].message_type = _RECOGNITIONAUDIO
_STREAMINGRECOGNIZEREQUEST.oneofs_by_name['request'].fields.append(
  _STREAMINGRECOGNIZEREQUEST.fields_by_name['config'])
_STREAMINGRECOGNIZEREQUEST.fields_by_name['config'].containing_oneof = _STREAMINGRECOGNIZEREQUEST.oneofs_by_name['request']
_STREAMINGRECOGNIZEREQUEST.oneofs_by_name['request'].fields.append(
  _STREAMINGRECOGNIZEREQUEST.fields_by_name['audio'])
_STREAMINGRECOGNIZEREQUEST.fields_by_name['audio'].containing_oneof = _STREAMINGRECOGNIZEREQUEST.oneofs_by_name['request']
_LISTMODELSRESPONSE.fields_by_name['models'].message_type = _MODEL
_RECOGNITIONRESPONSE.fields_by_name['results'].message_type = _RECOGNITIONRESULT
_RECOGNITIONCONFIG.fields_by_name['audio_encoding'].enum_type = _RECOGNITIONCONFIG_ENCODING
_RECOGNITIONCONFIG.fields_by_name['idle_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_RECOGNITIONCONFIG_ENCODING.containing_type = _RECOGNITIONCONFIG
_MODEL.fields_by_name['attributes'].message_type = _MODELATTRIBUTES
_RECOGNITIONRESULT.fields_by_name['alternatives'].message_type = _RECOGNITIONALTERNATIVE
_RECOGNITIONRESULT.fields_by_name['cnet'].message_type = _RECOGNITIONCONFUSIONNETWORK
_RECOGNITIONALTERNATIVE.fields_by_name['words'].message_type = _WORDINFO
_RECOGNITIONALTERNATIVE.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_RECOGNITIONALTERNATIVE.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_WORDINFO.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_WORDINFO.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_RECOGNITIONCONFUSIONNETWORK.fields_by_name['links'].message_type = _CONFUSIONNETWORKLINK
_CONFUSIONNETWORKLINK.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CONFUSIONNETWORKLINK.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CONFUSIONNETWORKLINK.fields_by_name['arcs'].message_type = _CONFUSIONNETWORKARC
DESCRIPTOR.message_types_by_name['ListModelsRequest'] = _LISTMODELSREQUEST
DESCRIPTOR.message_types_by_name['RecognizeRequest'] = _RECOGNIZEREQUEST
DESCRIPTOR.message_types_by_name['StreamingRecognizeRequest'] = _STREAMINGRECOGNIZEREQUEST
DESCRIPTOR.message_types_by_name['VersionResponse'] = _VERSIONRESPONSE
DESCRIPTOR.message_types_by_name['ListModelsResponse'] = _LISTMODELSRESPONSE
DESCRIPTOR.message_types_by_name['RecognitionResponse'] = _RECOGNITIONRESPONSE
DESCRIPTOR.message_types_by_name['RecognitionConfig'] = _RECOGNITIONCONFIG
DESCRIPTOR.message_types_by_name['RecognitionAudio'] = _RECOGNITIONAUDIO
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
DESCRIPTOR.message_types_by_name['ModelAttributes'] = _MODELATTRIBUTES
DESCRIPTOR.message_types_by_name['RecognitionResult'] = _RECOGNITIONRESULT
DESCRIPTOR.message_types_by_name['RecognitionAlternative'] = _RECOGNITIONALTERNATIVE
DESCRIPTOR.message_types_by_name['WordInfo'] = _WORDINFO
DESCRIPTOR.message_types_by_name['RecognitionConfusionNetwork'] = _RECOGNITIONCONFUSIONNETWORK
DESCRIPTOR.message_types_by_name['ConfusionNetworkLink'] = _CONFUSIONNETWORKLINK
DESCRIPTOR.message_types_by_name['ConfusionNetworkArc'] = _CONFUSIONNETWORKARC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListModelsRequest = _reflection.GeneratedProtocolMessageType('ListModelsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTMODELSREQUEST,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.ListModelsRequest)
  ))
_sym_db.RegisterMessage(ListModelsRequest)

RecognizeRequest = _reflection.GeneratedProtocolMessageType('RecognizeRequest', (_message.Message,), dict(
  DESCRIPTOR = _RECOGNIZEREQUEST,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.RecognizeRequest)
  ))
_sym_db.RegisterMessage(RecognizeRequest)

StreamingRecognizeRequest = _reflection.GeneratedProtocolMessageType('StreamingRecognizeRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMINGRECOGNIZEREQUEST,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.StreamingRecognizeRequest)
  ))
_sym_db.RegisterMessage(StreamingRecognizeRequest)

VersionResponse = _reflection.GeneratedProtocolMessageType('VersionResponse', (_message.Message,), dict(
  DESCRIPTOR = _VERSIONRESPONSE,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.VersionResponse)
  ))
_sym_db.RegisterMessage(VersionResponse)

ListModelsResponse = _reflection.GeneratedProtocolMessageType('ListModelsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTMODELSRESPONSE,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.ListModelsResponse)
  ))
_sym_db.RegisterMessage(ListModelsResponse)

RecognitionResponse = _reflection.GeneratedProtocolMessageType('RecognitionResponse', (_message.Message,), dict(
  DESCRIPTOR = _RECOGNITIONRESPONSE,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.RecognitionResponse)
  ))
_sym_db.RegisterMessage(RecognitionResponse)

RecognitionConfig = _reflection.GeneratedProtocolMessageType('RecognitionConfig', (_message.Message,), dict(
  DESCRIPTOR = _RECOGNITIONCONFIG,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.RecognitionConfig)
  ))
_sym_db.RegisterMessage(RecognitionConfig)

RecognitionAudio = _reflection.GeneratedProtocolMessageType('RecognitionAudio', (_message.Message,), dict(
  DESCRIPTOR = _RECOGNITIONAUDIO,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.RecognitionAudio)
  ))
_sym_db.RegisterMessage(RecognitionAudio)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), dict(
  DESCRIPTOR = _MODEL,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.Model)
  ))
_sym_db.RegisterMessage(Model)

ModelAttributes = _reflection.GeneratedProtocolMessageType('ModelAttributes', (_message.Message,), dict(
  DESCRIPTOR = _MODELATTRIBUTES,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.ModelAttributes)
  ))
_sym_db.RegisterMessage(ModelAttributes)

RecognitionResult = _reflection.GeneratedProtocolMessageType('RecognitionResult', (_message.Message,), dict(
  DESCRIPTOR = _RECOGNITIONRESULT,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.RecognitionResult)
  ))
_sym_db.RegisterMessage(RecognitionResult)

RecognitionAlternative = _reflection.GeneratedProtocolMessageType('RecognitionAlternative', (_message.Message,), dict(
  DESCRIPTOR = _RECOGNITIONALTERNATIVE,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.RecognitionAlternative)
  ))
_sym_db.RegisterMessage(RecognitionAlternative)

WordInfo = _reflection.GeneratedProtocolMessageType('WordInfo', (_message.Message,), dict(
  DESCRIPTOR = _WORDINFO,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.WordInfo)
  ))
_sym_db.RegisterMessage(WordInfo)

RecognitionConfusionNetwork = _reflection.GeneratedProtocolMessageType('RecognitionConfusionNetwork', (_message.Message,), dict(
  DESCRIPTOR = _RECOGNITIONCONFUSIONNETWORK,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.RecognitionConfusionNetwork)
  ))
_sym_db.RegisterMessage(RecognitionConfusionNetwork)

ConfusionNetworkLink = _reflection.GeneratedProtocolMessageType('ConfusionNetworkLink', (_message.Message,), dict(
  DESCRIPTOR = _CONFUSIONNETWORKLINK,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.ConfusionNetworkLink)
  ))
_sym_db.RegisterMessage(ConfusionNetworkLink)

ConfusionNetworkArc = _reflection.GeneratedProtocolMessageType('ConfusionNetworkArc', (_message.Message,), dict(
  DESCRIPTOR = _CONFUSIONNETWORKARC,
  __module__ = 'cubic_pb2'
  # @@protoc_insertion_point(class_scope:cobaltspeech.cubic.ConfusionNetworkArc)
  ))
_sym_db.RegisterMessage(ConfusionNetworkArc)


DESCRIPTOR._options = None

_CUBIC = _descriptor.ServiceDescriptor(
  name='Cubic',
  full_name='cobaltspeech.cubic.Cubic',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=2068,
  serialized_end=2542,
  methods=[
  _descriptor.MethodDescriptor(
    name='Version',
    full_name='cobaltspeech.cubic.Cubic.Version',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_VERSIONRESPONSE,
    serialized_options=_b('\202\323\344\223\002\016\022\014/api/version'),
  ),
  _descriptor.MethodDescriptor(
    name='ListModels',
    full_name='cobaltspeech.cubic.Cubic.ListModels',
    index=1,
    containing_service=None,
    input_type=_LISTMODELSREQUEST,
    output_type=_LISTMODELSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\021\022\017/api/listmodels'),
  ),
  _descriptor.MethodDescriptor(
    name='Recognize',
    full_name='cobaltspeech.cubic.Cubic.Recognize',
    index=2,
    containing_service=None,
    input_type=_RECOGNIZEREQUEST,
    output_type=_RECOGNITIONRESPONSE,
    serialized_options=_b('\202\323\344\223\002\023\"\016/api/recognize:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='StreamingRecognize',
    full_name='cobaltspeech.cubic.Cubic.StreamingRecognize',
    index=3,
    containing_service=None,
    input_type=_STREAMINGRECOGNIZEREQUEST,
    output_type=_RECOGNITIONRESPONSE,
    serialized_options=_b('\202\323\344\223\002\r\022\013/api/stream'),
  ),
])
_sym_db.RegisterServiceDescriptor(_CUBIC)

DESCRIPTOR.services_by_name['Cubic'] = _CUBIC

# @@protoc_insertion_point(module_scope)
