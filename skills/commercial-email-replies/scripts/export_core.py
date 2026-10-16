#!/usr/bin/env python3
"""Copy the reusable skill into a new empty directory, without personalization."""
import argparse
import re
from pathlib import Path


PUBLIC_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/personalization.example.md",
    "scripts/check_gmail_html.py",
    "scripts/export_core.py",
)


def export_core(destination):
    source = Path(__file__).resolve().parents[1]
    destination = Path(destination).resolve()
    if destination == source or source in destination.parents:
        raise ValueError("Choose a destination outside the installed skill.")
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise ValueError("Destination must be an empty directory or a new path.")
    # Validate every source before writing anything. An allowlist excludes private
    # files, temporary files and Git history even when new files are added later.
    contents = {name: (source / name).read_text() for name in PUBLIC_FILES}
    match = re.search(r"^name:\s*(\S+)\s*$", contents["SKILL.md"], re.M)
    if not match:
        raise ValueError("Skill frontmatter is missing its name.")
    installed_name = match.group(1)
    destination.mkdir(parents=True, exist_ok=True)
    for name, content in contents.items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if name in ("SKILL.md", "agents/openai.yaml"):
            content = content.replace(installed_name, "commercial-email-replies")
        if name == "agents/openai.yaml":
            content = "\n".join(line for line in content.splitlines()
                                if not line.strip().startswith(("icon_small:", "icon_large:"))) + "\n"
        target.write_text(content)
    return len(contents)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination")
    args = parser.parse_args()
    try:
        count = export_core(args.destination)
    except (ValueError, OSError) as error:
        parser.exit(1, f"Export failed: {error}\n")
    print(f"Exported {count} reusable files without personalization or Git history.")
