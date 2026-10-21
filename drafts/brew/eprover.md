---
name: eprover
title: E (eprover)
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, logic, math, science, theorem-proving]
homepage: https://eprover.org/
scout_score: 7
status: draft
---

# E (eprover)

**TLDR;** A research-grade automated theorem prover: give it axioms and a conjecture in first-order logic, and it searches for a proof.

E is an automated theorem prover for many-sorted first-order logic with equality, written in C. You write a problem file containing a specification (axioms) and a conjecture, in LOP, TPTP-2 or TPTP-3 format, which it detects on its own. E then searches for a proof. If it finds one, it prints it. If it does not, it may keep going for a very long time.

The README is candid about this. It says the prover will "run forever, using up all of your machines resources. Very occasionally it will find a proof for the conjecture and tell you so ;-)." Automated reasoning is a hard search problem, and E treats it that way: with `--auto` it picks a heuristic strategy based on the problem, and with `--auto-schedule` it runs a series of strategies in turn, assuming a 300-second budget unless told otherwise. `--auto-schedule=n` spreads those strategies across n cores.

The idea underneath is that a proof can be found by machine and then checked separately. E can write proof objects, and the bundled `checkproof` tool verifies them, though it skips the non-clausal parts. The package also ships helpers for strategy parameter search, axiom filtering, and a knowledge-base toolset (the `ekb_*` programs). Higher-order logic is possible only if E is built with `--enable-ho`, which the brew formula's description does not claim.

## Install

```
brew install eprover
```

## Try this

```
eprover --help
```
Prints usage information and the long list of options, a quick look at how many knobs a prover has.

```
eprover --auto --proof-object problem.p
```
Runs automatic strategy selection on your problem file and prints a proof object if it finds one.

```
eprover --auto-schedule=8 --proof-object problem.p
```
Tries a schedule of strategies spread across 8 CPU cores, usually stronger than a single automatic strategy.

## What's unique

E has a strategy-scheduling layer that tries many search strategies in sequence or across cores, rather than betting on one. It also pairs its proofs with an independent checker, so a claimed proof can be verified separately.

## Caveats

You must write or find your own problem files (TPTP is the usual source), auto mode may lose completeness on very large axiom sets, and the homepage returned nothing when checked, so the GitHub README is the main reference.

## Links

- [E homepage](https://eprover.org/)
- [GitHub repository and README](https://github.com/eprover/eprover)
