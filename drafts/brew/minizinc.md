---
name: minizinc
title: MiniZinc
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, constraints, language, math, optimisation, solvers]
homepage: https://www.minizinc.org/
scout_score: 6
status: draft
---

# MiniZinc

**TLDR;** A constraint modelling language where you describe a puzzle or scheduling problem and let interchangeable solvers find the answer.

MiniZinc is a language for stating discrete optimisation problems: what the variables are, what rules they must obey, and optionally what to minimise or maximise. You write the model in a readable, typed syntax with a large library of ready-made constraints. You do not write the search procedure.

The compiler translates your model into FlatZinc, a lower-level solver input language, and hands it to a solver of your choice. Because model and solver are separate, the same model can run on different solver technologies. In the project's words, you can "run the same model using a variety of different solver technologies, without being locked into a particular solver."

The idea underneath is declarative problem solving: say what a valid answer looks like and let the machinery search. That is the door into combinatorial optimisation, constraint programming and the solver world behind scheduling, packing and timetabling. The homepage also describes an IDE, Python and JavaScript embedding, and in-browser use.

The brew formula pulls in Gecode and the COIN-OR CBC stack as solver backends, and installs the `minizinc` and `mzn2doc` executables.

## Install

```
brew install minizinc
```

## Try this

```
minizinc --help
```
Lists the compiler's options, including how to choose a solver and pass data files.

```
minizinc --solver gecode nqueens.mzn
```
Solves the n-queens model from the README with the Gecode solver. You supply the nqueens.mzn model file.

```
mzn2doc --help
```
Shows the options for the documentation generator that ships alongside the compiler.

## What's unique

One model can be sent to several different solver backends, with a large built-in constraint library, so you learn modelling once instead of one solver's API.

## Caveats

The brew package installs the compiler and a few solvers, not the IDE; the project's bundled packages are the route to a full setup, and I did not confirm the brew install beyond its metadata.

## Links

- [MiniZinc homepage](https://www.minizinc.org/)
- [libminizinc repository (compiler source and README)](https://github.com/MiniZinc/libminizinc)
- [Documentation (redirect, not confirmed)](https://www.minizinc.org/doc-latest/)
