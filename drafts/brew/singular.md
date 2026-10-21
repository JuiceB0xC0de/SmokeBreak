---
name: singular
title: Singular
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, algebra, algebraic-geometry, math, science]
homepage: https://www.singular.uni-kl.de/
scout_score: 6
status: draft
---

# Singular

**TLDR;** A computer algebra system for polynomial ideals, algebraic geometry and singularity theory: real research mathematics you can run in a terminal.

Singular is a computer algebra system for polynomial computations, with special emphasis on commutative and non-commutative algebra, algebraic geometry, and singularity theory. You give it polynomials, ideals and related algebraic objects, and it computes with them symbolically. The brief does not describe output formats in detail, so expect to learn them from the manual.

The idea underneath is that geometry can be turned into algebra. A curve or surface defined by polynomial equations corresponds to an ideal, and questions about shape, such as where a surface crosses itself or how a point is singular, become questions about those ideals. A system like this does that translation work for you. It is a narrower specialist than the general-purpose systems, and that focus is the reason to look at it.

The project is free and open-source under the GNU General Public Licence. It comes with a published user manual and a developer reference manual, and it has an issue tracker. The Homebrew formula also installs libsingular-config and libpolys-config, which suggest the code can be used as a library as well as an interactive program, though the brief does not go into that.

## Install

```
brew install singular
```

## Try this

```
Singular --help
```
Prints the command-line options for the interactive interpreter.

```
TSingular --help
```
Shows the options for the TSingular front end, which is installed alongside the main program.

## What's unique

It is a free, open-source CAS aimed at the algebra of singularities and at non-commutative algebra, a narrower niche than general-purpose systems.

## Caveats

This is research-level mathematics with its own language, so expect to read the manual; the brief could not confirm release dates or recent activity.

## Links

- [Homepage](https://www.singular.uni-kl.de/)
- [User Manual](https://www.singular.uni-kl.de/Manual/latest)
- [Source code (git)](https://github.com/Singular/Singular)
