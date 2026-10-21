---
name: grin
title: Grin
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, cryptocurrency, cryptography, mimblewimble, protocol]
homepage: https://grin.mw/
scout_score: 5
status: draft
---

# Grin

**TLDR;** A small, deliberately minimal implementation of Mimblewimble, a cryptocurrency protocol with no addresses, no visible amounts, and a chain that can shed old data.

Grin is an in-progress implementation of the Mimblewimble protocol, written by developers around the world. The README calls it a "clean and minimal implementation, and aiming to stay as such," and says Grin "likes itself small and easy on the eyes." The brew formula installs one executable, `grin`. The pages read for this entry do not say what it takes in or prints, so the first run is a matter of checking its help output.

The homepage describes a currency with no amounts and no addresses. The README says the protocol hides amounts and has scaling advantages, and that fees depend on the number of outputs created or destroyed and the size of the transaction. A new transaction is relayed through a subset of peers before being broadcast widely, which hides where it came from. The homepage also says past transaction data can be removed without losing security, so the chain does not collapse under the weight of stored data.

Proof of work uses Cuckoo Cycle in two variants: Cuckaroo, which is ASIC-resistant, and Cuckatoo, which is ASIC-targeted. Blocks arrive every minute, and difficulty adjusts along a smooth curve. The README also states that there is no ICO, pre-mine or founder's reward, and that no company, foundation or individual controls it.

The door here is the protocol design. Mimblewimble is an unusual alternative to Bitcoin-style ledgers, and a small codebase is a more approachable way to read about it than a large one. The project's doc/intro.md is the place to start for the mechanism itself.

## Install

```
brew install grin
```

## Try this

```
grin --help
```
Prints the command's usage, the only way to see what the binary accepts, since the README pages read here show no commands.

## What's unique

It is a Mimblewimble coin, a design that drops addresses and visible amounts and can prune history, kept deliberately small and readable next to Bitcoin-style codebases.

## Caveats

The README says the project is in progress and that many protocol characteristics are still undefined; the brief did not read the build docs, so first-run steps and platform support are unknown.

## Links

- [Grin homepage](https://grin.mw/)
- [GitHub repository (README)](https://github.com/mimblewimble/grin)
- [Introduction to Mimblewimble and Grin (doc/intro.md)](https://github.com/mimblewimble/grin/blob/master/doc/intro.md)
- [Build docs (doc/build.md)](https://github.com/mimblewimble/grin/blob/master/doc/build.md)
