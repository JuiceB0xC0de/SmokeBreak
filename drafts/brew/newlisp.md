---
name: newlisp
title: newLISP
source: brew
category: languages-and-oddities
commitment: quick
tags: [ancient, language, lisp, quick, scripting]
homepage: https://www.newlisp.org/
scout_score: 7
status: draft
---

# newLISP

**TLDR;** A small Lisp-like scripting language with its own quirks, installed as a single binary with a readline prompt and a doc generator.

newLISP is described by its Homebrew formula as a Lisp-like, general-purpose scripting language. The formula installs three executables: `newlisp`, a version-suffixed copy `newlisp-10.7.5`, and `newlispdoc`. The names suggest a documentation tool alongside the interpreter, but the brief does not say what it does.

The brief could not reach the project's homepage or README, so there are no details here on syntax, features, or what a session looks like. The scout's impression is that it is a small member of the Lisp family with an obscure character, rarely seen today. That is the scout's view, not something confirmed from the project's own pages.

The door it opens is the Lisp family itself. Lisps share the idea that code and data have the same shape, and small dialects are a cheap way to see how one language's choices differ from another's. Start at the prompt and the homepage, and judge for yourself.

## Install

```
brew install newlisp

Brew caveat: if brew uses a custom prefix, the included examples need to be pointed at your newlisp executable. Depends on readline.
```

## Try this

```
newlisp --help
```
Prints the interpreter's command-line options, a safe first look at what it accepts.

```
newlispdoc --help
```
Shows usage for the bundled doc tool.

## What's unique

It is a Lisp-like language that is rarely seen today, according to the scout, with its own quirks rather than a copy of Scheme or Common Lisp.

## Caveats

The homepage was unreachable when the brief was written, so maintenance status, syntax and features are unverified.

## Links

- [Homepage (unreachable at time of fetch)](https://www.newlisp.org/)
