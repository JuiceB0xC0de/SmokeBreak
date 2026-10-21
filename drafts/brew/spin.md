---
name: spin
title: Spin
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, concurrency, formal-verification, language, model-checking]
homepage: https://spinroot.com/spin/whatispin.html
scout_score: 7
status: draft
---

# Spin

**TLDR;** Spin checks models of concurrent programs against assertions, so you can test a mutual exclusion algorithm like Peterson's before it ever runs as real code.

Spin is a verification tool for multi-threaded software. You do not point it at your code directly. You write a model of the system in its own modelling language, usually in a .pml file, and Spin checks that model against the assertions and properties you state. The homepage's example models Peterson's mutual exclusion algorithm: two processes, some shared variables, a goto loop, and an assertion that only one process is ever in the critical section.

Spin began at Bell Labs in 1980 and has been freely available since 1991. It won the ACM System Software Award in April 2002. Its sources moved to the BSD 3-Clause license in January 2016. The homepage says it "continues to evolve to keep pace with new developments in the field."

The idea underneath is formal verification of concurrency. Concurrent bugs tend to hide in rare orderings of events that testing seldom hits. A model checker works on a description of the system instead of a lucky run. The homepage mentions an automata-theoretic verification method in its course material, but it does not explain the internals, so treat the details as something to read up on after you have run the first example.

The homepage also lists a free online course and a semester-long course built around Spin, which makes it a reasonable entry point into the field.

## Install

```
brew install spin
```

## Try this

```
spin -run peterson.pml
```
Runs Spin's analysis on the homepage's Peterson's mutual exclusion model and reports whether the assertion holds. You write peterson.pml yourself from the example on the homepage.

```
spin --help
```
Prints the list of Spin's command-line options.

## What's unique

It has been around since 1980 and is aimed at concurrent and multi-threaded software rather than hardware. You describe the algorithm in a small modelling language and have it checked, instead of testing real code.

## Caveats

The latest release the homepage names is 6.5.1 from July 2020, and the page says nothing about platforms, build requirements, or limits on model size. Some course material is password-protected.

## Links

- [Spin homepage](https://spinroot.com/spin/whatispin.html)
- [Tau, a simple front-end tool for Spin (tarball)](https://spinroot.com/spin/tau_v1.tar.gz)
