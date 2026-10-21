---
name: wormhole-william
title: wormhole-william
source: brew
category: fundamentals
commitment: quick
tags: [cryptography, file-transfer, go, network, protocol, quick]
homepage: https://github.com/psanford/wormhole-william
scout_score: 6
status: draft
---

# wormhole-william

**TLDR;** Send a file between two computers with a short spoken code instead of accounts or addresses, end-to-end encrypted, in a single Go binary.

wormhole-william is a Go implementation of magic wormhole. One side runs `send` and gets a short code. The other side runs `receive` and types that code. The two machines find each other and the file, directory, or text goes across with end-to-end encryption. In the README's words: "The endpoints are connected using the same "wormhole code"."

It is wire-compatible with the official Python magic-wormhole client, so a Go sender can talk to a Python receiver and the other way round. It also ships as a Go library, and the README lists third-party tools built on it: desktop and Android apps, a tmux plugin, and a termshark integration.

The idea underneath is that a short, human-friendly code can stand in for a secret. No accounts, no key files, no addresses to look up. The scout's note describes the mechanism as password-authenticated key exchange, which is a good thread to pull on, though the README itself does not explain it. The upstream magic-wormhole documentation is the place to read about the protocol itself.

The `--code` flag on send lets you choose your own phrase, and `--verify` is there for checking a verification string. The global `--relay-url` flag selects a different relay.

## Install

```
brew install wormhole-william
# or, with a Go toolchain: go install github.com/psanford/wormhole-william@latest
```

## Try this

```
wormhole-william send --help
```
Shows send usage, including --code, --code-length, --hide-progress, --verify and the global --relay-url flag.

```
wormhole-william receive --help
```
Shows receive usage, which takes a code and has the alias recv, plus --hide-progress and --verify.

```
wormhole-william shell-completion -h
```
Prints instructions for enabling shell completion, which also completes the receive code.

## What's unique

It talks to the official Python magic-wormhole while being a single Go program that is also an importable library, with a small ecosystem of apps built on it.

## Caveats

The README shows no release or commit dates, so how actively it is maintained is unclear, and its build notes and API example are dated (Go 1.11, ioutil).

## Links

- [GitHub repository (homepage)](https://github.com/psanford/wormhole-william)
- [Go package docs (pkg.go.dev)](https://pkg.go.dev/github.com/psanford/wormhole-william/wormhole?tab=doc)
- [Magic wormhole documentation (upstream protocol)](https://magic-wormhole.readthedocs.io/en/latest/)
- [Examples directory](https://github.com/psanford/wormhole-william/tree/master/examples)
