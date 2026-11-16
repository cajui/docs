# Installation without Central

English | [Português brasileiro](../pt-BR/setup-without-central.md)

[Documentation](../../README.md)

Central is optional. This page covers an installation with Home Assistant or another
MQTT consumer, an existing broker, or configuration over USB. For the path with
Central, see [installation](setup.md).

## 1. Prepare the broker

Use a broker reachable from the receiver's network. Create a producer account for the
receiver with write access to its telemetry, management and Discovery namespaces, and
separate accounts for consumers; see [accounts and permissions](mqtt-integrations.md#accounts-and-permissions).
Central's Docker deployment also provides a broker and credential tools without using
the dashboard.

**Expected result:** the consumer connects to the broker with its own account.

## 2. Install the firmware

Follow step 2 of the [installation guide](setup.md#2-install-the-firmware).

## 3. Configure the receiver

1. Hold the receiver's PRG button for three seconds to open setup.
2. Join its temporary Wi-Fi network and open `http://192.168.4.1`.
3. Select a 2.4 GHz network or enter a hidden SSID and its credentials.
4. In the **MQTT broker** section, choose a broker found on the network or enter its
   address, then the port and the producer credentials.
5. Confirm both Wi-Fi and broker connection status.

The broker address must be reachable from the receiver's network. An internal container
hostname may only resolve inside Docker. The receiver lists brokers that answer on its
own subnet, and brokers announced through mDNS.

**Expected result:** the page reports **Broker: online**.

### Over USB

The [USB provisioning tool](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/provisioning.md#receiver-uplink-settings)
writes the receiver's network settings without the setup page. It requires every field,
including the Wi-Fi network and password, even to change only the broker. To change only
the broker, use the setup page, which keeps the saved Wi-Fi settings.

## 4. Enroll a transmitter

Use [radio pairing](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/radio-pairing.md)
from the receiver's setup page: choose **Search for transmitters**, hold the
transmitter's PRG button for three seconds and choose **Add**. Alternatively, use
[USB enrollment](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/provisioning.md#enroll-resume-and-verify).

Verify radio acceptance and downstream delivery separately: a matching radio ACK
confirms receiver acceptance; an application reading confirms the sample reached the consumer.

**Expected result:** the transmitter appears in the receiver page's list of enrolled
transmitters.

## 5. Configure Home Assistant

Enable Home Assistant's MQTT integration with the default `homeassistant` Discovery
prefix, then verify the supported entities; see
[Home Assistant](mqtt-integrations.md#home-assistant).

**Expected result:** the transmitter's measurements appear as entities.

## 6. Verify the installation

Follow step 6 of the [installation guide](setup.md#6-verify-the-installation).
