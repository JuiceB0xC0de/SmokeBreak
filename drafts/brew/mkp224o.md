---
name: mkp224o
title: mkp224o
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, cryptography, ed25519, network, onion, tor]
homepage: https://github.com/cathugger/mkp224o
scout_score: 6
status: draft
---

# mkp224o

**TLDR;** Brute-forces Tor v3 onion addresses until one starts with a prefix you choose, showing how a hidden service's name comes from its key.

mkp224o is a vanity address generator for Tor v3 hidden services. You give it a prefix or a few, and it generates ed25519 keypairs over and over until the resulting .onion name begins with what you asked for.

The idea underneath is that a v3 onion address is not assigned by anyone. It is derived from the service's public key, so the name and the key are the same thing seen two ways. A vanity address is therefore a search problem: each extra character you want multiplies the expected work by 32, because the address is base32.

That makes it a small door into how Tor hidden services are named, and into the arithmetic of brute-force search. It depends on libsodium for the ed25519 work. The brief for this entry was empty, so details such as flags and output layout are not covered here; the tool's own help is the place to start.

## Install

```
brew install mkp224o
```

## Try this

```
mkp224o --help
```
Prints the available options and usage, which is the way in to choosing a prefix and an output location.

## What's unique

It is a focused tool for one job: searching the v3 onion keyspace for a name you like. It is licensed CC0-1.0, so it is effectively public domain.

## Caveats

Longer prefixes get expensive fast, since each extra character multiplies the expected search time by about 32.

## Links

- [mkp224o on GitHub](https://github.com/cathugger/mkp224o)
