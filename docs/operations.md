# Operations and troubleshooting

[Documentation](../README.md)

## Troubleshooting

Trace a failing sample through sensor acquisition, radio delivery, MQTT forwarding and
application ingestion. Check each stage's status before changing configuration.

| Symptom | Checks | Relevant behavior |
| --- | --- | --- |
| No USB response | Data cable, port, stable device ID | Serial ports can change after reconnecting |
| Sensor error with successful radio ACK | Sensor power, wiring and driver | Measurement quality is independent of radio delivery |
| No radio ACK | Antennas, profile, enrollment and storage health | Receiver acceptance can operate while MQTT is unavailable |
| Wi-Fi connected but application receives nothing | Broker address, credentials, ACLs and subscriptions | Wi-Fi and MQTT have separate connection states |
| Broker search returns no results | mDNS announcement and multicast reachability | Manual address entry is supported |
| Receiver queue grows | Broker connection and PUBACK processing | The queue is bounded; inspect dropped-sample counters |
| Queue drains without consumer readings | Topic permissions, identity and consumer logs | MQTT 3.1.1 can acknowledge denied publications |
| Offline status is delayed after power loss | MQTT keepalive and Last Will | Offline detection follows the broker's timeout |
| Receiver connected but transmitter stale | Last unique sample and reporting interval | Sleeping transmitters are monitored through sample arrivals |
| New arrivals contain old conditions | Queued backlog and timestamps | Arrival time includes forwarding delay |
| HA entities are absent | Discovery permissions, prefix, source ID and metric support | Discovery and telemetry use separate topics |
| Removed items reappear | New samples or live device state | List removal preserves producer access |

## Diagnostics

Measurement history records readings over time. Device state records the latest queue,
uptime, firmware and availability values. Logs and the MQTT diagnostic buffer describe
recent processing events.

Check timestamps when interpreting diagnostics. An offline receiver's last-known Wi-Fi
signal or forwarding count may remain visible after its connection is lost.

## Updates

Back up the Central database before schema upgrades. Database schema downgrade is not
supported; rolling back may require the older binary and its corresponding backup.

Firmware updates must preserve enrollment and counter state. The receiver accepts signed
update packages uploaded through its setup page and uses two application slots with
rollback handling. Transmitters are updated over USB. The Stick Lite target is currently
excluded from the signed/web release pipeline.

Follow [firmware update instructions](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/updates.md) for image compatibility,
partition layout and recovery procedures. A new-board installation initializes enrollment
storage and must not be used as a routine update.

## Recovery verification

After configuration or firmware changes, verify saved settings after restart, enrollment,
fresh sample delivery, receiver queue progress and application reconnection. Reopening
and closing setup should preserve an established MQTT connection on firmware supporting
the updated recovery behavior.

Automated coverage and outstanding physical checks are documented in [project status](status.md).
For detailed log fields, see [radio applications](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md) and
[Central operations](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md).
