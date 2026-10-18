import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

FILE = Path(__file__).resolve().parents[1] / 'scripts/inspect_skill.py'
SPEC = importlib.util.spec_from_file_location('inspect_skill', FILE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class InspectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'demo-skill'
        self.root.mkdir()
        (self.root / 'SKILL.md').write_text('---\nname: demo-skill\ndescription: Handle a narrow fictional workflow.\n---\n\n# Demo\n', encoding='utf-8')

    def codes(self, terms=()):
        return {f['code'] for f in MODULE.inspect(self.root, terms)['findings']}

    def test_clean_package_and_no_mutation(self):
        before = (self.root / 'SKILL.md').read_bytes()
        self.assertEqual(set(), self.codes())
        self.assertEqual(before, (self.root / 'SKILL.md').read_bytes())

    def test_broken_reference(self):
        with (self.root / 'SKILL.md').open('a', encoding='utf-8') as stream:
            stream.write('\n[reference](references/absent.md)\n')
        self.assertIn('broken-local-link', self.codes())

    def test_optional_sibling_classified_separately(self):
        with (self.root / 'SKILL.md').open('a', encoding='utf-8') as stream:
            stream.write('\n[other](../other-skill/SKILL.md)\n')
        report = MODULE.inspect(self.root)
        self.assertEqual('missing-dependency-link', report['findings'][0]['code'])
        self.assertEqual('warning', report['findings'][0]['severity'])

    def test_fenced_example_is_not_a_reference(self):
        with (self.root / 'SKILL.md').open('a', encoding='utf-8') as stream:
            stream.write('\n```md\n[example](absent.md)\n```\n')
        self.assertEqual(set(), self.codes())

    def test_private_term_is_redacted(self):
        term = 'synthetic-' + 'account-identifier'
        (self.root / 'notes.md').write_text(term, encoding='utf-8')
        result = MODULE.inspect(self.root, [term])
        self.assertIn('private-term-match', {f['code'] for f in result['findings']})
        self.assertNotIn(term, json.dumps(result))

    def test_credential_value_is_not_echoed(self):
        value = 'synthetic' + 'credential123456789'
        (self.root / 'sample.ini').write_text('api_key=' + value, encoding='utf-8')
        result = MODULE.inspect(self.root)
        self.assertIn('credential-like-value', {f['code'] for f in result['findings']})
        self.assertNotIn(value, json.dumps(result))

    def test_private_filename_is_redacted(self):
        term = 'synthetic-private-filename'
        (self.root / (term + '.md')).write_text('generic contents', encoding='utf-8')
        result = MODULE.inspect(self.root, [term])
        self.assertIn('private-term-match', {f['code'] for f in result['findings']})
        self.assertNotIn(term, json.dumps(result))

    def test_read_failure_reports_incomplete_without_exception(self):
        with patch.object(Path, 'read_bytes', side_effect=PermissionError('sensitive details')):
            result = MODULE.inspect(self.root)
        self.assertIn('file-not-readable', {f['code'] for f in result['findings']})
        self.assertNotIn('sensitive details', json.dumps(result))
        self.assertNotIn(str(self.root), json.dumps(result))

    def test_service_key_in_filename_is_detected_and_redacted(self):
        value = 'AKIA' + 'X' * 16
        (self.root / (value + '.txt')).write_text('generic contents', encoding='utf-8')
        result = MODULE.inspect(self.root)
        self.assertIn('service-token-shape', {f['code'] for f in result['findings']})
        self.assertNotIn(value, json.dumps(result))

    def test_exact_duplicates_are_review_only(self):
        (self.root / 'a.md').write_text('repeated content', encoding='utf-8')
        (self.root / 'b.md').write_text('repeated content', encoding='utf-8')
        self.assertIn('exact-duplicate-file-review', self.codes())
        self.assertTrue((self.root / 'b.md').exists())

    def test_empty_required_field(self):
        (self.root / 'SKILL.md').write_text('---\nname: demo-skill\ndescription: " "\n---\n', encoding='utf-8')
        self.assertIn('invalid-description', self.codes())

    def test_invocation_policy_type(self):
        (self.root / 'agents').mkdir()
        (self.root / 'agents/openai.yaml').write_text('policy:\n  allow_implicit_invocation: "false"\n', encoding='utf-8')
        self.assertIn('invalid-invocation-policy', self.codes())


if __name__ == '__main__':
    unittest.main()
