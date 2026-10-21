---
name: binwalk
title: binwalk
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binary-analysis, entropy, firmware, reverse-engineering]
homepage: https://github.com/ReFirmLabs/binwalk
scout_score: 8
status: draft
---

# binwalk

**TLDR;** Scans a binary blob such as a firmware image and lists the files, filesystems and compressed data hidden inside it.

Binwalk reads a binary file and looks for signatures, the telltale byte patterns that mark where a known file type begins. Point it at a firmware image and it prints a list of what it found and at what offset. It can also extract those pieces if asked. You do not need to know the layout of the image beforehand.

The README describes this version as an updated Binwalk "re-written in Rust for speed and accuracy." Its main focus is firmware analysis, though it supports a wide range of file and data types. The wiki has a page listing the supported signatures.

The idea underneath is that a firmware file is not one thing. It is often a bootloader, a kernel, a compressed filesystem and assorted data concatenated together, and nothing labels the joins. Binwalk shows where they are. That is a first step into reverse engineering and file format poking.

It also does entropy analysis. Compressed and encrypted data look like random noise, so a region with very high entropy is a clue. The README says that through this it "can even help to identify unknown compression or encryption." It can be embedded in other Rust projects as a library too.

## Install

```
brew install binwalk
# The README's preferred routes are a Docker image, Cargo, or building from source. It does not mention Homebrew, so the brew build may differ from the Rust v3 it describes. No hardware or accounts needed.
```

## Try this

```
binwalk --help
```
Lists the advanced options, including extraction and entropy analysis.

```
binwalk DIR-890L_AxFW110b07.bin
```
Scans the D-Link DIR-890L firmware image from the README and prints what is embedded inside it, with offsets. You need to download that image or substitute your own.

## What's unique

It pairs signature-based carving with entropy analysis, so it can flag regions that look compressed or encrypted even when no signature matches. It is also usable as a Rust library.

## Caveats

The brief could not confirm release dates or maintenance status, and the Homebrew build may not match the Rust v3 the README describes.

## Links

- [Homepage / repository](https://github.com/ReFirmLabs/binwalk)
- [Wiki: Usage](https://github.com/ReFirmLabs/binwalk/wiki#usage)
- [Wiki: Supported Signatures](https://github.com/ReFirmLabs/binwalk/wiki/Supported-Signatures)
