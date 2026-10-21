---
name: etsh
title: etsh
source: brew
category: languages-and-oddities
commitment: quick
tags: [ancient, quick, shell, unix-history, v6]
homepage: https://etsh.dev/
scout_score: 8
status: draft
---

# etsh

**TLDR;** Ports of the 1975 Sixth Edition UNIX Thompson shell that run as ordinary interactive shells, so you can type at the ancestor of sh.

Etsh is a set of ports of the original /bin/sh from V6 UNIX, May 1975, maintained by J.A. Neitzel. That shell was written by Ken Thompson, and the project site calls its language a predecessor and subset of the Bourne and C shell languages. There are two shells. etsh is an enhanced but backward-compatible port. tsh is the unenhanced one. The site also describes glob, a port of the V6 global command.

The Thompson shell is small. It has pipelines (written | or ^), sequential and asynchronous commands (; and &), I/O redirection, globbing, and $1-style parameter substitution. The utilities if, goto, and fd2 are built into etsh and are external programs under tsh. Control flow in this shell is done with those utilities rather than built-in syntax, so scripts read quite differently from modern ones.

The idea underneath is that the shells most people use grew out of this one. Running it shows what was there at the start and what later shells added. You can also run old V6-style command files as they were written.

The homepage does not explain what osh and sh6 are, though both are installed. The project also has a gopher hole, and releases are signed with signify.

## Install

```
brew install etsh
```

## Try this

```
etsh --help
```
Prints the usage summary for the enhanced port.

```
tsh --help
```
Shows usage for the strict, unenhanced port, for comparing against etsh.

```
sh6 --help
```
Tries one of the other installed executables, which the homepage does not explain.

## What's unique

It is a faithful revival of a 1975 shell rather than a reimagining. It ships both a strict port (tsh) and a backward-compatible enhanced one (etsh), so you can compare them.

## Caveats

The homepage does not say which platforms are supported or what osh and sh6 are, and the dialect differs from modern shells, so expect old-style scripting.

## Links

- [Etsh (V6Sh) Project homepage](https://etsh.dev/)
- [Gopher hole](gopher://etsh.nl/1/)
