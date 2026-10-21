---
name: ssh-audit
title: ssh-audit
source: brew
category: fundamentals
commitment: quick
tags: [crypto, network, protocol, quick, security, ssh]
homepage: https://github.com/jtesta/ssh-audit
scout_score: 5
status: draft
---

# ssh-audit

**TLDR;** Connects to an SSH server, or poses as one for your client, and lists every algorithm offered, each graded weak, legacy or fine.

ssh-audit opens a TCP connection to an SSH server, reads the banner, and records the key-exchange, host-key, cipher and MAC algorithms the server advertises. It checks each against an internal database of algorithms and known software versions. Each line comes back annotated with when the algorithm appeared, whether it has been removed or disabled, and whether it is weak or legacy. It also gives recommendations tuned to the software it recognizes. Output is plain text or JSON.

The tool also works the other way around. With `-c` it listens as a fake server on port 2222 and audits whatever SSH client connects, so you can see what your own `ssh` offers. Policy mode compares a server against a built-in or custom policy file. `-M` builds a starting policy from a known-good host so other hosts can be checked against it.

The idea underneath is that SSH opens every session with a negotiation. Both sides list what they support and they settle on a common set. Seeing that list shows how a protocol everyone uses stays flexible and how old choices linger in configs. Recent changelog entries add warnings for key exchanges with no protection against quantum attacks, citing the Harvest Now, Decrypt Later strategy.

This is the maintained v2.0+ fork of arthepsy/ssh-audit. The README says it was forked "due to inactivity".

## Install

```
brew install ssh-audit
# needs Python 3 (brew pulls it in). Alternatives from the README: pip3 install ssh-audit, snap, Docker. To audit a client, you need an SSH client to point at the listener.
```

## Try this

```
ssh-audit localhost
```
Audits the SSH server on your own machine and prints the banner and every algorithm with its security status.

```
ssh-audit -c
```
Starts a listener on port 2222. Run ssh -p 2222 anything@localhost in another terminal to see how your SSH client is configured.

```
ssh-audit -L
```
Lists the built-in policies, whose names can be passed to -P for a policy audit.

## What's unique

It audits both directions, so it can grade an SSH client as well as a server. Policy mode can also generate a baseline from a known-good host and check other hosts against it.

## Caveats

The standard audit runs a connection rate test unless you pass --skip-rate-test, and the --dheat option performs a real denial-of-service attack, so only point it at hosts you are allowed to test.

## Links

- [GitHub repository and README](https://github.com/jtesta/ssh-audit)
- [Web front-end](https://www.ssh-audit.com/)
- [Hardening guides](https://www.ssh-audit.com/hardening_guides.html)
