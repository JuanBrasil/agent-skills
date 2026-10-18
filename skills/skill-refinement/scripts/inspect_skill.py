"""Read-only local inspection. Reports categories/locations, never matched values.

Heuristics are review aids, not a privacy certification or an automatic editor.
"""
import argparse
import ast
import hashlib
import json
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit('PyYAML is required. Install requirements.txt in the selected local environment.') from None

TEXT_SUFFIXES = {'.md', '.yaml', '.yml', '.json', '.py', '.js', '.ts', '.txt', '.toml', '.ini', '.cfg', '.csv', '.env'}
SKIP = {'.git', '__pycache__', '.venv', 'node_modules'}
SENSITIVE_PATTERNS = {
    'credential-like-value': r'(?i)(?:api[_-]?key|access[_-]?token|password|secret|extension[_-]?token)\s*[=:]\s*[\x22\x27]?[A-Za-z0-9_+/=-]{12,}',
    'private-key-material': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'service-token-shape': r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16})\b',
    'email-address': r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}',
    'local-user-path': r'(?i)[A-Z]:[\\/]+Users[\\/]+[^\s\\/]+|/(?:home|Users)/[^\s/]+/',
    'credential-url': r'(?i)https?://[^\s)]+[?&](?:token|key|auth|secret|password)=[^\s)&]{8,}',
    'real-item-link': r'https?://trello\.com/[bc]/[A-Za-z0-9]+|ari:cloud:[a-z]+:',
}


def without_fences(text):
    lines, marker, length = [], None, 0
    for line in text.splitlines():
        fence = re.match(r'^\s*(`{3,}|~{3,})(.*)$', line)
        if fence:
            token = fence.group(1)
            if marker is None:
                marker, length = token[0], len(token)
            elif token[0] == marker and len(token) >= length and not fence.group(2).strip():
                marker = None
            continue
        if marker is None:
            lines.append(line)
    return '\n'.join(lines)


def inspect(root, private_terms=()):
    root = Path(root).resolve()
    findings, hashes, texts = [], {}, {}

    def add(code, path, severity='warning'):
        safe_path = str(path).replace('\\', '/')
        if any(term.casefold() in safe_path.casefold() for term in private_terms):
            safe_path = '[private-path]'
        elif any(re.search(pattern, safe_path) for pattern in SENSITIVE_PATTERNS.values()):
            safe_path = '[sensitive-path]'
        findings.append({'code': code, 'path': safe_path, 'severity': severity})

    if not root.is_dir():
        return {'files': 0, 'findings': [{'code': 'missing-directory', 'path': '.', 'severity': 'error'}]}
    try:
        files = sorted(p for p in root.rglob('*') if p.is_file() and not (set(p.relative_to(root).parts) & SKIP))
    except OSError:
        return {'files': 0, 'findings': [{'code': 'inventory-incomplete', 'path': '.', 'severity': 'error'}]}
    for path in files:
        rel = path.relative_to(root)
        if path.is_symlink():
            add('symlink-not-inspected', rel)
            continue
        try:
            if path.stat().st_size > 2_000_000:
                add('large-file-not-inspected', rel)
                continue
            raw = path.read_bytes()
        except OSError:
            add('file-not-readable', rel, 'error')
            continue
        hashes.setdefault(hashlib.sha256(raw).hexdigest(), []).append(rel)
        if any(part.lower() in ('personalization', 'private', 'backups', 'logs', 'originals') for part in rel.parts):
            add('private-directory-in-package', rel)
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in ('NOTICE', 'LICENSE', '.gitignore', 'requirements.txt'):
            add('nontext-requires-manual-review', rel)
            continue
        try:
            text = raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            add('non-utf8-text', rel, 'error')
            continue
        texts[rel] = text
        for code, pattern in SENSITIVE_PATTERNS.items():
            if re.search(pattern, text) or re.search(pattern, str(rel)):
                add(code, rel)
        if any(term.casefold() in text.casefold() or term.casefold() in str(rel).casefold() for term in private_terms):
            add('private-term-match', rel)
        if path.suffix == '.py':
            try:
                ast.parse(text)
            except SyntaxError:
                add('python-syntax', rel, 'error')
        if path.suffix == '.md':
            for link in re.findall(r'\]\(([^)]+)\)', without_fences(text)):
                if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:|^#', link):
                    continue
                target = link.split('#')[0].strip('<>')
                if not target:
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    add('missing-dependency-link' if not resolved.is_relative_to(root) else 'broken-local-link', rel, 'warning' if not resolved.is_relative_to(root) else 'error')
    for paths in hashes.values():
        if len(paths) > 1:
            for rel in paths:
                add('exact-duplicate-file-review', rel)

    skill_text = texts.get(Path('SKILL.md'))
    if skill_text is None:
        add('missing-entrypoint', 'SKILL.md', 'error')
    else:
        match = re.match(r'^---\r?\n(.*?)\r?\n---(?:\r?\n|$)', skill_text, re.S)
        if not match:
            add('invalid-frontmatter', 'SKILL.md', 'error')
        else:
            try:
                fm = yaml.safe_load(match.group(1))
                if not isinstance(fm, dict):
                    raise ValueError()
                name, desc = fm.get('name'), fm.get('description')
                if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64 or name != root.name:
                    add('invalid-name-or-folder', 'SKILL.md', 'error')
                if not isinstance(desc, str) or not desc.strip() or len(desc.strip()) > 1024:
                    add('invalid-description', 'SKILL.md', 'error')
                if isinstance(desc, str) and desc.startswith('[TODO:'):
                    add('unfinished-description', 'SKILL.md', 'error')
            except (yaml.YAMLError, ValueError):
                add('invalid-frontmatter-yaml', 'SKILL.md', 'error')
            if re.search(r'^\s*\[TODO:[^\n]*\]\s*$', without_fences(skill_text[match.end():]), re.M):
                add('unfinished-instructions', 'SKILL.md', 'error')
    ui = texts.get(Path('agents/openai.yaml'))
    if ui:
        try:
            metadata = yaml.safe_load(ui)
            interface = metadata.get('interface', {})
            if 'short_description' in interface and not (isinstance(interface['short_description'], str) and 25 <= len(interface['short_description']) <= 64):
                add('ui-description-length', 'agents/openai.yaml', 'error')
            if 'default_prompt' in interface and f'${root.name}' not in interface['default_prompt']:
                add('ui-invocation-name', 'agents/openai.yaml', 'error')
            for key in ('icon_small', 'icon_large'):
                if key in interface and not (root / interface[key]).is_file():
                    add('missing-ui-asset', 'agents/openai.yaml', 'error')
            if 'allow_implicit_invocation' in metadata.get('policy', {}) and not isinstance(metadata['policy']['allow_implicit_invocation'], bool):
                add('invalid-invocation-policy', 'agents/openai.yaml', 'error')
        except (yaml.YAMLError, AttributeError, TypeError):
            add('invalid-ui-yaml', 'agents/openai.yaml', 'error')
    return {'files': len(files), 'findings': findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skill_path')
    parser.add_argument('--private-terms', type=Path)
    args = parser.parse_args()
    terms = []
    if args.private_terms:
        try:
            terms = json.loads(args.private_terms.read_text(encoding='utf-8'))
            if not isinstance(terms, list) or any(not isinstance(s, str) or not s.strip() for s in terms):
                raise ValueError()
        except (OSError, ValueError):
            parser.exit(2, 'Private terms must be a readable JSON array of nonempty strings; values omitted.\n')
    try:
        result = inspect(args.skill_path, terms)
    except OSError:
        result = {'files': 0, 'findings': [{'code': 'inspection-incomplete', 'path': '.', 'severity': 'error'}]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result['findings'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
