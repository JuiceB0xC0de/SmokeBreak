---
name: le
title: le
source: brew
category: languages-and-oddities
commitment: quick
tags: [editor, hex, old-school, quick, tui]
homepage: https://github.com/lavv17/le
scout_score: 5
status: draft
---

# le

**TLDR;** A small console text editor with rectangular block selection, a hex mode, and binary-clean editing, modelled loosely on Norton Editor for DOS.

LE is a terminal text editor that treats blocks as a central idea. You can select a stream of text or a rectangular column, then copy, move, or delete it. It reads and writes both Unix (LF) and DOS (CRLF) line endings, and it is binary clean, so it will open files that are not really text without mangling them. A hex mode is built in.

The README describes it as "slightly similar to Norton Editor for DOS, but has more features." That is the only stated motivation. The lineage is the interesting part: it comes from the era of menu-driven, CUA-style console editors, before modal editors and IDEs set the terms for what an editor should feel like.

It also has a shared mode for editing files and mmap-able devices in place, where only replacement is allowed, so the size of the data never changes. Syntax highlighting, colour scheme, key map, and menu are all configurable. It supports multibyte encodings and full undo/redo.

## Install

```
brew install le
```

## Try this

```
le --help
```
Prints the command-line options so you can see what the editor accepts.

## What's unique

Rectangular and stream block operations, a hex mode, and mmap shared-mode device editing are rare to find together in one small console editor. Its Norton Editor roots give it a menu-driven feel unlike vi or emacs.

## Caveats

The README gives no release dates or changelog, so maintenance status is unclear, and it documents only source builds.

## Links

- [GitHub repository (homepage)](https://github.com/lavv17/le)
