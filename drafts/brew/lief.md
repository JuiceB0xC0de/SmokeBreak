---
name: lief
title: LIEF
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, elf, library, mach-o, pe, python, reverse-engineering]
homepage: https://lief.re/
scout_score: 7
status: draft
---

# LIEF

**TLDR;** A library that parses, edits and rewrites ELF, PE and Mach-O executables through one API in C++, Python or Rust.

LIEF reads an executable file, or an in-memory buffer, and turns it into an object model: sections, symbols, relocations, an entry point. For ELF, PE and Mach-O it also offers a shared abstraction, so the same ideas carry across formats. You can change the model, for example by adding a section or renaming a symbol, and write a valid binary back to disk.

The homepage pitches this as a way to move "from raw executable file formats to a high-level representation, make precise changes, then write a valid binary back to disk", without booting a heavyweight reverse-engineering stack. Many tools focus on analysis. LIEF is built for rewriting.

The idea underneath is that an executable is just a structured file, and once you can see the structure you can edit it. Headers, section tables and symbol tables stop being mysterious. The project also ships lief-patchelf, a reimplementation of NixOS patchelf, plus Ghidra and Binary Ninja plugins.

A separate tier, LIEF Extended, adds disassembly, assembly, DWARF and PDB debug info, and Objective-C metadata. Its demo disassembles an instruction, reassembles it as same-size NOPs and rebuilds the ELF.

## Install

```
brew install lief
# the Homebrew formula installs the library and has no executables; for Python use: pip install lief
```

## Try this

```
brew install lief
```
Installs the LIEF library through Homebrew. It provides no command-line tools, so you use it from code.

```
pip install lief
```
Installs the Python package from PyPI, the quickest way to load a binary and look at its sections and symbols.

```
pip install [--user] --force-reinstall --index-url https://lief.s3-website.fr-par.scw.cloud/latest lief==2.0.0.dev0
```
Installs a nightly Python build from the project's own index instead of PyPI.

## What's unique

One API covers ELF, PE and Mach-O, and it is aimed at modifying and rebuilding binaries rather than only analysing them.

## Caveats

The Homebrew formula installs no executables, so it is a library you write code against; disassembly and assembly live in LIEF Extended, which is distributed separately and requires GitHub OAuth sign-in.

## Links

- [Homepage](https://lief.re/)
- [Documentation (Sphinx)](https://lief.re/doc/latest/index.html)
- [GitHub repository](https://github.com/lief-project/LIEF)
- [LIEF Extended](https://extended.lief.re)
