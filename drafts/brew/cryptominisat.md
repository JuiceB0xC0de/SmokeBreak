---
name: cryptominisat
title: CryptoMiniSat
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, library, logic, math, sat, solver]
homepage: https://www.msoos.org/cryptominisat5/
scout_score: 5
status: draft
---

# CryptoMiniSat

**TLDR;** A SAT solver that decides whether a Boolean formula can be satisfied, then hands back a working assignment or a proof that none exists.

CryptoMiniSat reads a formula in DIMACS CNF format, extended with XOR clauses, and prints either `s SATISFIABLE` followed by `v` lines giving a variable assignment, or `s UNSATISFIABLE`. It runs from the command line. It also has C++, Python (pycryptosat), C and Rust interfaces, which support assumptions and repeated solve calls on the same problem.

The idea underneath is that a huge range of problems can be rewritten as a pile of true/false constraints: scheduling, circuit verification, puzzle solving, cryptanalysis. A SAT solver then searches that space far better than hand-written code would. The homepage describes it as "a modern, multi-threaded, feature-rich, simplifying SAT solver". The simplifying part means it rewrites the problem while it searches, using techniques such as variable elimination, subsumption, vivification and failed-literal probing. It also recovers XOR structure, which matters for crypto-style problems. The homepage describes the CryptoMiniSat 4 era, and the README does not explain the internals.

Two features make it more than a plain solver binary. You can enumerate every solution by banning each model as you find it, and the older homepage shows `--maxsol` for listing several. It can also write XLRUP proofs of its answers, which a formally verified checker called cake_xlrup can confirm independently. So an answer does not have to be taken on trust.

The README is written for people who already know CNF and assumptions. Encode a small puzzle yourself and watch what comes back, and you get a first look at the field.

## Install

```
brew install cryptominisat
# installs cryptominisat5 and oracle; needs gmp (pulled in automatically)
# Python bindings: pip3 install pycryptosat
```

## Try this

```
cryptominisat5 --help
```
Lists the solver's options, a quick view of how many knobs a modern SAT solver has.

```
cryptominisat5 --verb 0 file.cnf
```
Solves a DIMACS CNF file quietly and prints `s SATISFIABLE` with `v` assignment lines, or `s UNSATISFIABLE`.

```
cryptominisat5 input.cnf proof.xlrup
```
Solves the file and writes an XLRUP proof that the cake_xlrup checker can verify.

## What's unique

It supports incremental solving with assumptions and XOR clauses, and writes proofs that a formally verified checker can confirm. It also sits in a wider research toolchain with the author's Arjun model counter.

## Caveats

The README assumes you already know CNF and assumptions, and the homepage is an older page with outdated binary names, Python 2 syntax and a licence note that disagrees with the README's MIT.

## Links

- [Homepage (CryptoMiniSat 5 page)](https://www.msoos.org/cryptominisat5/)
- [GitHub repository and README](https://github.com/msoos/cryptominisat)
- [Arjun, companion model counting and preprocessing tool](https://www.github.com/meelgroup/arjun)
