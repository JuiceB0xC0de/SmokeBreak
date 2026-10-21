---
name: execline
title: execline
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, exec, language, shell, skarnet, unix]
homepage: https://skarnet.org/software/execline/
scout_score: 6
status: draft
---

# execline

**TLDR;** A scripting language with no interpreter loop: each command execs the next program in the chain, giving a different way to think about shells.

execline is a non-interactive scripting language from skarnet.org. In the homepage's words, it is "like sh - but its syntax is quite different from a traditional shell syntax." A script is a text file handed to `execlineb`, which parses it and launches the first command.

The rest of the package is a set of small single-purpose programs: `cd`, `if`, `forx`, `elglob`, `redirfd`, `importas` and so on. They are meant to be used inside an execlineb script. Each command does its piece of work and then runs the next program in the chain, so a script is effectively a sequence of execs and not a loop evaluating lines.

The stated motivation is that execline is as powerful as a shell, but "its syntax is far more logical and predictable than the shell's syntax, and has no security issues." The homepage links a page titled 'Why not just use /bin/sh?' which makes the longer case. The idea underneath is that a lot of what a shell does is arranging processes, file descriptors and environment, and you can do that with composable programs instead of a big parser.

The homepage also carries a set of quines, including one by Sertonix that uses only execline commands and no external programs. That is a good way to see how the language is put together.

## Install

```
brew install execline
# depends on skalibs, which Homebrew pulls in
```

## Try this

```
execlineb --help
```
Prints usage for the script launcher, the entry point for running an execline script file.

## What's unique

There is no interpreter loop at all: a script is a chain of small programs that exec each other, and the whole toolkit is made of those single-purpose commands.

## Caveats

It is non-interactive only, not a login or interactive shell, and the homepage gives no worked examples to copy, so expect to read the docs.

## Links

- [execline homepage](https://skarnet.org/software/execline/)
- [execline git repository](git://git.skarnet.org/execline)
