# Contributing

These guides explain the public Cajuí ecosystem. Keep content in English and distinguish
implemented behavior, unreleased experiments, plans and physical validation.

1. Identify the owning source and exact revision for a claim.
2. Update the relevant guide and the capability inventory when status changes.
3. Keep technical contracts in their owning project; link rather than duplicate them.
4. Edit Mermaid diagram sources in Markdown when changing a flow.
5. Run `python3 scripts/check_docs.py` before opening a pull request.
6. Preview affected Markdown and diagrams on GitHub.

Do not add credentials, device-specific configuration, private notes, local machine paths
or photographs without authorization. Use illustrative identities rather than installation
data. Do not publish unvalidated hardware as assembly instructions.

The check script verifies local file/heading links, balanced code fences, diagram presence
and unresolved source placeholders. It does not check external website availability,
render Mermaid or validate technical claims; those require review.

GitHub Pages is a future presentation option, not part of the current repository build.
No runtime dependency is added to Central or firmware by editing these guides.

Contributions are licensed under Apache-2.0, as described in [LICENSE](LICENSE).
