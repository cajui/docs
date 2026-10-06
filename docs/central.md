# Cajuí Central

[Documentation home](../README.md) · [MQTT](mqtt-integrations.md)

Central is a Go monitoring server with SQLite storage and an embedded browser interface.
It receives the MQTT sample contract and an HTTP readings API, validates data and stores
history. The UI does not require a frontend build or a separate frontend service.

## Responsibilities

| Area | What it does | Important distinction |
| --- | --- | --- |
| Ingestion | Validates samples and atomically persists them | A received MQTT message can still be rejected |
| Deduplication | Uses source/device/sample identity | Repeated delivery is not a new observation |
| Devices and sensors | Names observed items and assigns locations | Registration does not establish radio trust |
| Dashboard | Organizes sections, sensors and measurements | Removing a dashboard item does not delete history |
| History/export | Presents saved measurements and CSV | Arrival time can differ from measurement time |
| Receiver state | Shows connection, queue, firmware and diagnostics | Retained state may describe a previous connection |
| Management | Requests pairing and transmitter revocation | Requires reachable receiver and advertised capability |
| Broker diagnostics | Shows connection/subscription state and recent observations | Not a broker-wide traffic capture or administration console |
| Localization | Offers en-US and pt-BR UI | User-defined names are not translated |

## Status is not a single boolean

- **Receiver offline:** broker availability says it lost its connection; a sudden power
  loss is detected after the MQTT timeout.
- **Transmitter stale:** no new unique sample within three expected reporting intervals.
- **Sensor error:** communication happened, but a measurement failed.
- **Unknown/old state:** no trustworthy fresh value; absence is not a zero measurement.

The receiver page and dashboard use SSE for live device-state snapshots, pause when
hidden and recover broken streams. They update after Central receives evidence; SSE
cannot make the broker detect a power failure earlier. General page refresh remains
separate from live connection-state events.

## Removal versus revocation

Removing receiver/sensor items preserves history and does not revoke credentials.
Fresh qualifying observations may bring them back. Transmitter revocation is a radio
management action. MQTT account revocation is a broker action. These are different
operations and should not share an explanation of "delete device".

## Diagnostic and access limits

The broker table holds the last 100 inbound observations in memory, limited to Central's
subscriptions. It supports filtering, pausing and expanded JSON; it resets on restart.
It is not a durable audit log. Settings still come from environment variables and
secret files, not a general broker-management form.

The local browser interface has a local-access policy and capability checks. Do not
assume it is ready for unauthenticated remote internet exposure. Brand examples and
component references are development documentation, separate from the product UI.
Central currently has no actuator control or general automation engine.

Source: [Central README and interface contract](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md),
[HTTP/UI implementation](https://github.com/cajui/cajui-central/tree/76a9a189d9a8101bc74b07f6723f9541f9acb05d/internal/httpapi).
