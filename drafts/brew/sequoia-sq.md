---
name: sequoia-sq
title: sq (Sequoia-PGP)
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cli, crypto, openpgp, pgp, protocol, rust]
homepage: https://sequoia-pgp.org
scout_score: 5
status: draft
---

# sq (Sequoia-PGP)

**TLDR;** A Rust OpenPGP command-line tool that encrypts, signs and verifies, and can inspect keys and messages as of any past date.

sq is the command-line frontend for Sequoia, a Rust implementation of OpenPGP. It covers the usual tasks: encrypt and decrypt, sign and verify (including detached signatures), generate and manage keys and certificates, query keyrings, and look up or publish certificates over the network. Armor is handled automatically, and output is ASCII-armored by default.

The homepage describes Sequoia as a new OpenPGP library focused on safety and correctness, and says that improving the security of OpenPGP users "requires more than a new implementation". The sq manual also pitches a Web of Trust model as an alternative to X.509 certificate authorities.

The interesting door is inspection. `sq inspect` describes any OpenPGP data in human-readable form, much like file(1) does for other formats. Beneath it, `sq packet dump` shows the packet structure, and the manual says it may be useful "as a learning tool". Time is also a real input: `--time` and `--policy-as-of` let you verify or inspect data as it would have looked on a past date, under the cryptographic policy of that era.

sq is not fully stateless. It uses a certificate store under `$HOME/.local/share/pgp.cert.d` and starts a key store server on first use unless you pass `--key-store=none`. `--home` or `SEQUOIA_HOME` isolates its data, which is a good idea while experimenting.

## Install

```
brew install sequoia-sq
# Optional: keep experiments away from your real data
# export SEQUOIA_HOME=$(mktemp -d)
```

## Try this

```
sq --help
```
Lists the subcommands: encrypt, decrypt, sign, verify, download, inspect, cert, key, pki, network, keyring, packet and more.

```
sq inspect message.pgp
```
Describes an OpenPGP message or certificate in human-readable form, like file(1) does for other formats.

```
sq inspect --time 20130721 juliet.pgp
```
Shows how a certificate looked on a past date, such as July 21, 2013.

## What's unique

sq treats time as a first-class input, so you can inspect or verify data as of any past date and policy. `sq download` also fetches a file and authenticates it against a signer fingerprint in one step.

## Caveats

A January 2026 Sequoia blog post answers a 39C3 talk that reported vulnerabilities in several tools including sq, blaming literal gpg-to-sq command translation and ignored output; the README is also thin, so the manual is where the real docs are.

## Links

- [Sequoia-PGP homepage](https://sequoia-pgp.org)
- [sq manual pages](https://sequoia-pgp.gitlab.io/sequoia-sq/)
- [sequoia-sq source repository (GitLab)](https://gitlab.com/sequoia-pgp/sequoia-sq)
- [Sequoia book](https://book.sequoia-pgp.org/)
