# Operations and diagnosis

[Documentation home](../README.md) · [Setup](setup.md)

Work along the [measurement path](data-flow.md). A success at one boundary is not proof
that later boundaries succeeded. Do not erase storage as the first troubleshooting step.

| Symptom | Inspect first | Interpretation / next check |
| --- | --- | --- |
| No USB response | Data-capable cable, port and stable device ID | A charging cable or changed port is not lost enrollment |
| Sensor error but radio ACK succeeds | Sensor power, pin mapping and driver | Radio delivery can work while sensing fails |
| No radio ACK | Antennas, matching profile, enrollment, device/storage faults | Wi-Fi/MQTT is not required to durably accept a radio sample |
| Receiver says Wi-Fi connected, Central offline | Broker address, credentials, ACLs and subscriptions | Wi-Fi connection alone does not reach the application |
| Broker search returns nothing | Host mDNS announcement and multicast reachability | Enter a reachable address manually; search is optional |
| Queue grows | Broker reachability and matching PUBACKs | Capacity is finite; inspect dropped-sample count |
| Queue drains but no downstream readings | ACLs, topic identity, consumer connection and validation logs | MQTT 3.1.1 can acknowledge denied publications |
| Receiver stays online briefly after unplugging | MQTT keepalive/Last Will | The UI cannot detect physical loss before evidence arrives |
| Connected receiver, stale transmitter | Last unique sample and expected interval | Sleeping transmitters have no continuous online connection |
| New arrivals have suspiciously old conditions | Backlog and arrival-time semantics | Forwarded time is not measurement time |
| HA has no entities | Discovery ACL, prefix, username and supported metrics | Telemetry may work even when Discovery is disabled |
| Removed item returns | New telemetry or live state | List removal does not block producers |

## Keep three kinds of information separate

1. **Measurements:** environmental and diagnostic readings saved as history.
2. **Device state:** latest queue, uptime, firmware, pairing and availability.
3. **Logs/diagnostic buffer:** temporary explanations of what the software did.

Record which one supports a diagnosis. An old RSSI value displayed next to an offline
badge is not proof the receiver is currently connected.

## Updates and recovery

Back up the Central database before schema upgrades. Preserve firmware enrollment,
cryptographic counters and queued samples during normal updates. A new-board install
is destructive to existing enrollment, unlike an update preserving the dedicated partition.

The receiver accepts signed local update packages through its setup page, with two
application slots and rollback behavior described by the firmware project. This is not
a Central-managed download service or an over-LoRa transmitter updater. Stick Lite is
not part of the signed/web release pipeline in the reviewed snapshot.

For physical validation, independently check: fresh measurement delivery; an ordinary
restart preserving enrollment; consumer reconnection; Wi-Fi-only persistence in the new
firmware; and a read-only portal visit without MQTT reconnect. Some of these behaviors
have automated coverage but still have pending hardware validation. Log observations,
not inferred guarantees. Do not interrupt flash writes merely to claim a power-loss test.

Sources: [radio diagnostics](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md),
[updates](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/updates.md), [Central operations](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md).
