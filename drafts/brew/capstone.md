---
name: capstone
title: Capstone
source: brew
category: take-things-apart
commitment: quick
tags: [c, disassembly, library, quick, reverse-engineering]
homepage: https://www.capstone-engine.org/
scout_score: 5
status: draft
---

# Capstone

**TLDR;** A disassembly engine that turns raw machine-code bytes into readable instructions for dozens of CPU architectures, with a small shell tool, cstool, for trying it.

Capstone takes bytes, an architecture and a mode, and gives back decoded instructions. Each one comes with operand details and some semantics, such as the implicit registers it reads and writes. It is written in pure C and is mostly used as a library through many language bindings. Debuggers, emulators and analysis tools often build on it.

The homepage states the goal plainly: "to make Capstone the ultimate disassembly engine for binary analysis and reversing in the security community." It was created by Nguyen Anh Quynh and is now maintained by a small community.

The idea underneath is an architecture-neutral API. The same calls work whether the bytes are AArch64, x86 or something obscure. The homepage lists niche instruction sets such as M680X, TriCore, XCore and TMS320C64X. It also mentions thread-safety by design and support for embedding in firmware or OS kernels.

The command-line door is cstool. Give it an architecture and a hex string and it prints the instruction. That is a quick way to see how the same four bytes read under different modes, and a first step toward reading binaries.

## Install

```
brew install capstone
```

## Try this

```
cstool aarch64 0xe402a012
```
Disassembles one AArch64 instruction; the homepage shows it as mov w4, #-0x170001.

```
cstool aarch64+explicitwideimm 0xe402a012
```
Decodes the same bytes with the explicit-wide-immediate option, giving movn w4, #0x17, lsl #16.

```
cstool --help
```
Lists the supported architectures and mode options.

## What's unique

It exposes per-instruction detail, like implicit register reads and writes, through one architecture-neutral API, and it can be embedded in firmware and kernels. Its architecture list is long and includes older, niche instruction sets.

## Caveats

The current 6.0 line is still alpha with some API churn such as enum renames, and cstool is a thin wrapper around what is mainly a library.

## Links

- [Capstone homepage](https://www.capstone-engine.org/)
- [GitHub repository](https://github.com/capstone-engine/capstone)
- [6.0.0-Alpha10 release notes](https://github.com/capstone-engine/capstone/releases/tag/6.0.0-Alpha10)
