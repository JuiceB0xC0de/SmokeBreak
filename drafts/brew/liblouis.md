---
name: liblouis
title: liblouis
source: brew
category: fundamentals
commitment: afternoon
tags: [accessibility, afternoon, braille, library, tables, text]
homepage: https://liblouis.io
scout_score: 7
status: draft
---

# liblouis

**TLDR;** A table-driven braille translator that turns text into braille and back again, the engine inside screen readers like NVDA and Orca.

Liblouis is a C library that converts text to braille and braille back to text. It handles computer braille and literary braille, contracted and uncontracted, for many languages, plus hyphenation and math codes (Nemeth and Marburg). It is named in honor of Louis Braille.

The rules are not hard-coded. They live in table files, such as `en-us-g2.ctb` and `en-us-g1.ctb`, and one engine reads whichever table you point it at. New languages and braille codes are added by writing tables that use a rule-based or dictionary-based approach. Back-translation runs on the same tables in reverse.

The project grew out of the translation routines in the BRLTTY screen reader and, in the README's words, has 'gone far beyond these routines'. It is used by NVDA and Orca and in commercial products such as ViewPlus. Because it is plain C with no runtime, it can be called from Python, Java and JavaScript bindings.

The command-line tools are the part to play with. `lou_translate` converts text, while `lou_trace`, `lou_debug`, `lou_checktable` and `lou_checkhyphens` exist for testing and debugging tables. Braille contractions are a lot like a compression scheme with context-dependent rules, and the tools let you watch those rules fire.

## Install

```
brew install liblouis
# Homebrew pulls in python@3.15. The upstream README describes a source build instead: ./configure, make, sudo make install, then sudo ldconfig if needed.
```

## Try this

```
lou_translate --help
```
Shows how to pick a translation table and translate text to braille or back.

```
lou_tableinfo --help
```
Shows how to inspect what a braille table file declares.

```
lou_trace --help
```
Shows how to trace which table rules fire during a translation.

## What's unique

Braille rules are data in table files, so one engine covers many languages and codes. It also ships back-translation and table-debugging tools, which is less common than forward translation alone.

## Caveats

The brief did not cover the tools' usage, so check the liblouis.io documentation for table names and options; the library is LGPL but the command-line tools are GPLv3+.

## Links

- [Homepage](https://liblouis.io)
- [Documentation](http://www.liblouis.io/documentation/liblouis.html)
- [GitHub repository](https://github.com/liblouis/liblouis)
- [Releases](https://github.com/liblouis/liblouis/releases)
