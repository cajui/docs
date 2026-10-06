# Evidence and implementation status

[Documentation home](../README.md) · [Inventory](inventory.md)

Reviewed on **2026-10-06** against these public revisions:

| Project | Reviewed revision | Integration status at review |
| --- | --- | --- |
| Cajuí Central | [`76a9a18`](https://github.com/cajui/cajui-central/tree/76a9a189d9a8101bc74b07f6723f9541f9acb05d) | [PR #33](https://github.com/cajui/cajui-central/pull/33) merged |
| Cajuí Firmware | [`a2ce332`](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968) | [PR #25](https://github.com/cajui/cajui-firmware/pull/25) open |

Links in these guides are pinned to those revisions so that evidence remains inspectable
when branches move. They do not assert that a checkout of `main`, an installed image or
a published release already contains every feature. Refresh this table and affected pages
when adopting a newer baseline.

## Reading a status

- **Implemented:** behavior exists in the reviewed source. Release availability and
  physical validation are separate questions.
- **Experimental / PR:** source exists but is still under review or excluded from normal
  release/install paths. Current firmware applications are experimental in general.
- **Planned / not implemented:** describes a direction or absence, not a supported option.
- **Unvalidated:** the relevant observation or independent check has not been established.

## Known evidence gaps

- Radio range, collisions at scale, sustained cadence and real sleep consumption.
- Battery divider calibration and provisional low-voltage thresholds.
- Arbitrary power-loss behavior and flash endurance on the physical storage adapter.
- Independent security audit and active-attacker authentication during radio pairing.
- Receiver MQTT TLS and authenticated setup access point.
- Full Home Assistant installation test (Discovery messages/templates have narrower checks).
- PR #25 Wi-Fi-only power-cycle persistence and read-only setup visit without MQTT interruption.

The project does not provide a finalized public enclosure/custom PCB assembly here.
NFC pairing, a dedicated OS distribution, a native Windows installer and LoRaWAN are not
current capabilities. These directions are not delivery commitments.

## Source-of-truth index

| Subject | Owning reference |
| --- | --- |
| Firmware implementation and limits | [README](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968/README.md) |
| Radio wire format and ACK | [Protocol](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968/docs/protocol-v1.md) |
| Runtime delivery | [Runtime](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968/docs/runtime.md) |
| Durable state | [Persistence](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968/docs/persistence.md) |
| Board behavior and MQTT forwarding | [Applications](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md) |
| Stick Lite/SHT4x | [Board guide](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968/docs/stick-lite.md) |
| Provisioning and pairing | [USB](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968/docs/provisioning.md), [radio](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-pairing.md) |
| MQTT state and commands | [Management](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968/docs/management-v1.md) |
| Home Assistant | [Integration](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968/docs/home-assistant.md) |
| Signed updates and installation | [Updates](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968/docs/updates.md) |
| Monitoring, UI and consumer semantics | [Central README](https://github.com/cajui/cajui-central/tree/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md) |

When source documentation contains historical wording inconsistent with a newer section,
check the implementation and revision before generalizing. File a correction in the owning
project rather than silently inventing a contract in this repository.
