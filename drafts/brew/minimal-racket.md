---
name: minimal-racket
title: Racket (minimal)
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, language-design, lisp, macros, racket, scheme]
homepage: https://racket-lang.org/
scout_score: 5
status: draft
---

# Racket (minimal)

**TLDR;** A Lisp-family language built for making new languages: define your own syntax with macros and have it compile down to ordinary Racket.

Racket is a general-purpose language in the Lisp/Scheme family. The homepage shows small programs in several dialects side by side: plain Racket with a GUI message box, Typed Racket, Scribble documents, and Datalog. This minimal Homebrew formula installs two executables, `racket` and `raco`. The homepage describes a standard library covering GUI, web servers, databases, and math, plus thousands of packages installed with a single command.

The idea underneath is stated plainly on the homepage: "Racket is a language for making languages, so that a programmer can write every module in a well-suited language." Instead of treating a language as something you only use, Racket treats it as something you build as a library. Macros rewrite custom syntax into Racket expressions or definitions, so a new construct looks like an ordinary function when a module exports it.

The surface syntax does not have to look like Lisp. Parsing packages can map other notation, such as commas and braces, onto a parenthesized language that compiles through the macro system. The homepage says DrRacket's IDE features, such as go-to-definition arrows, can extend to languages built this way.

The homepage also claims Racket is the first language to support higher-order software contracts and safe gradual typing. That claim is the project's own and was not checked here. It does point at Typed Racket, which is a good place to see the language-building idea at work.

## Install

```
brew install minimal-racket

This is the minimal distribution and does not include the DrRacket IDE. To add it: raco pkg install --auto drracket
The full distribution is available as a cask: brew install --cask racket
```

## Try this

```
racket --help
```
Lists the options of the main executable, including how to run a file or start the interactive prompt.

```
raco --help
```
Lists the subcommands of raco, the tool for managing packages, compiling, and testing.

## What's unique

Racket makes writing a new language a normal, supported activity rather than a compiler project. Macros, modules, and tooling are designed so a new language can plug into the same system.

## Caveats

The homepage carried a banner reading "Important notice: Racket infrastructure compromise" with no details in the fetched text, so read it before installing; the minimal build also leaves out DrRacket and the GUI tooling.

## Links

- [Racket homepage](https://racket-lang.org/)
