---
name: ecoji
title: Ecoji
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [cli, emoji, encoding, quick, unicode]
homepage: https://ecoji.io
scout_score: 6
status: draft
---

# Ecoji

**TLDR;** Ecoji turns any data into a string of emoji and back again, from the command line or a small web page.

Ecoji encodes data as emoji and decodes it back. The command line tool is a single executable named `ecoji`. The homepage at ecoji.io offers the same transform in the browser, with one panel labelled "Encode using Ecoji" and another labelled "Decode using Ecoji", plus a "Copy Link" button for sharing a result.

The page opens with a sample of eight emoji, which is the encoded form of some input. The emoji are the output itself, not decoration. That makes it a quick way to see what an encoding does: bytes go in, a visible alphabet comes out, and the same tool reverses it.

The brief found no stated motivation from the author, and the homepage shows nothing about how the scheme works. The idea underneath is the same one behind base64 and hex: any data can be written in some chosen alphabet, and the choice of alphabet is a design decision. Here the alphabet is emoji. Reading the source or any specification is the way to learn the details, but the brief did not reach either.

## Install

```
brew install ecoji
```

## Try this

```
ecoji --help
```
Prints the tool's usage and options, which is the safest way to see how to encode and decode from the terminal.

## What's unique

Most encodings use letters and digits. This one uses emoji as its alphabet, and its own homepage leads with a sample of its output.

## Caveats

The homepage was thin, with no README, docs or repository link, and nothing shows whether the project is maintained.

## Links

- [Homepage (web encoder/decoder)](https://ecoji.io)
