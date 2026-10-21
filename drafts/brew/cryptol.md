---
name: cryptol
title: Cryptol
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, cryptography, formal-methods, language, smt]
homepage: https://galoisinc.github.io/cryptol/master/RefMan.html
scout_score: 8
status: draft
---

# Cryptol

**TLDR;** A language for writing cryptographic algorithms as executable specs, which you can test with random inputs or prove correct for all inputs with an SMT solver.

Cryptol is an interpreter and REPL for a small domain-specific language built for describing cryptographic algorithms. You write the algorithm as a specification, and the specification runs. You can evaluate expressions, feed in values, and watch the design behave while you are still changing it. In the README's words: "Unlike current specification mechanisms, Cryptol is fully executable, allowing designers to experiment with their programs incrementally as their designs evolve."

The interesting part is what the REPL does with properties. Write a predicate, say that decrypting an encrypted message returns the original. Then `:check` runs it against randomly generated inputs, in the style of QuickCheck. `:prove` hands the same predicate to an SMT solver (Z3 by default, or Yices or CVC5) and asks whether it holds for every possible input. `:sat` asks the opposite question: does any input satisfy it.

Galois designed the language for the NSA Laboratory for Advanced Cybersecurity Research, as a public standard for specifying cryptographic algorithms. The idea is that a Cryptol reference spec can serve as the formal documentation for a cryptographic module. Galois also builds tools, described on the SAW website, that compare a spec against C or Java implementations. The README says this takes some work.

The door it opens is formal methods: tests sample behaviour, proofs cover all of it, and here both live in the same file.

## Install

```
brew install cryptol
# Homebrew installs a matching Z3 automatically. On Linux, prebuilt binaries are on the GitHub releases page, and you may need to fetch Z3 yourself because distro packages can be old.
```

## Try this

```
cryptol --help
```
Lists the interpreter's command-line options.

```
:check
```
Inside the REPL, tests a Cryptol predicate against randomly generated inputs, QuickCheck-style.

```
:prove
```
Inside the REPL, asks an SMT solver such as Z3 to prove a predicate holds for all inputs.

## What's unique

The same file is an executable spec, a randomized test target, and a theorem for an SMT solver to prove. It can also connect to tooling that checks real C or Java implementations against it.

## Caveats

It is aimed at cryptographers and implementers, needs Z3 on your PATH, and the homepage is only a reference manual, so expect to lean on the GitHub README and cryptol-specs for examples.

## Links

- [Cryptol Reference Manual (homepage)](https://galoisinc.github.io/cryptol/master/RefMan.html)
- [GitHub repository and README](https://github.com/GaloisInc/cryptol)
- [cryptol-specs repository (example specs)](https://github.com/galoisinc/cryptol-specs)
- [GitHub releases (binaries)](https://github.com/GaloisInc/cryptol/releases)
- [SAW website (implementation verification tooling)](https://saw.galois.com)
