# Glossary

[Documentation home](../README.md)

| Term | Meaning in this project |
| --- | --- |
| Cajuí | The ecosystem of firmware, radio devices and monitoring software |
| Cajuí Central | The monitoring application; not the LoRa receiver |
| Sensor | A physical component measuring one or more quantities |
| Metric / measurement | A quantity such as temperature or humidity |
| Sample | A group of readings with a shared identity |
| Transmitter / node | Enrolled remote device that reads and sends samples |
| Receiver | LoRa device that accepts samples and forwards them to MQTT |
| Firmware | Program running on a board |
| LoRa | Radio modulation used for the link |
| LoRaWAN | A distinct networking protocol; not implemented by this firmware |
| Radio profile | Shared modulation/frequency settings required for communication |
| CAD | Channel activity detection before a send attempt; not collision prevention |
| RSSI | Received signal strength, reported in dBm |
| SNR | Signal-to-noise ratio, reported in dB |
| Enrollment / binding | Association of node, network and credentials |
| Radio ACK | Authenticated confirmation of receiver acceptance |
| MQTT | Publish/subscribe messaging used between receiver, broker and applications |
| Broker | Server routing MQTT publications to subscribers |
| Topic | Address-like message channel within the broker |
| QoS 1 / PUBACK | MQTT acknowledged publication with possible duplicate delivery |
| ACL | Rules granting an account access to specific topics |
| Retained message | Broker's last saved value for a topic; not full history |
| Last Will | Message broker publishes after an unexpected client disconnection |
| mDNS | Local discovery mechanism used to find an advertised broker |
| MQTT Discovery | HA entity-definition messages; different from mDNS |
| Queue | Pending samples awaiting their next delivery boundary |
| Replay | Reuse of an old authenticated frame; handled through durable state |
| Deduplication | Recognizing repeated sample identities instead of storing them twice |
| Vext / Ve | Switched external sensor supply on the reference board |
| I2C / SDA / SCL | Sensor bus and its data/clock signals |
| Qwiic / STEMMA QT | Connector conventions for compatible I2C wiring |
| SSE | Server-sent events for updating the browser's device state |
| SQLite | Central's local database |
| OTA slot | An application partition used by firmware update/rollback mechanisms |

For exact contracts, follow [the evidence index](status.md).
