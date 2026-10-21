---
name: maxima
title: Maxima
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, computer-algebra, lisp, math, plotting, symbolic]
homepage: https://maxima.sourceforge.io/
scout_score: 6
status: draft
---

# Maxima

**TLDR;** A free computer algebra system descended from MIT's 1960s Macsyma: type an expression, get exact symbolic answers for calculus, algebra and more.

Maxima manipulates mathematical expressions as symbols rather than just numbers. The homepage lists differentiation, integration, Taylor series, Laplace transforms, ordinary differential equations, systems of linear equations, polynomials, sets, lists, vectors, matrices and tensors. It uses exact fractions, arbitrary-precision integers and variable-precision floats, so results stay exact until you ask for a number. It can also plot functions and data in two and three dimensions.

The plain `maxima` program is a terminal prompt. You type an expression and it returns a simplified, symbolic or numerical result. Graphical front ends, wxMaxima and XMaxima, give a notebook-style interface with formatted math output. The brew formula also installs `rmaxima` and `xmaxima`.

The history is the interesting part. The homepage calls Maxima "a descendant of Macsyma, the legendary computer algebra system developed in the late 1960s at the Massachusetts Institute of Technology," and says many later systems, such as Maple and Mathematica, were inspired by that line of work. William Schelter maintained the Maxima branch from 1982 until his death in 2001. In 1998 he obtained permission to release the source under the GPL, and a user and developer group has carried it on since.

The idea underneath is that algebra and calculus can be done by a program that rewrites expressions by rule, the way you would on paper. Using it shows you what a computer algebra system does that a calculator cannot.

## Install

```
brew install maxima
# the formula pulls in sbcl (a Lisp), gnuplot, rlwrap and gettext
```

## Try this

```
maxima --help
```
Lists the command-line options for the terminal program.

```
rmaxima --help
```
Shows the options for the rlwrap-wrapped variant, which is meant to give line editing and history at the prompt.

```
xmaxima --help
```
Shows the options for the graphical XMaxima front end.

## What's unique

It is a direct line of descent from Macsyma, the 1960s MIT system, and it is GPL-licensed and still developed. That is unusual for a computer algebra system this old.

## Caveats

The plain maxima program is terminal-only, so the notebook experience depends on wxMaxima or XMaxima, and the brief did not check the documentation or install details.

## Links

- [Maxima homepage](https://maxima.sourceforge.io/)
