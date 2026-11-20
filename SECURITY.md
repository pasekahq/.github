# Security Policy

## Reporting a vulnerability
**Please do not report security vulnerabilities in public issues, discussions or pull requests.**

Use GitHub private vulnerability reporting: open the affected repository → **Security** tab → **Report a vulnerability**
(direct link pattern: `https://github.com/pasekahq/<repo>/security/advisories/new`).


Please include: affected repository and version/commit, impact, reproduction steps or proof of concept, and any suggested fix.

## What to expect
- Acknowledgement within **3 business days**.
- Initial assessment within **10 business days**.
- We coordinate a fix and a GitHub Security Advisory (with CVE when applicable) and credit you unless you prefer otherwise.
- Please give us up to **90 days** before public disclosure; we will agree on a date with you.

## Supported versions
The projects are pre-1.0. Only the latest release (or `main` where no release exists) receives security fixes.

## Scope
In scope: code in pasekahq repositories, published release artifacts, install scripts.
Out of scope: third-party services, vulnerabilities requiring a compromised host/root, social engineering, DoS by volume.

Particularly interesting for us: anything that lets an agent act without owner consent (paseka-gate), credential leakage from the model gateway (qb), and sandbox escapes of worker heads (ummanu).
