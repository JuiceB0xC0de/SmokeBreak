---
name: arturo
title: Arturo
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, language, nim, rebol-like, scripting]
homepage: https://arturo-lang.io/
scout_score: 6
status: draft
---

# Arturo

**TLDR;** A small scripting language with no reserved words, where code is just a list of words and symbols read by context, descended from Rebol, Forth and Lisp.

Arturo is an independently developed scripting language written in Nim. Scripts are plain text files, run with the `arturo` executable on a bytecode VM that the homepage says has no warm-up or compilation step. The homepage also lists a built-in web server, UI toolkit, databases, cryptography, HTTP clients and templating, and says scripts can be bundled into standalone executables.

The README says it is 'vaguely related to various other ones', naming Logo, Rebol, Forth, Ruby, Haskell, D, Smalltalk, Tcl and Lisp. The author named it after a pet Emperor Scorpion, a quiet and docile creature, as a hint at what the language aims to be.

The idea underneath is the one worth poking at. The README puts it this way: 'Code is just a list of words, symbols and literal values.' Words and symbols in a block are interpreted according to context, and there are no keywords at all. The README's challenge is to 'look for them as hard as you can; there are absolutely none'. That Rebol-style block model is what lets you redefine operators and build small domain-specific languages inside the language itself.

It is a good door into how a language can be built from very few parts, and into what a language looks like when its syntax is mostly data.

## Install

```
brew install arturo
# The README warns the Homebrew version may lag behind; pre-built binaries or the installer are the safer route:
# curl -sSL https://get.arturo-lang.io | sh
```

## Try this

```
arturo --help
```
Lists the options the executable accepts, a first look at how scripts are run.

```
docker run -it arturolang/arturo
```
Starts the official Docker image for a quick taste without installing anything. The README says it is not meant for everyday use.

```
curl -sSL https://get.arturo-lang.io/latest | sh
```
Installs the nightly build instead of the stable release.

## What's unique

Most scripting languages reserve keywords. Arturo has none, so code is a list of words interpreted by context, and you can redefine operators and build your own DSLs. It also ships a wide standard library and its own bundling.

## Caveats

The language is young and maintained by a small group in their spare time, and the Homebrew formula may lag the latest release.

## Links

- [Homepage](https://arturo-lang.io/)
- [Documentation](https://arturo-lang.io/documentation/)
- [Examples](https://arturo-lang.io/documentation/examples/)
- [GitHub repository](https://github.com/arturo-lang/arturo)
