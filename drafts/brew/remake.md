---
name: remake
title: remake
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, build-systems, debugger, make, profiling, tracing]
homepage: https://bashdb.sourceforge.net/remake/
scout_score: 5
status: draft
---

# remake

**TLDR;** A patched GNU Make with tracing, target listing, profiling and an actual debugger, so you can watch a build run and see why.

remake is GNU Make with extra features patched in. You run it on a Makefile as you would run make, and it can print more about what it is doing: better error reports, a trace of each target as it is considered, a list of targets, and the parent of a target. It can also write profiling output, which the README says can be opened in KCachegrind. A debugger is documented on the project's Read the Docs site.

The homepage describes it as "an enahanced version of GNU Make that adds improved error reporting, better tracing, profiling and a debugger." The current line is based on GNU Make 4.3 sources. There are separate branches for 4.2, 4.1, 3.82 and 3.81, so you can match the version your project already uses.

The idea underneath is that a Makefile is a program. It is a dependency graph that gets evaluated, with rules, variables and expansion order, and it usually fails with very little explanation. Treating it like code you can trace, step through and profile turns the question of why make rebuilt something into one you can answer by looking. The homepage says the same debugger approach is applied to several other languages, including Python, Bash, Zsh, Perl and Node.js.

## Install

```
brew install remake
```

## Try this

```
remake --tasks
```
Lists the targets in the Makefile in the current directory. The README shows this in an animated GIF.

```
remake --trace
```
Runs the build while tracing its execution. The short form is -x.

```
remake --profile
```
Produces profiling output of the build, which the README says KCachegrind can display.

## What's unique

It is a debugger for Make itself, not for the programs Make builds. It can trace a build, show why a target is being made, and profile it.

## Caveats

The brief could not confirm the release date or recent activity, and the README gives option names but no full command lines, so check --help for exact usage.

## Links

- [Homepage](https://bashdb.sourceforge.net/remake/)
- [Read the Docs guide](https://remake.readthedocs.io/en/latest/index.html)
- [GitHub repository](https://github.com/rocky/remake)
