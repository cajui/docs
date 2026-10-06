# Installation and configuration

English | [Português brasileiro](../pt-BR/setup.md)

[Documentation](../../README.md)

## Requirements

- A supported transmitter board and sensor.
- A supported receiver board and suitable LoRa antennas for both devices.
- Power supplies appropriate for the boards and sensors.
- A 2.4 GHz Wi-Fi network reachable by the receiver.
- An MQTT broker and a monitoring application: Cajuí Central, Home Assistant or another compatible consumer.
- A data-capable USB connection for initial firmware installation and optional provisioning.

Check [supported targets](components.md) and [version coverage](status.md) before
selecting firmware. The Stick Lite/SHT4x target currently requires a development build
installed over USB.

## 1. Start the broker and application

Follow [Central's installation instructions](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md) for Docker or Go.
The Docker deployment includes a broker; existing brokers can be used with the documented
accounts and topic permissions. For a Home Assistant deployment, configure its MQTT
integration using the [integration guide](mqtt-integrations.md).

Verify that the application connects to the broker and subscribes successfully.
Central's database health endpoint does not check MQTT connectivity.

## 2. Install firmware

Build or select the correct image for each board and role. Follow the
[installation and update instructions](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/updates.md) and
[USB provisioning guide](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/provisioning.md).

Use the new-board installation procedure only for an uninitialized board. Normal updates
preserve the dedicated storage partition containing enrollment, counters and queued samples.
Identify devices by stable ID; serial-port names can change after reconnection.

## 3. Configure receiver networking

1. Hold the receiver's PRG button for three seconds to open setup.
2. Join its temporary Wi-Fi network and open `http://192.168.4.1`.
3. Select a 2.4 GHz network or enter a hidden SSID and its credentials.
4. Enter the broker address, port and dedicated producer credentials.
5. Confirm both Wi-Fi and broker connection status.

The broker address must be reachable from the receiver's network. An internal container
hostname may only resolve inside Docker. mDNS search is available when the broker host
advertises its service on the local network.

Firmware with independent Wi-Fi persistence saves verified Wi-Fi settings before broker
configuration. Earlier versions require complete uplink settings. Consult
[version coverage](status.md) to determine which behavior applies.

Central's receiver setup assistant provides connection details and verifies incoming
device state. A receiver becomes visible through its MQTT publications.

## 4. Enroll a transmitter

Choose [USB enrollment](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/provisioning.md) or
[radio pairing](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-pairing.md). For radio pairing, open a receiver pairing
window, request joining on the transmitter and approve the candidate identity.
Central can initiate supported pairing actions through the receiver's MQTT management
channel when the receiver is online.

Verify radio acceptance and downstream delivery separately: a matching radio ACK
confirms receiver acceptance; an application reading confirms the sample reached the consumer.

## 5. Configure monitoring

In Central, register observed devices, assign names and locations, and organize the
dashboard by device, sensor or measurement. In Home Assistant, verify the supported
entities published through MQTT Discovery.

## 6. Verify the installation

- Confirm that valid measurements arrive at the expected interval.
- Check the receiver's queue and forwarding status.
- Restart devices and confirm that saved configuration and enrollment are retained.
- Test application reconnection and verify subsequent samples.

See [operations](operations.md) for troubleshooting and [project status](status.md) for
hardware validation still required by the project.
