# Paseka: how the pieces fit, what is decided, where things stand

This page is the long version of the [org profile](profile/README.md). It is written for people who
want to understand the project before reading code. Each repository's own README, roadmap and ADRs
are the source of truth; when this page and a repository disagree, the repository wins, and a PR
here to fix the page is welcome.

Last updated: 2026-11-24.

## The shape

```
            you (Telegram)
                 │
         ┌───────┴────────────────────────── ulei (monorepo) ──────────────┐
         │  ulei-tg ──▶ ulei-engine ◀── ulei-inbox                          │
         │                 │   ▲                                            │
         │                 │   └── memory: archive ▸ forest ▸ garden        │
         │                 │       source connectors feed the archive       │
         │                 │   task hive: cards run by agent heads          │
         └─────────────────┼────────────────────────────────────────────────┘
                           │ C4G over a unix socket
                     qb gateway ── qbd ── subscriptions, API keys, OpenRouter

   other people's agents ◀──▶ paseka-gate ◀──▶ your agent (MCP inbox; no approve tool)
                                   └── you approve the exact bytes in a consent bot

   ummanu: the development side. Sprints, worker and reviewer heads, the board.
```

There are two kinds of modules, and the line between them is a test, not a taste
([ulei ADR-0002](https://github.com/pasekahq/ulei/blob/main/docs/architecture/adr/0002-two-module-classes.md)):

- **Standalone products** have value without the rest of Paseka, speak a wire protocol, have their
  own releases and threat model, and never import ecosystem code. Today: qb, paseka-gate, ummanu.
  Each lives in its own repository; ulei pins the versions it works with in `ecosystem.lock`.
- **Internal modules** only make sense together: the core and inbox, the engine, the channels,
  memory, the task hive, the connectors. They live in `crates/` of the ulei monorepo.

Modules never call each other's code. They share versioned contracts (JSON Schema and OpenAPI files
with golden fixtures, numbered C1 to C11 in ulei) and talk over sockets.

## Modules

### ulei: the assistant

A Rust cargo workspace. The agent loop is ours; its behaviour is ported from
[Hermes Agent](https://github.com/NousResearch/hermes-agent) (MIT, credited in ulei's
`THIRD_PARTY_NOTICES.md`) rather than invented again, and any departure from it needs an ADR.

Done so far:

- **Agent loop** (`ulei-engine`): tools, sessions in a SQLite journal, context compaction through a
  qb route, skills as files, an MCP client, web tools, guard policies, prompt caching.
- **Telegram channel** (`ulei-tg`): text, photos, documents, voice with speech-to-text, replies and
  outgoing media, `/new /stop /status /model`.
- **Owner inbox** (`ulei-inbox`): events from other parts of the system reach the chat when it is
  free, with no loss and no duplicates across process kills.
- **Operations**: one `ulei.toml`, `ulei status`, systemd user units, and reproducible static musl
  builds with `SHA256SUMS`. There is no tagged release yet.
- **Memory, first version**: the archive daemon `ulei-memory` (raw items from every source, never
  lossy, full-text indexed) and the garden `ulei-garden` (short facts with a source and dates, hybrid
  full-text and vector search in one SQLite file, and a seedbed for today's new facts).
- **Source connectors** (`ulei-connectors`): small programs that pull data from a source into the
  archive on a schedule, each run sandboxed with Landlock, seccomp and systemd limits, with network
  access only to the addresses it declares.

In progress:

- **The task hive moves in.** The board that hands work to agent heads ran as a Python package in a
  private repository. It is moving into `hive-py/` of ulei
  ([ADR-0068](https://github.com/pasekahq/ulei/blob/main/docs/architecture/adr/0068-python-hive-in-hive-py.md)),
  cleaned of personal data, with its own CI lane and a board reform in the same step (below). A Rust
  hive in `crates/hive` comes later and takes over behind a flag.
- **The night gardener**: the process that turns the archive into the forest and the forest into
  garden facts. It is the main thing standing between the current state and the first real
  deployment.

Next: a pilot on a test bot, fixes from it, then the first real deployment moves from the old
Python stack to ulei, with the old stack kept switched off on the same server for rollback.

### qb (quota-balancer): the road to the models

qb answers one question fast: where should this run go, given which subscriptions and keys have
quota left and which windows reset soonest. Its optional gateway role holds the credentials and
serves `/v1/messages`, `/v1/chat/completions` and `/v1/responses`, with fallback chains, route
aliases with hot reload, spend caps on keys, an admin API and a model ladder per role.

- **Released:** [0.1.0](https://github.com/pasekahq/quota-balancer/releases/tag/v0.1.0) on
  2026-11-22, with checksums.
- **In progress:** Anthropic Message Batches for API-key logins (submit, status, results, cancel,
  costs counted against the spend cap).
- **Next:** task tags bound to logins (below), and use across several hosts.

### paseka-gate: consent between agents

Your agent keeps everything it knows, but it has no tool to approve its own messages. When another
person's agent asks something, your agent drafts a reply, the gate scores the risk, and you see the
exact bytes in a Telegram consent bot or Mini App. Only then does the gate sign and send. Pairing
uses a six-digit check; a source registry of Allow / Ask / Never decides what can go to whom, and
one-time codes are always Never.

- **Done:** the core (M1): protocol types, mandates bound to a hash of the exact bytes, conformance
  attacks. The design review of November 2026 is fully applied (key rotation separate from the
  address, a PIN level above plain approval, a tripwire mode, the source registry, peers that skipped the
  check kept at a low trust level), recorded in ADRs 0013 to 0022. 44 of the 57 conformance attacks
  run and pass; the other 13 wait for parts that do not exist yet.
- **Next, in order:** M2 local gate (storage, MCP server, journal), M3 consent bot and Mini App,
  M4 peers, M5 release and install.
- It is a clean slate: no compatibility with the older Python peer gate it grew out of
  ([ADR 0009](https://github.com/pasekahq/paseka-gate/blob/main/docs/adr/0009-clean-slate.md)).

### ummanu: the development side

A Python tool that runs projects, issues and sprints with worker, reviewer and observer agent heads
and a board. Every sprint of ulei, qb and paseka-gate goes through it. It is a standalone product for
developers, not part of the assistant's base install.

## What moved, and what is moving

| What | From | To | When / state |
|---|---|---|---|
| ulei, quota-balancer, ummanu | personal account | `pasekahq/*`, AGPL-3.0-only + DCO | moved 2026-11-20 |
| paseka-gate | private draft | `pasekahq/paseka-gate`, public | 2026-11-21 |
| Task hive (Python board) | private repository | `pasekahq/ulei`, `hive-py/` | in progress ([ADR-0068](https://github.com/pasekahq/ulei/blob/main/docs/architecture/adr/0068-python-hive-in-hive-py.md)) |
| Garden and archive | Python prototype | `ulei-garden`, `ulei-memory` crates | first version done |
| Encrypted backups | shell scripts of one deployment | `ulei-backup` binary in ulei | design accepted ([ADR-0057](https://github.com/pasekahq/ulei/blob/main/docs/architecture/adr/0057-encrypted-external-backups.md)), code after the MVP launch |
| Task tag → model login | hard-coded launcher | a qb config rule | planned in qb, consumed by the hive |
| Old Python peer gate | | retired after paseka-gate M4 | not started |

## Decisions worth knowing

Dated where the date helps. Each one has an ADR or issue in the repository it touches.

**Architecture**

- *2026-11-16.* Two module classes, as above. New code in Rust; Python is reached only over the wire,
  no PyO3.
- *2026-11-17.* Our own agent loop instead of wrapping a vendor CLI. Every model call goes through
  qb, including API keys and OpenRouter; ulei has no vendor adapter and CI enforces it.
- *2026-11-17.* Port Hermes Agent behaviour instead of reinventing it; deviate only with an ADR.
- *2026-11-20.* License: AGPL-3.0-only with a DCO sign-off. Anyone may host Paseka for others, as
  long as they publish their changes. No CLA.

**Memory**

- Three layers. The **archive** keeps raw items exactly as they came, forever, compressed, with a
  full-text index and no model calls. The **forest** is the archive with spam dropped and long
  threads condensed without losing facts. The **garden** holds short facts (up to 300 tokens each),
  each with the people it is about, topic tags, dates and a link to its source in the archive.
- New facts of the day land in a **seedbed**, searchable right away; a nightly pass deduplicates,
  reconciles them with the garden and reports only real contradictions to the owner.
- When a fact changes, the old one is rewritten in the past tense with its dates and a new one is
  added. "Forget" hides a record from retrieval; the archive itself is touched only on an explicit
  command.
- The agent does not curate memory. It gets a `garden_propose` call for "remember this" and owner
  corrections; the rest is the gardener's job.
- The prompt stays thin: a personality, three default safeguards and a few skills for finding the
  rest. Facts, tools and skills come in through retrieval, not as a full catalogue in every request.

**Safety defaults** (all of them can be changed by the owner)

- The assistant does not write to other people without a direct command.
- It never says "I'll do it later" unless a task really exists.
- It does not delete data irreversibly without a direct command.

**Connectors and data**

- Source connectors are plugins: the core only knows "put raw items into the archive" and a schedule.
  A connector can be a crate, any program over stdin/stdout, or a wrapped MCP server. Only the ones
  you enable are installed.
- Connectors you write stay on your server under local git. Sharing one to a common catalogue is
  opt-in; nothing is collected silently.
- Data on the server is not encrypted at rest. External backups are, with age and one data key
  wrapped separately for each recovery method (SSH key, password; passkeys through age plugins), so
  you can restore after a wipe on your own. We keep no copy of your key.
- Backup targets are pluggable (S3-compatible storage, Google Drive and so on). If you skip the
  choice, the assistant keeps reminding you.

**Tasks and models**

- The hive board gets three columns: In progress, Waiting (with a reason), Done for the last couple
  of days. Schedules leave the board; their runs go to the schedule's history.
- A card counts as in progress while its process is alive. Done is decided by a one-shot judge
  that checks the result against the task, with a model picked by tier from qb.
- No built-in "personal vs. public" classes. You define task tags and bind each tag to specific qb
  logins in the config. A tagged task goes only through those logins; if none fits, qb refuses
  instead of falling back to another one.

## Where to look

| | Roadmap | Decisions |
|---|---|---|
| ulei | [docs/roadmap.md](https://github.com/pasekahq/ulei/blob/main/docs/roadmap.md) | [docs/architecture/adr/](https://github.com/pasekahq/ulei/tree/main/docs/architecture/adr) |
| qb | [docs/roadmap.md](https://github.com/pasekahq/quota-balancer/blob/main/docs/roadmap.md), [CHANGELOG](https://github.com/pasekahq/quota-balancer/blob/main/CHANGELOG.md) | [docs/adr/](https://github.com/pasekahq/quota-balancer/tree/main/docs/adr) |
| paseka-gate | [docs/MVP.md](https://github.com/pasekahq/paseka-gate/blob/main/docs/MVP.md) | [docs/adr/](https://github.com/pasekahq/paseka-gate/tree/main/docs/adr) |
| ummanu | [docs/ROADMAP.md](https://github.com/pasekahq/ummanu/blob/main/docs/ROADMAP.md) | [docs/ARCHITECTURE.md](https://github.com/pasekahq/ummanu/blob/main/docs/ARCHITECTURE.md) |
