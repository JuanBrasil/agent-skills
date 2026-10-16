#!/usr/bin/env python3
"""Validate the new reply body only, before saving and after reading it back."""
import argparse
import re
import sys
from html import unescape
from pathlib import Path


def check(source, *, english_greeting=None, emoticon_ends_paragraph=False):
    source = source.strip()
    errors = []
    blocks = re.findall(r"<div>(.*?)</div>", source, re.S)
    if not blocks or "".join(f"<div>{b}</div>" for b in blocks) != source:
        return ["Use only top-level <div> blocks with no attributes or outer wrapper."]
    if len(blocks) % 2 != 1:
        errors.append("Do not put an empty separator before or after the reply.")
    for i, block in enumerate(blocks):
        if i % 2:
            if block != "<br>":
                errors.append("Separate every paragraph with exactly <div><br></div>.")
            continue
        text = unescape(re.sub(r"<[^>]+>", "", block)).strip()
        if not text:
            errors.append("Content blocks must not be blank.")
        if re.search(r"</?(?:p|div)\b|\bmargin(?:-[a-z]+)?\s*:", block, re.I):
            errors.append("Do not use p elements, nested divs or margins for paragraph spacing.")
        if re.search(r"^\s*<br\s*/?>|<br\s*/?>\s*$|<br\s*/?>\s*<br\s*/?>", block, re.I):
            errors.append("Do not add leading, trailing or doubled breaks inside a content block.")
        if emoticon_ends_paragraph and re.search(r":\)\s*\S", text):
            errors.append("Start a new paragraph after :).")
        if english_greeting == "Hey" and i == 0 and re.match(r"Hi\b", text, re.I):
            errors.append("Use the configured English greeting: Hey.")
    return sorted(set(errors))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="HTML body file; otherwise read stdin")
    parser.add_argument("--english-greeting", choices=["Hey"])
    parser.add_argument("--emoticon-ends-paragraph", action="store_true")
    args = parser.parse_args()
    source = Path(args.path).read_text() if args.path else sys.stdin.read()
    errors = check(source, english_greeting=args.english_greeting,
                   emoticon_ends_paragraph=args.emoticon_ends_paragraph)
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print("Gmail reply formatting is valid.")
    sys.exit(bool(errors))
