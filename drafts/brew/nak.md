---
name: nak
title: nak
source: brew
category: fundamentals
commitment: quick
tags: [cli, go, json, network, nostr, protocol, quick]
homepage: https://github.com/fiatjaf/nak
scout_score: 5
status: draft
---

# nak

**TLDR;** A single Go binary that lets you create, query, sign and relay Nostr events from the terminal, with JSON output you can pipe into jq.

nak is a command-line tool for the Nostr protocol, a decentralized system where signed JSON events are passed around by simple relay servers. Each subcommand is a verb: `event`, `req`, `fetch`, `decode`, `encode`, `key`, `profile`, `verify`, `bunker`, `serve`, `fs`, `blossom`, `gift`, `sync`, `admin`. The README calls it a "nostr army knife" for "doing all things nostr" and tells you to read the built-in help to learn everything it can do. It gives no longer statement of motive.

Output is line-delimited JSON, so commands chain like Unix tools. The README pipes `nak req ...` into `nak event relay1 relay2` to republish events, and into `jq` to pull out fields. Built-in jq helpers are available through `--jq` and a `~/.jq` file.

The idea underneath is that a social network can be reduced to signed JSON blobs, keys and dumb relays, so you can poke at all of it by hand. With nak you can generate a key, sign a note, publish it to two relays, and query it back. You can also run a local relay at `ws://localhost:10547` for testing, or mount Nostr as a FUSE filesystem where writing a file creates a note.

Further in are NIP-49 encrypted keys, a NIP-46 remote-signing bunker, MuSig2 co-signing, gift wrap, Blossom file servers and negentropy sync between relays. You do not need any of them to start.

## Install

```
brew install nak
# No account needed for basic use. Publishing needs a relay that accepts your key.
```

## Try this

```
nak key generate
```
Prints a new random private key in hex.

```
nak serve
```
Runs a verbose local relay at ws://localhost:10547, handy for testing without touching public relays.

```
nak req -k 1 -t t=gm -l 2 nostr.mom nostr.wine nostr-pub.wellorder.net | jq .content
```
Asks three relays for kind 1 notes tagged t=gm, two each, and prints just the text.

## What's unique

One binary covers a wide slice of Nostr, from event signing to a FUSE mount to relay sync, and its JSON output composes through pipes like an ordinary Unix tool.

## Caveats

Public relays often reject writes from unknown keys (the README's own output shows 'blocked: not on white-list'), and the bunker, MuSig2 and FUSE features need extra setup.

## Links

- [Homepage / README](https://github.com/fiatjaf/nak)
- [Releases](https://github.com/fiatjaf/nak/releases)
- [jq helper functions (jq.go)](https://github.com/fiatjaf/nak/blob/master/jq.go#L10)
