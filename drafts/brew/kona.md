---
name: kona
title: Kona
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, apl, array-programming, interpreter, k, language]
homepage: https://github.com/kevinlawler/kona
scout_score: 7
status: draft
---

# Kona

**TLDR;** An open-source reimplementation of k3, a terse ASCII array language descended from APL and LISP, run as an interactive interpreter called k.

Kona is an interpreter for the k programming language, specifically k3, an older version from Kx Systems. Kx no longer distributes it, and the README says k3 has been unavailable for about 20 years. Kona exists to keep that version runnable. It is unaffiliated with Kx.

The README describes k as "a synthesis of APL and LISP." Like LISP, it is ASCII-based, so you don't need a special keyboard. Its fundamental data construct is the list, where APL uses multi-dimensional arrays. The README also positions k as the preferred APL dialect for people in finance and data-heavy analysis who care about performance.

The idea underneath is array programming at extreme density: whole operations on lists expressed in a few characters, with no loops in sight. That compression carries into the implementation. The C source deliberately imitates Arthur Whitney's terse style, and the README makes the point by setting his 11-line buddy memory allocator beside a conventional C version of roughly 750 lines.

You use it as a REPL. Run `k`, type expressions, and see what comes back. It is a quick way to get a feel for a language family that most developers never meet.

## Install

```
brew install kona
# Source build (macOS, Linux, BSD, Cygwin, Android): git clone https://github.com/kevinlawler/kona.git, cd kona, make (gmake on BSD; make OS=android for Android)
# Windows: download k.exe from the GitHub releases page
# Needs a C toolchain and make only for source builds; no accounts or runtimes.
```

## Try this

```
k
```
Starts an interactive Kona session where you can type k expressions and see results.

```
k --help
```
Prints the interpreter's command-line options.

## What's unique

It is a carefully scoped revival of a historical language that its original vendor no longer distributes, written in C that imitates Arthur Whitney's famously compressed style.

## Caveats

The README shows no release dates or maintenance note, so its current status is unclear; arrow keys may show as raw characters unless you wrap it with rlwrap, and Windows setup takes extra steps.

## Links

- [Homepage (GitHub repository)](https://github.com/kevinlawler/kona)
- [Project site](http://kona.github.io/)
- [Wiki](https://github.com/kevinlawler/kona/wiki)
- [Comparison of k incarnations](https://ngn.bitbucket.io/k.html)
