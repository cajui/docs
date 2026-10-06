# Glossary

[Documentation](../README.md)

| Term | Definition |
| --- | --- |
| Cajuí | The sensor telemetry ecosystem, including firmware and monitoring software |
| Cajuí Central | The monitoring server and web application |
| Sensor | A component that measures one or more physical quantities |
| Metric | A quantity identifier, such as temperature or relative humidity |
| Reading | A metric's value or quality status in a sample |
| Sample | A group of readings sharing a delivery identity |
| Transmitter / node | An enrolled radio device that acquires and sends samples |
| Receiver | A radio device that accepts samples and forwards them to MQTT |
| Firmware | Software installed on a board |
| LoRa | The modulation used for the radio link |
| LoRaWAN | A networking protocol built on LoRa, unsupported by the current firmware |
| Radio profile | Frequency and modulation settings shared by communicating devices |
| CAD | Channel activity detection before transmission |
| RSSI | Received signal strength, expressed in dBm |
| SNR | Signal-to-noise ratio, expressed in dB |
| Enrollment / binding | An authorized association between a node, network and credentials |
| Radio ACK | Authenticated acknowledgement of receiver acceptance |
| MQTT | Publish/subscribe messaging between receivers, broker and applications |
| Broker | Server that routes MQTT messages to subscribed clients |
| Topic | Message channel within the broker |
| QoS 1 | MQTT delivery level with acknowledgement and possible duplicates |
| PUBACK | MQTT acknowledgement of a QoS 1 publication |
| ACL | Access-control rules governing an account's topic permissions |
| Retained message | The broker's stored last value for a topic |
| Last Will | Message published by the broker after an unexpected client disconnection |
| mDNS | Local service-discovery mechanism used to locate an advertised broker |
| MQTT Discovery | Entity-definition messages used by Home Assistant |
| Queue | Samples awaiting forwarding to the next delivery stage |
| Replay | Reuse of an earlier frame, evaluated against persisted acceptance state |
| Deduplication | Recognition of repeated sample identities |
| Vext / Ve | Switched external sensor supply on the reference board |
| I2C / SDA / SCL | Sensor bus and its data and clock signals |
| Qwiic / STEMMA QT | Connector conventions for compatible I2C wiring |
| SSE | Server-sent events used to update browser device state |
| SQLite | The database used by Central |
| OTA slot | An application partition used during firmware updates and rollback |

See [architecture](overview.md) for component relationships and
[data flow](data-flow.md) for delivery semantics.
