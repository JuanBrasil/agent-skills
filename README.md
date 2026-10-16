# Agent Skills

Reusable AI agent skills for business workflows, communication, and productivity, maintained by Juan Brasil.

Each skill lives in its own directory, with a `SKILL.md` entry point and any supporting references, scripts, or checks. Install the skills you need individually.

## Available skills

| Skill | Purpose | Documentation |
| --- | --- | --- |
| [commercial-email-replies](skills/commercial-email-replies) | Draft and review commercial email replies, quotes, negotiations, refusals, and follow-ups using the conversation history. | [Usage and checks](skills/commercial-email-replies/README.md) |

## Getting started

1. Open the skill's documentation and review its requirements.
2. Copy the skill directory into your assistant's skills directory, or import that directory through your environment's skill workflow. Do not import the repository root as a single skill.
3. Provide the task, relevant context, and the actions you authorize.

For example:

> Use $commercial-email-replies to review this email thread and prepare a concise reply. Save a draft; do not send it.

Tool access and import mechanisms depend on the assistant environment. Skills provide instructions; they do not supply account credentials or integrations.

## Private configuration

Public skills contain reusable workflows and generic examples. Keep personal profiles, contacts, client conversations, rates, and confidential business rules outside the public files.

The email skill supports an optional local `personalization/` directory and includes a generic setup template. Git ignores personalization directories and common local environment files. Ignore rules do not remove files already committed: review staged changes and history before publishing.

## Adding a skill

- Create `skills/<skill-name>/SKILL.md` with the skill's name, description, and instructions.
- Add a README explaining usage, requirements, and any checks.
- Include only reusable material and examples without private data.
- Update the catalog above and run the skill's checks before opening a pull request.

For the current email skill:

```bash
python -m unittest discover -s skills/commercial-email-replies/tests -v
```

## License

[MIT License](LICENSE), copyright 2026 Juan Brasil.
