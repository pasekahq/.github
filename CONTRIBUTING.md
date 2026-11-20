# Contributing to Paseka

Thanks for helping. This file applies to every repository in **pasekahq** unless the repository has its own CONTRIBUTING.md.

## Before you start
- **Bugs:** open an issue with the bug template. Include version/commit, OS, and the smallest reproduction you have.
- **Features / design changes:** open an issue (or Discussion) first. Changes to wire contracts, protocols or security model need an ADR (`docs/adr/`) before code.
- **Security issues:** never in public issues. See [SECURITY.md](SECURITY.md).

## Development
Rust repositories:
```sh
rustup show                 # toolchain is pinned in rust-toolchain.toml
cargo fmt --all --check
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace
cargo deny check            # licenses, advisories, banned crates (see deny.toml)
```
Size/RSS budgets are enforced by `ci/budgets.sh`; a PR that breaks a budget needs an explicit justification.

Python repository (ummanu): see its README; `ruff check`, `ruff format --check`, `mypy`, `pytest`.

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
