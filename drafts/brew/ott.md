---
name: ott
title: Ott
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, coq, formal-methods, language, latex, math, semantics]
homepage: https://www.cl.cam.ac.uk/~pes20/ott/
scout_score: 6
status: draft
---

# Ott

**TLDR;** Write a programming language's syntax and semantics once in ASCII math notation, then generate LaTeX, Coq, Isabelle, HOL and Lem definitions from it.

Ott is a command-line tool for writing definitions of programming languages and calculi. You describe a grammar and a set of inference rules in a concise ASCII notation that reads like informal mathematics. Ott parses the file, sort-checks it, and emits the output you ask for: typeset LaTeX, or definitions for Coq, HOL, Isabelle/HOL and Lem. It can also emit an OCaml syntax module.

The README frames it as a way to ease the move from informal to formal mathematics. A paper's language definition normally exists twice, once as typeset rules and once as a proof assistant encoding, and the two drift apart. Ott keeps one editable source and generates both. Parsing catches simple mistakes early, such as inconsistent judgement forms or metavariable naming.

It also generates helper functions for you: free variables, single and multiple substitution, subgrammar checks and binding auxiliaries. A filter mode goes the other way: it reads existing LaTeX or proof-assistant files, finds embedded Ott terms, and replaces them with typeset versions.

The underlying idea is formal semantics, the practice of defining a language precisely enough that you can prove things about it. The README lists real systems written in Ott, including TAPL-style calculi, POPLmark Fsub, the Leroy JFP96 ML module system, Lightweight Java and an OCaml-light semantics. These make good reading material alongside the tool.

## Install

```
brew install ott
# Optional, via opam instead: opam install ott (opam 2.0 or later)
# Coq support: opam repo add coq-released https://coq.inria.fr/opam/released, then opam install coq-ott
```

## Try this

```
ott --help
```
Lists the command-line options, including the input and output flags and which backends exist.

```
ott -i tests/test10.ott -o test10.tex -o test10.v
```
Run from a checkout of the repo, this reads the bundled test file and writes a LaTeX version and a Coq version of the same definition.

## What's unique

One ASCII source feeds both a typeset paper and several proof assistants, and it is sort-checked as it is parsed. The filter mode that typesets Ott terms inside existing LaTeX or proof files is a practical extra.

## Caveats

Maintained thinly: the README says resources for fixing issues are very limited, and only the fully concrete binding representation is fully supported, with the locally-nameless backend marked experimental.

## Links

- [GitHub repository and README](https://github.com/ott-lang/ott)
- [Ott homepage (now only a notice that it moved)](https://www.cl.cam.ac.uk/~pes20/ott/)
- [User manual (HTML)](http://www.cl.cam.ac.uk/~pes20/ott/top2.html)
- [Ott: Effective Tool Support for the Working Semanticist (JFP 2010)](http://www.cl.cam.ac.uk/users/pes20/ott/ott-jfp.pdf)
