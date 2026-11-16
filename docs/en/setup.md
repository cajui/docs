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
- A 2.4 GHz Wi-Fi network with a password of at least eight characters; open networks
  are not supported. The receiver and the computer running Central must be on the same
  network: the receiver looks for the broker only on its own subnet.
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

Before the first upload to a factory board, erase its dedicated `cajui` storage
partition with esptool's `erase_region`, at the offset and size in the firmware's
[partition layout](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/persistence.md#partition-layout),
so that leftovers of the firmware the board shipped with are not read as corrupt storage.
The web installer's
[new-board installation](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/updates.md#web-installer-usb)
does the same; the source upload does not. Never erase it on an enrolled board: the
partition holds enrollment keys, counters and queued samples, and normal updates
preserve it. Identify devices by stable ID; serial-port names can change after
reconnection.

**Expected result:** the installation finishes without errors. A receiver without
transmitters starts listening; a transmitter without enrollment waits for pairing.

## 3. Add the receiver

In Central, open **Equipment → Receivers → Add receiver** and follow its three steps.

1. **Connect to receiver.** Hold the receiver's PRG button for three seconds, join
   its `Cajui-XXXX` Wi-Fi network from the phone and open `http://192.168.4.1`. Choose
   your 2.4 GHz network and save its password. Tap **Refresh** until the status shows
   **Wi-Fi: connected** and **Wi-Fi settings: saved**.
2. **Connection details.** Once Wi-Fi connects, the receiver searches the network for
   brokers, which takes up to about a minute. Tap **Refresh** until the page's
   **MQTT broker** section lists a broker, and choose it; if more than one appears, use
   the computer running Central. **Search again** repeats the search. Enter the username
   and the password shown by the assistant and save, then tap **Refresh** until the
   status shows **Broker: online**.
3. **Find receiver.** The assistant lists the receiver when it connects. Confirm it.

**Expected result:** the receiver appears in **Equipment → Receivers** as online.

Before relying on the setup page, note how it works; the firmware's
[receiver setup page](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/radio-applications.md#receiver-setup-page)
reference has the details:

- The page answers only on the receiver's own Wi-Fi network, which the PRG button opens.
  It closes 30 minutes after opening, after ten minutes without use, or when PRG is held
  again. Configuring another broker later requires physical access to the receiver: the
  PRG button or USB.
- The setup network is open while active; see [radio and security](radio-security.md).
- Choosing another Wi-Fi network clears the saved broker settings, so that the password
  is never sent to a broker on an unknown network. Choose the broker and enter the
  credentials again.
- The list shows brokers announced through mDNS and brokers that answer on port 1883, or
  on the port already entered, at the addresses of the receiver's subnet; on a network
  larger than 254 addresses, only the /24 block around the receiver is searched. If the
  broker is not listed, enter the computer's LAN address.

If the receiver does not appear, the page's status lines tell Wi-Fi and broker apart:

| The receiver page shows | Check |
| --- | --- |
| **Wi-Fi: could not connect** | Network name and password, of at least eight characters; the network must offer 2.4 GHz |
| No broker in the **MQTT broker** section after the search | Receiver and Central on the same subnet, and the broker on port 1883. Otherwise enter the computer's LAN address and port |
| **Wi-Fi: connected** with **Broker: offline** | Address, port, username and password; receiver and Central on the same network. On the Central computer, `docker compose logs broker` shows whether connection attempts reach the broker |
| **Broker: online**, but the assistant lists nothing | The assistant lists receivers that connect after it opened. One already online appears in **Equipment → Receivers** |

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
