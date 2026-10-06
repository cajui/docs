# Cajuí ecosystem documentation

A map of the components, responsibilities and delivery boundaries of Cajuí: sensor
transmitters, a direct LoRa receiver, MQTT and monitoring applications.

Use this repository to remember how the whole system fits together, then follow the
links to the implementation details. It documents experimental software, not a
production-ready kit or a guarantee of field reliability.

## Start here

- [System overview](docs/overview.md): the physical system and the software running it.
- [Capability inventory](docs/inventory.md): what exists, where it runs and its limits.
- [A measurement's journey](docs/data-flow.md): every handoff and what each ACK means.
- [Components](docs/components.md): the purpose and dependencies of each part.

## Explore a subject

| Question | Guide |
| --- | --- |
| How do nodes join and communicate securely? | [Radio, pairing and security](docs/radio-security.md) |
| How does data reach applications? | [MQTT and integrations](docs/mqtt-integrations.md) |
| How do I assemble the first working system? | [Setup walkthrough](docs/setup.md) |
| What does Central actually do? | [Cajuí Central](docs/central.md) |
| What should I check when something stops working? | [Operations and diagnosis](docs/operations.md) |
| Where is a feature implemented and tested? | [Development map](docs/development.md) |
| What do the names mean? | [Glossary](docs/glossary.md) |
| Which versions support these claims? | [Evidence and status](docs/status.md) |

## Read the status labels

**Implemented** means present in the referenced code; it does not mean released,
audited or field-proven. **Experimental / PR** identifies work still under review.
**Planned** is not an instruction to enable an existing feature. **Unvalidated**
identifies an evidence gap rather than a missing implementation.

The reviewed snapshot is dated **2026-10-06**. Central PR #33 is merged; firmware
PR #25 is open at this snapshot. See [exact revisions and limits](docs/status.md).

Diagrams use editable Mermaid blocks rendered by GitHub. There is no site generator,
frontend build or documentation service to install. A GitHub Pages site can be added
later using this content; this repository does not deploy one.

## Repositories

- [cajui-central](https://github.com/cajui/cajui-central): monitoring application.
- [cajui-firmware](https://github.com/cajui/cajui-firmware): transmitter and receiver firmware.
- [docs](https://github.com/cajui/docs): cross-project explanations and navigation.

Technical contracts stay in their owning repository. This map links to reviewed
revisions instead of copying full specifications. Public mechanical files and a
custom PCB build guide are not supplied here.

[Contributing](CONTRIBUTING.md) · [Documentation maintenance](AGENTS.md) ·
[Apache-2.0 license](LICENSE)
