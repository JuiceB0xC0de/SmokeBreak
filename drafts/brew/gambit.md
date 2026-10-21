---
name: gambit
title: Gambit
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, game-theory, math, nash-equilibrium, python, science]
homepage: https://www.gambit-project.org/
scout_score: 6
status: draft
---

# Gambit

**TLDR;** Gambit computes Nash equilibria and quantal response equilibria for finite games, from a GUI, a set of command-line solvers, or Python.

Gambit is a toolkit for computation on finite, noncooperative games, in either extensive form (game trees) or strategic form (payoff tables). You build a game by hand or read it from a standard file format. Then you ask it for pure and mixed-strategy Nash equilibria. It also computes quantal response equilibria, and it can fit quantal response models to data.

The same code comes three ways: a GUI for interactive work, command-line tools for scripting, and a Python package, pygambit, for automating games at scale. The Homebrew formula installs the command-line solvers, one per algorithm family, with names like gambit-enummixed, gambit-lcp, gambit-logit and gambit-simpdiv. The project's own line is "Command-line tools suitable for scripting or calling from other programs".

The project was founded in the mid-1980s at the California Institute of Technology, so it is old, and the homepage credits Alan Turing Institute funding for Gambit 17. The idea underneath is that an equilibrium is something you can compute, not only prove exists. Different algorithms find different equilibria, or only some of them, and a game can have several. Running several solvers on the same small game is a good way into that.

## Install

```
brew install gambit
# The formula depends on wxwidgets (for the GUI). For Python instead: pip install pygambit (needs a working Python and pip).
```

## Try this

```
gambit-lcp --help
```
Shows the options for the linear complementarity solver, one of the command-line equilibrium finders.

```
gambit-enummixed --help
```
Shows the options for the solver that enumerates mixed-strategy equilibria.

```
pip install pygambit
```
Installs the Python package from PyPI so you can build and solve games from a script.

## What's unique

One codebase, developed since the mid-1980s, is offered as a GUI, scriptable command-line solvers and a Python package. Few other tools cover Nash and quantal response equilibria together.

## Caveats

It covers finite games only, and I could not confirm the file formats or the full algorithm list, since the documentation was not read.

## Links

- [Homepage](https://www.gambit-project.org/)
- [Documentation](https://gambitproject.readthedocs.io/)
- [GitHub repository](https://github.com/gambitproject/gambit)
- [pygambit on PyPI](https://pypi.org/project/pygambit/)
