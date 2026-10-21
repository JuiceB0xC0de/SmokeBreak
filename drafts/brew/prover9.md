---
name: prover9
title: Prover9 and Mace4
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, logic, math, science, theorem-proving]
homepage: https://www.cs.unm.edu/~mccune/prover9/
scout_score: 7
status: draft
---

# Prover9 and Mace4

**TLDR;** Prover9 tries to prove theorems in first-order and equational logic from axioms you write, and Mace4 hunts for finite counterexamples when a claim is false.

Prover9 is an automated theorem prover. You write axioms and a goal as logic formulas, and it searches for a derivation using resolution and paramodulation. Paramodulation is the mechanism that lets it reason about equality, so it can handle equational theorems and not only pure first-order clauses.

Mace4 is the companion tool. Instead of looking for a proof, it searches for a finite model that satisfies your axioms. If it finds one where your conjecture fails, that model is a counterexample. Used together, the two tools cover both outcomes: either the claim follows, or here is a small world where it does not.

The project presents Prover9 as the successor to William McCune's Otter prover. The current LADR-2026 revision is a modernization of McCune's codebase by two maintainers, Jeffrey P. Machado and Larry Lesyna, who say they stay faithful to his documented intentions. It adds native TPTP input and TSTP proof output, so proofs can be checked by outside verifiers such as GDV and Ivy. The site says existing input files run unchanged.

The door this opens is mechanized reasoning. You state a theory, such as a group or a lattice, and ask a machine whether something follows. Watching it succeed, or fail and produce a counterexample, shows how proof search actually works.

## Install

```
brew install prover9
```

## Try this

```
prover9 --help
```
Prints the prover's usage and options, a starting point before writing your first input file.

```
mace4 --help
```
Prints usage for the finite model finder, the tool that looks for counterexamples.

## What's unique

It handles equational reasoning through paramodulation, and it ships with Mace4, so one toolkit both proves claims and refutes them with concrete finite models.

## Caveats

The brief shows no example commands or input syntax, so you will need the manual on prover9.org; performance claims on the site are the project's own and were not verified.

## Links

- [prover9.org (LADR-2026 homepage, docs, and downloads)](https://prover9.org)
- [Prover9 and Mace4 (original McCune page, older version)](https://www.cs.unm.edu/~mccune/prover9/)
