---
name: desed
title: desed
source: brew
category: take-things-apart
commitment: quick
tags: [debugger, language, quick, reverse-engineering, sed]
homepage: https://soptik.tech/articles/building-desed-the-sed-debugger.html
scout_score: 6
status: draft
---

# desed

**TLDR;** A step debugger for sed scripts that lets you watch a stream editor run one command at a time.

desed is a debugger for sed, the old stream editor that most people only ever use for `s/foo/bar/`. Sed is also a small programming language, with a pattern space, a hold space, labels and branches. Scripts written in it are famously hard to read and harder to debug.

A debugger for sed runs a script step by step and shows what the editor is holding at each point. The Homebrew description is just 'Debugger for Sed', and the scout notes say it displays the execution state as it goes. The exact interface, key bindings and input handling are not confirmed here, so run `desed --help` to see what it expects.

The homepage is an article titled 'Building desed, the sed debugger', which suggests the author wrote it to make sed scripts easier to follow. The idea underneath is worth the visit: a tiny, decades-old language with hidden state becomes much easier to understand once you can watch that state change.

## Install

```
brew install desed
```

## Try this

```
desed --help
```
Prints the available options and shows how to point the debugger at a sed script and input.

## What's unique

Debuggers for sed are rare. This one lets you watch a very old, very terse language execute instead of guessing what it does.

## Caveats

The project's own page could not be read when this entry was written, so usage details, maintenance status and release history are unverified.

## Links

- [Homepage (article: Building desed, the sed debugger)](https://soptik.tech/articles/building-desed-the-sed-debugger.html)
