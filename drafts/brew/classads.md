---
name: classads
title: ClassAds
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, htcondor, language, library, matchmaking]
homepage: https://research.cs.wisc.edu/htcondor/classad/
scout_score: 6
status: draft
---

# ClassAds

**TLDR;** An expression language from HTCondor where two records match only if each one's requirements evaluate true against the other, a two-sided matchmaking data model.

A classad is a mapping from attribute names to expressions. Many of those expressions are plain integers, floats or strings, so an ad can read like a property list. Expressions can also refer to another ad: `other.size > 3` is true when the other ad has an integer `size` greater than three.

That reference to "the other ad" is the idea underneath. Per the project, two classads match if each ad has a `requirements` attribute that evaluates to true in the context of the other ad. Both sides state what they need, and both must accept the pairing. A job can say what kind of machine it wants, and a machine can say what kind of jobs it will take.

It was built for HTCondor, where classads are described as "the lingua franca": they describe jobs and workstations, are exchanged between processes to schedule work, are logged for debugging and statistics, and are queried for the current state of the system. The listed papers extend the model from two-way matches to multiway "gangmatching" across several resources at once.

The brew package installs the C++ library plus six executables: `classad_functional_tester`, `classad_version`, `cxi` and an `_ns` variant of each. The homepage does not describe them, so start with `--help` and see what they offer.

## Install

```
brew install classads
```

## Try this

```
classad_version
```
Probably prints the version of the installed ClassAd library; the homepage does not document it, so this is a guess from the name.

```
cxi --help
```
Shows the usage text for the cxi tool, whose purpose the homepage does not explain.

```
classad_functional_tester --help
```
Shows the options for the functional tester, which is presumably the library's test driver.

## What's unique

It is built around two-sided matching rather than queries or plain records: each ad carries its own constraints, and a match needs both to hold. It has a formal language reference and academic papers behind it.

## Caveats

The ClassAd homepage lists its newest C++ release as 1.0.10 from April 2011, and it gives no install steps or documentation for the brew executables.

## Links

- [ClassAd homepage](https://research.cs.wisc.edu/htcondor/classad/)
