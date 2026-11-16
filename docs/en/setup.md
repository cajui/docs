# Installation and configuration

English | [Português brasileiro](../pt-BR/setup.md)

[Documentation](../../README.md)

This guide installs one receiver and one transmitter with Cajuí Central and its bundled
broker. Each step ends with what you should see before continuing. To use Home Assistant
without Central, an existing broker or USB configuration, see
[installation without Central](setup-without-central.md).

## Requirements

- A supported transmitter board and sensor.
- A supported receiver board and suitable LoRa antennas for both devices.
- Power supplies appropriate for the boards and sensors.
- A 2.4 GHz Wi-Fi network. The receiver and the computer running Central must be on the
  same network: the receiver looks for the broker only on its own subnet.
- A computer with Docker that stays on to receive and store readings.
- A phone or another computer with Wi-Fi, to open the receiver's setup page.
- A data-capable USB cable to install the firmware.

Check [supported targets](components.md) and [version coverage](status.md) before
selecting firmware.

## 1. Start Central

Follow [Central's Docker installation](https://github.com/cajui/cajui-central/blob/05f58ba12b6c2542018f9cbc7ee2d913b4e4a27f/docs/installation.md#docker)
and open http://127.0.0.1:8080 on the computer running it. The dashboard has no login,
so it only opens on that computer. On a server without a screen, open it from another
computer through an
[SSH local port forward](https://github.com/cajui/cajui-central/blob/05f58ba12b6c2542018f9cbc7ee2d913b4e4a27f/docs/installation.md#server-without-a-screen).

Optionally, set `CAJUI_RECEIVER_HOST` to the computer's LAN address so the receiver
assistant shows it; see
[broker address for receivers](https://github.com/cajui/cajui-central/blob/05f58ba12b6c2542018f9cbc7ee2d913b4e4a27f/docs/installation.md#broker-address-for-receivers).

**Expected result:** the dashboard opens, and **System → MQTT broker** shows Central
connected to the broker.

## 2. Install the firmware

[Build and install from source](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/provisioning.md#build-and-install)
over USB: the receiver image on the receiver board and the transmitter image on the
transmitter board, from the firmware's main branch at revision `47a6a65` or later. The
only published release, v0.1.0, and the web installer that installs it predate the
management channel Central uses to find receivers and pair transmitters: with that
release, the receiver never appears in step 3.

Use the new-board installation procedure only for an uninitialized board. Normal updates
preserve the dedicated storage partition containing enrollment, counters and queued samples.
Identify devices by stable ID; serial-port names can change after reconnection.

**Expected result:** the installation finishes without errors. A receiver without
transmitters starts listening; a transmitter without enrollment waits for pairing.

## 3. Add the receiver

In Central, open **Equipment → Receivers → Add receiver** and follow its three steps.

1. **Connect to the receiver.** Hold the receiver's PRG button for three seconds, join
   its `Cajui-XXXX` Wi-Fi network from the phone and open `http://192.168.4.1`. Choose
   your 2.4 GHz network and save its password. The page reports Wi-Fi connected and the
   settings saved.
2. **Connection details.** In the page's **MQTT broker** section, choose the broker
   found on the network. If more than one appears, use the computer running
   Central. Enter the username and password shown by the assistant and save. The page
   reports **Broker: online**.
3. **Find the receiver.** The assistant lists the receiver when it connects. Confirm it.

**Expected result:** the receiver appears in **Equipment → Receivers** as online.

Before relying on the setup page, note how it works:

- The page answers only on the receiver's own Wi-Fi network, which opens with the PRG
  button for up to 30 minutes. Changing the broker later requires someone next to the
  receiver, or USB.
- The setup network is open while active; see [radio and security](radio-security.md).
- Choosing another Wi-Fi network clears the saved broker settings, so that the password
  is never sent to a broker on an unknown network. Choose the broker and enter the
  credentials again.
- The list shows brokers that answer on port 1883 of the receiver's subnet, without
  Central's mDNS announcement helper. Older firmware lists only brokers announced through
  mDNS. If the broker is not listed, enter the computer's LAN address.

If the receiver does not appear, the page's status lines tell Wi-Fi and broker apart:

| The receiver page shows | Check |
| --- | --- |
| Wi-Fi could not connect | Network name and password; the network must offer 2.4 GHz |
| Wi-Fi connected, broker offline | Address, port, username and password; receiver and Central on the same network. On the Central computer, `docker compose logs broker` shows whether connection attempts reach the broker |
| Broker online, but the assistant lists nothing | The assistant lists receivers that connect after it opened. One already online appears in **Equipment → Receivers** |

## 4. Pair a transmitter

Open **Equipment → Devices → Add device**, choose **Search for transmitters**, hold the
transmitter's PRG button for three seconds and choose **Add** when it appears. The
receiver must be online. Radio pairing is not authenticated against an attacker in
range during the two-minute search; see
[radio pairing](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/radio-pairing.md).

**Expected result:** Central reports the transmitter paired and then sending readings.
Give it a name.

## 5. Organize the dashboard

Name sensors, assign locations and organize the dashboard by device, sensor or
measurement. See the [Central guide](central.md).

**Expected result:** the overview shows each measurement with its name.

## 6. Verify the installation

- Confirm that valid measurements arrive at the expected interval.
- Check the receiver's queue and forwarding status.
- Restart devices and confirm that saved configuration and enrollment are retained.
- Test application reconnection and verify subsequent samples.

See [operations](operations.md) for troubleshooting and [project status](status.md) for
hardware validation still required by the project.
