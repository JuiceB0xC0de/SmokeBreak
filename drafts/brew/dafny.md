---
name: dafny
title: Dafny
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, formal-methods, language, math, verification]
homepage: https://github.com/dafny-lang/dafny/blob/master/README.md
scout_score: 7
status: draft
---

# Dafny

**TLDR;** A programming language where you write specifications beside your code and a built-in verifier proves the code meets them, then compiles to C#, Go, Python, Java, or JavaScript.

Dafny is a language with a static verifier built in. You write ordinary code, and alongside it you write what the code is supposed to do: preconditions, postconditions, loop invariants, termination conditions. All of it is in Dafny itself. The verifier then checks that the implementation satisfies the specification, and reports errors or counterexamples where it cannot.

The verifier runs continuously while you edit, much like a language server checking a file. In the project's words, "Dafny's verifier constantly looks over your shoulder, flags any errors, shows you counterexamples, and congratulates you when your code matches your specifications." The proof obligations sit next to the code they are about.

The idea underneath is that testing shows a program works on the inputs you tried, while verification argues it works on all inputs allowed by the specification. The README frames the goal as reducing costly late-stage bugs that testing tends to miss. Once the code verifies, Dafny compiles it to C#, Go, Python, Java, or JavaScript, so verified pieces can fit into an existing toolchain.

Its design draws on Euclid, Eiffel, CLU, ML, and Coq/VeriFast, which makes it an unusually practical door into formal methods. Expect to spend your first hour learning to write specifications, not code.

## Install

```
brew install dafny
# pulls in dotnet@8 and z3 as dependencies. The README also suggests the Dafny extension for Visual Studio Code to get live verification in the editor.
```

## Try this

```
dafny --help
```
Lists the command-line subcommands and options, a starting point for verifying and compiling a file.

## What's unique

Verification is part of the language rather than a separate tool, with live feedback in the editor and output that compiles to mainstream languages.

## Caveats

Verification has a real learning curve, and the README points to a tutorial and course lectures rather than a quick start.

## Links

- [Project homepage (README on GitHub)](https://github.com/dafny-lang/dafny/blob/master/README.md)
- [Official site](https://dafny.org)
