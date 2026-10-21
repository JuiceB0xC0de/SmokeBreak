---
name: magic-wormhole.rs
title: magic-wormhole.rs
source: brew
category: fundamentals
commitment: quick
tags: [file-transfer, network, pake, protocol, quick, rust]
homepage: https://github.com/magic-wormhole/magic-wormhole.rs
scout_score: 5
status: draft
---

# magic-wormhole.rs

**TLDR;** Send a file between two computers by reading a short code aloud; the Rust take on Magic Wormhole, with direct connections through NATs and firewalls.

magic-wormhole.rs is a Rust port of the Python Magic Wormhole client. It installs one command, `wormhole-rs`, and also ships as a Rust library. The sender points it at a file or folder, and it prints a wormhole code. The receiver types that code on their own machine, and the file arrives. No accounts, no setup, no server address to share.

The idea underneath is that the code is the whole shared secret. The README says the two endpoints are identified by identical "wormhole codes", and that is all the pair needs to find each other. The README does not explain the cryptography. It points to a separate protocol specification (magic-wormhole-protocols) for the details, and that spec is the real rabbit hole: how two strangers can agree on a secure channel from a short, human-speakable code.

This port adds things the README says other implementations lack: direct connections across NATs and firewalls, automatic copying of the code to the clipboard, fuzzy code completion, and experimental `send-many` (one file, several recipients) and `forward` (port forwarding) subcommands. The library is meant for embedding, and the README lists GUI clients such as Warp and a Flutter Android client as users.

The tool is a way to see a protocol in motion. Send something between two machines, then read the spec to see what just happened.

## Install

```
brew install magic-wormhole.rs
# alternatives: cargo binstall magic-wormhole-cli, or cargo install --locked magic-wormhole-cli
```

## Try this

```
wormhole-rs --help
```
Lists the subcommands: send (alias tx), receive (alias rx), send-many, and forward.

```
wormhole-rs send <PATH>
```
Prints a wormhole code for the file or folder at PATH and waits for the receiver. The CLI README writes this as `wormhole send`, but the installed binary is `wormhole-rs`.

```
wormhole-rs receive <CODE>
```
On the other machine, takes the code shown by the sender and receives the file.

## What's unique

It is one of several Magic Wormhole implementations, but the README claims direct connections through NATs and firewalls, clipboard copy of the code, fuzzy code completion, and a library built for embedding in other apps.

## Caveats

Per the README, folders are sent as a tarball you unpack by hand, Tor is unsupported, and send-many and forward are experimental; I could not confirm a recent release date.

## Links

- [Project homepage (Magic Wormhole)](http://magic-wormhole.io/)
- [magic-wormhole.rs on GitHub](https://github.com/magic-wormhole/magic-wormhole.rs)
- [CLI README (usage and install)](https://github.com/magic-wormhole/magic-wormhole.rs/blob/main/cli/README.md)
- [Protocol specification](https://github.com/magic-wormhole/magic-wormhole-protocols)
- [Original Python implementation](https://github.com/magic-wormhole/magic-wormhole)
