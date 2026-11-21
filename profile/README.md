# Paseka

**Rust ecosystem for personal AI agents** — small, auditable binaries you run on your own server.

| Module | What it does | Status |
|---|---|---|
| [ulei](https://github.com/pasekahq/ulei) | Agent harness: engine, Telegram channel, inbox. Contracts C1–C9 | pre-alpha |
| [quota-balancer (qb)](https://github.com/pasekahq/quota-balancer) | Quota balancer and model gateway: subscriptions and keys behind one endpoint, fallback chains, spend caps | alpha |
| [paseka-gate](https://github.com/pasekahq/paseka-gate) | Consent firewall between your agent and other people's agents (A2A): hash-bound mandates, owner approval | pre-alpha (design / M1) |
| [ummanu](https://github.com/pasekahq/ummanu) | Development module: projects, sprints, worker/reviewer heads, board | in daily use |

### Principles
- **Self-host first.** Your keys, your data, your box.
- **Small and measurable.** Every binary has a size/RSS budget enforced in CI.
- **Contracts over coupling.** Modules talk over versioned wire contracts; each standalone product works without the rest.
- **The agent never approves itself.** Anything leaving your machine on your behalf needs your consent.

### License
All published repositories are [AGPL-3.0-only](https://www.gnu.org/licenses/agpl-3.0.html); contributions come with a DCO sign-off, no CLA.

### Get involved
- Read [CONTRIBUTING](https://github.com/pasekahq/.github/blob/main/CONTRIBUTING.md) and the [Code of Conduct](https://github.com/pasekahq/.github/blob/main/CODE_OF_CONDUCT.md).
- Report vulnerabilities privately: see [SECURITY](https://github.com/pasekahq/.github/blob/main/SECURITY.md).
