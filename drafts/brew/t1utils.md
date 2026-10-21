---
name: t1utils
title: t1utils
source: brew
category: take-things-apart
commitment: quick
tags: [file-formats, fonts, postscript, quick, reverse-engineering]
homepage: https://www.lcdf.org/type/
scout_score: 5
status: draft
---

# t1utils

**TLDR;** Six small tools that take a PostScript Type 1 font apart into editable text and put it back together, plus Mac font extraction.

t1utils is a set of command-line programs for PostScript Type 1 fonts, an old outline font format that most people only ever see as a file in a font folder. `t1disasm` turns a font into a human-readable text form, and `t1asm` assembles that text back into a working font. The README says the disassembled output is meant for "subsequent hand editing, tweaking, hint fixing, and so forth."

The other tools handle containers. `t1ascii` and `t1binary` convert between the ASCII (PFA) and binary (PFB) forms of the same font. `t1unmac` pulls a Type 1 font out of classic Macintosh packaging (MacBinary, AppleSingle, AppleDouble, BinHex, or a raw resource fork) on any Unix or Windows machine, and `t1mac` goes the other direction.

The idea underneath is that a font is a program. A Type 1 font is PostScript code describing glyph outlines and hints, and a text round-trip lets you read it, change it, and rebuild it. It is a quiet way into how digital type was built before OpenType.

The package is a revision by Eddie Kohler of I. Lee Hetherington's original t1utils, which the homepage calls "beloved".

## Install

```
brew install t1utils
```

## Try this

```
t1disasm --help
```
Shows how to turn a PFA or PFB font into editable text.

```
t1asm --help
```
Shows how to assemble that text back into a PFA or PFB font.

```
t1unmac --help
```
Shows how to extract a Type 1 font from a Macintosh font file.

## What's unique

The disassemble, edit, reassemble round-trip lets you change a font's internals by hand, which is rare for a format most people never open. t1unmac also reads classic Mac font files on non-Mac systems.

## Caveats

Type 1 is a legacy format, and t1mac output will not work on a Mac by itself because it also needs a font suitcase with bitmap fonts, which t1utils does not create.

## Links

- [LCDF Type Software homepage (t1utils section)](https://www.lcdf.org/type/)
- [t1utils on GitHub (README)](https://github.com/kohler/t1utils)
