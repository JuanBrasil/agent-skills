# Skill Refinement

Review an existing skill without losing its learned behavior. Consolidate equivalent rules, resolve conflicts, organize references, keep personal configuration outside the package, and validate before authorized publication.

Install this directory as `skill-refinement`. Use `$skill-refinement` with the target skill and say whether you want an audit, edits, export or publication. These are separate permissions. The skill can run without Skill Creator; an available creator validator is a useful complement.

## Local inspection

Install `requirements.txt` in your chosen isolated environment, then run `python scripts/inspect_skill.py PATH`. An optional `--private-terms LOCAL_JSON` accepts a list of private names/domains without echoing the values. Keep that list and reports outside distribution. The helper never edits files or uses the network; findings need review and do not authorize deletion.

Tests: `python -m unittest discover -s tests -v`. Structural checks and pattern scans do not prove behavioral correctness or absence of sensitive data. Follow the decision scenarios and inspect the exact export manifest/diff.
