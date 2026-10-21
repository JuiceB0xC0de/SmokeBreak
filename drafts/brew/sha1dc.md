---
name: sha1dc
title: sha1dc
source: brew
category: take-things-apart
commitment: quick
tags: [cryptography, hashing, math, quick, reverse-engineering]
homepage: https://github.com/cr-marcstevens/sha1collisiondetection
scout_score: 6
status: draft
---

# sha1dc

**TLDR;** A sha1sum lookalike that also notices when a file was crafted to collide, like the SHAttered PDFs, by spotting the fingerprints of the attack.

sha1dcsum computes the SHA-1 of a file or stdin, like sha1sum, and also checks whether the input carries signs of a cryptanalytic collision attack. If it finds one, it prints a warning along with the hash. The package ships two programs: `sha1dcsum` for SHAttered-style and sha-mbles attacks, and `sha1dcsum_partialcoll` for attacks on reduced-round SHA-1.

The idea underneath is counter-cryptanalysis, from the author's CRYPTO 2013 paper. A collision attack has to push the hash's internal state along a particular path, called a disturbance vector. The detector does not need to know the colliding partner. It looks at a single file and asks whether the hash computation passes through the tell-tale states such an attack leaves behind. The README claims it catches any attack using the top 32 disturbance vectors with probability 1, with false positives below 2^-90.

There is also a library with a safe-hash mode. An ordinary file gets its real SHA-1. A detected collision gets a different, unpredictable hash, so two files that collide under plain SHA-1 no longer match. In the README's words: "Colliding files will have the same SHA-1 hash, but will have different unpredictable safe-hashes." The aim is to let applications that already use SHA-1 defend against forged signatures without rewriting much code.

The repository includes the SHAttered PDF as a test file, so you can run the detector against a real broken-hash example.

## Install

```
brew install sha1dc
```

## Try this

```
sha1dcsum --help
```
Shows the usage text for the main detector.

```
sha1dcsum test/shattered-1.pdf
```
Hashes the SHAttered PDF and warns about a collision attack. You need a copy of the file, such as the one in the project's test directory.

```
pipe_data | sha1dcsum -
```
Reads from stdin when the file argument is '-'. Replace pipe_data with anything that produces data.

## What's unique

Rather than only flagging collisions, its safe-hash mode makes colliding files hash differently, so an application already using SHA-1 gets protection with few code changes.

## Caveats

It only catches attacks using the known disturbance vectors or the reduced-round cases, and the README says the partial-collision tool covers 'a few examples so far'. The README's copyright line says 2017, and the speed claim is the author's own.

## Links

- [GitHub repository (homepage)](https://github.com/cr-marcstevens/sha1collisiondetection)
- [shattered.io, the SHAttered attack](https://shattered.io/)
- [Counter-cryptanalysis paper (CRYPTO 2013, PDF)](https://marc-stevens.nl/research/papers/C13-S.pdf)
