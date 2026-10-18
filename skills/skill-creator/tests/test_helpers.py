import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('quick_validate', ROOT / 'scripts/quick_validate.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class HelpersTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def skill(self, name='demo-skill', description='Handle a fictional focused workflow.'):
        self.path = self.root / 'demo-skill'
        self.path.mkdir(exist_ok=True)
        (self.path / 'SKILL.md').write_text('---\nname: ' + yaml.safe_dump(name).strip().removesuffix('...').strip() + '\ndescription: ' + yaml.safe_dump(description).strip().removesuffix('...').strip() + '\n---\n\n# Demo\n', encoding='utf-8')
        return self.path

    def test_valid_utf8(self):
        self.assertTrue(MODULE.validate_skill(self.skill(description='Organizar ações e preservar informação útil.'))[0])

    def test_reject_empty_name_and_description(self):
        for name, desc in [('', 'Valid description.'), (' ', 'Valid description.'), ('demo-skill', ''), ('demo-skill', ' ')]:
            with self.subTest(name=name, desc=desc):
                self.assertFalse(MODULE.validate_skill(self.skill(name, desc))[0])

    def test_reject_bad_name_and_scaffold(self):
        self.assertFalse(MODULE.validate_skill(self.skill(name='Bad Name'))[0])
        self.skill()
        with (self.path / 'SKILL.md').open('a', encoding='utf-8') as out:
            out.write('\n[TODO: Finish instruction]\n')
        self.assertFalse(MODULE.validate_skill(self.path)[0])

    def test_initializer_and_metadata(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/init_skill.py'), 'sample-skill', '--path', str(self.root), '--interface', 'default_prompt=Use $sample-skill para organizar ações.'], capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        ui = yaml.safe_load((self.root / 'sample-skill/agents/openai.yaml').read_text(encoding='utf-8'))
        self.assertIn('$sample-skill', ui['interface']['default_prompt'])
        self.assertTrue(25 <= len(ui['interface']['short_description']) <= 64)
        # An initializer creates a scaffold, not a finished usable skill.
        self.assertFalse(MODULE.validate_skill(self.root / 'sample-skill')[0])

    def test_initializer_does_not_overwrite(self):
        self.skill()
        before = (self.path / 'SKILL.md').read_bytes()
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/init_skill.py'), 'demo-skill', '--path', str(self.root)], capture_output=True)
        self.assertNotEqual(0, result.returncode)
        self.assertEqual(before, (self.path / 'SKILL.md').read_bytes())

    def test_invalid_yaml(self):
        self.skill()
        (self.path / 'SKILL.md').write_text('---\nname: [\ndescription: invalid\n---\n', encoding='utf-8')
        self.assertFalse(MODULE.validate_skill(self.path)[0])

    def test_invalid_ui_does_not_leave_partial_directory(self):
        for override in ('short_description=tiny', 'unknown_field=value'):
            with self.subTest(override=override):
                result = subprocess.run([sys.executable, str(ROOT / 'scripts/init_skill.py'), 'unfinished-skill', '--path', str(self.root), '--interface', override], capture_output=True)
                self.assertNotEqual(0, result.returncode)
                self.assertFalse((self.root / 'unfinished-skill').exists())


if __name__ == '__main__':
    unittest.main()
