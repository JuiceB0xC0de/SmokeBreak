---
name: zlint
title: zlint
source: brew
category: fundamentals
commitment: quick
tags: [certificates, go, linter, pki, quick, tls, x509]
homepage: https://zmap.io/
scout_score: 7
status: draft
---

# zlint

**TLDR;** A certificate linter that checks X.509 certificates against RFC 5280, CA/Browser Forum rules, and root store policies, the same checks CAs run before issuing.

ZLint reads a PEM certificate and runs a registry of named lints against it. Each lint ties to a clause in a source document: RFC 5280, the CA/Browser Forum Baseline Requirements, Mozilla's root policy, Apple's CT policy, or ETSI standards. It reports where the certificate departs from those rules. It also handles certificate revocation lists in PEM form.

It exists because the Mozilla root program strongly recommends pre-issuance linting, so a CA can catch a malformed certificate before it goes out. ZLint began with RFC 5280 and an early version of the Baseline Requirements, then was restructured so lints from other sources could be added more easily. The README lists CAs and tools that integrate it, including Let's Encrypt's Boulder, Sectigo, crt.sh, Google Trust Services, and Microsoft.

The idea underneath is that the Web PKI rulebook is spread across many documents, and someone has to turn the prose into executable checks. Reading the lint names and sources shows how the rules are enforced in practice. You can include or exclude whole sources or individual lints, and some lints read settings from an optional TOML file. Certificates are parsed with ZCrypto's lenient x509 package, and a certificate that fails to parse counts as rejected.

## Install

```
brew install zlint
# The README's own documented install is from Go source (needs Go 1.16 or newer): go get github.com/zmap/zlint/v3/cmd/zlint
# You need a PEM-encoded certificate file to lint. No account or setup required.
```

## Try this

```
zlint mycert.pem
```
Lints the certificate with all applicable lints.

```
zlint -list-lints-source
```
Lists the available lint sources, such as the standards bodies the rules come from.

```
zlint -excludeSources=ETSI_ESI mycert.pem
```
Lints the certificate with everything except the ETSI ESI lints.

## What's unique

Most linters check syntax or one spec. ZLint combines RFC, CA/Browser Forum, root program, and ETSI rules in one registry, each tagged by source so you choose which apply.

## Caveats

The README says lint coverage is not complete, and because lint names and results can change between versions, upgrades can alter outcomes for anyone relying on them for policy.

## Links

- [ZMap Project homepage](https://zmap.io/)
- [ZLint GitHub repository and README](https://github.com/zmap/zlint)
- [Contributing guide (extending ZLint with new lints)](https://github.com/zmap/zlint/blob/master/CONTRIBUTING.md)
- [ZCertificate (command-line certificate parser that links against ZLint)](https://github.com/zmap/zcertificate)
