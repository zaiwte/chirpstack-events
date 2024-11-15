# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gw/gw.proto
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
    'gw/gw.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import common_pb2 as common_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgw/gw.proto\x12\x02gw\x1a\x13\x63ommon/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x95\x01\n\nModulation\x12&\n\x04lora\x18\x03 \x01(\x0b\x32\x16.gw.LoraModulationInfoH\x00\x12$\n\x03\x66sk\x18\x04 \x01(\x0b\x32\x15.gw.FskModulationInfoH\x00\x12+\n\x07lr_fhss\x18\x05 \x01(\x0b\x32\x18.gw.LrFhssModulationInfoH\x00\x42\x0c\n\nparameters\"\x8d\x02\n\x12UplinkTxInfoLegacy\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12&\n\nmodulation\x18\x02 \x01(\x0e\x32\x12.common.Modulation\x12\x36\n\x14lora_modulation_info\x18\x03 \x01(\x0b\x32\x16.gw.LoraModulationInfoH\x00\x12\x34\n\x13\x66sk_modulation_info\x18\x04 \x01(\x0b\x32\x15.gw.FskModulationInfoH\x00\x12;\n\x17lr_fhss_modulation_info\x18\x05 \x01(\x0b\x32\x18.gw.LrFhssModulationInfoH\x00\x42\x11\n\x0fmodulation_info\"E\n\x0cUplinkTxInfo\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12\"\n\nmodulation\x18\x02 \x01(\x0b\x32\x0e.gw.Modulation\"\xbe\x01\n\x12LoraModulationInfo\x12\x11\n\tbandwidth\x18\x01 \x01(\r\x12\x18\n\x10spreading_factor\x18\x02 \x01(\r\x12\x18\n\x10\x63ode_rate_legacy\x18\x03 \x01(\t\x12\x1f\n\tcode_rate\x18\x05 \x01(\x0e\x32\x0c.gw.CodeRate\x12\x1e\n\x16polarization_inversion\x18\x04 \x01(\x08\x12\x10\n\x08preamble\x18\x06 \x01(\r\x12\x0e\n\x06no_crc\x18\x07 \x01(\x08\"B\n\x11\x46skModulationInfo\x12\x1b\n\x13\x66requency_deviation\x18\x01 \x01(\r\x12\x10\n\x08\x64\x61tarate\x18\x02 \x01(\r\"\x86\x01\n\x14LrFhssModulationInfo\x12\x1f\n\x17operating_channel_width\x18\x01 \x01(\r\x12\x18\n\x10\x63ode_rate_legacy\x18\x02 \x01(\t\x12\x1f\n\tcode_rate\x18\x04 \x01(\x0e\x32\x0c.gw.CodeRate\x12\x12\n\ngrid_steps\x18\x03 \x01(\r\"V\n\x16\x45ncryptedFineTimestamp\x12\x15\n\raes_key_index\x18\x01 \x01(\r\x12\x14\n\x0c\x65ncrypted_ns\x18\x02 \x01(\x0c\x12\x0f\n\x07\x66pga_id\x18\x03 \x01(\x0c\">\n\x12PlainFineTimestamp\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xbe\x07\n\x0cGatewayStats\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x11 \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x08location\x18\x03 \x01(\x0b\x32\x10.common.Location\x12\x16\n\x0e\x63onfig_version\x18\x04 \x01(\t\x12\x1b\n\x13rx_packets_received\x18\x05 \x01(\r\x12\x1e\n\x16rx_packets_received_ok\x18\x06 \x01(\r\x12\x1b\n\x13tx_packets_received\x18\x07 \x01(\r\x12\x1a\n\x12tx_packets_emitted\x18\x08 \x01(\r\x12\x30\n\x08metadata\x18\n \x03(\x0b\x32\x1e.gw.GatewayStats.MetadataEntry\x12M\n\x18tx_packets_per_frequency\x18\x0c \x03(\x0b\x32+.gw.GatewayStats.TxPacketsPerFrequencyEntry\x12M\n\x18rx_packets_per_frequency\x18\r \x03(\x0b\x32+.gw.GatewayStats.RxPacketsPerFrequencyEntry\x12\x39\n\x19tx_packets_per_modulation\x18\x0e \x03(\x0b\x32\x16.gw.PerModulationCount\x12\x39\n\x19rx_packets_per_modulation\x18\x0f \x03(\x0b\x32\x16.gw.PerModulationCount\x12G\n\x15tx_packets_per_status\x18\x10 \x03(\x0b\x32(.gw.GatewayStats.TxPacketsPerStatusEntry\x12,\n\x10\x64uty_cycle_stats\x18\x12 \x01(\x0b\x32\x12.gw.DutyCycleStats\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a<\n\x1aTxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a<\n\x1aRxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x39\n\x17TxPacketsPerStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"G\n\x12PerModulationCount\x12\"\n\nmodulation\x18\x01 \x01(\x0b\x32\x0e.gw.Modulation\x12\r\n\x05\x63ount\x18\x02 \x01(\r\"\x85\x01\n\x0e\x44utyCycleStats\x12&\n\nregulation\x18\x01 \x01(\x0e\x32\x12.common.Regulation\x12)\n\x06window\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12 \n\x05\x62\x61nds\x18\x03 \x03(\x0b\x32\x11.gw.DutyCycleBand\"\xa9\x01\n\rDutyCycleBand\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rfrequency_min\x18\x02 \x01(\r\x12\x15\n\rfrequency_max\x18\x03 \x01(\r\x12+\n\x08load_max\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0cload_tracked\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x80\x05\n\x12UplinkRxInfoLegacy\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x14time_since_gps_epoch\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0c\n\x04rssi\x18\x05 \x01(\x05\x12\x10\n\x08lora_snr\x18\x06 \x01(\x01\x12\x0f\n\x07\x63hannel\x18\x07 \x01(\r\x12\x10\n\x08rf_chain\x18\x08 \x01(\r\x12\r\n\x05\x62oard\x18\t \x01(\r\x12\x0f\n\x07\x61ntenna\x18\n \x01(\r\x12\"\n\x08location\x18\x0b \x01(\x0b\x32\x10.common.Location\x12\x32\n\x13\x66ine_timestamp_type\x18\x0c \x01(\x0e\x32\x15.gw.FineTimestampType\x12>\n\x18\x65ncrypted_fine_timestamp\x18\r \x01(\x0b\x32\x1a.gw.EncryptedFineTimestampH\x00\x12\x36\n\x14plain_fine_timestamp\x18\x0e \x01(\x0b\x32\x16.gw.PlainFineTimestampH\x00\x12\x0f\n\x07\x63ontext\x18\x0f \x01(\x0c\x12\x11\n\tuplink_id\x18\x10 \x01(\x0c\x12!\n\ncrc_status\x18\x11 \x01(\x0e\x32\r.gw.CRCStatus\x12\x36\n\x08metadata\x18\x12 \x03(\x0b\x32$.gw.UplinkRxInfoLegacy.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x10\n\x0e\x66ine_timestamp\"\x9f\x04\n\x0cUplinkRxInfo\x12\x12\n\ngateway_id\x18\x01 \x01(\t\x12\x11\n\tuplink_id\x18\x02 \x01(\r\x12+\n\x07gw_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07ns_time\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x14time_since_gps_epoch\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12<\n\x19\x66ine_time_since_gps_epoch\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0c\n\x04rssi\x18\x06 \x01(\x05\x12\x0b\n\x03snr\x18\x07 \x01(\x02\x12\x0f\n\x07\x63hannel\x18\x08 \x01(\r\x12\x10\n\x08rf_chain\x18\t \x01(\r\x12\r\n\x05\x62oard\x18\n \x01(\r\x12\x0f\n\x07\x61ntenna\x18\x0b \x01(\r\x12\"\n\x08location\x18\x0c \x01(\x0b\x32\x10.common.Location\x12\x0f\n\x07\x63ontext\x18\r \x01(\x0c\x12\x30\n\x08metadata\x18\x0f \x03(\x0b\x32\x1e.gw.UplinkRxInfo.MetadataEntry\x12!\n\ncrc_status\x18\x10 \x01(\x0e\x32\r.gw.CRCStatus\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x82\x04\n\x14\x44ownlinkTxInfoLegacy\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12\x11\n\tfrequency\x18\x05 \x01(\r\x12\r\n\x05power\x18\x06 \x01(\x05\x12&\n\nmodulation\x18\x07 \x01(\x0e\x32\x12.common.Modulation\x12\x36\n\x14lora_modulation_info\x18\x08 \x01(\x0b\x32\x16.gw.LoraModulationInfoH\x00\x12\x34\n\x13\x66sk_modulation_info\x18\t \x01(\x0b\x32\x15.gw.FskModulationInfoH\x00\x12\r\n\x05\x62oard\x18\n \x01(\r\x12\x0f\n\x07\x61ntenna\x18\x0b \x01(\r\x12\"\n\x06timing\x18\x0c \x01(\x0e\x32\x12.gw.DownlinkTiming\x12<\n\x17immediately_timing_info\x18\r \x01(\x0b\x32\x19.gw.ImmediatelyTimingInfoH\x01\x12\x30\n\x11\x64\x65lay_timing_info\x18\x0e \x01(\x0b\x32\x13.gw.DelayTimingInfoH\x01\x12\x37\n\x15gps_epoch_timing_info\x18\x0f \x01(\x0b\x32\x16.gw.GPSEpochTimingInfoH\x01\x12\x0f\n\x07\x63ontext\x18\x10 \x01(\x0c\x42\x11\n\x0fmodulation_infoB\r\n\x0btiming_info\"\xa3\x01\n\x0e\x44ownlinkTxInfo\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12\r\n\x05power\x18\x02 \x01(\x05\x12\"\n\nmodulation\x18\x03 \x01(\x0b\x32\x0e.gw.Modulation\x12\r\n\x05\x62oard\x18\x04 \x01(\r\x12\x0f\n\x07\x61ntenna\x18\x05 \x01(\r\x12\x1a\n\x06timing\x18\x06 \x01(\x0b\x32\n.gw.Timing\x12\x0f\n\x07\x63ontext\x18\x07 \x01(\x0c\"\x9b\x01\n\x06Timing\x12\x30\n\x0bimmediately\x18\x01 \x01(\x0b\x32\x19.gw.ImmediatelyTimingInfoH\x00\x12$\n\x05\x64\x65lay\x18\x02 \x01(\x0b\x32\x13.gw.DelayTimingInfoH\x00\x12+\n\tgps_epoch\x18\x03 \x01(\x0b\x32\x16.gw.GPSEpochTimingInfoH\x00\x42\x0c\n\nparameters\"\x17\n\x15ImmediatelyTimingInfo\";\n\x0f\x44\x65layTimingInfo\x12(\n\x05\x64\x65lay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"M\n\x12GPSEpochTimingInfo\x12\x37\n\x14time_since_gps_epoch\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"\xc8\x01\n\x0bUplinkFrame\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12.\n\x0etx_info_legacy\x18\x02 \x01(\x0b\x32\x16.gw.UplinkTxInfoLegacy\x12.\n\x0erx_info_legacy\x18\x03 \x01(\x0b\x32\x16.gw.UplinkRxInfoLegacy\x12!\n\x07tx_info\x18\x04 \x01(\x0b\x32\x10.gw.UplinkTxInfo\x12!\n\x07rx_info\x18\x05 \x01(\x0b\x32\x10.gw.UplinkRxInfo\"k\n\x0eUplinkFrameSet\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12!\n\x07tx_info\x18\x02 \x01(\x0b\x32\x10.gw.UplinkTxInfo\x12!\n\x07rx_info\x18\x03 \x03(\x0b\x32\x10.gw.UplinkRxInfo\"\x95\x01\n\rDownlinkFrame\x12\x13\n\x0b\x64ownlink_id\x18\x03 \x01(\r\x12\x1a\n\x12\x64ownlink_id_legacy\x18\x04 \x01(\x0c\x12$\n\x05items\x18\x05 \x03(\x0b\x32\x15.gw.DownlinkFrameItem\x12\x19\n\x11gateway_id_legacy\x18\x06 \x01(\x0c\x12\x12\n\ngateway_id\x18\x07 \x01(\t\"\x7f\n\x11\x44ownlinkFrameItem\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12\x30\n\x0etx_info_legacy\x18\x02 \x01(\x0b\x32\x18.gw.DownlinkTxInfoLegacy\x12#\n\x07tx_info\x18\x03 \x01(\x0b\x32\x12.gw.DownlinkTxInfo\"\x95\x01\n\rDownlinkTxAck\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x06 \x01(\t\x12\x13\n\x0b\x64ownlink_id\x18\x02 \x01(\r\x12\x1a\n\x12\x64ownlink_id_legacy\x18\x04 \x01(\x0c\x12$\n\x05items\x18\x05 \x03(\x0b\x32\x15.gw.DownlinkTxAckItem\"4\n\x11\x44ownlinkTxAckItem\x12\x1f\n\x06status\x18\x01 \x01(\x0e\x32\x0f.gw.TxAckStatus\"\xb5\x01\n\x14GatewayConfiguration\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x05 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12*\n\x08\x63hannels\x18\x03 \x03(\x0b\x32\x18.gw.ChannelConfiguration\x12\x31\n\x0estats_interval\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x87\x02\n\x14\x43hannelConfiguration\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12-\n\x11modulation_legacy\x18\x02 \x01(\x0e\x32\x12.common.Modulation\x12:\n\x16lora_modulation_config\x18\x03 \x01(\x0b\x32\x18.gw.LoraModulationConfigH\x00\x12\x38\n\x15\x66sk_modulation_config\x18\x04 \x01(\x0b\x32\x17.gw.FskModulationConfigH\x00\x12\r\n\x05\x62oard\x18\x05 \x01(\r\x12\x13\n\x0b\x64\x65modulator\x18\x06 \x01(\rB\x13\n\x11modulation_config\"^\n\x14LoraModulationConfig\x12\x18\n\x10\x62\x61ndwidth_legacy\x18\x01 \x01(\r\x12\x11\n\tbandwidth\x18\x03 \x01(\r\x12\x19\n\x11spreading_factors\x18\x02 \x03(\r\"S\n\x13\x46skModulationConfig\x12\x18\n\x10\x62\x61ndwidth_legacy\x18\x01 \x01(\r\x12\x11\n\tbandwidth\x18\x03 \x01(\r\x12\x0f\n\x07\x62itrate\x18\x02 \x01(\r\"\xf4\x01\n\x19GatewayCommandExecRequest\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x06 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\x12\x0f\n\x07\x65xec_id\x18\x07 \x01(\r\x12\r\n\x05stdin\x18\x04 \x01(\x0c\x12\x43\n\x0b\x65nvironment\x18\x05 \x03(\x0b\x32..gw.GatewayCommandExecRequest.EnvironmentEntry\x1a\x32\n\x10\x45nvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8b\x01\n\x1aGatewayCommandExecResponse\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x06 \x01(\t\x12\x0f\n\x07\x65xec_id\x18\x07 \x01(\r\x12\x0e\n\x06stdout\x18\x03 \x01(\x0c\x12\x0e\n\x06stderr\x18\x04 \x01(\x0c\x12\r\n\x05\x65rror\x18\x05 \x01(\t\"Y\n\x17RawPacketForwarderEvent\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x04 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"[\n\x19RawPacketForwarderCommand\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x04 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"\x80\x01\n\tConnState\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x03 \x01(\t\x12\"\n\x05state\x18\x02 \x01(\x0e\x32\x13.gw.ConnState.State\" \n\x05State\x12\x0b\n\x07OFFLINE\x10\x00\x12\n\n\x06ONLINE\x10\x01\"\x8f\x01\n\rMeshHeartbeat\x12\x12\n\ngateway_id\x18\x01 \x01(\t\x12\x10\n\x08relay_id\x18\x02 \x01(\t\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nrelay_path\x18\x04 \x03(\x0b\x32\x1a.gw.MeshHeartbeatRelayPath\"E\n\x16MeshHeartbeatRelayPath\x12\x10\n\x08relay_id\x18\x01 \x01(\t\x12\x0c\n\x04rssi\x18\x02 \x01(\x05\x12\x0b\n\x03snr\x18\x03 \x01(\x05*\xb5\x01\n\x08\x43odeRate\x12\x10\n\x0c\x43R_UNDEFINED\x10\x00\x12\n\n\x06\x43R_4_5\x10\x01\x12\n\n\x06\x43R_4_6\x10\x02\x12\n\n\x06\x43R_4_7\x10\x03\x12\n\n\x06\x43R_4_8\x10\x04\x12\n\n\x06\x43R_3_8\x10\x05\x12\n\n\x06\x43R_2_6\x10\x06\x12\n\n\x06\x43R_1_4\x10\x07\x12\n\n\x06\x43R_1_6\x10\x08\x12\n\n\x06\x43R_5_6\x10\t\x12\r\n\tCR_LI_4_5\x10\n\x12\r\n\tCR_LI_4_6\x10\x0b\x12\r\n\tCR_LI_4_8\x10\x0c*;\n\x0e\x44ownlinkTiming\x12\x0f\n\x0bIMMEDIATELY\x10\x00\x12\t\n\x05\x44\x45LAY\x10\x01\x12\r\n\tGPS_EPOCH\x10\x02*7\n\x11\x46ineTimestampType\x12\x08\n\x04NONE\x10\x00\x12\r\n\tENCRYPTED\x10\x01\x12\t\n\x05PLAIN\x10\x02*0\n\tCRCStatus\x12\n\n\x06NO_CRC\x10\x00\x12\x0b\n\x07\x42\x41\x44_CRC\x10\x01\x12\n\n\x06\x43RC_OK\x10\x02*\xd5\x01\n\x0bTxAckStatus\x12\x0b\n\x07IGNORED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0c\n\x08TOO_LATE\x10\x02\x12\r\n\tTOO_EARLY\x10\x03\x12\x14\n\x10\x43OLLISION_PACKET\x10\x04\x12\x14\n\x10\x43OLLISION_BEACON\x10\x05\x12\x0b\n\x07TX_FREQ\x10\x06\x12\x0c\n\x08TX_POWER\x10\x07\x12\x10\n\x0cGPS_UNLOCKED\x10\x08\x12\x0e\n\nQUEUE_FULL\x10\t\x12\x12\n\x0eINTERNAL_ERROR\x10\n\x12\x17\n\x13\x44UTY_CYCLE_OVERFLOW\x10\x0b\x42\xa0\x01\n\x14io.chirpstack.api.gwB\x0cGatewayProtoP\x01Z-github.com/chirpstack/chirpstack/api/go/v4/gw\xaa\x02\x12\x43hirpstack.Gateway\xca\x02\x12\x43hirpstack\\Gateway\xe2\x02\x1eGPBMetadata\\Chirpstack\\Gatewayb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gw.gw_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024io.chirpstack.api.gwB\014GatewayProtoP\001Z-github.com/chirpstack/chirpstack/api/go/v4/gw\252\002\022Chirpstack.Gateway\312\002\022Chirpstack\\Gateway\342\002\036GPBMetadata\\Chirpstack\\Gateway'
  _globals['_GATEWAYSTATS_METADATAENTRY']._loaded_options = None
  _globals['_GATEWAYSTATS_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY']._loaded_options = None
  _globals['_GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY']._serialized_options = b'8\001'
  _globals['_GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY']._loaded_options = None
  _globals['_GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY']._serialized_options = b'8\001'
  _globals['_GATEWAYSTATS_TXPACKETSPERSTATUSENTRY']._loaded_options = None
  _globals['_GATEWAYSTATS_TXPACKETSPERSTATUSENTRY']._serialized_options = b'8\001'
  _globals['_UPLINKRXINFOLEGACY_METADATAENTRY']._loaded_options = None
  _globals['_UPLINKRXINFOLEGACY_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_UPLINKRXINFO_METADATAENTRY']._loaded_options = None
  _globals['_UPLINKRXINFO_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY']._loaded_options = None
  _globals['_GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY']._serialized_options = b'8\001'
  _globals['_CODERATE']._serialized_start=7069
  _globals['_CODERATE']._serialized_end=7250
  _globals['_DOWNLINKTIMING']._serialized_start=7252
  _globals['_DOWNLINKTIMING']._serialized_end=7311
  _globals['_FINETIMESTAMPTYPE']._serialized_start=7313
  _globals['_FINETIMESTAMPTYPE']._serialized_end=7368
  _globals['_CRCSTATUS']._serialized_start=7370
  _globals['_CRCSTATUS']._serialized_end=7418
  _globals['_TXACKSTATUS']._serialized_start=7421
  _globals['_TXACKSTATUS']._serialized_end=7634
  _globals['_MODULATION']._serialized_start=136
  _globals['_MODULATION']._serialized_end=285
  _globals['_UPLINKTXINFOLEGACY']._serialized_start=288
  _globals['_UPLINKTXINFOLEGACY']._serialized_end=557
  _globals['_UPLINKTXINFO']._serialized_start=559
  _globals['_UPLINKTXINFO']._serialized_end=628
  _globals['_LORAMODULATIONINFO']._serialized_start=631
  _globals['_LORAMODULATIONINFO']._serialized_end=821
  _globals['_FSKMODULATIONINFO']._serialized_start=823
  _globals['_FSKMODULATIONINFO']._serialized_end=889
  _globals['_LRFHSSMODULATIONINFO']._serialized_start=892
  _globals['_LRFHSSMODULATIONINFO']._serialized_end=1026
  _globals['_ENCRYPTEDFINETIMESTAMP']._serialized_start=1028
  _globals['_ENCRYPTEDFINETIMESTAMP']._serialized_end=1114
  _globals['_PLAINFINETIMESTAMP']._serialized_start=1116
  _globals['_PLAINFINETIMESTAMP']._serialized_end=1178
  _globals['_GATEWAYSTATS']._serialized_start=1181
  _globals['_GATEWAYSTATS']._serialized_end=2139
  _globals['_GATEWAYSTATS_METADATAENTRY']._serialized_start=1909
  _globals['_GATEWAYSTATS_METADATAENTRY']._serialized_end=1956
  _globals['_GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY']._serialized_start=1958
  _globals['_GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY']._serialized_end=2018
  _globals['_GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY']._serialized_start=2020
  _globals['_GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY']._serialized_end=2080
  _globals['_GATEWAYSTATS_TXPACKETSPERSTATUSENTRY']._serialized_start=2082
  _globals['_GATEWAYSTATS_TXPACKETSPERSTATUSENTRY']._serialized_end=2139
  _globals['_PERMODULATIONCOUNT']._serialized_start=2141
  _globals['_PERMODULATIONCOUNT']._serialized_end=2212
  _globals['_DUTYCYCLESTATS']._serialized_start=2215
  _globals['_DUTYCYCLESTATS']._serialized_end=2348
  _globals['_DUTYCYCLEBAND']._serialized_start=2351
  _globals['_DUTYCYCLEBAND']._serialized_end=2520
  _globals['_UPLINKRXINFOLEGACY']._serialized_start=2523
  _globals['_UPLINKRXINFOLEGACY']._serialized_end=3163
  _globals['_UPLINKRXINFOLEGACY_METADATAENTRY']._serialized_start=1909
  _globals['_UPLINKRXINFOLEGACY_METADATAENTRY']._serialized_end=1956
  _globals['_UPLINKRXINFO']._serialized_start=3166
  _globals['_UPLINKRXINFO']._serialized_end=3709
  _globals['_UPLINKRXINFO_METADATAENTRY']._serialized_start=1909
  _globals['_UPLINKRXINFO_METADATAENTRY']._serialized_end=1956
  _globals['_DOWNLINKTXINFOLEGACY']._serialized_start=3712
  _globals['_DOWNLINKTXINFOLEGACY']._serialized_end=4226
  _globals['_DOWNLINKTXINFO']._serialized_start=4229
  _globals['_DOWNLINKTXINFO']._serialized_end=4392
  _globals['_TIMING']._serialized_start=4395
  _globals['_TIMING']._serialized_end=4550
  _globals['_IMMEDIATELYTIMINGINFO']._serialized_start=4552
  _globals['_IMMEDIATELYTIMINGINFO']._serialized_end=4575
  _globals['_DELAYTIMINGINFO']._serialized_start=4577
  _globals['_DELAYTIMINGINFO']._serialized_end=4636
  _globals['_GPSEPOCHTIMINGINFO']._serialized_start=4638
  _globals['_GPSEPOCHTIMINGINFO']._serialized_end=4715
  _globals['_UPLINKFRAME']._serialized_start=4718
  _globals['_UPLINKFRAME']._serialized_end=4918
  _globals['_UPLINKFRAMESET']._serialized_start=4920
  _globals['_UPLINKFRAMESET']._serialized_end=5027
  _globals['_DOWNLINKFRAME']._serialized_start=5030
  _globals['_DOWNLINKFRAME']._serialized_end=5179
  _globals['_DOWNLINKFRAMEITEM']._serialized_start=5181
  _globals['_DOWNLINKFRAMEITEM']._serialized_end=5308
  _globals['_DOWNLINKTXACK']._serialized_start=5311
  _globals['_DOWNLINKTXACK']._serialized_end=5460
  _globals['_DOWNLINKTXACKITEM']._serialized_start=5462
  _globals['_DOWNLINKTXACKITEM']._serialized_end=5514
  _globals['_GATEWAYCONFIGURATION']._serialized_start=5517
  _globals['_GATEWAYCONFIGURATION']._serialized_end=5698
  _globals['_CHANNELCONFIGURATION']._serialized_start=5701
  _globals['_CHANNELCONFIGURATION']._serialized_end=5964
  _globals['_LORAMODULATIONCONFIG']._serialized_start=5966
  _globals['_LORAMODULATIONCONFIG']._serialized_end=6060
  _globals['_FSKMODULATIONCONFIG']._serialized_start=6062
  _globals['_FSKMODULATIONCONFIG']._serialized_end=6145
  _globals['_GATEWAYCOMMANDEXECREQUEST']._serialized_start=6148
  _globals['_GATEWAYCOMMANDEXECREQUEST']._serialized_end=6392
  _globals['_GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY']._serialized_start=6342
  _globals['_GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY']._serialized_end=6392
  _globals['_GATEWAYCOMMANDEXECRESPONSE']._serialized_start=6395
  _globals['_GATEWAYCOMMANDEXECRESPONSE']._serialized_end=6534
  _globals['_RAWPACKETFORWARDEREVENT']._serialized_start=6536
  _globals['_RAWPACKETFORWARDEREVENT']._serialized_end=6625
  _globals['_RAWPACKETFORWARDERCOMMAND']._serialized_start=6627
  _globals['_RAWPACKETFORWARDERCOMMAND']._serialized_end=6718
  _globals['_CONNSTATE']._serialized_start=6721
  _globals['_CONNSTATE']._serialized_end=6849
  _globals['_CONNSTATE_STATE']._serialized_start=6817
  _globals['_CONNSTATE_STATE']._serialized_end=6849
  _globals['_MESHHEARTBEAT']._serialized_start=6852
  _globals['_MESHHEARTBEAT']._serialized_end=6995
  _globals['_MESHHEARTBEATRELAYPATH']._serialized_start=6997
  _globals['_MESHHEARTBEATRELAYPATH']._serialized_end=7066
# @@protoc_insertion_point(module_scope)
