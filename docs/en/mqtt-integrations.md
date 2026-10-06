# MQTT and integrations

English | [Português brasileiro](../pt-BR/mqtt-integrations.md)

[Documentation](../../README.md)

The MQTT broker connects receivers to monitoring applications. Receivers publish
telemetry, device state and Home Assistant entity definitions. Authorized clients can
request supported administrative actions through the management channel.

## Topics

| Family | Topic pattern | Purpose | Retained |
| --- | --- | --- | --- |
| Telemetry | `telemetry/v1/<source>/<node>/samples` | Sensor and diagnostic readings | No |
| Availability | `manage/v1/<source>/<device>/availability` | Receiver online/offline status | Yes |
| State | `manage/v1/<source>/<device>/state` | Queue, firmware, pairing and node state | Yes |
| Commands | `manage/v1/<source>/<device>/commands` | Administrative requests | No |
| Results | `manage/v1/<source>/<device>/results` | Command outcomes | No |
| HA Discovery | `homeassistant/sensor/<source>/<object>/config` | Entity definitions | Yes |

`source` is the receiver's MQTT username. Identifiers must satisfy the restrictions of
each contract. In particular, the current Home Assistant integration requires a source
containing only letters, digits, underscores and hyphens. A username containing a dot
can publish telemetry but disables Discovery publication.

## Broker discovery

The receiver can search the local network for an mDNS `_mqtt._tcp` announcement.
Discovery supplies the broker address and port; authentication requires separately
configured credentials.

The broker host must advertise the service on a network reachable by the receiver.
On Docker Desktop, run the project's announcement helper on the host because container
multicast is not automatically exposed to the LAN. Manual address entry is available
when multicast discovery is unavailable.

## Home Assistant

Configure the receiver and Home Assistant to use a reachable broker, then enable Home
Assistant's MQTT integration with the default `homeassistant` Discovery prefix.
The receiver publishes retained entity definitions for supported metrics. Central is
optional and can run alongside Home Assistant.

Supported entities include temperature, humidity, radio diagnostics, battery voltage
and receiver diagnostics where available. Entity availability follows receiver status
and measurement-expiry rules. Driver support is required for additional sensor models.

Discovery publications and templates have been tested; validation against a running
Home Assistant installation remains pending. See the [integration reference](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/home-assistant.md)
for entity definitions, topic permissions and handling of old retained configurations.

## Accounts and permissions

Use separate receiver and application accounts. Grant each receiver access to its
telemetry, management and Discovery namespaces. Grant consumers the subscriptions they
need; administrative commands require additional permissions.

The bundled stack includes tools to create, import and revoke producer credentials.
Central's receiver setup assistant uses a configured producer account; it does not
create a new account for each device. Current receiver connections use plain MQTT on
a trusted network.

## Sessions and retention

Central uses a persistent MQTT session. The bundled broker configuration permits up to
1000 queued messages per client and expires a session after seven days of absence.
Adjustments to broker configuration can change these limits.

Retained messages provide last-known state and entity definitions. Telemetry is published
without retention; historical readings are stored by consuming applications. MQTT QoS 1
permits duplicate delivery, handled by Central through sample identity.

## References

[MQTT management](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/management-v1.md) ·
[Central broker configuration](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md) · [Delivery semantics](data-flow.md)
