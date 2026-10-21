---
name: xlispstat
title: XLISP-STAT
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, graphics, lisp, statistics, x11]
homepage: https://homepage.stat.uiowa.edu/~luke/xls/xlsinfo/
scout_score: 6
status: draft
---

# XLISP-STAT

**TLDR;** A 1990s statistics environment built on Lisp, where dynamic graphics and a prototype object system are the core idea, and regression models are objects.

Lisp-Stat is a statistical computing environment for data analysis, teaching and research, built on a subset of Common Lisp. It stretches ordinary Lisp arithmetic so it works element-wise on lists and vectors, then adds basic statistics and linear algebra on top. The executable Homebrew installs is `xlispstat`.

Its main emphasis is dynamic graphics. In the homepage's words, it aims to provide "a framework for exploring the use of dynamic graphical methods." The graphics sit on a portable window system that was meant to look the same on Mac OS, the X Window System and Microsoft Windows. That is why the formula depends on libx11.

The idea underneath is a prototype-based object system. The same system that builds and customizes the graphics also represents statistical models, including linear and nonlinear regression and generalized linear models. A plot and a model are both objects you can extend by cloning and adjusting them.

The design was influenced by the S language, the ancestor of R. Lisp-Stat shows a road not taken: a statistics tool that is a full Lisp, rather than a scripting language built for statistics.

## Install

```
brew install xlispstat

Needs X11 (libx11) for the graphics. I could not confirm how it behaves on current macOS, so you may want an X server such as XQuartz.
```

## Try this

```
xlispstat --help
```
Prints the command-line options, if any, for the interpreter. The brief did not confirm what it shows.

## What's unique

Statistics, interactive graphics and regression models all share one Lisp object system, instead of being a scripting layer over a numeric library.

## Caveats

The homepage is dated 1998, no maintenance information was found, and I could not confirm that it runs well on current systems.

## Links

- [Lisp-Stat Information (homepage)](https://homepage.stat.uiowa.edu/~luke/xls/xlsinfo/)
