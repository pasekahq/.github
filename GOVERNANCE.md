# How decisions are made

Paseka is young and has one maintainer, [@vladmesh](https://github.com/vladmesh). This page says how
that works in practice, so nobody has to guess.

## Who decides
- Product direction, licensing, which modules exist and where they live: the maintainer.
- Budgets (binary size, memory, idle wake-ups) change only by the maintainer's decision. A PR that
  needs more room says so and waits for that decision; it does not raise the number itself.
- Everything else is decided in the open, in issues, Discussions and pull requests.

## How a decision is recorded
- Architecture and protocol decisions get an ADR in the repository they affect (`docs/adr/`, or
  `docs/architecture/adr/` in ulei), merged before or with the code. An ADR states the context, the
  decision and what it costs. Superseding one means writing a new ADR, not editing history.
- Decisions that span repositories are summarised in [ECOSYSTEM.md](ECOSYSTEM.md), with links to
  the ADRs behind them.
- Roadmaps (`docs/roadmap.md` or `docs/ROADMAP.md`) describe intent and order, not promises or dates.

## How work happens
Most changes are made through sprints run by [ummanu](https://github.com/pasekahq/ummanu): AI agent
heads write and review the code, a human owns the result. Contributions from people are reviewed the
same way as any other PR: green CI, a reviewer who understands the change, a DCO sign-off.

## Licensing
All repositories are AGPL-3.0-only. Contributions are accepted under the same license with a
[DCO](https://developercertificate.org/) sign-off; there is no CLA. If that ever changes, it will
apply to new contributions only and will be announced here first.

## Changes to this page
By pull request to this repository, like anything else.
