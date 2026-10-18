# Skill Creator — portable distribution

Create or update reusable Codex skills. This is a reviewed derivative of the OpenAI-bundled Skill Creator, not a replacement installed over a managed system skill. See [NOTICE](NOTICE) and the original [Apache 2.0 license](license.txt). The repository's root MIT license does not replace this directory's license.

## Setup and use

Copy this directory to an environment that does not already supply Skill Creator; avoid installing a duplicate alongside a managed version. Install `requirements.txt` in an isolated Python environment. Use `$skill-creator` for creation/update, or run the initializer documented in [SKILL.md](SKILL.md).

Skill Refinement is complementary: it audits and reorganizes an existing skill while checking behavior, privacy and release contents. Creator does not need it for ordinary creation.

## Review changes

The portable helpers explicitly use UTF-8 for reads/writes, reject empty required name/description and reject invalid UI arguments before creating a partial skill directory. UI metadata includes an invocation prompt and a valid description length. Decorative upstream icons are omitted; functional references and helpers are retained. The managed local installation is unchanged.

Run `python -m unittest discover -s tests -v` for helper regression tests and `python scripts/quick_validate.py PATH` for frontmatter/scaffold validation. Passing a structural validator is not a test of live integrations or a guarantee that instructions are correct.
