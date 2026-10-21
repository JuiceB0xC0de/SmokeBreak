---
name: cafeobj
title: CafeOBJ
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, formal-methods, language, math, rewriting, theorem-proving]
homepage: https://cafeobj.org/
scout_score: 8
status: draft
---

# CafeOBJ

**TLDR;** An algebraic specification language from Japan where you describe software as equations, run them by rewriting, and prove properties by executing proof scores.

CafeOBJ is a formal specification language with an interpreter. You write modules that declare sorts (types) and operators, add equations, and then ask the interpreter to reduce terms. Evaluation is equational rewriting: the equations are applied as rules until nothing more can be simplified. Its syntax and typing come from OBJ3, including mix-fix operators, ordered sorts, parameterized modules, views, and module expressions.

The homepage describes it as a language for writing formal (mathematical) specifications of models for a wide variety of software and systems, and for verifying their properties. It is positioned as a successor to OBJ3 with more advanced features.

The unusual part is how proofs work. A proof score is an ordinary CafeOBJ program. You write it, run it, and the result of the run carries out the proof. The homepage says the semantics rest on institution theory rather than on one fixed logic, and it shows a "CafeOBJ cube" diagram mapping how the combined logics relate. Few language front pages come with one.

The brief does not say in detail what the interpreter prints beyond rewriting results and proof-score execution, so expect to learn it from the tutorials and manuals.

## Install

```
brew install cafeobj
# Homebrew route needs XCode and the Command Line Tools. The formula depends on clisp.
# Alternatively, the download page offers binary tarballs for macOS (Intel and ARM) and Linux 64-bit, and a zip for Windows 64-bit.
```

## Try this

```
cafeobj --help
```
Prints the interpreter's command-line options.

```
cafeobj --list-engines
```
Lists the engine dumps the wrapper script knows about, useful when several Lisp builds are installed.

```
cafeobj --engine sbcl
```
Starts the interpreter on the SBCL engine, if that build is installed.

## What's unique

Theorem proving is done by writing and running ordinary programs (proof scores), and the logic underneath is grounded in institution theory rather than one fixed system.

## Caveats

Allegro CL builds and Debian/Ubuntu builds have been discontinued, several manuals are Japanese only, and the user manual is described as slightly outdated.

## Links

- [Homepage](https://cafeobj.org/)
- [Download and install page](https://cafeobj.org/download/)
- [Documentation (reference and user manuals, PTcalc, tutorials)](https://cafeobj.org/documentation/)
- [Development repository on GitHub](https://github.com/CafeOBJ/cafeobj)
