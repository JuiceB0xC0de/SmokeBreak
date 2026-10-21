---
name: unicorn
title: Unicorn
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cpu, emulation, library, qemu, reverse-engineering]
homepage: https://www.unicorn-engine.org/
scout_score: 7
status: draft
---

# Unicorn

**TLDR;** A CPU emulator library: hand it machine code for ARM, MIPS, x86 and more, and run it in isolation while hooks watch every step.

Unicorn is a library, not an app. You give it machine code for a supported architecture, set up some memory and registers, and tell it to run. The code executes on an emulated CPU, with no operating system and no real process around it. The list of supported CPUs includes ARM, ARM64, M68K, MIPS, PowerPC, RISC-V, SPARC, S390X, TriCore, and x86 in 16, 32 and 64-bit modes.

The interesting part is the hooks. You can instrument execution at fine-grained levels and inspect what the code does as it runs. That makes it a handy way to take a few bytes out of a firmware image or a malware sample and see what they do, without needing the hardware or a full system. Per the homepage, it was introduced at BlackHat USA 2015 and became a foundation for security research.

Under the hood it is based on QEMU, but it is a rewritten, library-only core with an architecture-neutral API and just-in-time compilation for speed. In the project's words: "Unicorn is based on QEMU, but it goes much further with a lot more to offer." The core is written in C, with bindings for Python, Rust, Go, Ruby, Java, Lua and others.

The idea underneath is that a CPU is just a state machine you can drive from your own code. Once you can step one, watch its memory, and stop it when you like, executing unknown code becomes something you can study.

## Install

```
brew install unicorn
# This installs the library only; there are no executables. To use it you write code against it, for example via one of the language bindings. The README points to docs/COMPILE.md for building from source, and the homepage lists precompiled binaries.
```

## Try this

## What's unique

One API covers many CPU architectures, rather than one emulator per CPU. You embed it and drive execution from your own code, using hooks to watch it.

## Caveats

The homepage's latest news is from November 2022 and the README asks for contributors, so maintenance status is unclear; it is also GPLv2, which matters for closed-source use.

## Links

- [Homepage](https://www.unicorn-engine.org/)
- [GitHub repository and README](https://github.com/unicorn-engine/unicorn)
