# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common/common.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'common/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63ommon/common.proto\x12\x06\x63ommon\x1a\x1fgoogle/protobuf/timestamp.proto\"{\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x01\x12&\n\x06source\x18\x04 \x01(\x0e\x32\x16.common.LocationSource\x12\x10\n\x08\x61\x63\x63uracy\x18\x05 \x01(\x02\"1\n\x0bKeyEnvelope\x12\x11\n\tkek_label\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x65s_key\x18\x02 \x01(\x0c\"\x91\x01\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\ntimestamps\x18\x02 \x03(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x08\x64\x61tasets\x18\x03 \x03(\x0b\x32\x15.common.MetricDataset\x12 \n\x04kind\x18\x04 \x01(\x0e\x32\x12.common.MetricKind\",\n\rMetricDataset\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\x02\"S\n\x11JoinServerContext\x12\x16\n\x0esession_key_id\x18\x01 \x01(\t\x12&\n\tapp_s_key\x18\x02 \x01(\x0b\x32\x13.common.KeyEnvelope*,\n\nModulation\x12\x08\n\x04LORA\x10\x00\x12\x07\n\x03\x46SK\x10\x01\x12\x0b\n\x07LR_FHSS\x10\x02*\xaa\x01\n\x06Region\x12\t\n\x05\x45U868\x10\x00\x12\t\n\x05US915\x10\x02\x12\t\n\x05\x43N779\x10\x03\x12\t\n\x05\x45U433\x10\x04\x12\t\n\x05\x41U915\x10\x05\x12\t\n\x05\x43N470\x10\x06\x12\t\n\x05\x41S923\x10\x07\x12\x0b\n\x07\x41S923_2\x10\x0c\x12\x0b\n\x07\x41S923_3\x10\r\x12\x0b\n\x07\x41S923_4\x10\x0e\x12\t\n\x05KR920\x10\x08\x12\t\n\x05IN865\x10\t\x12\t\n\x05RU864\x10\n\x12\x0b\n\x07ISM2400\x10\x0b*\xb3\x01\n\x05MType\x12\x10\n\x0cJOIN_REQUEST\x10\x00\x12\x0f\n\x0bJOIN_ACCEPT\x10\x01\x12\x17\n\x13UNCONFIRMED_DATA_UP\x10\x02\x12\x19\n\x15UNCONFIRMED_DATA_DOWN\x10\x03\x12\x15\n\x11\x43ONFIRMED_DATA_UP\x10\x04\x12\x17\n\x13\x43ONFIRMED_DATA_DOWN\x10\x05\x12\x12\n\x0eREJOIN_REQUEST\x10\x06\x12\x0f\n\x0bPROPRIETARY\x10\x07*~\n\nMacVersion\x12\x11\n\rLORAWAN_1_0_0\x10\x00\x12\x11\n\rLORAWAN_1_0_1\x10\x01\x12\x11\n\rLORAWAN_1_0_2\x10\x02\x12\x11\n\rLORAWAN_1_0_3\x10\x03\x12\x11\n\rLORAWAN_1_0_4\x10\x04\x12\x11\n\rLORAWAN_1_1_0\x10\x05*v\n\x11RegParamsRevision\x12\x05\n\x01\x41\x10\x00\x12\x05\n\x01\x42\x10\x01\x12\x0f\n\x0bRP002_1_0_0\x10\x02\x12\x0f\n\x0bRP002_1_0_1\x10\x03\x12\x0f\n\x0bRP002_1_0_2\x10\x04\x12\x0f\n\x0bRP002_1_0_3\x10\x05\x12\x0f\n\x0bRP002_1_0_4\x10\x06*\x8e\x01\n\x0eLocationSource\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03GPS\x10\x01\x12\n\n\x06\x43ONFIG\x10\x02\x12\x15\n\x11GEO_RESOLVER_TDOA\x10\x03\x12\x15\n\x11GEO_RESOLVER_RSSI\x10\x04\x12\x15\n\x11GEO_RESOLVER_GNSS\x10\x05\x12\x15\n\x11GEO_RESOLVER_WIFI\x10\x06*7\n\x0b\x41ggregation\x12\x08\n\x04HOUR\x10\x00\x12\x07\n\x03\x44\x41Y\x10\x01\x12\t\n\x05MONTH\x10\x02\x12\n\n\x06MINUTE\x10\x03*2\n\nMetricKind\x12\x0b\n\x07\x43OUNTER\x10\x00\x12\x0c\n\x08\x41\x42SOLUTE\x10\x01\x12\t\n\x05GAUGE\x10\x02*9\n\nRegulation\x12\x16\n\x12REGULATION_UNKNOWN\x10\x00\x12\x13\n\x0f\x45TSI_EN_300_220\x10\x01*4\n\x0b\x44\x65viceClass\x12\x0b\n\x07\x43LASS_A\x10\x00\x12\x0b\n\x07\x43LASS_B\x10\x01\x12\x0b\n\x07\x43LASS_C\x10\x02\x42\x9d\x01\n\x11io.chirpstack.apiB\x0b\x43ommonProtoP\x01Z1github.com/chirpstack/chirpstack/api/go/v4/common\xaa\x02\x11\x43hirpstack.Common\xca\x02\x11\x43hirpstack\\Common\xe2\x02\x1dGPBMetadata\\Chirpstack\\Commonb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021io.chirpstack.apiB\013CommonProtoP\001Z1github.com/chirpstack/chirpstack/api/go/v4/common\252\002\021Chirpstack.Common\312\002\021Chirpstack\\Common\342\002\035GPBMetadata\\Chirpstack\\Common'
  _globals['_MODULATION']._serialized_start=519
  _globals['_MODULATION']._serialized_end=563
  _globals['_REGION']._serialized_start=566
  _globals['_REGION']._serialized_end=736
  _globals['_MTYPE']._serialized_start=739
  _globals['_MTYPE']._serialized_end=918
  _globals['_MACVERSION']._serialized_start=920
  _globals['_MACVERSION']._serialized_end=1046
  _globals['_REGPARAMSREVISION']._serialized_start=1048
  _globals['_REGPARAMSREVISION']._serialized_end=1166
  _globals['_LOCATIONSOURCE']._serialized_start=1169
  _globals['_LOCATIONSOURCE']._serialized_end=1311
  _globals['_AGGREGATION']._serialized_start=1313
  _globals['_AGGREGATION']._serialized_end=1368
  _globals['_METRICKIND']._serialized_start=1370
  _globals['_METRICKIND']._serialized_end=1420
  _globals['_REGULATION']._serialized_start=1422
  _globals['_REGULATION']._serialized_end=1479
  _globals['_DEVICECLASS']._serialized_start=1481
  _globals['_DEVICECLASS']._serialized_end=1533
  _globals['_LOCATION']._serialized_start=64
  _globals['_LOCATION']._serialized_end=187
  _globals['_KEYENVELOPE']._serialized_start=189
  _globals['_KEYENVELOPE']._serialized_end=238
  _globals['_METRIC']._serialized_start=241
  _globals['_METRIC']._serialized_end=386
  _globals['_METRICDATASET']._serialized_start=388
  _globals['_METRICDATASET']._serialized_end=432
  _globals['_JOINSERVERCONTEXT']._serialized_start=434
  _globals['_JOINSERVERCONTEXT']._serialized_end=517
# @@protoc_insertion_point(module_scope)
