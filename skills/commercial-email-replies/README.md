# Commercial Email Replies

An AI skill for drafting and reviewing individual commercial emails using the actual conversation context.

It helps with partnership inquiries, proposals, negotiation, polite refusals and follow-ups. The workflow separates reusable instructions from optional, private business personalization.

## What it does

- Reads the relevant history before replying and avoids repeating answered questions.
- Preserves agreed terms and distinguishes a quote from an approval.
- Requests only information needed for the current stage.
- Keeps drafts, sending and inbox organization as separately authorized actions.
- Checks paragraph spacing in Gmail-style HTML before and after saving.
- Supports optional policies without embedding anyone's contacts, prices or talent roster.

## Install and use

Copy this directory (`skills/commercial-email-replies`) into your AI assistant's skills directory, keeping the folder name `commercial-email-replies`. Alternatively, use your environment's skill import workflow and select this folder rather than the whole repository.

Invoke the skill with the email and relevant conversation history:

> Use $commercial-email-replies to prepare a concise reply based on this thread. Save a draft; do not send it.

The skill instructions are written in Portuguese. Replies follow the language and voice requested by the user or established in the conversation.

## Private personalization

The core works without a profile. To configure your own installation, follow [the generic template](references/personalization.example.md) and create a local `personalization/profile.md`.

Keep business restrictions, price sources, contact details and real examples inside `personalization/`. That directory is excluded from Git by default. The public repository contains no actual personalization or client conversation history.

## HTML validation

Requires Python, with no third-party dependencies:

```bash
python scripts/check_gmail_html.py reply.html
```

Optional voice settings are configured by each user's profile:

```bash
python scripts/check_gmail_html.py --english-greeting Hey --emoticon-ends-paragraph reply.html
```

The validator checks the new reply body, without quoted history or an automatic signature. It does not verify commercial facts or grant permission to send emails.

## Export a reusable copy

```bash
python scripts/export_core.py /path/to/new/empty-directory
```

The exporter uses an explicit file allowlist and does not copy personalization, private assets, temporary files or Git history. It refuses to overwrite an existing nonempty directory. Review the exported files before publishing your own version.

## Run checks

```bash
python -m unittest discover -s tests -v
```

## License

[MIT](../../LICENSE), copyright 2026 Juan Brasil.
