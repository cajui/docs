"""Regression tests for bilingual documentation navigation checks."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    'check_docs', Path(__file__).resolve().parents[1] / 'scripts/check_docs.py')
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class DocumentationChecks(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name).resolve()
        for base in ('README', 'CONTRIBUTING'):
            self.write(f'{base}.md', f'# Guide\n\nEnglish | [Português brasileiro]({base}.pt-BR.md)\n')
            self.write(f'{base}.pt-BR.md', f'# Guia\n\n[English]({base}.md) | Português brasileiro\n')
        diagrams = '\n```mermaid\nflowchart LR\nA-->B\n```\n' * 2
        self.write('docs/en/overview.md', '# Architecture\n\nEnglish | [Português brasileiro](../pt-BR/overview.md)\n' + diagrams)
        self.write('docs/pt-BR/overview.md', '# Arquitetura\n\n[English](../en/overview.md) | Português brasileiro\n' + diagrams)

    def write(self, name, text):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def errors(self):
        return CHECKER.check(self.root)[2]

    def test_complete_locales_pass(self):
        self.assertEqual([], self.errors())

    def test_missing_page_fails(self):
        (self.root / 'docs/pt-BR/overview.md').unlink()
        self.assertTrue(any('missing translation page' in error for error in self.errors()))

    def test_selector_must_target_equivalent_page(self):
        p = self.root / 'docs/pt-BR/overview.md'
        p.write_text(p.read_text().replace('../en/overview.md', '../../README.md'))
        self.assertTrue(any('missing counterpart language selector' in error for error in self.errors()))
        self.assertTrue(any('cross-language navigation' in error for error in self.errors()))

    def test_translation_cannot_omit_diagram(self):
        p = self.root / 'docs/pt-BR/overview.md'
        p.write_text(p.read_text() + '\n```mermaid\nflowchart LR\nA-->B\n```\n')
        self.assertTrue(any('translated diagram count differs' in error for error in self.errors()))

    def test_links_and_localized_anchors_are_checked(self):
        p = self.root / 'docs/pt-BR/overview.md'
        p.write_text(p.read_text() + '\n[Seção](#arquitetura)\n')
        self.assertEqual([], self.errors())
        p.write_text(p.read_text() + '\n[Ausente](missing.md)\n[Seção](#absent)\n')
        self.assertTrue(any('missing target' in error for error in self.errors()))
        self.assertTrue(any('missing heading' in error for error in self.errors()))


if __name__ == '__main__':
    unittest.main()
