---
name: numbat
title: Numbat
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, calculator, language, math, repl, science, units]
homepage: https://numbat.dev/
scout_score: 6
status: draft
---

# Numbat

**TLDR;** A scientific calculator and statically typed language where physical units are part of the type system, so 15 km/h * 30 min comes out as 7.5 km.

Numbat is an interactive calculator and small programming language for scientific work. You type expressions, it checks that the units make sense, and it prints the answer. The `->` operator converts between compatible units, so `30 km/h -> mph` does what it looks like. Run with no arguments, it opens a REPL with history, Ctrl-R search and tab completion.

The idea underneath is dimensional analysis as a type system. Dimensions such as Length and Time act as static types. Annotated functions and constants are checked before anything is calculated, and unannotated ones are inferred. Adding a length to a time is an error, not a number.

The unit system is not hardcoded. The standard library is written in Numbat itself, so a single line such as `unit bathtub = 150 L` defines a new unit. You can put your own definitions in an `init.nbt` file, or replace the prelude module entirely. Units can be entered many ways: `km/h`, `kilometer/hour`, `m^2`, `m²`.

It describes itself as a calculator, not a computer algebra system. It does not solve differential equations or compute integrals. The parser is also strict: in the README's words, it "never tries to be 'smart' on syntactically incorrect input."

## Install

```
brew install numbat
```

## Try this

```
numbat
```
Opens the interactive REPL, where you can type expressions like `30 km/h -> mph` and get a unit-converted answer.

```
unit bathtub = 150 L
```
Defines a new unit on one line, which you can then use in later expressions and conversions.

```
numbat --help
```
Lists the command-line options of the CLI.

## What's unique

Units are first-class typed values rather than strings, and the unit system is ordinary editable code in a standard library written in Numbat. That makes it a practical way to see dimensional analysis as type checking.

## Caveats

It is a calculator rather than a computer algebra system, unit coverage is large but not exhaustive, and the brief could not confirm how actively it is maintained.

## Links

- [Homepage and web version](https://numbat.dev/)
- [Documentation](https://numbat.dev/docs/)
- [Installation](https://numbat.dev/docs/cli/installation/)
- [GitHub repository](https://github.com/sharkdp/numbat)
