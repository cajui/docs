# Contributing to Cajuí Documentation

English | [Português brasileiro](CONTRIBUTING.pt-BR.md)

Contributions are welcome, including corrections, installation guidance, troubleshooting
procedures and architecture explanations.

## Writing conventions

- Write for users and contributors of the project in English and Brazilian Portuguese.
- Introduce a component's purpose before its implementation details.
- Use consistent names for devices, services and message types.
- Document requirements, expected results and relevant failure cases.
- Distinguish implemented features from development work and outstanding validation.
- Keep technical specifications in their implementation repositories and link to them.
- Use synthetic examples and omit credentials or identifying deployment data.

## Translations

English guides live in `docs/en`; Brazilian Portuguese guides live in `docs/pt-BR`.
Use matching filenames in both directories and a language selector linking each page
to its counterpart. Keep internal navigation in the selected language. The root README
and contribution guide also have a `.pt-BR.md` counterpart.

English is the technical reference. Update both languages in the same pull request,
including diagram labels. Keep commands, paths, configuration keys, identifiers and
MQTT topics unchanged. External technical references may remain in English.

## Updating documentation

1. Check the implementation and the versions listed in [project status](docs/en/status.md).
2. Update the affected guides, feature reference and diagrams together.
3. Keep source links pinned to the documented revisions. Update the version table when
   changing the implementation baseline.
4. Run `python3 scripts/check_docs.py` and `python3 -m unittest discover -s tests -v`.
5. Preview the Markdown and Mermaid diagrams, then submit a pull request.

The validation script checks local file and heading links, balanced code fences,
page parity, language selectors, internal navigation, diagram counts and unresolved
source placeholders. These checks do not assess translation quality or prove that the
content is synchronized. Review technical meaning, diagram rendering and external
references separately.

## License

Contributions are licensed under [Apache-2.0](LICENSE).
