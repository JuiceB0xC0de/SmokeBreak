---
name: kawa
title: Kawa
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, java, jvm, language, lisp, repl, scheme]
homepage: https://www.gnu.org/software/kawa/
scout_score: 5
status: draft
---

# Kawa

**TLDR;** Kawa is a Scheme implementation for the Java platform: a Lisp REPL on the JVM that also compiles to bytecode and works with Java classes.

Kawa is a general-purpose programming language that runs on the Java platform. It is an extension of Scheme, a long-established member of the Lisp family. You can type Scheme into a REPL, run it as a script, or compile it, and it all runs on the JVM.

The manual states the aim directly: combine the benefits of dynamic scripting languages (non-verbose code, fast and easy startup, a REPL, no required compilation step) with those of traditional compiled languages (fast execution, static error detection, modularity, zero-overhead Java platform integration). Whether it fully gets there is for you to judge, but the goal explains why it exists.

The idea underneath is that a language can be a thin, flexible layer over a big runtime. The manual also calls Kawa "a useful framework for implementing other programming languages on the Java platform", with many utility classes. That makes it a door into how languages get built on the JVM, not only a place to write Scheme.

The project says it has nothing to do with the defunct Kawa commercial Java IDE, so ignore older search results about that.

## Install

```
brew install kawa
# depends on openjdk, which brew installs as a dependency
```

## Try this

```
kawa --help
```
Prints the command-line options, a good first look at how Kawa runs interactively, runs scripts, or compiles.

## What's unique

It is Scheme that treats the Java platform as its home, and it is also pitched as a toolkit for building other JVM languages.

## Caveats

The manual describes version 3.1.1, updated January 2020, and I could not confirm recent maintenance; its own tutorial is called 'woefully incomplete'.

## Links

- [Kawa homepage (GNU)](https://www.gnu.org/software/kawa/)
- [Kawa manual and index (GNU)](https://www.gnu.org/software/kawa/index.html)
