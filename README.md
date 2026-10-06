# Cajuí Documentation

English | [Português brasileiro](README.pt-BR.md)

Cajuí is an open-source system for collecting sensor measurements over LoRa and
making them available on a local network. It includes transmitter and receiver
firmware, MQTT integration, and Cajuí Central, a monitoring application with a web
interface and persistent storage.

Transmitters send measurements to a receiver, which forwards them to an MQTT broker.
Cajuí Central and Home Assistant can consume these messages independently.

## Getting started

1. Read the [system overview](docs/en/overview.md) for the architecture and component roles.
2. Check [supported hardware and interfaces](docs/en/components.md) and [project status](docs/en/status.md).
3. Follow the [installation guide](docs/en/setup.md) to configure a receiver, transmitter and application.

## Documentation

| Section | Contents |
| --- | --- |
| [Architecture](docs/en/overview.md) | Physical topology, services and terminology |
| [Components](docs/en/components.md) | Hardware, firmware, power and sensor interfaces |
| [Features](docs/en/inventory.md) | Capabilities and implementation status by subsystem |
| [Data flow](docs/en/data-flow.md) | Sample identity, acknowledgements, buffering and delivery semantics |
| [Radio and security](docs/en/radio-security.md) | Enrollment, scheduling, encryption and trust boundaries |
| [MQTT and integrations](docs/en/mqtt-integrations.md) | Topics, permissions, discovery and Home Assistant |
| [Installation](docs/en/setup.md) | Requirements, provisioning and initial configuration |
| [Cajuí Central](docs/en/central.md) | Registration, dashboards, history and administration |
| [Operations](docs/en/operations.md) | Troubleshooting, updates and recovery |
| [Development](docs/en/development.md) | Source layout, module responsibilities and testing |
| [Glossary](docs/en/glossary.md) | Terms and abbreviations |
| [Project status](docs/en/status.md) | Version coverage and known limitations |

## Project status

Cajuí is under active development. Firmware applications are experimental, and some
features are available only in development branches. Consult [project status](docs/en/status.md)
for the versions covered by this documentation and current validation limits.

## Repositories

| Repository | Purpose |
| --- | --- |
| [cajui-firmware](https://github.com/cajui/cajui-firmware) | Radio protocol, board firmware and provisioning tools |
| [cajui-central](https://github.com/cajui/cajui-central) | Monitoring server, storage and web interface |
| [docs](https://github.com/cajui/docs) | Architecture, installation and cross-project documentation |

## Contributing

Documentation contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for
editing conventions and validation commands.

## License

This documentation is licensed under [Apache-2.0](LICENSE).
