# Contributing to Paseka

Thanks for helping. This file applies to every repository in **pasekahq** unless the repository has its own CONTRIBUTING.md.

## Which repository
- **ulei**: the assistant (agent loop, Telegram channel, inbox, memory, connectors, and the task hive,
  which is moving into `hive-py/`). Rust, plus one Python lane for the hive.
- **quota-balancer** (`qb`): quota scheduler and model gateway. Rust.
- **paseka-gate**: consent firewall between agents. Rust.
- **ummanu**: sprints and agent heads for developers. Python.
- **.github**: this file, the org profile and [ECOSYSTEM.md](ECOSYSTEM.md). Fixes to the overview
  are welcome when a repository has moved on and the page has not.

Not sure where something belongs? Open a Discussion in the repository closest to it.

## Before you start
- **Bugs:** open an issue with the bug template. Include version/commit, OS, and the smallest reproduction you have.
- **Features / design changes:** open an issue (or Discussion) first. Changes to wire contracts, protocols, the security model, a new crate or a new dependency need an ADR before code. ADRs live in `docs/architecture/adr/` in ulei and in `docs/adr/` elsewhere.
- **Security issues:** never in public issues. See [SECURITY.md](SECURITY.md).
- **Each repository's own `AGENTS.md` and `CONTRIBUTING.md`** have the rules specific to it (module boundaries, banned crates, budgets). Read them; they win over this file.

## Development
Rust repositories:
```sh
rustup show                 # the toolchain is pinned in the repository
cargo fmt --all --check
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace
cargo deny check            # licenses, advisories, banned crates (see deny.toml)
```
ulei also has `cargo xtask check` (module boundaries, contracts, ADR format) and `python3 -m ci.broad_check`, which runs everything at once.

Size, memory and idle wake-up budgets are enforced by `ci/budgets.sh`. A PR does not raise a budget to make itself pass; budgets change only by a maintainer's decision, recorded in an ADR.

Contracts between modules are versioned files with golden fixtures (ulei `contracts/`). A standalone product is never edited from ulei: ulei changes only its pin in `ecosystem.lock` and the vendored contract.

Python code (ummanu, and `hive-py/` in ulei once the hive lands there): see the repository's README; `ruff check`, `ruff format --check`, `mypy`, `pytest` where configured.

**No personal data or deployment details** in code, tests, fixtures, logs or commit messages: no real names, hostnames, home paths, tokens or account ids. Use neutral examples (`vendor-a`, `example.org`).

## Pull requests
- One logical change per PR; keep it reviewable. Branch from `main`, rebase rather than merge `main` into your branch.
- CI must be green; `main` is protected by a ruleset (pull request and green required checks, no force-push or deletion).
- Write tests for behaviour changes. Update docs/CHANGELOG when user-visible.
- Commit messages: imperative mood, short subject (≤72 chars), body explains *why*.
- Dependencies: new crates/packages must pass `cargo deny` and be justified in the PR description. Some crates are banned by policy (see `deny.toml`).
- AI-assisted contributions are welcome; you are responsible for every line and must be able to explain it. Keep `Co-Authored-By` trailers if your tool adds them.

## Sign-off (DCO), no CLA
Every commit must be signed off under the [Developer Certificate of Origin 1.1](https://developercertificate.org/):
```
Signed-off-by: Your Name <you@example.com>
```
Use `git commit -s` (or `git rebase --signoff main` for commits you already made). The sign-off must match the commit author. The `dco` check enforces it on pull requests. There is no CLA.

## License
Paseka repositories are licensed under the [GNU Affero General Public License v3.0 only](https://www.gnu.org/licenses/agpl-3.0.html) (SPDX `AGPL-3.0-only`); the `LICENSE` file of each repository is authoritative. By signing off you certify that you have the right to submit your contribution under that license, and you license it under the same terms.
