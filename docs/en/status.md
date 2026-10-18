# Project status and compatibility

English | [Português brasileiro](../pt-BR/status.md)

[Documentation](../../README.md)

Cajuí is under active development. The firmware applications are experimental.
Supported features and known limitations are listed below; the [feature reference](inventory.md)
provides the complete subsystem index.

## Documentation versions

This documentation covers the following source revisions, checked on 2026-10-17:

| Project | Revision | Availability at documentation update |
| --- | --- | --- |
| Cajuí Central | [`23ee539`](https://github.com/cajui/cajui-central/tree/23ee539454c133fee42e020975e7d3dc662937e9) | Main branch, including persisted history from [PR #46](https://github.com/cajui/cajui-central/pull/46) |
| Cajuí Firmware | [`de9ddaa`](https://github.com/cajui/cajui-firmware/tree/de9ddaa602faa6507a686a9f468d8f7377fd09dd) | Main branch; experimental applications |

Technical reference links target these revisions. Installed images and published releases
may contain an earlier feature set.

The main branch includes the Stick Lite/SHT4x target, Wi-Fi scan recovery,
independent persistence of verified Wi-Fi settings and MQTT recovery improvements.
The Stick Lite target supports USB installation and is excluded from signed/web release
artifacts at this version.

## Feature labels

- **Implemented:** available in the documented implementation.
- **Validation pending:** implemented behavior with outstanding physical or integration checks.
- **Unsupported:** outside the current implementation.

These labels describe software availability; hardware compatibility and validation
requirements still apply.

## Known limitations

### Radio and hardware

Radio range, operation under sustained interference, capacity at scale, sleep consumption,
battery calibration and low-voltage thresholds require further measurement. Physical
storage testing for arbitrary power loss and flash endurance is incomplete.

Current sensor applications support the documented climate sensors. Additional drivers
and application configuration are required for other models. The protocol provides direct
LoRa telemetry; LoRaWAN, mesh, TDMA and actuator control are unsupported.

### Security

The protocol has not undergone an independent security audit. Radio pairing lacks
active-attacker authentication. The temporary setup access point is open while enabled,
and the receiver uses plain MQTT rather than TLS. Deploy within the trust boundaries
specified in [radio and security](radio-security.md).

### Integration testing

Home Assistant Discovery messages and templates have been checked; testing against a
running Home Assistant installation remains pending. The development firmware's
Wi-Fi-only persistence across physical power cycles and uninterrupted MQTT during a
read-only setup visit also require hardware verification.

## Technical references

| Subject | Reference |
| --- | --- |
| Firmware capabilities | [README](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/README.md) |
| Radio protocol | [Specification](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/protocol-v1.md) |
| Delivery state machine | [Runtime](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/runtime.md) |
| Durable records and queue | [Persistence](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/persistence.md) |
| Board behavior and MQTT forwarding | [Applications](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/radio-applications.md) |
| Stick Lite/SHT4x | [Board guide](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/stick-lite.md) |
| Provisioning and pairing | [USB](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/provisioning.md), [radio](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/radio-pairing.md) |
| MQTT management | [Contract](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/management-v1.md) |
| Home Assistant | [Integration](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/home-assistant.md) |
| Installation and updates | [Firmware updates](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/updates.md) |
| Central APIs and configuration | [Central README](https://github.com/cajui/cajui-central/blob/23ee539454c133fee42e020975e7d3dc662937e9/README.md) |
