---
name: gforth
title: Gforth
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, forth, gnu, language, repl, stack-based]
homepage: https://www.gnu.org/software/gforth/
scout_score: 7
status: draft
---

# Gforth

**TLDR;** The GNU implementation of Forth, a stack-based language with almost no syntax, where you type words at a prompt and build the language up yourself.

Gforth is the GNU Project's take on Forth. You start it, get a prompt, and type words. Values go onto a stack and words consume them, so there is no conventional expression syntax to learn. You can also run Forth source files in batch. The homepage calls it "a free, fast, featureful and portable implementation of the Forth 2012 language" and says it is fully ANS Forth compliant.

The project's stated goal is "to develop a standard model for ANSI Forth": follow the standard, model its implementation-dependent parts, and be easy to port. It also wants to stay close to older systems like fig-Forth and F83. The bundled libraries include an object-oriented package written in plain ANS Forth, which shows how little the core language needs.

Underneath, the interpreter is built on Vmgen, a virtual-machine generator. Primitives are written in a small specification language and compiled through GCC into threaded code. Two engines ship: `gforth-fast` is quicker, and plain `gforth` is the debugging engine, which gives precise backtraces for things like illegal memory access but runs roughly 1 to 2 times slower.

The bigger idea is a language you extend from inside itself. Defining a word is how you program, and the prompt can be asked about its own vocabulary. There are also Gforth EC variants aimed at small controllers, which is unusual for a GNU project.

## Install

```
brew install gforth
# runtime needs libtool and gcc (for the C interface); a Docker image also exists: docker run -it --rm forthy42/gforth
```

## Try this

```
gforth
```
Starts the interactive interpreter with the debugging engine and gives you a Forth prompt.

```
words
```
Typed at the Gforth prompt, lists every word currently defined, a quick tour of what the system already knows.

```
gforth-fast --help
```
Shows the options for the faster engine, which skips the precise-backtrace debugging support.

## What's unique

It is a standards-focused Forth with two execution engines and a VM generator underneath, plus embedded variants for tiny controllers.

## Caveats

The GNU homepage was last updated in 2015 and names 0.7.3 as current, though development continues in git, so version history is a little muddled.

## Links

- [GNU Gforth homepage](https://www.gnu.org/software/gforth/)
- [gforth.org (project site, manual, install instructions)](https://gforth.org/)
- [Git repository on Savannah](https://git.savannah.gnu.org/git/gforth/)
