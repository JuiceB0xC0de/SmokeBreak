---
name: gnucobol
title: GnuCOBOL
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, cobol, compiler, language]
homepage: https://gnucobol.sourceforge.io/
scout_score: 6
status: draft
---

# GnuCOBOL

**TLDR;** A free COBOL compiler that turns the language behind banks and mainframes into native executables on an ordinary laptop.

GnuCOBOL compiles COBOL source into native executables. Homebrew installs three tools: `cobc`, the compiler; `cobcrun`, which runs compiled modules; and `cob-config`, which reports the compiler and library settings you need when linking. The homepage says it runs on Linux, BSD, macOS, Windows and several proprietary Unixes.

COBOL is the language still running a large share of banking, insurance and government batch processing. Most developers never see it because it lives on mainframes behind proprietary toolchains. GnuCOBOL lets you write and run it at home. The homepage frames the project around software freedom, in the FSF's terms, and offers a free/libre alternative to those toolchains.

The homepage lists support for 19 COBOL dialects, switched with `-std` flags, along with REPORT SECTION, SCREEN SECTION, FUNCTION-ID and a COBOL 2014 Compiler Directing Facility feature set. It also supports C integration, so COBOL and C can be mixed in one program. The project claims more than 9740 passed NIST COBOL 85 tests, a concrete conformance figure.

The idea underneath is a language designed in about 1959 for business records, with fixed-point decimal data and column-oriented source. Writing even a small program shows how different the assumptions behind it are from modern languages.

## Install

```
brew install gnucobol
```

## Try this

```
cobc --help
```
Lists the compiler's options, including the `-std` flags that switch between COBOL dialects.

```
cobcrun --help
```
Shows how to run compiled COBOL modules.

```
cob-config --help
```
Shows the options for querying the compiler and library settings used when linking with C.

## What's unique

It is a native-code COBOL compiler with a long dialect list and C integration, and it runs on ordinary desktops instead of mainframes.

## Caveats

The homepage gives no install commands or known limitations, and recent commit activity was not checked. The latest release it lists is 3.2, from July 2023.

## Links

- [GnuCOBOL homepage](https://gnucobol.sourceforge.io/)
