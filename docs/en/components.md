# Components

English | [Português brasileiro](../pt-BR/components.md)

[Documentation](../../README.md)

## System components

| Component | Location | Responsibilities | Dependencies |
| --- | --- | --- | --- |
| Sensor | Measurement point | Measures environmental quantities | Compatible supply, wiring and driver |
| Transmitter | Remote radio board | Reads sensors, encrypts frames, sends samples and processes ACKs | Sensor, power, antenna and enrollment |
| Receiver | Radio board with network access | Validates frames, queues samples, sends ACKs and publishes MQTT | Antenna, persistent storage, Wi-Fi and broker configuration |
| MQTT broker | Network host | Routes messages and enforces topic permissions | Network listener, accounts and ACLs |
| Cajuí Central | Computer or server | Stores readings, provides monitoring and requests device-management actions | SQLite and MQTT for receiver traffic |
| Browser | Client computer or tablet | Presents Central's web interface | Access permitted by Central's interface policy |
| Home Assistant | Separate service | Consumes telemetry and entity definitions | MQTT integration and broker permissions |

## Firmware targets

| Target | Board | Role | Sensor |
| --- | --- | --- | --- |
| `runtime_tx` | Heltec WiFi LoRa 32 V3 | Transmitter | DHT22/AM2302 |
| `runtime_rx` | Heltec WiFi LoRa 32 V3 | Receiver | Receives enrolled nodes |
| `runtime_tx_stick_lite` | Heltec Wireless Stick Lite V3 | Transmitter | SHT4x over I2C |

The Stick Lite target is in development and supports USB installation only. See
[version coverage](status.md) before selecting an image. Board profiles define pin
assignments and display behavior; use the image built for the target board.

## Sensor interfaces

DHT22/AM2302 uses a data signal and a DHT driver. SHT4x uses I2C with SDA, SCL, power
and ground. The sensor model determines the driver and supported measurements.

Passive Qwiic/STEMMA QT adapters provide compatible I2C wiring. Direct wiring with the
same electrical connections uses the same driver. Connector compatibility alone does
not establish voltage compatibility, address availability or firmware support.

The experimental Stick Lite profile assigns GPIO33 to SDA and GPIO34 to SCL, with
GPIO35 reserved for the onboard LED. Refer to the [board guide](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/stick-lite.md)
for wiring and power sequencing. The [reference applications](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md)
document the DHT22 mapping and receiver configuration.

## Power and antennas

Transmitters switch the sensor supply and enter deep sleep between reporting cycles.
The receiver remains available for radio reception and Wi-Fi forwarding. Both roles
transmit: receivers send acknowledgements and pairing messages. Fit each board with a
suitable LoRa antenna before radio operation.

Battery-voltage measurement and low-battery scheduling are implemented. Divider
calibration, thresholds and sleep consumption require further hardware validation.
Battery protection is an electrical design requirement separate from firmware power
management. See [project limitations](status.md) for validation status.
