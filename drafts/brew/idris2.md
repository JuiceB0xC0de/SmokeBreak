---
name: idris2
title: Idris 2
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, functional, language, math, types]
homepage: https://www.idris-lang.org/
scout_score: 7
status: draft
---

# Idris 2

**TLDR;** A purely functional language where types are ordinary values, so the compiler can check things like list lengths before your program ever runs.

Idris 2 is a purely functional programming language with first-class types. You write programs in .idr files, and the idris2 compiler checks them against their types, then produces an executable. Because types are ordinary values, a type can mention a value, such as the length of a list. A function's type can say that two lists have the same length, or that a list is non-empty, and the compiler checks that before anything runs.

The idea behind it is Type-Driven Development. In the project's words: "We treat the type as the plan for a program, and use the compiler and type checker as our assistant, guiding us to a complete program that satisfies the type." You write the type first, and the compiler helps you fill in the program. The more precise the type you start with, the more you can trust the result.

Most dependently typed languages are proof assistants or research tools. Idris 2 aims to be a general-purpose language where these types are used in ordinary programs. It has a package workflow built on .ipkg project files, an LSP, and more than one code generator. The compiler emits code through a Scheme backend, Chez Scheme by default with Racket as an option.

It is a door into a different way of thinking about what a program is allowed to promise. Expect to spend an afternoon just getting used to writing types that carry real information.

## Install

```
brew install idris2
# Homebrew pulls in Chez Scheme as a dependency. The README also recommends the pack package manager (github.com/stefan-hoeck/idris2-pack), which manages versions and installs the LSP. No account or hardware needed.
```

## Try this

```
idris2 --help
```
Lists the compiler's options and shows what the REPL and build modes offer.

```
idris2 --init
```
Generates an .ipkg project file describing a new Idris project.

```
eval "$(idris2 --bash-completion-script idris2)"
```
Turns on tab completion for idris2 in the current bash session.

## What's unique

It treats dependent types as a tool for everyday programs rather than only for proofs. The type-driven workflow, where the compiler helps you fill in a program from its type, is the distinctive part.

## Caveats

The language currently has Type : Type because cumulativity is missing, which the README says to keep in mind before trusting that you proved something, and the old Idris 1 book describes the older version.

## Links

- [Homepage](https://www.idris-lang.org/)
- [Official documentation](https://idris2.readthedocs.io/en/latest/index.html)
- [Source repository](https://github.com/idris-lang/Idris2)
- [pack package manager](https://github.com/stefan-hoeck/idris2-pack)
