#!/usr/bin/env python3
"""Check repository-local documentation structure without network access."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import os
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


def translation_pairs(root, failures):
    pairs = [(root / 'README.md', root / 'README.pt-BR.md'),
             (root / 'CONTRIBUTING.md', root / 'CONTRIBUTING.pt-BR.md')]
    directories = [root / 'docs' / locale for locale in ('en', 'pt-BR')]
    names = [{p.relative_to(folder) for p in folder.rglob('*.md')}
             for folder in directories]
    if not names[0] or not names[1]:
        failures.append('Expected guides in both docs/en and docs/pt-BR')
    for name in sorted(names[0] | names[1]):
        pairs.append(tuple(folder / name for folder in directories))
    return pairs


def check(root):
    root = root.resolve()
    failures = []
    counterparts = {}
    for en, pt in translation_pairs(root, failures):
        for page, other, label in ((en, pt, 'Português brasileiro'), (pt, en, 'English')):
            if not page.is_file():
                failures.append(f'{page.relative_to(root)}: missing translation page')
                continue
            counterparts[page] = other
            href = Path(os.path.relpath(other, page.parent)).as_posix()
            selector = f'[{label}]({href})'
            if selector not in '\n'.join(page.read_text().splitlines()[:6]):
                failures.append(f'{page.relative_to(root)}: missing counterpart language selector')
        if en.is_file() and pt.is_file():
            counts = [p.read_text().count('```mermaid') for p in (en, pt)]
            if counts[0] != counts[1]:
                failures.append(f'{en.relative_to(root)}: translated diagram count differs')
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
            elif page in counterparts and target.suffix == '.md':
                locale = 'pt-BR' if ('pt-BR' in page.parts or page.name.endswith('.pt-BR.md')) else 'en'
                target_locale = ('pt-BR' if ('pt-BR' in target.parts or target.name.endswith('.pt-BR.md'))
                                 else 'en')
                if locale != target_locale and target != counterparts[page]:
                    failures.append(f'{label}: cross-language navigation: {href}')
            if target.is_relative_to(root) and target.is_file() and url.fragment and target.suffix == '.md':
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
