---
name: sfst
title: SFST
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c++, finite-state, language, morphology, nlp, transducers]
homepage: https://www.cis.uni-muenchen.de/~schmid/tools/SFST/
scout_score: 7
status: draft
---

# SFST

**TLDR;** A finite-state transducer toolbox for building morphological analysers, the machinery that lets software split words into stems and endings.

SFST is a C++ toolbox for building morphological analysers and other tools based on finite state transducers. Per its homepage, it has four parts: a compiler that turns transducer programs into minimised transducers, interactive and batch-mode analysis programs, tools for comparing and printing transducers, and a C++ transducer library.

A morphological analyser takes a word form and works out its structure, such as stem, tense or case. Run the other way, the same transducer can generate word forms from a description. A finite state transducer is a compact way to encode that mapping, and one compiled machine can serve both directions. The executables installed here (fst-compiler, fst-mor, fst-generate, fst-infl and others) fit that pipeline, though the brief did not verify each one against documentation.

The author says it is easy to learn for people who know grep, sed, or Perl, which hints at a pattern-and-rewrite flavour in the transducer language. The homepage does not describe that language in detail.

The homepage points to real morphologies built with SFST: SMOR (German), LatMor (Latin), EMOR (English), TRMOR (Turkish), mlmorph (Malayalam) and yakutmorph (Yakut). It also lists HFST, which was built on top of SFST, and AFST, which is based on it. That makes it a good entry point into computational morphology and the FST family of tools.

## Install

```
brew install sfst
```

## Try this

```
fst-compiler --help
```
Shows the options of the compiler that turns transducer source programs into minimised transducers.

```
fst-mor --help
```
Shows the usage of the interactive analysis program that runs a compiled transducer over input words.

```
fst-generate --help
```
Shows usage for the tool that generates output strings from a transducer.

## What's unique

It is a long-lived, GPL-licensed FST toolkit that other projects, including HFST and AFST, were built on or from, with real morphologies for German, Latin, Turkish and more.

## Caveats

The homepage has no install steps or usage examples, and no release dates, so expect to read the manual and paper to get started and check how actively it is maintained.

## Links

- [SFST homepage](https://www.cis.uni-muenchen.de/~schmid/tools/SFST/)
