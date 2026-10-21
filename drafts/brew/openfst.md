---
name: openfst
title: OpenFst
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, automata, cpp, formal-languages, library, nlp, speech]
homepage: https://www.openfst.org/twiki/bin/view/FST/WebHome
scout_score: 6
status: draft
---

# OpenFst

**TLDR;** A library and about 60 pipeable shell tools for weighted finite-state transducers, the machinery behind speech recognition and machine translation.

OpenFst is a C++ template library for building, combining, optimizing and searching weighted finite-state transducers. A transducer is a graph where each arc has an input label, an output label and a weight. A finite-state acceptor is the special case where input and output match, so it represents a set of strings. A transducer represents a relation between strings.

The shell tools are the easy way in. Each one reads binary FST files, runs one operation such as composition, determinization, minimization or shortest path, and writes a new file. With file names omitted they use stdin and stdout, so a whole computation can be a Unix pipeline. You write a machine as AT&T-format text, compile it with `fstcompile`, and look at it with `fstinfo` or `fstdraw`, which emits Graphviz dot.

The idea underneath is the semiring. Weights have one operation to combine alternative paths (Plus) and another to combine weights along a path (Times). Swap the semiring, for example Tropical for shortest-path problems or Log for probabilities, and the same composition and search algorithms work on different problems. The homepage lists speech recognition and synthesis, machine translation, OCR, pattern matching and information extraction as key uses.

The library was developed by contributors from Google Research and NYU's Courant Institute. It aims to be "comprehensive, reliable, flexible, efficient, and to scale well."

## Install

```
brew install openfst
# The homepage itself documents conda instead: conda install -c conda-forge openfst
# No accounts, hardware or first-run setup are mentioned. Graphviz (dot) is needed to render fstdraw output.
```

## Try this

```
fstcompile --isymbols=isyms.txt --osymbols=osyms.txt text.fst binary.fst
```
Turns a hand-written AT&T-format text description of a machine into a binary FST, mapping symbol names through your symbol tables.

```
fstinfo binary.fst
```
Prints state and arc counts, initial and final states, and properties such as deterministic, acyclic and weighted.

```
fstarcsort --sort_type=ilabel model.fst | fstcompose input.fst - | fstproject --project_output result.fst
```
Sorts a model, composes an input with it, and keeps only the output side, all as one pipeline.

## What's unique

One semiring framework covers acceptors, transducers and probabilistic models, so composition, determinization and shortest path behave the same across very different uses. The command-line tools are small filters that pipe together.

## Caveats

The main interface is the C++ template library, with the shell tools secondary. The docs live on an old TWiki site, and the quick tour was last edited in 2020 with one broken link on the homepage.

## Links

- [OpenFst homepage](https://www.openfst.org/twiki/bin/view/FST/WebHome)
- [Quick Tour (working URL)](https://www.openfst.org/twiki/bin/view/FST/FstQuickTour)
