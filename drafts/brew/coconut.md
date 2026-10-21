---
name: coconut
title: Coconut
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, functional, language, python]
homepage: https://coconut-lang.org/
scout_score: 5
status: draft
---

# Coconut

**TLDR;** A functional language that compiles to plain Python, adding pipelines, pattern matching and short lambdas while staying a superset of Python.

Coconut is a source-to-source compiler. You write `.coco` files in Python plus extra syntax, and it produces ordinary Python that runs on a standard interpreter. The README calls it "a variant of Python that adds on top of Python syntax new features for simple, elegant, Pythonic functional programming."

The added syntax covers a lot of ground: short lambdas like `x -> x + 1`, pipelines with `|>`, composition with `..>`, partial application such as `map$(.**2)`, destructuring assignment, pattern matching, algebraic data types via `data`, lazy recursive iterators, `parallel_map`, tail call optimization and multidimensional array literals.

The author's stated aim is to let Python programmers use the tools of modern functional programming in as Pythonic a way as possible. The homepage also says Coconut "can backport almost all modern Python features as far back as Python 2.6", so the same source can target many Python versions. It claims that all valid Python is valid Coconut, so existing code should carry over, though that is the project's own framing.

The idea underneath is that a language can be a thin layer over another one. Because the output is readable Python, you can see exactly what each pipeline or pattern match turns into, which makes it a way into how functional features map onto a language that was not designed for them.

## Install

```
brew install coconut
# The README's own install route is: pip install coconut
```

## Try this

```
coconut --help
```
Lists the compiler's options and modes.

```
coconut-run --help
```
Shows how to compile and run a Coconut file in one step.

## What's unique

It extends Python with pipelines, pattern matching and partial application without leaving the Python ecosystem, since the output is plain Python. It also backports newer Python features to older versions.

## Caveats

Release dates and current maintenance status were not visible in the sources, and the many version-pinned executables installed by brew are unexplained.

## Links

- [Homepage](https://coconut-lang.org/)
- [Tutorial](http://coconut.readthedocs.io/en/latest/HELP.html)
- [Documentation](http://coconut.readthedocs.io/en/latest/DOCS.html)
- [GitHub](https://github.com/evhub/coconut)
- [Online Interpreter](https://cs121-team-panda.github.io/coconut-interpreter)
