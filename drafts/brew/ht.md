---
name: ht
title: ht (HT Editor)
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, disassembler, hex-editor, reverse-engineering, tui]
homepage: https://hte.sourceforge.net/
scout_score: 7
status: draft
---

# ht (HT Editor)

**TLDR;** A terminal hex editor and disassembler that parses executable formats like ELF, PE and Mach-O, so you can browse a binary's structure and patch it in place.

HT opens a file and shows it as raw bytes in a hex view, as text, or, for executables, as parsed structure: headers, sections, symbols, imports, relocations. It reads ELF, PE32/PE64, Mach-O, MZ, NE, LE, COFF, XBE, PEF and Java class files, disassembles the code, and writes your edits back to the file.

On top of the loader sits a code and data analyser. It follows branch sources and destinations recursively, finds procedure entries, and builds labels and cross-references. You can steer it by hand: `c` continues code analysis at the cursor, `n` names an address, `#` adds a comment. Your labels and comments are saved in a `FILENAME.htcfg` file beside the target.

The idea underneath is that a binary is a structured document, and a good viewer reads that structure for you. Search and block operations use a built-in expression evaluator with functions like `readbyte(ofs)` and `readstring(ofs, size)`. The README describes the program as "a file viewer, editor and analyzer for text, binary, and (especially) executable files." It is a small, old-school way into reverse engineering without a large framework.

## Install

```
brew install ht
# No accounts or hardware needed. Config is created on first run at ~/.htcfg2.
```

## Try this

```
ht --help
```
Lists the command-line options, including the mode switches for text, hex and auto-detect.

```
ht --bin /bin/ls
```
Opens a file in hex editor mode so you can look at the raw bytes of a real executable.

```
ht --auto /bin/ls
```
Guesses the file type, then opens the binary with its parsed format and disassembly where supported.

## What's unique

Most hex editors stop at bytes. HT pairs a format-aware loader and disassembler for many executable formats with an analyser that stores labels, xrefs and comments per file. Its search can run a boolean expression over every offset, for example to flag high-entropy regions that suggest packed or encrypted data.

## Caveats

The newest release is 2.1.0 from January 2015, some formats are unfinished (MZ is disassembly only, Flat has no disassembler), and some keys do not work in the POSIX build, where Escape stands in for Control.

## Links

- [Homepage](https://hte.sourceforge.net/)
- [GitHub repository (README)](https://github.com/sebastianbiallas/ht)
- [SourceForge project](http://sourceforge.net/projects/hte)
