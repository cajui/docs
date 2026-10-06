# MQTT and integrations

[Documentation home](../README.md) · [Measurement journey](data-flow.md)

The broker routes messages between clients. It is a service, not a Cajuí radio board.
The receiver is a publisher and a management-command subscriber. Central and Home
Assistant are consumers with different responsibilities and accounts.

## Message families

| Family | Topic pattern | Purpose | Retained? |
| --- | --- | --- | --- |
| Telemetry | `telemetry/v1/<source>/<node>/samples` | Environmental and diagnostic readings | No |
| Availability | `manage/v1/<source>/<device>/availability` | Receiver online/offline | Yes |
| State | `manage/v1/<source>/<device>/state` | Queue, firmware, pairing and node state | Yes |
| Commands | `manage/v1/<source>/<device>/commands` | Supported administrative actions | No |
| Results | `manage/v1/<source>/<device>/results` | Outcome of requested action | No |
| HA Discovery | `homeassistant/sensor/<source>/<object>/config` | Entity definitions for Home Assistant | Yes |

Here `source` is the receiver's MQTT username, not its display name. Use the exact
identity restrictions in the linked contracts; the allowed character sets for telemetry
and HA Discovery differ. A username with a dot can work for telemetry while disabling
HA Discovery in the current firmware.

## Three different kinds of discovery

- **Broker discovery (mDNS):** receiver finds an advertised MQTT address on the local network.
  It still needs credentials. The host announcement must actually run, and multicast
  must be reachable; Docker Desktop does not automatically advertise that service to the LAN.
- **Radio pairing discovery:** receiver lists transmitters asking to join during an authorized window.
  Finding a candidate is not approving it.
- **Home Assistant MQTT Discovery:** receiver publishes definitions of supported entities
  so HA knows their measurements, units and availability topics.

## Home Assistant without Central

Use a broker reachable by the receiver and Home Assistant. Give the receiver permissions
for its telemetry, management and Discovery namespaces; give HA the required subscriptions.
Enable HA's MQTT integration with the default `homeassistant` Discovery prefix.
The receiver then announces supported entities; Central is not in the path.

Current entities include temperature/humidity and diagnostic radio, battery and receiver
state where available. This is a registry of supported metrics, not universal recognition
of every I2C sensor. The implementation and template outputs have been checked, but the
referenced firmware documentation does not claim validation against a running HA installation.

## Permissions and persistence

Keep producer and consumer accounts separate. Do not distribute Central's account to
receivers. The included stack can create/import/revoke producer credentials; the current
Central setup assistant uses a configured receiver account rather than generating a
new isolated account per device.

Central uses a persistent MQTT session. The bundled broker configuration bounds its
queue to 1000 messages per client and expires sessions after seven days of absence.
These are configuration limits, not inherent MQTT promises. Retained state describes
last-known values; telemetry history belongs to a consumer database. A broker restart,
incorrect ACL or full queue must be diagnosed separately from radio delivery.

Sources: [Central MQTT configuration](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md),
[management contract](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/management-v1.md),
[Home Assistant contract and ACLs](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/home-assistant.md).
