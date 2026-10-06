# Capability inventory

[Documentation home](../README.md) · [Status definitions and revisions](status.md)

This is a functional index, not a release checklist. All firmware applications remain
experimental, including rows marked implemented. Follow each area's reference for
precise behavior, supported versions and tests.

| Capability | Owner | Snapshot status | Boundary or limitation |
| --- | --- | --- | --- |
| DHT22/AM2302 temperature and humidity | Transmitter | Implemented | WiFi LoRa 32 V3 reference target |
| SHT4x driver and Stick Lite V3 target | Transmitter | Experimental / PR #25 | USB-only target; not in signed/web releases |
| CRC validation of SHT4x readings | Sensor driver | Experimental / PR #25 | Invalid readings become errors, not zero measurements |
| Sensor power switching and deep sleep | Transmitter | Implemented; SHT4x path in PR #25 | Actual consumption not established by tests |
| Battery voltage and low-battery schedule | Transmitter | Implemented, unvalidated calibration | Thresholds provisional; USB readings may reflect charger |
| Stable device identity and binding keys | Both radio roles | Implemented | Public IDs are not credentials |
| USB enrollment, resume and revocation | Provisioning tool + firmware | Implemented | Identify device, not just serial port |
| Operator-triggered radio pairing | Both radio roles | Implemented | Two-minute window; active-attacker authentication pending |
| AES-128-GCM protected DATA/ACK | Protocol | Implemented | No independent security audit |
| Counter reservation and replay handling | Protocol/storage | Implemented | Never restore old counter state under the same key |
| Channel assessment, jitter and bounded retries | Sender/radio | Implemented | No collision-free guarantee or TDMA |
| Queue-before-ACK durable acceptance | Receiver | Implemented | ACK confirms receiver acceptance, not server delivery |
| Bounded persistent forwarding queue | Receiver | Implemented | Newest 128 samples; oldest dropped when full |
| Unconfirmed sample backlog on transmitter | Transmitter | Not implemented | Failed cycle is logged; not kept for a later wake |
| RSSI and SNR telemetry | Receiver | Implemented | Measured for the received frame, not ambient sensor data |
| Configurable transmit-power ceiling | Device settings | Implemented | Region/antenna compliance not auto-configured |
| Power command in version-2 ACK | Protocol | Implemented | Receiver policy currently requests no change |
| Temporary Wi-Fi setup page | Receiver | Implemented | Open AP after physical action; local safeguards are not AP authentication |
| Network selector and scan recovery | Receiver | Experimental / PR #25 | Manual hidden-network entry remains available |
| Save verified Wi-Fi without MQTT | Receiver | Experimental / PR #25 | Wi-Fi-only storage v2; physical power-cycle validation pending |
| Read-only setup visit preserves MQTT | Receiver | Experimental / PR #25 | Recovery policy tested; physical no-disconnect test pending |
| Find broker through mDNS | Receiver + host announcer | Implemented | Finds address; does not provision credentials |
| QoS 1 forwarding and PUBACK removal | Receiver | Implemented | Broker boundary only; correct ACLs required |
| Online/offline state and Last Will | Receiver + broker | Implemented | Abrupt loss detected after timeout, not instantly |
| Pairing/revocation commands over MQTT | Receiver + authorized client | Implemented | Consumer-independent management channel |
| HA MQTT Discovery | Receiver | Implemented; integration partially validated | Supported registry only; full running HA validation pending |
| Atomic sample storage and deduplication | Central | Implemented | Source/device/sample identity; conflicting content rejected |
| Durable MQTT consumer session | Central + broker | Implemented | Bounded broker queues and session expiry |
| Names, locations and dashboard arrangement | Central | Implemented | Registration does not enroll a radio |
| History, CSV export and silence indication | Central | Implemented | Arrival time is not necessarily measurement time |
| Receiver setup assistant and item removal | Central | Implemented, PR #33 merged | Removing a list item does not revoke radio/MQTT access |
| Compact MQTT diagnostic table | Central | Implemented, PR #33 merged | Last 100 observations; subscribed topics only; volatile |
| Live receiver/dashboard state through SSE | Central | Implemented, PR #33 merged | Does not reduce broker failure-detection time |
| English and Brazilian Portuguese UI | Central | Implemented | Source documentation remains English |
| Signed receiver updates and rollback | Firmware/release tooling | Implemented | Local uploaded package; hardware/security limits apply |
| Transmitter updates over LoRa | Firmware | Not implemented | USB update path remains separate |
| Arbitrary sensors and automatic driver selection | Transmitter | Planned direction | A connector alone cannot add software support |
| LoRaWAN, mesh, TDMA and actuator control | Radio/application | Not implemented | Current network is direct LoRa telemetry |
| NFC pairing, dedicated OS and native Windows installer | Ecosystem | Future ideas, not implemented | Not prerequisites for the current architecture |

## Evidence by area

- Sensors, power and applications: [radio applications](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md),
  [Stick Lite](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/stick-lite.md).
- Radio delivery and storage: [protocol](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/protocol-v1.md),
  [runtime](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/runtime.md), [persistence](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/persistence.md).
- Setup and administration: [USB](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/provisioning.md),
  [radio pairing](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-pairing.md), [management](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/management-v1.md).
- MQTT/HA: [forwarding](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md),
  [Discovery](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/home-assistant.md).
- Monitoring, setup assistant and SSE: [Central README](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md).
- Maintenance: [updates](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/updates.md), [testing](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/testing.md).

Future ideas are context, not approved implementation schedules. See
[status](status.md) before using this inventory as a build plan.
