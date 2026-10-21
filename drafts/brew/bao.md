---
name: bao
title: bao
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, blake3, cryptography, hashing, protocol, rust, streaming]
homepage: https://github.com/oconnor663/bao
scout_score: 6
status: draft
---

# bao

**TLDR;** Encodes a file with its BLAKE3 hash tree so a reader can verify every byte as it streams in, or check just one slice.

Bao is a Rust implementation of BLAKE3 verified streaming, as described in Section 6.4 of the BLAKE3 spec. A normal hash is serial: you have to read the whole file before you know whether it matches. BLAKE3 is a tree hash, so the pieces can be checked one at a time against a single root hash. Bao stores the file's bytes together with the nodes of that tree, and a decoder checks each piece as it reads.

The motivating case in the README is a secure messaging app that sends attachments with a hash in the message metadata. With a serial hash, the recipient must download an entire large video before verifying it. With Bao, they can stream and verify as they go. The author says this scenario was the original motivation for the project.

The `bao` tool can encode, hash, decode, slice, and decode-slice. A slice is an encoded byte range that can be decoded with the same root hash and no seeking on the receiving end. The sender does the seeking over the full encoding. Combined mode interleaves content and tree nodes. Outboard mode writes only the tree nodes to a separate file. If the hash or the data is wrong, decoding fails with a 'hash mismatch' error.

The repo also includes tests/bao.py, a second implementation in Python that the README says is designed to be as short and readable as possible. It is a good way into the algorithm before you read the Rust.

## Install

```
brew install bao
# Building from source instead needs a Rust toolchain: cargo install bao_bin (with ~/.cargo/bin on your PATH)
```

## Try this

```
head -c 1000000 /dev/urandom > f && bao encode f f.bao && hash=`bao hash f` && bao decode $hash < f.bao > f2 && cmp f f2
```
Makes a 1 MB random file, encodes it with its hash tree (about 6% larger), then decodes it with verification and checks the round trip.

```
bao slice 500000 100000 f.slice < f.bao
```
Extracts a 100 KB slice starting at byte 500000 from the encoded file, ready to be decoded with the same root hash.

```
bao encode f --outboard f.obao
```
Writes only the hash tree nodes (about 62 KB for the 1 MB file) to a separate outboard file, leaving the original untouched.

## What's unique

The root hash is just the plain BLAKE3 hash of the file, yet a recipient can verify any byte range without downloading everything. The readable Python second implementation makes the algorithm approachable.

## Caveats

The README warns: 'Bao is beta cryptography software. It has not been formally audited yet.'

## Links

- [Homepage (GitHub repo)](https://github.com/oconnor663/bao)
- [Bao spec](https://github.com/oconnor663/bao/blob/master/docs/spec.md)
- [Rust crate bao_bin on crates.io](https://crates.io/crates/bao_bin)
- [Rust docs for bao](https://docs.rs/bao)
