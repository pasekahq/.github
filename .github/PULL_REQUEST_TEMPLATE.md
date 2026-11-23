## What and why
<!-- One logical change. Link the issue: Fixes #123 -->

## How it was tested
<!-- Commands you ran, new/changed tests -->

## Checklist
- [ ] `cargo fmt`, `clippy -D warnings`, `cargo test`, `cargo deny check` pass locally (ruff/mypy/pytest for Python; `cargo xtask check` in ulei)
- [ ] Size/RSS budgets still hold (`ci/budgets.sh`); budgets are not raised in a PR without a maintainer decision
- [ ] Contracts, protocol, a new crate or dependency → ADR added, contract version bumped where it applies
- [ ] Docs / CHANGELOG updated for user-visible changes
- [ ] Commits are signed off (`git commit -s`)
- [ ] No secrets, tokens, hostnames or personal data in code, tests or logs
