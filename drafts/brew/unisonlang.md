---
name: unisonlang
title: Unison
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, content-addressed, functional, language, repl]
homepage: https://unison-lang.org/
scout_score: 5
status: draft
---

# Unison

**TLDR;** A statically-typed functional language that stores code as hashed syntax trees in a database instead of text files, so renames are instant and never break anything.

Unison is a functional language with type inference and an effect system. What sets it apart is where the code lives. You do not edit source files. You work inside the Unison Codebase Manager, `ucm`, a terminal tool where you add, update and run definitions. Each definition is stored as its syntax tree in a codebase database.

Functions are identified by a hash of their implementation, not by their name. Names are just labels attached to hashes. That is why a rename is instant and cannot break callers, and why two libraries using the same name for different things do not collide. The project's own phrasing: "Since Unison references code by hash instead of by name, an entire class of conflicts can be eliminated."

The same structure supports other things. Compilation is incremental with a shared cache that is part of the codebase format. Deterministic tests are cached and rerun only when something they depend on changes. Refactors happen in structured sessions, so the codebase stays typecheckable in the middle of one. Side effects are tracked as abilities, written like `{IO, Exception}`, and delayed computations are marked with a leading apostrophe.

The homepage also pitches distributed computation through a `Remote` ability, and says you no longer write encoders and decoders at every network boundary. According to the README, that part is used together with Unison Cloud. The language is worth a look even without it, mostly as a working answer to the question of what code would be if it were not text.

## Install

```
brew install unisonlang
# installs the `ucm` executable; building from source instead needs the Haskell Stack toolchain
```

## Try this

```
ucm --help
```
Lists the options for the Unison Codebase Manager, the terminal tool where you write and run Unison code.

## What's unique

Code is stored as hashed syntax trees in a database rather than as text, so renames are free, name collisions mostly vanish, and version control can work on structure instead of lines.

## Caveats

The brief could not confirm recent activity or a last release date, and the distributed features are tied to Unison Cloud according to the README.

## Links

- [Unison homepage](https://unison-lang.org/)
- [The big idea (content-addressed code)](https://www.unison-lang.org/learn/the-big-idea/)
- [Learn Unison](https://www.unison-lang.org/learn/)
- [GitHub repository and README](https://github.com/unisonweb/unison)
- [Unison ecosystem registry](https://share.unison-lang.org/)
