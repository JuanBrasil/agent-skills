# Agent Skills

Reusable AI agent skills for business workflows, communication, and productivity, maintained by Juan Brasil.

Each skill lives in its own directory, with a `SKILL.md` entry point and any supporting references, scripts, or checks. Install the skills you need individually.

## Available skills

| Skill | Purpose | Documentation |
| --- | --- | --- |
| [commercial-email-replies](skills/commercial-email-replies) | Draft and review commercial email replies, quotes, negotiations, refusals, and follow-ups using the conversation history. | [Usage and checks](skills/commercial-email-replies/README.md) |
| [product-requests](skills/product-requests) | Turn product observations, screenshots, bugs and ideas into implementation-ready cards, issues and correction comments. | [Usage and checks](skills/product-requests/README.md) |
| [delivery-validation](skills/delivery-validation) | Check a delivered request in the product, present evidence and handle approval or return for correction. | [Usage and checks](skills/delivery-validation/README.md) |

## Product Requests + Delivery Validation

These skills have distinct entry points and work together. **Product Requests** can document a new request directly from an observation or idea. **Delivery Validation** checks an existing delivery against the current request and calls Product Requests when a correction comment is needed.

Install both as sibling directories to enable their relative links. The handoff carries the item, current scope, evidence, user verdict, authorized actions and excluded changes. It does not restart the review or request approval again for the same authorized action. A separate new idea becomes a new item only when requested.

Example: validate a delivery → the user accepts most of it and identifies one missing interaction → Product Requests writes that specific correction → comment on the original item → move it to the configured correction state. The workflow supports Trello or GitHub; account access and project/status mappings come from your environment and private configuration.

## Getting started

1. Open the skill's documentation and review its requirements.
2. Copy the skill directory into your assistant's skills directory, or import that directory through your environment's skill workflow. Do not import the repository root as a single skill.
3. Provide the task, relevant context, and the actions you authorize.

For example:

> Use $commercial-email-replies to review this email thread and prepare a concise reply. Save a draft; do not send it.

Tool access and import mechanisms depend on the assistant environment. Skills provide instructions; they do not supply account credentials or integrations.

## Private configuration

Public skills contain reusable workflows and generic examples. Keep personal profiles, contacts, client conversations, rates, and confidential business rules outside the public files.

The email skill supports an optional local `personalization/` directory and includes a generic setup template. The product skills read an optional profile at `personalization/product-workflows/profile.md` under `CODEX_HOME` (or `~/.codex/`). Keep that profile outside this repository; it can contain board/project destinations and individual preferences, but never credentials. Git ignores personalization directories and common local environment files. Ignore rules do not remove files already committed: review staged changes and history before publishing.

## Adding a skill

- Create `skills/<skill-name>/SKILL.md` with the skill's name, description, and instructions.
- Add a README explaining usage, requirements, and any checks.
- Include only reusable material and examples without private data.
- Update the catalog above and run the skill's checks before opening a pull request.

For the current email skill:

```bash
python -m unittest discover -s skills/commercial-email-replies/tests -v
```

For the product skills:

```bash
python scripts/check_product_skills.py
```

The product check is offline: it validates package structure, relative references, UI metadata and privacy patterns. It does not prove live product behavior or guarantee absence of sensitive information; inspect publication diffs as well.

## License

[MIT License](LICENSE), copyright 2026 Juan Brasil.
