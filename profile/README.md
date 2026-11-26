# Paseka

Paseka is a set of Rust programs for running a personal AI assistant on your own server. The
assistant talks to you in Telegram, remembers what matters about your life, uses your model
subscriptions and keys, and does not send anything to other people without your say-so.

Nothing here is a hosted service. You run the binaries; your keys and your data stay on your box.
Everything is early: one module has a release, the others are still being built in the open.

## Modules

| Repository | What it is | Status (Nov 2026) |
|---|---|---|
| [ulei](https://github.com/pasekahq/ulei) | The assistant itself: our own agent loop, the Telegram channel, the owner inbox, memory (archive and garden), source connectors, and the task hive | pre-alpha, no release |
| [quota-balancer](https://github.com/pasekahq/quota-balancer) (`qb`) | Quota scheduler and model gateway. Every model call of the ecosystem goes through it: subscriptions, API keys, OpenRouter, fallback chains, spend caps | alpha, [0.1.0](https://github.com/pasekahq/quota-balancer/releases/tag/v0.1.0) |
| [paseka-gate](https://github.com/pasekahq/paseka-gate) | Consent firewall between your agent and other people's agents. Your agent can draft a reply; only you can let it out | pre-alpha, core (M1) done |
| [ummanu](https://github.com/pasekahq/ummanu) | A tool for developers: projects, sprints, worker and reviewer agent heads, a board. It runs the development of everything above | in daily use (Python) |

qb, paseka-gate and ummanu are standalone: each is useful without the rest and talks to it only
over a documented wire protocol. The memory, the task hive and the core live together in the ulei
monorepo, because they make no sense apart.

## What we have decided

- **Our own agent loop, in Rust.** No vendor CLI or SDK sits inside the assistant. New code is
  Rust; older Python parts talk to it over the wire, never through bindings.
- **One road to the models.** ulei knows a single provider, the qb gateway. Switching a
  subscription, key, vendor or model is a qb config change, and CI fails if ulei grows a vendor
  adapter.
- **The agent never approves itself.** Anything that leaves on your behalf needs your consent to
  the exact bytes, or a narrow rule you signed in advance.
- **Small and measured.** Each binary has a size, memory and idle wake-up budget checked in CI.
- **Your data stays on your server.** Only external backups are encrypted, with your own keys
  (SSH key, password, later a passkey). We hold no spare key.
- **AGPL-3.0-only with a DCO sign-off, no CLA.** If you run a modified copy for others over a
  network, you share your changes.

The longer version, with what moved where, what is in progress and why, is in
[ECOSYSTEM.md](https://github.com/pasekahq/.github/blob/main/ECOSYSTEM.md).

## Get involved

- Start with [CONTRIBUTING](https://github.com/pasekahq/.github/blob/main/CONTRIBUTING.md) and the
  [Code of Conduct](https://github.com/pasekahq/.github/blob/main/CODE_OF_CONDUCT.md).
- Questions and ideas go to Discussions in the repository they concern; see
  [SUPPORT](https://github.com/pasekahq/.github/blob/main/SUPPORT.md).
- Found a vulnerability? Report it privately, see
  [SECURITY](https://github.com/pasekahq/.github/blob/main/SECURITY.md).

Maintained by [@vladmesh](https://github.com/vladmesh). He takes part-time contracts on LLM agents and evals: [vladmesh.dev/en/llm-systems](https://vladmesh.dev/en/llm-systems/).
