"""Offline package checks. Heuristics complement, never replace, content review."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('product-requests', 'delivery-validation')
errors = []
count = 0

def check(condition, message):
    if not condition:
        errors.append(message)

for name in NAMES:
    folder = ROOT / 'skills' / name
    check(folder.is_dir(), f'Missing skill: {name}')
    for file in folder.rglob('*'):
        if not file.is_file():
            continue
        count += 1
        rel = file.relative_to(ROOT)
        check(file.suffix in ('.md', '.yaml'), f'Unexpected artifact: {rel}')
        check(not any(p in ('personalization', 'originals', 'backups', 'logs') for p in rel.parts), f'Private directory: {rel}')
        text = file.read_text(encoding='utf-8')
        patterns = {
            'legacy skill name': r'trello-(?:analysis|feedback)',
            'real Trello URL': r'https?://trello\.com/(?:c|b)/',
            'workspace identifier': r'ari:cloud:|[0-9a-f]{24,}',
            'local absolute user path': r'(?i)[A-Z]:[\\/](?:Users|Documents)[\\/]|/Users/|/home/[^\s/]+/',
            'email address': r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}',
            'credential assignment': r'(?i)(?:PLAYWRIGHT_MCP_EXTENSION_TOKEN|password|api_key|access_token|secret)\s*[:=]\s*\S+',
            'credential-bearing URL': r'https?://[^\s)]+[?&](?:token|key|auth|secret)=',
            'unfinished scaffold': r'\[TODO:',
        }
        for label, pattern in patterns.items():
            check(not re.search(pattern, text), f'{label}: {rel}')
        # Cross-skill links are checked together; placeholders in fenced examples are not URLs.
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'https?://|mailto:|#', target):
                continue
            target = target.split('#')[0]
            check((file.parent / target).resolve().exists(), f'Broken link in {rel}: {target}')
    skill = folder / 'SKILL.md'
    if skill.exists():
        text = skill.read_text(encoding='utf-8')
        match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        check(bool(match), f'Invalid frontmatter: {name}')
        if match:
            check(f'name: {name}' in match.group(1).splitlines(), f'Name mismatch: {name}')
            check(bool(re.search(r'^description: .+', match.group(1), re.M)), f'Missing description: {name}')
        metadata = (folder / 'agents/openai.yaml').read_text(encoding='utf-8')
        check(f'${name}' in metadata, f'Invocation mismatch: {name}')
        short = re.search(r'short_description: "([^"]+)"', metadata)
        check(bool(short) and 25 <= len(short.group(1)) <= 64, f'UI description length: {name}')

check('[Product Requests](../product-requests/SKILL.md)' in (ROOT / 'skills/delivery-validation/SKILL.md').read_text(encoding='utf-8'), 'Missing validation-to-requests link')
check('[Delivery Validation](../delivery-validation/SKILL.md)' in (ROOT / 'skills/product-requests/SKILL.md').read_text(encoding='utf-8'), 'Missing requests-to-validation link')

if errors:
    for error in errors:
        print('FAIL:', error)
    sys.exit(1)
print(f'PASS: {count} public skill files; structure, relative links, metadata and privacy patterns.')
print('This does not test live integrations or guarantee absence of sensitive data.')
