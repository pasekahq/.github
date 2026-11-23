# Security Policy

## Reporting a vulnerability
**Please do not report security vulnerabilities in public issues, discussions or pull requests.**

Use GitHub private vulnerability reporting: open the affected repository → **Security** tab → **Report a vulnerability**
(direct link pattern: `https://github.com/pasekahq/<repo>/security/advisories/new`).
If you are not sure which repository is affected, pick the closest one; we will move the report.

Please include: affected repository and version/commit, impact, reproduction steps or proof of concept, and any suggested fix.

## What to expect
- Acknowledgement within **3 business days**.
- Initial assessment within **10 business days**.
- We coordinate a fix and a GitHub Security Advisory (with CVE when applicable) and credit you unless you prefer otherwise.
- Please give us up to **90 days** before public disclosure; we will agree on a date with you.

## Supported versions
The projects are pre-1.0. Only the latest release (or `main` where no release exists) receives security fixes.
Today that means qb 0.1.x and `main` of ulei, paseka-gate and ummanu. A repository's own SECURITY.md, where present, takes precedence over this file.

## Scope
In scope: code in pasekahq repositories, published release artifacts, install scripts.
Out of scope: third-party services, vulnerabilities requiring a compromised host/root, social engineering, DoS by volume.

Particularly interesting for us:
- **paseka-gate:** anything that lets an agent send something without the owner's consent to those exact bytes, or widens what a mandate allows.
- **qb:** credential leakage from the model gateway, a client reaching a login or route it is not allowed to use, a tagged request that ends up on a login outside its tag.
- **ulei:** a source connector escaping its sandbox (files, network, other connectors' keys), secrets reaching the model or the logs, a backup that can be read or restored without one of the owner's recovery methods.
- **ummanu:** worker heads escaping their sandbox or reaching data outside their scope.
