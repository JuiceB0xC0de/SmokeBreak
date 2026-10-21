---
name: icon
title: Icon
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, backtracking, language, snobol]
homepage: https://www2.cs.arizona.edu/icon/
scout_score: 7
status: draft
---

# Icon

**TLDR;** A 1979 successor to SNOBOL4 where expressions can yield multiple results and the runtime backtracks until something succeeds.

Icon is a high-level, general-purpose programming language from the University of Arizona. Its homepage names two novel features: string scanning and goal-directed evaluation. It was first released in 1979 as a successor to SNOBOL4 and kept evolving for about two decades.

The idea underneath is goal-directed evaluation. In most languages an expression produces one value. In Icon an expression can produce several results, and the runtime backtracks to find one that makes the surrounding expression succeed. Success and failure, rather than booleans, drive control flow. The scout's notes describe this in terms of generators and backtracking, though the homepage itself does not spell out the mechanism.

String scanning is the second feature, a built-in way of walking through and picking apart text. The brief does not go into how it works, so the language reference is the place to learn it.

Development is frozen, so Icon will not change under you. In the homepage's words, "the Unix implementation is still in active use and is maintained as necessary." The Homebrew formula installs three executables: icon, icont and iconx.

## Install

```
brew install icon
```

## Try this

```
icon --help
```
Prints the usage summary for the Icon command, a first look at what the tool accepts.

```
icont --help
```
Shows usage for the translator, which compiles Icon source before iconx runs it.

## What's unique

Expressions that can produce multiple results, with automatic backtracking until one succeeds, make for a control-flow model very unlike most mainstream languages. It comes from the lineage that grew out of SNOBOL4.

## Caveats

Development is frozen, so no new language features are coming, and the brief did not cover documentation, examples, or the Windows build.

## Links

- [Icon homepage](https://www2.cs.arizona.edu/icon/)
