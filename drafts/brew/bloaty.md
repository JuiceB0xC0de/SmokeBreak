---
name: bloaty
title: Bloaty
source: brew
category: take-things-apart
commitment: quick
tags: [binaries, dwarf, elf, quick, reverse-engineering, size-profiling]
homepage: https://github.com/google/bloaty
scout_score: 6
status: draft
---

# Bloaty

**TLDR;** Bloaty breaks a compiled binary down by section, symbol, or source file, showing where every byte went and what grew between builds.

Bloaty is a command-line size profiler. You give it a compiled file (ELF, Mach-O, and experimentally PE/COFF or WebAssembly, plus object files and static libraries) and it prints a table of how many bytes each piece takes on disk (FILE SIZE) and in memory (VM SIZE). You choose the breakdown: sections, segments, symbols, compile units, inlines, or input files.

The README opens with a question: "Ever wondered what's making your binary big?" It aims to attribute every byte of the binary to the symbol or compile unit that produced it. To do that it uses its own ELF, DWARF, and Mach-O parsers instead of calling external tools. It maps each byte to a section, segment, symbol, or debug-info entry, and it can disassemble the binary to find references to anonymous data.

The idea underneath is that a binary is a map you can read. Breakdowns can be stacked, so you can see segments, then sections within them, then symbols within those. A diff mode compares two binaries and shows which parts grew or shrank, which is how it gets pitched for CI. Custom data sources are regex rewrites of the built-in breakdowns, so you can bucket results by library or package.

Debug-based views such as compileunits and symbols need debug info. That info can live in a separate file matched by build ID, which lets you profile a stripped binary.

## Install

```
brew install bloaty
```

## Try this

```
bloaty --help
```
Prints the full option list, including --demangle, -n, -s, --domain, and --source-filter.

```
bloaty -d segments,sections <binary>
```
Prints a hierarchical profile, with sections nested under segments, for the binary you name.

```
bloaty <new-binary> -- <old-binary>
```
Shows a size diff: the file after -- is the base, and the table shows what grew or shrank.

## What's unique

It attributes bytes to source compile units and inlined source lines, not just symbols, using its own parsers. Its diff mode and regex-based custom data sources suit tracking size in CI.

## Caveats

PE/COFF, WebAssembly, and --disassemble are marked experimental, separate debug files need build IDs (Clang needs -Wl,--build-id), and the README says it is not an official Google product.

## Links

- [GitHub repository and README](https://github.com/google/bloaty)
- [User Documentation (doc/using.md)](https://github.com/google/bloaty/blob/main/doc/using.md)
- [How Bloaty Works (doc/how-bloaty-works.md)](https://github.com/google/bloaty/blob/main/doc/how-bloaty-works.md)
