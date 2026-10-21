---
name: rocq
title: Rocq
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, language, math, ocaml, proofs, type-theory]
homepage: https://rocq-prover.org/
scout_score: 6
status: draft
---

# Rocq

**TLDR;** Rocq, formerly Coq, is a proof assistant where you write theorems and programs together and a small kernel checks every step.

Rocq is an interactive theorem prover and a dependently-typed programming language. You write definitions, algorithms and theorems in one formal language, then build the proofs step by step with tactics. A small kernel written in OCaml checks the result. It can also extract executable programs from specifications as OCaml or Haskell source.

The project describes itself as "a trustworthy, industrial-strength interactive theorem prover and dependently-typed programming language for mechanised reasoning in mathematics, computer science and more." It was formerly known as the Coq Proof Assistant, which is why most of the installed executables still start with `coq`. The newer `rocq` command is the new entry point.

The idea underneath is that a proof is a program and a statement is a type. If the kernel accepts your term, the theorem holds, and you only have to trust that one small core rather than the whole tool. The MetaRocq project formalises the core type theory itself, and a verified reference checker can be extracted to shrink the trusted base further.

The lineage is long. Coq has decades of use behind it, including the Four Colour Theorem, the CompCert verified C compiler, and HoTT. The Homebrew blurb says "higher-order logic", but the project's own framing is dependent type theory.

## Install

```
brew install rocq
# The Homebrew build has limited external packages and no language server. For editor support the project recommends the Rocq Platform or opam; see the install guide.
```

## Try this

```
rocq -v
```
Prints the Rocq version through the new entry point.

```
coqtop -v
```
Prints the version through the older Coq-named toplevel.

```
rocq --help
```
Lists what the rocq command can do.

## What's unique

It is the long-running Coq lineage, with large real-world verification projects behind it. Its kernel's own type theory is being formalised in MetaRocq.

## Caveats

The Homebrew route lacks many external packages and a language server, so VS Code users need VsCoq Legacy, and native_compute only works on some x86 setups with OCaml 5.

## Links

- [Homepage](https://rocq-prover.org/)
- [Install guide](https://rocq-prover.org/install)
- [Documentation (last release)](https://rocq-prover.org/docs)
- [GitHub repository](https://github.com/rocq-prover/rocq)
