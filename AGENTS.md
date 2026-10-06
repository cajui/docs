# Documentation guidelines

- Read README.md and docs/en/status.md before editing.
- Maintain English and Brazilian Portuguese documentation for project users and contributors.
- Use docs/en as the technical reference and keep matching filenames under docs/pt-BR.
- Update both languages in the same change, including diagram labels and navigation.
- Keep code, commands, API identifiers and MQTT topics unchanged in translations.
- Keep conversation history, editorial rationale and individual requests out of public documentation.
- Describe the system directly. Put compatibility and validation limits where they affect usage.
- Keep implementation claims tied to the documented source versions.
- Maintain technical contracts in their implementation repositories; link rather than duplicate them.
- Keep Mermaid diagrams editable and consistent with the surrounding text.
- Exclude credentials and identifying deployment data.
- Run python3 scripts/check_docs.py and python3 -m unittest discover -s tests -v.
- Preview affected diagrams before publication.
