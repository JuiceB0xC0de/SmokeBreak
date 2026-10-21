---
name: acl2
title: ACL2
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [days-off, formal-verification, lisp, math, theorem-prover]
homepage: https://www.cs.utexas.edu/~moore/acl2/
scout_score: 8
status: draft
---

# ACL2

**TLDR;** A Lisp-based programming language and theorem prover where you write models of computer systems, then ask the machine to prove things about them.

ACL2 is both a programming language and a logic. You write definitions in an applicative (side-effect-free) dialect of Common Lisp, then state theorems about them. The accompanying prover tries to prove each theorem, and either accepts it or fails, which tells you something about your model or your idea.

The odd part is that the model is executable. The same definitions you run on test inputs are the ones you prove properties about, so there is no separate specification language to keep in sync. Definitions and theorems are collected into files called books, which can be certified and reused. The community maintains a large shared library of them.

It belongs to the Boyer-Moore family of provers, which the homepage says received the 2005 ACM Software System Award. Extensions include ACL2(r) for real numbers via non-standard analysis, ACL2(p) for parallel evaluation, and ACL2s, an Eclipse-based variant from a separate group that adds termination-proof automation and counterexample generation.

The idea underneath is that a program can be treated as a mathematical object and checked by machine, not just tested. The homepage is frank that the learning curve is steep: "If you are a newcomer to ACL2, we do not recommend that you wander off into the full documentation." It points newcomers to the START-HERE topic instead.

## Install

```
brew install acl2
# installs the acl2 and acl2p executables; sbcl is pulled in as a dependency
```

## Try this

```
acl2 --help
```
Prints the command-line options for starting the ACL2 prover.

```
acl2p --help
```
Shows the options for the parallel-evaluation build of ACL2.

```
:DOC
```
Typed at the ACL2 prompt, opens the built-in documentation browser; start with the START-HERE topic.

## What's unique

The models are written in an executable Lisp dialect, so the same artefact can be both run and proved. It also has a large community library of reusable proven books.

## Caveats

The learning curve is steep, community books are installed separately, and building the full manual from source is slow.

## Links

- [ACL2 homepage](https://www.cs.utexas.edu/~moore/acl2/)
