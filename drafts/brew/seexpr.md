---
name: seexpr
title: SeExpr
source: brew
category: quick-weird-payoffs
commitment: afternoon
tags: [afternoon, disney, expression-language, generative, graphics, library]
homepage: https://wdas.github.io/SeExpr/
scout_score: 5
status: draft
---

# SeExpr

**TLDR;** Disney Animation's embeddable expression language for artists, with small demo tools that graph formulas and synthesize images from the command line.

SeExpr is a C++ library that evaluates scalar and vector arithmetic expressions against a large built-in function library. A host program hands it a string of text, and SeExpr returns a value. The homepage lists uses such as procedural geometry synthesis, image synthesis, simulation control, crowd animation, and geometry deformation.

It exists so artists can adjust a look or behaviour by editing a short expression inside a larger program, instead of asking someone to write and recompile code for each change. In the README's words, it is "an embeddable, arithmetic expression language that enables flexible artistic control and customization in creating computer graphics images."

The underlying idea is the small, embedded language. A host subclasses the Expression class and declares the extra variables and functions its expressions may use. The README points to the demo apps in src/demo as the worked examples of this pattern. The homepage adds that extensions can also be loaded as DSOs (dynamically loaded shared objects).

The Homebrew formula installs the demos as command-line tools: asciiCalc2, asciiGraph2, imageSynth2, and imageSynthPaint3d2. They are the easiest way to see what the evaluator does without writing any C++. The project also ships UI components for editing and visualizing expressions.

## Install

```
brew install seexpr
```

## Try this

```
asciiGraph2 "x^3-8*x"
```
Plots the expression x^3-8*x as a text graph. The README shows this as ./asciiGraph, but the Homebrew executable is named asciiGraph2.

```
asciiCalc2 --help
```
Prints usage for the command-line calculator demo that evaluates expressions.

```
imageSynth2 --help
```
Prints usage for the image synthesis demo, which builds pictures from expressions.

## What's unique

It is an expression language built for artists and embedded in production graphics tools, not a standalone scripting language, and it comes from Walt Disney Animation Studios. It also ships reusable editing UI components alongside the evaluator.

## Caveats

The project is quiet: the newest release the homepage mentions is v3.0.1 from November 2019, and the demos are described as test applications.

## Links

- [SeExpr homepage](https://wdas.github.io/SeExpr/)
- [GitHub repository and README](https://github.com/wdas/SeExpr)
- [Doxygen API docs](http://wdas.github.io/SeExpr/doxygen/)
- [SeExpr v3 FAQ (porting and new features)](http://wdas.github.io/SeExpr/doxygen/html/SeExpr_FAQ.html)
