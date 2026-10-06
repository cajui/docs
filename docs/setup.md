# First-system setup walkthrough

[Documentation home](../README.md) · [Diagnosis](operations.md)

This is the order of operations and acceptance checks, not a replacement for the
board-specific flashing commands. The system is experimental. Select a supported
board/image pair and follow its technical instructions before powering or flashing it.

## 1. Choose compatible parts and versions

Use a supported transmitter with its matching sensor driver, a receiver, suitable LoRa
antennas, power and a computer for the broker and optional Central. Both radios transmit.
The Stick Lite/SHT4x target is experimental in PR #25 and USB-only; do not install the
WiFi LoRa 32 image merely because both boards contain an ESP32-S3 and SX1262.

Follow [applications](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md) and, if appropriate,
[Stick Lite](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/stick-lite.md). Do not treat an arbitrary sensor with the same
connector as supported. Public custom-PCB/enclosure build files are outside this guide.

## 2. Start the broker and consumer

Follow [Central's Docker or Go setup](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md). The bundled Docker stack
provides a broker; an existing broker can also be used with the documented permissions.
Alternatively, use Home Assistant and its MQTT integration without Central.

**Check:** the intended consumer connects and subscribes. A healthy database endpoint
alone does not prove an MQTT subscription is working.

## 3. Install the correct firmware and identify devices

Use [USB provisioning](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/provisioning.md) and
[update/install instructions](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/updates.md). Distinguish a new-board installation
from an update: initializing storage on an enrolled board discards its credentials.
Identify each board by its stable ID; serial-port names can change after reconnection.

## 4. Connect the receiver to Wi-Fi and MQTT

Hold receiver PRG for three seconds, join its temporary setup network and open
`http://192.168.4.1`. Select the 2.4 GHz Wi-Fi network or enter a hidden SSID manually.
Then configure the broker address, port and dedicated producer credentials.

The address must be reachable from the receiver, not only inside a container. Broker
mDNS search works only with an announcement on a reachable local network. Discovery
provides an address, not an authorization token.

**Version difference:** PR #25 saves verified Wi-Fi independently of MQTT. Earlier
setup code required complete uplink settings. Confirm the running image before assuming
Wi-Fi alone persists. Saving credentials does not require sending them to this repository.

**Check:** distinguish Wi-Fi connected, broker connected and consumer receiving data.
In Central, the receiver setup assistant provides instructions and verifies observed
state; it does not magically enroll a receiver that only joined Wi-Fi.

## 5. Enroll a transmitter

Use USB enrollment or operator-triggered radio pairing. On the receiver, open pairing;
on the transmitter, request joining; approve the candidate identity. Follow the
[complete pairing instructions and security limits](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-pairing.md).
Central can request supported management actions through MQTT when the receiver is online.

**Check:** an authenticated radio ACK confirms receiver acceptance. Verify a forwarded
sample separately, rather than interpreting the ACK as successful database storage.

## 6. Name and arrange the data

Register/name observed devices and sensors in Central; arrange the dashboard by device,
sensor or individual measurement. A climate sensor has two measurements, not two boards.
For Home Assistant, verify the supported Discovery entities instead.

**Check:** observe a real fresh reading, its quality and timing, then test a controlled
restart and recovery. Document what was actually tested. Pairing survives normal power
cycles; a disconnected receiver should not need to be added again simply because it rebooted.

Sources: [receiver setup and forwarding](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md),
[Central setup and interface](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md).
