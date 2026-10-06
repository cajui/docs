# Feature reference

English | [Português brasileiro](../pt-BR/inventory.md)

[Documentation](../../README.md)

Features are grouped by subsystem. Status labels refer to the versions listed in
[project status](status.md); firmware applications remain experimental.

## Sensors and power

| Feature | Status | Details |
| --- | --- | --- |
| DHT22/AM2302 readings | Implemented | Temperature and humidity on the WiFi LoRa 32 V3 transmitter |
| SHT4x readings | Development | I2C driver and Wireless Stick Lite V3 target |
| SHT4x CRC validation | Development | Checks both response words and reports measurement errors |
| Sensor supply switching and deep sleep | Implemented; SHT4x integration in development | Sensor power is disabled between reporting cycles |
| Battery measurement and low-voltage scheduling | Validation pending | Divider calibration and thresholds require hardware measurement |

References: [sensor applications](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md),
[Stick Lite](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/stick-lite.md).

## Radio and enrollment

| Feature | Status | Details |
| --- | --- | --- |
| Stable identities and per-binding keys | Implemented | Network and node IDs identify devices; keys authorize communication |
| USB enrollment, resume and revocation | Implemented | Provisioning tool with recovery support |
| Operator-triggered radio pairing | Implemented | Two-minute window and candidate approval; active-attacker authentication pending |
| AES-128-GCM DATA/ACK protection | Implemented | Authenticated payloads with per-binding credentials |
| Durable counters and replay handling | Implemented | Counter reservation and persisted acceptance records |
| Channel assessment and bounded retries | Implemented | Jitter and retry limits reduce contention |
| Configurable transmit-power ceiling | Implemented | Per-device setting within the radio's range |
| Version-2 ACK power command | Implemented | Protocol supports a command; the receiver currently requests no change |
| RSSI and SNR readings | Implemented | Receiver reports diagnostics for accepted radio frames |

References: [protocol](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/protocol-v1.md), [runtime](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/runtime.md),
[USB provisioning](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/provisioning.md), [pairing](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-pairing.md).

## Receiver setup and forwarding

| Feature | Status | Details |
| --- | --- | --- |
| Durable acceptance before radio ACK | Implemented | Receipt and sample are committed before acknowledgement |
| Persistent sample queue | Implemented | Holds the newest 128 samples; counts dropped oldest entries |
| QoS 1 MQTT forwarding | Implemented | Removes a queued sample after its matching publisher PUBACK |
| Temporary Wi-Fi setup page | Implemented | Button-triggered access point, configuration and status |
| Network selector and scan recovery | Development | Bounded scan retries and manual hidden-network entry |
| Independent Wi-Fi persistence | Development | Saves verified Wi-Fi before MQTT configuration |
| MQTT recovery after Wi-Fi trials | Development | Restores suspended connections with bounded retries |
| Broker discovery | Implemented | mDNS address discovery with a host announcement |
| Availability and device state | Implemented | Retained MQTT state and receiver Last Will |
| MQTT pairing and revocation commands | Implemented | Available to authorized clients through the management channel |
| Home Assistant MQTT Discovery | Implemented; integration validation pending | Publishes supported entity definitions |

References: [applications](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md),
[management](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/management-v1.md), [Home Assistant](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/home-assistant.md).

## Monitoring

| Feature | Status | Details |
| --- | --- | --- |
| Atomic storage and sample deduplication | Implemented | Source/device/sample identity with conflict detection |
| Persistent MQTT consumer session | Implemented | Broker buffers messages within configured limits |
| Device and sensor registration | Implemented | Display names and locations |
| Dashboard arrangement | Implemented | Sections containing devices, sensors or individual measurements |
| History and CSV export | Implemented | Stored readings and measurement-quality indicators |
| Silence detection | Implemented | Based on new unique samples and expected reporting intervals |
| Receiver setup assistant | Implemented | Connection details and incoming-state verification |
| Receiver and sensor list removal | Implemented | Preserves history; qualifying observations restore items |
| MQTT diagnostic table | Implemented | Last 100 subscribed observations in memory |
| Live connection-state updates | Implemented | SSE with interruption recovery |
| UI localization | Implemented | English and Brazilian Portuguese |

Reference: [Central configuration and interface](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md).

## Maintenance

| Feature | Status | Details |
| --- | --- | --- |
| Signed receiver updates | Implemented | Locally uploaded packages with verification |
| Application rollback | Implemented | Two application slots and boot validation |
| USB installation and updates | Implemented | Separate new-board and storage-preserving update procedures |

Reference: [firmware updates](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/updates.md).

## Unsupported capabilities

Current applications do not provide arbitrary sensor-driver selection, transmitter
sample backlogs across reporting cycles, transmitter firmware updates over LoRa,
LoRaWAN, mesh routing, TDMA or actuator control. See [project status](status.md) for
compatibility and validation requirements.
