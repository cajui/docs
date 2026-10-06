# Contributing to Cajuí Documentation

Contributions are welcome, including corrections, installation guidance, troubleshooting
procedures and architecture explanations.

## Writing conventions

- Write in English for users and contributors of the project.
- Introduce a component's purpose before its implementation details.
- Use consistent names for devices, services and message types.
- Document requirements, expected results and relevant failure cases.
- Distinguish implemented features from development work and outstanding validation.
- Keep technical specifications in their implementation repositories and link to them.
- Use synthetic examples and omit credentials or identifying deployment data.

## Updating documentation

1. Check the implementation and the versions listed in [project status](docs/status.md).
2. Update the affected guides, feature reference and diagrams together.
3. Keep source links pinned to the documented revisions. Update the version table when
   changing the implementation baseline.
4. Run `python3 scripts/check_docs.py`.
5. Preview the Markdown and Mermaid diagrams, then submit a pull request.

The validation script checks local file and heading links, balanced code fences,
diagram presence and unresolved source placeholders. Diagram rendering and external
references require separate review.

## License

Contributions are licensed under [Apache-2.0](LICENSE).
