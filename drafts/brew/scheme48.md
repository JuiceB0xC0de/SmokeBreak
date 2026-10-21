---
name: scheme48
title: Scheme 48
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, byte-code, interpreter, language, pre-scheme, research, scheme]
homepage: https://www.s48.org/
scout_score: 6
status: draft
---

# Scheme 48

**TLDR;** A Scheme interpreter built on a byte-code VM, made by Kelsey and Rees as a testbed and teaching tool, and the birthplace of Pre-Scheme.

Scheme 48 is an implementation of the Scheme language written by Richard Kelsey and Jonathan Rees. It runs Scheme programs on a byte-code interpreter. The homepage describes it as "a testbed for experiments in implementation techniques and as an expository tool", so it is meant to be read and studied as well as run.

The idea underneath is that a language system can be small enough to understand. Scheme 48's virtual machine is not written in C by hand. It is written in Pre-Scheme, "a statically typed dialect of the Scheme programming language, combining the flexibility of Scheme with the efficiency and low-level machine access of C". Pre-Scheme originated here, so the system is partly written in a dialect of the language it implements.

The project also led to related systems: Kali, a distributed Scheme, and scsh, a scripting and systems environment built on top of it. The homepage links a manual in HTML, PDF and PostScript. Homebrew installs four executables: scheme48, scheme48-config, scheme-r5rs and scheme-srfi-7.

## Install

```
brew install scheme48
```

## Try this

```
scheme48 --help
```
Prints the command-line options for the main Scheme 48 executable.

```
scheme48-config --help
```
Shows the options for the configuration helper that reports how this install is set up.

```
scheme-r5rs --help
```
Shows the options for the launcher variant that starts Scheme 48 in R5RS mode.

## What's unique

It is a Scheme built to be studied, with a VM written in Pre-Scheme, a dialect that began in this very project. It is also the base that scsh and Kali were built on.

## Caveats

The brief found no first-run steps beyond installing, so expect to read the manual on the homepage to get going.

## Links

- [Scheme 48 homepage](https://www.s48.org/)
