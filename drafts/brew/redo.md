---
name: redo
title: redo
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, build-system, djb, make, python, shell]
homepage: https://redo.rtfd.io/
scout_score: 5
status: draft
---

# redo

**TLDR;** A build system where each target is a small shell script and dependencies are declared by running ordinary commands, from djb's design as a replacement for make.

redo is a Python implementation of Daniel J. Bernstein's redo, an alternative to make. Instead of a Makefile with its own syntax, you write one shell script per target, such as default.o.do or myprog.do. The script receives $1, $2 and $3 (target name, base name and a temporary output file) and writes its result there.

The central idea, in the docs' words: "declaring a dependency is just another shell command." A script calls redo-ifchange on its inputs, which builds them if needed and records that the current target depends on them. That record goes into a persistent .redo database, so later runs rebuild only what changed. Dependencies can even be declared after the build. The README's example compiles with gcc -MD, reads the generated .d file, and then passes the header list to redo-ifchange.

The author says redo keeps make's simplicity and flexibility while avoiding its flaws. Bernstein's original design existed only as terse notes with no code, so this implementation was written from those notes. The package installs eleven executables, including redo-log for build logs, redo-ood for out-of-date targets, redo-targets and redo-sources for inspecting the dependency graph.

It is a small door into a bigger question: what should a build system know, and when should it find out? Reading the .do scripts is a good way to see the answer redo gives.

## Install

```
brew install redo
# Depends on Python, which brew pulls in. No accounts or hardware needed.
```

## Try this

```
redo --help
```
Prints the options for the main command, including the parallel build flag.

```
redo myprog
```
Builds myprog from myprog.do, running the .do scripts it needs and recording their dependencies. Assumes you have written those scripts, as in the README example.

```
touch b.h
```
Simulates an edit to a header. Running redo myprog again then rebuilds only the objects affected by it.

## What's unique

Dependencies are plain shell commands run inside the build script, not a special syntax. The author also says this is the only known redo variant with parallel builds (redo -j) and log linearization (redo-log).

## Caveats

The author says the Python version is slower than make for some things, with a C rewrite planned but not done, and the docs page may not match the current release exactly.

## Links

- [redo documentation (homepage)](https://redo.rtfd.io/)
- [Source code on GitHub (apenwarr/redo)](https://github.com/apenwarr/redo)
- [Daniel J. Bernstein's original redo notes](http://cr.yp.to/redo.html)
- [Mailing list archives](https://groups.google.com/group/redo-list)
