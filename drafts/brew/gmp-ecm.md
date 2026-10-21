---
name: gmp-ecm
title: gmp-ecm
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, cryptography, factoring, math, number-theory]
homepage: https://gitlab.inria.fr/zimmerma/ecm
scout_score: 7
status: draft
---

# gmp-ecm

**TLDR;** A command-line implementation of the Elliptic Curve Method, which hunts for prime factors of large integers using arithmetic on elliptic curves.

The `ecm` program takes a large integer and tries to split it. It uses the Elliptic Curve Method, a factoring algorithm that is especially good at finding medium-sized prime factors of numbers far too big to factor by trial division. When it finds a factor, it prints it.

The brief could not read the README, so this entry does not describe the options or the internals. What the sources do confirm is the Homebrew description, the GPL licence, and a GitLab project page that links to a changelog.

The idea underneath is the door. Factoring is the hard problem that public-key cryptography leans on, and ECM is one of the classic ways people chip at it. It does not try to crack everything at once. It tries a random elliptic curve, and if the curve happens to behave well modulo a hidden prime factor, that factor falls out. Running it on a laptop is a hands-on way to see why factoring large numbers is hard and why some numbers are easier than others.

## Install

```
brew install gmp-ecm
# installs the `ecm` executable; depends on gmp, primesieve and libomp
```

## Try this

```
ecm --help
```
Prints the usage text and the list of options, which is the quickest way to learn what the program accepts.

## What's unique

It is a dedicated, long-established implementation of one specific factoring algorithm, so you can watch real number theory at work on your own machine.

## Caveats

The README loaded empty and the old homepage returned a 404, so usage, platform notes and project status are unverified.

## Links

- [Project homepage (GitLab)](https://gitlab.inria.fr/zimmerma/ecm)
- [README on GitLab (loaded empty)](https://gitlab.inria.fr/zimmerma/ecm/-/blob/master/README)
