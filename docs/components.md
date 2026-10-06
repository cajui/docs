# Components and responsibilities

[Documentation home](../README.md) · [Inventory](inventory.md)

| Component | Runs or lives where | Responsibility | Depends on | Does not do |
| --- | --- | --- | --- | --- |
| Sensor | At the measurement point | Measures environmental quantities | Correct supply, wiring and a supported driver | Send LoRa by itself |
| Transmitter | Remote radio board | Samples, identifies, encrypts, sends and waits for radio ACK | Sensor, energy, antenna, enrollment and compatible radio profile | Publish MQTT in normal operation |
| Receiver | Radio board near network coverage | Validates radio frames, durably queues samples, ACKs and forwards | Antenna, healthy storage, Wi-Fi and broker settings for forwarding | Provide the historical dashboard |
| Broker | Network host or service | Routes MQTT publications to authorized subscribers | Reachable listener, credentials and ACLs | Understand sensor semantics or pair radios |
| Cajuí Central | Computer/server | Validates, stores, names and displays readings; requests supported management actions | SQLite; MQTT for receiver traffic | Replace receiver radio hardware |
| Browser | User's computer or tablet | Displays the Central interface | Access to Central under its local-access policy | Receive LoRa frames |
| Home Assistant | Separate installation | Consumes supported telemetry and Discovery entities | Its MQTT integration and broker permissions | Require Central to forward its data |

## Physical connections

DHT22/AM2302 uses its data signal and a DHT driver. SHT4x uses I2C SDA/SCL plus
power and ground. The reference boards have different firmware targets and explicit
pin assignments; similar connectors do not make their images interchangeable.

A passive Qwiic/STEMMA QT adapter changes the physical connection, not the sensor
protocol. Equivalent correctly wired connections do not need a different driver.
A cable gland secures a cable at an enclosure opening; it is not an electrical
connector. A removable external connector such as M8 would also need an agreed
pin assignment and suitable electrical/environmental ratings. No enclosure design
or certified ingress-protection rating is specified here.

See the [reference applications](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md) and experimental
[Stick Lite wiring](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/stick-lite.md) for actual board mappings. The Stick Lite
target uses GPIO33/SDA and GPIO34/SCL; GPIO35 is the onboard LED. Do not infer wiring
from another ESP32 board's pin numbers.

## Power and antennas

Transmitters use deep sleep and switch the sensor supply off between cycles.
The receiver stays available to receive packets and forwards them over Wi-Fi.
Both roles transmit: a receiver sends radio ACKs. Use a suitable connected LoRa
antenna on both, even for a short bench test. Minimum transmit power does not make
an antenna-free test safe.

Battery-voltage measurement and low-battery scheduling exist, but divider calibration,
thresholds and sleep consumption still need physical validation. Firmware does not
substitute for a battery protection circuit. No finalized custom PCB or battery
protection assembly is published in this repository.

Source: [power, radio and validation boundaries](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md).
