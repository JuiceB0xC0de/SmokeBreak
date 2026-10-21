---
name: lrzsz
title: lrzsz
source: brew
category: fundamentals
commitment: quick
tags: [ancient, file-transfer, protocol, quick, serial, zmodem]
homepage: https://www.ohse.de/uwe/software/lrzsz.html
scout_score: 7
status: draft
---

# lrzsz

**TLDR;** Send and receive files over a serial line or terminal session with XMODEM, YMODEM and ZMODEM, the pre-network protocols that once moved files between machines.

lrzsz is a set of command-line programs, `sz` to send and `rz` to receive among them, that implement three old file transfer protocols. They work over a plain communication link such as a serial line or a terminal session, not over a network protocol of their own. The sender reads files, the receiver writes them, and both sides handle error checking and block sizes along the way.

ZMODEM is the interesting one. According to the project page it supports crash recovery, block sizes up to 8KB, and automatic block-size tuning based on how many errors it sees. The page's own words: "Most other communication protocols of that time are already forgotten."

The package is a reworked version of the last public domain release of Omen Technologies' rzsz. The author, Uwe Ohse, took it up again after security flaws were reported. His changelog is candid about the old design: "The ability to let the receiver execute any command the sender tells him is nothing more then a really large security hole, and a hackers dreams come true." He plans to remove command execution from `lsz`.

That makes lrzsz two doors in one. One leads to how terminals moved files before networks were everywhere. The other is a case study in a maintainer hardening a protocol whose design assumed a friendly peer.

## Install

```
brew install lrzsz
# Homebrew caveats are empty. Source builds use GNU autoconf and need a C toolchain. A real transfer needs a serial line or terminal session with a peer that speaks the protocol.
```

## Try this

```
sz --help
```
Prints the sender's options, a quick look at what the protocol lets you control.

```
rz --help
```
Prints the receiver's options, the other half of a transfer.

## What's unique

Its changelog and essays document a public-domain protocol tool being hardened in the open, including a blunt account of why ZMODEM's design is a security problem.

## Caveats

The homepage is the author's own, gives no usage examples, and notes incomplete ZMODEM documentation, undocumented protocol extensions and incompatibilities between the 0.12 and 0.13 series.

## Links

- [Homepage (Uwe Ohse, lrzsz)](https://www.ohse.de/uwe/software/lrzsz.html)
