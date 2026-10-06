# Project status and compatibility

[Documentation](../README.md)

Cajuí is under active development. The firmware applications are experimental.
Supported features and known limitations are listed below; the [feature reference](inventory.md)
provides the complete subsystem index.

## Documentation versions

This documentation covers the following source revisions, checked on 2026-10-06:

| Project | Revision | Availability at documentation update |
| --- | --- | --- |
| Cajuí Central | [`76a9a18`](https://github.com/cajui/cajui-central/tree/76a9a189d9a8101bc74b07f6723f9541f9acb05d) | Included through merged [PR #33](https://github.com/cajui/cajui-central/pull/33) |
| Cajuí Firmware | [`a2ce332`](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968) | Development branch, [PR #25](https://github.com/cajui/cajui-firmware/pull/25) |

Technical reference links target these revisions. Installed images and published releases
may contain an earlier feature set.

The development firmware adds the Stick Lite/SHT4x target, Wi-Fi scan recovery,
independent persistence of verified Wi-Fi settings and MQTT recovery improvements.
The Stick Lite target supports USB installation and is excluded from signed/web release
artifacts at this version.

## Feature labels

- **Implemented:** available in the documented implementation.
- **Development:** available in the firmware development revision above.
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
| Firmware capabilities | [README](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/README.md) |
| Radio protocol | [Specification](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/protocol-v1.md) |
| Delivery state machine | [Runtime](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/runtime.md) |
| Durable records and queue | [Persistence](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/persistence.md) |
| Board behavior and MQTT forwarding | [Applications](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md) |
| Stick Lite/SHT4x | [Board guide](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/stick-lite.md) |
| Provisioning and pairing | [USB](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/provisioning.md), [radio](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-pairing.md) |
| MQTT management | [Contract](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/management-v1.md) |
| Home Assistant | [Integration](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/home-assistant.md) |
| Installation and updates | [Firmware updates](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/updates.md) |
| Central APIs and configuration | [Central README](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md) |
