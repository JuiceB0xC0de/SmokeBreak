---
name: ares
title: ares
source: brew
category: take-things-apart
commitment: quick
tags: [ciphers, crypto, ctf, encodings, puzzles, quick, rust]
homepage: https://github.com/bee-san/Ares
scout_score: 6
status: draft
---

# ares

**TLDR;** Paste in encoded or encrypted text and it searches chains of decoders, with no key or hint, until plaintext falls out.

Ares takes a blob of text and works out how to undo it. It tries combinations of encodings and classical ciphers, such as Base64, hex, Caesar/ROT13, Vigenere and Morse, several layers deep. The output is the candidate plaintext, the path it took (for example Base64 → Hexadecimal → caesar), and any key it found. It runs under a time limit, five seconds by default, so it gives up instead of running forever.

The project is the Rust successor to a Python tool called Ciphey, and the README says the old one "could run forever" with no sign it had failed. The rewrite is about speed and a clear stopping point. Names are tangled: Ares was the earlier name, and the current README describes the binary as `ciphey`. After installing, check which executable you actually got.

Underneath is a search problem. An A* search tries chains of decoders, runs cheap ones like Base64 first, and orders the rest with a heuristic from the cipher_identifier crate. The hard part is knowing when to stop, so each candidate is checked by an English checker (trigrams and a dictionary), LemmeKnow (a Rust port of pyWhat that recognises 120+ formats), and a common-password check. It can also say what the plaintext is, such as an IP address or a TOTP URI, rather than just printing it.

That makes it a small door into classical crypto, encodings, and CTF-style puzzles. You can watch which layers it peels and think about why some chains are easy to detect and others are not.

## Install

```
brew install ares
# The README's own route is `cargo install ciphey` (needs a Rust toolchain); prebuilt binaries for Linux, macOS and Windows are on the GitHub releases page.
# First run asks a few setup questions (colour theme, result display, wordlist) and writes ~/.ciphey/config.toml.
```

## Try this

```
ciphey -t 'aGVsbG8gdGhlcmUgZ2VuZXJhbA=='
```
Decodes a Base64 string, asks you to confirm with y/N, and reports 'hello there general'.

```
ciphey -c 15 -t 'NTA3NjYzNzU3MjZjMjA3NjY2MjA2OTcyNjU2YzIwNzM2ZTY2Njc='
```
Unwinds a three-layer chain (ROT13 → hex → Base64) with the timeout raised from 5 to 15 seconds.

```
ciphey -r 'flag\{' -t '...'
```
Crib mode: only accepts plaintext matching the regex, handy for CTF flag formats.

## What's unique

Most decoders make you name the cipher or brute-force one at a time. This one searches chains of decoders with no hint and tells you what kind of thing the plaintext is.

## Caveats

The brew formula is named ares but the README documents a ciphey binary, plaintext detection misses short phrases, non-English text and odd flag formats, and no release dates were visible.

## Links

- [Homepage (bee-san/Ares)](https://github.com/bee-san/Ares)
- [Current repository (bee-san/Ciphey)](https://github.com/bee-san/Ciphey)
- [API docs on docs.rs](https://docs.rs/ciphey)
- [Blog post: Introducing Ares](https://skerritt.blog/introducing-ares/)
