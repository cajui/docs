#!/usr/bin/env python3
"""Check repository-local documentation structure without network access."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def headings(text):
    result, counts = set(), {}
    for title in re.findall(r'^#{1,6}\s+(.+)$', text, re.MULTILINE):
        slug = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(f'{slug}-{count}' if count else slug)
    return result


def check(root):
    failures = []
    diagrams = 0
    pages = list(root.rglob('*.md'))
    for page in pages:
        text = page.read_text()
        label = page.relative_to(root)
        fences = re.findall(r'^```[^\n]*$', text, re.MULTILINE)
        if len(fences) % 2:
            failures.append(f'{label}: unbalanced code fences')
        diagrams += fences.count('```mermaid')
        if re.search(r'\{(?:FW|CENTRAL)\}', text):
            failures.append(f'{label}: unresolved source placeholder')
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            target = (page.parent / unquote(url.path)).resolve() if url.path else page
            if not target.is_relative_to(root):
                failures.append(f'{label}: link escapes repository: {href}')
            elif not target.exists():
                failures.append(f'{label}: missing target: {href}')
            elif url.fragment and target.suffix == '.md':
                if unquote(url.fragment) not in headings(target.read_text()):
                    failures.append(f'{label}: missing heading: {href}')
    if diagrams < 4:
        failures.append('Expected at least four ecosystem diagrams')
    return pages, diagrams, failures


if __name__ == '__main__':
    pages, diagrams, failures = check(ROOT)
    for failure in failures:
        print(failure, file=sys.stderr)
    if failures:
        sys.exit(1)
    print(f'Checked {len(pages)} Markdown files and {diagrams} Mermaid diagrams.')
