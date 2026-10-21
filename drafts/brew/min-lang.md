---
name: min-lang
title: min
source: brew
category: languages-and-oddities
commitment: quick
tags: [concatenative, language, nim, quick, repl, stack]
homepage: https://min-lang.org
scout_score: 8
status: draft
---

# min

**TLDR;** A small concatenative language with a REPL, where programs are words and quoted blocks acting on a stack, shipped as one binary.

min is a functional, concatenative programming language. A program is a sequence of words that push values or quotations onto a stack, and other words consume them. There are few data types: integers, floats, strings, booleans, dictionaries, and quotations, which are parenthesised lists of code. The standard library is small and namespaced, with names like `sys.pwd`, `sys.ls-r` and `fs.mtime`.

The idea underneath is concatenative programming. There are no named arguments to thread around. Functions compose by being written next to each other, and combinators such as `filter` and `linrec` take quotations off the stack and run them. Because the language is homoiconic, a quotation is both code and a list you can inspect. Once that clicks, the stack stops feeling like a puzzle and starts to feel like a pipeline.

It is also meant for everyday scripting. The homepage's first example is a one-line file finder: list the current directory recursively and keep entries modified in the last hour. The REPL has auto-completion and history, so it works as a shell-like prompt, though the project describes it as a language rather than a Unix shell replacement.

The implementation is written in Nim and compiled statically into a single file. It can be embedded in other Nim programs. A sibling called mn is the even more bare-bones version for people who do not need everything min offers.

## Install

```
brew install min-lang
```

## Try this

```
min --help
```
Lists the options for running a file, evaluating code, or starting the REPL.

```
sys.pwd sys.ls-r (fs.mtime time.now 3600 - >) filter
```
Typed into the REPL, this recursively lists files in the current folder modified within the last hour. The homepage writes it across three lines.

```
5 (stack.dup 0 ==) (1 +) (stack.dup 1 -) (*) linrec
```
Computes the factorial of 5 using the linrec combinator, entered in the REPL.

## What's unique

It is a concatenative, homoiconic language that is also practical for file-and-shell tasks, with a REPL and a standard library, all in one self-contained binary.

## Caveats

The project moved from GitHub to sourcehut, where the latest commits are about four months old, so some links may be stale and the release cadence is unclear.

## Links

- [Homepage](https://min-lang.org)
- [Source on sourcehut (current repo)](https://git.sr.ht/~h3rald/min)
- [Old GitHub repo (now points to sourcehut)](https://github.com/h3rald/min)
