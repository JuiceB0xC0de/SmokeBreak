---
name: patchelf
title: patchelf
source: brew
category: take-things-apart
commitment: quick
tags: [elf, linking, linux, quick, reverse-engineering]
homepage: https://github.com/NixOS/patchelf
scout_score: 5
status: draft
---

# patchelf

**TLDR;** Edits a compiled Linux binary's loader path, library search paths and dependency list in place, without recompiling, and shows how dynamic linking works.

PatchELF rewrites header metadata in existing dynamic ELF executables and shared libraries. You hand it a binary and a flag, and it changes the dynamic loader (the ELF interpreter), the RPATH search directories, the DT_NEEDED list of required libraries, or a library's SONAME. Nothing is recompiled.

The README gives no formal problem statement. The operations it lists are the fixes you reach for when a prebuilt binary cannot find its libraries or its loader. In the README's words, "PatchELF is a simple utility for modifying existing ELF executables and libraries." It lives under the NixOS organisation on GitHub.

The idea underneath is that a Linux program does not carry its libraries with it. It carries a list of names and a set of places to look, and a loader resolves them at startup. Once you can edit that list, you can see how it works: add a dependency, swap one for another, point the binary at a different loader, then watch what breaks.

`--shrink-rpath` is a good concrete case. It removes every RPATH directory that contains no library the binary actually needs, so a stray build-tree path disappears. A newer option, `--build-resolution-cache`, pre-resolves each dependency and records the result in a `.note.nixos.ldcache` note, for loaders that understand it.

## Install

```
brew install patchelf
```

## Try this

```
patchelf --help
```
Lists every operation the tool supports on ELF files.

```
patchelf --shrink-rpath my-program
```
Removes RPATH directories that contain no library the binary lists in DT_NEEDED.

```
patchelf --replace-needed liboriginal.so.1 libreplacement.so.1 my-program
```
Swaps one declared library dependency for another in the binary.

## What's unique

It is a small, focused tool that changes a binary's linking metadata after the build, so you can experiment with the loader and library search without a rebuild.

## Caveats

The README implies ELF systems such as Linux only, gives no safety checks, and a wrong interpreter or RPATH can leave a binary unable to start.

## Links

- [Homepage / source (GitHub)](https://github.com/NixOS/patchelf)
- [Matrix chat #patchelf:nixos.org](https://matrix.to/#/#patchelf:nixos.org)
