---
name: planck
title: Planck
source: brew
category: languages-and-oddities
commitment: quick
tags: [clojurescript, deprecated, javascriptcore, quick, repl, scripting]
homepage: https://planck-repl.org/
scout_score: 5
status: draft
---

# Planck

**TLDR;** A ClojureScript REPL that starts instantly with no JVM, so Clojure-flavoured scripting works from the shell like a quick scripting language.

Planck is a stand-alone ClojureScript REPL for macOS and Linux, built on JavaScriptCore, the JavaScript engine from WebKit. You run `planck` (or `plk`) in a terminal, then type ClojureScript at the prompt or point it at a script file.

ClojureScript normally means a JVM-based toolchain compiling to JavaScript. Planck skips that at run time. It evaluates ClojureScript on JavaScriptCore directly, and supplies file and process access through ported namespaces: planck.core, planck.io and planck.shell, which cover a subset of clojure.core, clojure.java.io and clojure.java.shell. The README's example reads a file line by line and hands each line to the macOS `say` command.

The idea underneath is that a language usually run as a big compiled project can also be a small scripting tool, if the runtime starts fast. The project's own pitch is: "Planck launches instantly and is useful for scripting." The `plk` wrapper calls the `clojure` CLI so deps.edn and options like -Aalias still work, which keeps Clojure-style dependency handling available.

Homebrew lists the formula as deprecated. The README the brief draws on says nothing about that, so check the repository before relying on it.

## Install

```
brew install planck
# Ubuntu: sudo add-apt-repository ppa:mfikes/planck && sudo apt-get install planck
# Other Linux: prebuilt binaries at https://planck-repl.org/binaries/ or build from source
```

## Try this

```
planck -h
```
Prints the command-line options, a quick tour of what the REPL can do.

```
plk -h
```
Prints the options for the wrapper that hooks into the clojure CLI and deps.edn.

```
planck
```
Starts the REPL at a prompt, where you can type ClojureScript directly.

## What's unique

It is a ClojureScript REPL with no JVM and a fast start, aimed at shell-style scripting. The plk wrapper still lets deps.edn manage dependencies.

## Caveats

Homebrew marks it deprecated (the README does not say so), it supports only macOS and Linux, and its Clojure API coverage is a listed subset, not the full library.

## Links

- [Planck homepage](https://planck-repl.org/)
- [GitHub repository and README](https://github.com/planck-repl/planck)
- [API docs on cljdoc](https://cljdoc.org/d/planck/planck/CURRENT)
- [Prebuilt binaries](https://planck-repl.org/binaries/)
