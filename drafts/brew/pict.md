---
name: pict
title: pict
source: brew
category: deeper-rabbit-holes
commitment: quick
tags: [combinatorics, covering-arrays, math, quick, testing]
homepage: https://github.com/Microsoft/pict/
scout_score: 5
status: draft
---

# pict

**TLDR;** Microsoft's pairwise test generator turns a list of parameters and values into a small table of test cases that still covers every pair of values.

PICT reads a plain-text model file: parameter names, each followed by its possible values. It prints a tab-separated table to stdout. Instead of every combination, it aims for a much smaller set in which every pair of values from different parameters appears together in at least one row. The `/o` option raises that to triplets or higher.

The idea underneath is covering arrays. Exhaustive testing grows multiplicatively with each new parameter, but the README's framing is that "Research shows that testing all pairs is an effective alternative to exhaustive testing and much less costly." Packing combinations into as few rows as possible is a real combinatorial problem, and PICT solves it with deterministic heuristics. `/r:N` sets a random seed and `/b:N` tries N seeds and keeps the smallest suite. The docs say seeds commonly shift the row count by about 5% to 10% while coverage stays the same.

The model language is more than a list. Sub-models such as `{ PLATFORM, CPUS, RAM, HDD } @ 2` give a group of parameters its own combination order. Constraints are written as `IF ... THEN ...` over `[Parameter]` names. Values can carry weights and aliases. A `~` prefix marks a negative value, so each test contains at most one invalid input and invalid inputs cannot mask each other.

The repository also ships `pict-benchmark`, which runs the pairwise.org benchmark scenarios many times with different seeds and reports the smallest suite for each. That makes it a handy way to watch the heuristic work.

## Install

```
brew install pict
```

## Try this

```
pict --help
```
Prints the usage line and the list of options, including order, seeding, and randomization.

```
pict model [options]
```
Reads your model file of parameters and values and prints a tab-separated table of test cases to stdout.

```
pict.exe model.txt /e:seedrows.txt
```
Seeds generation with rows from a tab-separated file so required or earlier combinations are kept (written as pict.exe in the docs; the Homebrew binary is pict).

## What's unique

Negative testing with a `~` prefix keeps invalid values from masking each other, and per-group sub-models let hardware-like parameters use a different combination order than the rest.

## Caveats

The brief found no release or commit dates, weights are only "opportunistic hints", and randomized output varies from run to run.

## Links

- [GitHub repository (homepage)](https://github.com/Microsoft/pict/)
- [Full documentation: doc/pict.md](https://github.com/Microsoft/pict/blob/main/doc/pict.md)
- [Pairwise testing background at pairwise.org](http://pairwise.org)
- [Releases (pict.exe builds)](https://github.com/microsoft/pict/releases/)
