## What and why
<!-- One logical change. Link the issue: Fixes #123 -->

## How it was tested
<!-- Commands you ran, new/changed tests -->

## Checklist
- [ ] `cargo fmt`, `clippy -D warnings`, `cargo test`, `cargo deny check` pass locally (or ruff/mypy/pytest for Python)
- [ ] Size/RSS budgets still hold (`ci/budgets.sh`) or the change is justified below
- [ ] Contracts/protocol changed → ADR added and contract version bumped
- [ ] Docs / CHANGELOG updated for user-visible changes
- [ ] Commits are signed off (`git commit -s`)
- [ ] No secrets, tokens, hostnames or personal data in code, tests or logs
