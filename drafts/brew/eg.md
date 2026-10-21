---
name: eg
title: eg (Expert Guide)
source: brew
category: languages-and-oddities
commitment: quick
tags: [ancient, dos, help-files, hypertext, quick, tui]
homepage: https://github.com/davep/eg
scout_score: 6
status: draft
---

# eg (Expert Guide)

**TLDR;** A terminal reader for Norton Guide, the compiled hypertext help format from 1990s DOS programming tools, so old help files can be read on Linux.

Norton Guide was a hypertext help format from the DOS era. Programmers kept these compiled databases open while writing code, and they carried reference material for languages, libraries and tools. eg opens one of these files and lets you browse it in a text-mode interface drawn with the S-Lang library.

The author's site describes the wider project as keeping access to the information in these files alive, since many of them date from the 1990s. The README says anyone who has used Norton Guide or Expert Help should find eg familiar. It does not describe the interface in detail.

eg has a long lineage. According to the author's page, it began as an OS/2 text-mode Norton Guide reader, was rewritten for GNU/Linux, and was later reworked for macOS. The same author maintains related tools: a Python library (ngdb.py), an HTML converter (ng2web), an Emacs package (eg.el) and another terminal reader called AgiNG. Together they make a way into a small, nearly forgotten corner of software documentation history.

You need a Norton Guide file to read. The brief does not say where to find them, but the author's Norton Guides page is the place to start.

## Install

```
brew install eg
# Building from source instead: install S-Lang first, check the settings at the top of the Makefile, then run make and make install.
# You also need a Norton Guide file to open.
```

## Try this

```
eg --help
```
Prints the usage summary for the reader.

```
make
```
Builds eg from source, if you are not using Homebrew. S-Lang must be installed first.

```
make install
```
Installs the built eg. Check the Makefile settings first.

## What's unique

It is a working reader for a 1990s help format, descended from an OS/2 tool, with a family of sibling tools for converting and reading the same files.

## Caveats

Documentation is, in the README's words, "a little thin on the ground at the moment", and the brief could not confirm a recent release date.

## Links

- [Homepage (GitHub README)](https://github.com/davep/eg)
- [Author's Norton Guide readers page (latest version)](http://www.davep.org/norton-guides/)
- [S-Lang library (build dependency)](http://www.jedsoft.org/slang/)
