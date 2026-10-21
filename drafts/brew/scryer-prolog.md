---
name: scryer-prolog
title: Scryer Prolog
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, constraints, language, logic-programming, prolog, rust]
homepage: https://www.scryer.pl
scout_score: 8
status: draft
---

# Scryer Prolog

**TLDR;** A modern ISO Prolog written in Rust, with constraint solving, tabling and an HTTP server, for trying logic programming where you state facts and ask questions.

Scryer Prolog is a Prolog system. You write facts and rules in a file, or type queries at an interactive toplevel, and the engine searches for bindings that make your query true. It loads files with `consult`, prints answers such as `X = "Scryer Prolog!"`, and ships with a large library set: constraint solving over booleans and integers (clp(B), clp(Z)), definite clause grammars, tabling, TCP sockets, an HTTP client and server, and cryptography.

The project states its aim plainly: to become "to ISO Prolog what GHC is to Haskell: an open source industrial strength production environment that is also a testbed for bleeding edge research in logic and constraint programming, which is itself written in a high-level language." It claims to pass the ISO syntax conformity tests, which makes it useful for checking whether existing Prolog code is portable.

Under the hood it is an implementation of the Warren Abstract Machine, built in phases following Warren's tutorial. Its best-known trick is a packed UTF-8 representation of strings, which the README says cuts memory use by up to 24-fold compared with one WAM cell per character. Tabling is built on delimited continuations (`reset/3`, `shift/1`) rather than as a separate engine mode.

The larger idea is programming by describing relations instead of writing steps. The same predicate can often answer in several directions, and constraints let you narrow a search space declaratively. The README also calls it well suited to teaching and learning Prolog.

## Install

```
brew install scryer-prolog
# No account or hardware needed. Precompiled binaries are also on the GitHub releases page, and a Docker image exists: docker run -it mjt128/scryer-prolog
```

## Try this

```
scryer-prolog
```
Starts the interactive toplevel, where you type queries ending in a period.

```
?- "abc" = [a,b,c].
```
Inside the toplevel, shows that double-quoted text is a list of characters by default.

```
?- use_module(library(lists)).
```
Loads the bundled lists library so you can use its predicates. Type `halt.` to quit.

## What's unique

Its packed string representation makes character lists cheap, and the README says it is the first Prolog system to implement it. It also aims at strict ISO conformance while bundling modern libraries such as CLP(Z), tabling and TLS.

## Caveats

Only Linux, macOS and Windows are regularly tested, and several features such as JIT indexing and a compacting garbage collector are still in progress.

## Links

- [Homepage](https://www.scryer.pl)
- [GitHub repository and README](https://github.com/mthom/scryer-prolog)
- [Latest binary releases](https://github.com/mthom/scryer-prolog/releases/latest)
