---
name: bend
title: Bend
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, dependent-types, functional, gpu, language, parallel, proofs]
homepage: https://bend-lang.com
scout_score: 6
status: draft
---

# Bend

**TLDR;** A parallel functional language whose type checker doubles as a proof checker, pitched as a way to stop AI coding agents from breaking your declared rules.

Bend is a functional language that compiles to native code and runs on CPUs (up to sixteen cores) or GPUs. You write the work as ordinary recursive calls, and the runtime spreads them across available cores and joins the results. There are no threads, locks, or kernels to write.

The other half is the type checker, which works as a proof checker in the style of Lean and Rocq. Rules go in a LAWS.bend file as checkable declarations. The homepage's example is that no sequence of moves leads to victory. A PROOF.bend file must then prove the implementation satisfies those laws, and `bend PROOF.bend` runs the check. The homepage's phrase for it: "LAWS.bend is AGENTS.md backed by proof."

The stated reason is that people will want an unambiguous way to tell AI systems what they want, and laws are more precise than natural language. A fast checker makes it practical to run after every edit. The core type theory is called BendTT, an affine dependent type theory, and the parallel runtime is BendRT.

The homepage says the PROOF.bend body is written by the AI, so the guarantee is only as good as the laws you wrote and the proofs actually covering them. Treat it as a way to see dependent types and automatic parallelism side by side in one young language.

## Install

```
brew install bend
# the homepage's own install is: curl -fsSL https://bend-lang.com/install.sh | sh
# the brew formula depends on bun. The homepage lists no account requirements and no GPU setup steps.
```

## Try this

```
bend guide
```
Prints GUIDE.md, which the homepage describes as the whole language, so you can read it in one go.

```
bend PROOF.bend
```
Runs the proof check against the laws, the step the homepage says to run before committing.

```
bend --help
```
Lists the commands the executable offers.

## What's unique

It combines automatic CPU and GPU parallelism with a Lean-style proof checker in one language. Its pitch is that the checker, not a human reviewer, rejects an AI agent's bad changes.

## Caveats

The homepage says Bend is young and says "Expect bugs"; its speed numbers are vendor charts from an Apple M4 Max, and it works best on the back-end on Linux and macOS.

## Links

- [Homepage](https://bend-lang.com)
