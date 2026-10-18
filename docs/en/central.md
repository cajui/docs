# Cajuí Central

English | [Português brasileiro](../pt-BR/central.md)

[Documentation](../../README.md)

Cajuí Central is a Go monitoring server with SQLite storage and an embedded web interface.
It accepts MQTT samples and HTTP readings, validates incoming data, and provides device
registration, dashboards and historical views. The web interface is served by the Go
application and requires no separate frontend service.

## Data ingestion

MQTT samples are validated and committed atomically. Central deduplicates deliveries by
source, device and sample identity, rejecting conflicting content under an existing
identity. Readings retain their quality status and arrival timestamp.

Receiver availability and device state are stored separately from measurement history.
These records supply connection, queue, firmware and pairing information.

## Device and sensor registration

Registration assigns display names and locations to observed devices and sensors.
Names are independent of radio identities and MQTT credentials. A sensor registration
can contain several measurements, such as temperature and humidity.

The dashboard supports named sections containing devices, complete sensors or individual
measurements. Layout changes preserve registrations and history. History charts
query stored readings by channel and date, with original rows available in a
paginated table. CSV export covers recent overview readings only. The interface
supports English and Brazilian Portuguese.

## History

Choose preset periods through 30 days or a custom interval of up to 366 days per
query. Data has no automatic age-based deletion. History uses arrival at Central,
not an inferred acquisition time for queued samples. Large charts retain selected
original points; the paginated table exposes original readings, newest first.
Back up the database before upgrades: schema migrations are not reversible by
starting an older binary.

## Connection and measurement status

| Status | Interpretation |
| --- | --- |
| Receiver offline | MQTT availability reports a disconnected receiver |
| Transmitter stale | No new unique sample arrived within three expected reporting intervals |
| Sensor error | A sample arrived with a failed measurement |
| Unknown or old state | A current value is unavailable or the stored state has uncertain age |

Receiver and dashboard state updates use server-sent events (SSE). The browser pauses
streams while hidden and reconnects after interruptions. Abrupt receiver power loss
still depends on the broker's MQTT timeout before an offline event is available.

## Administration

Central can request pairing and transmitter revocation when an online receiver
advertises those capabilities. Radio enrollment is managed by the receiver.

Removing a receiver or sensor from a list preserves its history and credentials. New
qualifying observations may restore it to the list. Radio revocation and MQTT account
revocation are separate administrative actions.

## MQTT diagnostics

The broker page displays connection and subscription status, read-only settings and the
last 100 inbound observations. Entries can be filtered, paused and expanded to inspect
normalized JSON. The buffer covers Central's subscriptions and resets on restart.
Broker configuration is supplied through environment variables and secret files.

## Access and scope

The browser interface uses local-access restrictions and capability checks. Keep the interface on the local computer and follow the
[access policy](https://github.com/cajui/cajui-central/blob/23ee539454c133fee42e020975e7d3dc662937e9/README.md).
Current functionality covers monitoring and supported device administration; actuator
control and a general automation engine are not implemented.

## Reference

[Central README](https://github.com/cajui/cajui-central/blob/23ee539454c133fee42e020975e7d3dc662937e9/README.md) · [API and interface source](https://github.com/cajui/cajui-central/tree/23ee539454c133fee42e020975e7d3dc662937e9/internal/httpapi)
