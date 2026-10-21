---
name: joker
title: Joker
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, clojure, formatter, go, linter, lisp, scripting]
homepage: https://joker-lang.org/
scout_score: 6
status: draft
---

# Joker

**TLDR;** A small Clojure dialect written in Go that starts fast, so you can script with it, and that doubles as a Clojure linter and formatter.

Joker is an interpreter for a dialect of Clojure, written in Go instead of running on the JVM. You can run `.joke` scripts, open a REPL, evaluate a single expression with `-e`, or pipe source in on stdin. The same binary also lints and formats Clojure and ClojureScript, and runs named functions from a `tasks.joke` file as a task runner.

The author wanted a Clojure-flavoured language that suits scripting, with lightweight, fast startup, which Clojure on the JVM does not give you. The README also puts weight on good error messages and stack traces, and states that Joker should be a dialect of Clojure, not just a language inspired by it. Performance is listed as a non-goal.

Under the hood it executes bytecode by default on a VM, documented in VM.md in the repo. The core namespaces are pre-built into the executable to speed up startup. The standard library covers JSON, HTTP, the filesystem, the OS and base64.

The linter reads and parses every form in a file and prints problems as file:line:column messages. A `.joker` config file, found by walking up the directory tree, tells it about your macros, ignored namespaces and rule toggles. That makes it a small, readable example of how a Lisp is implemented outside its home runtime, and of what a language has to drop to fit: no threads, no protocols, no records.

## Install

```
brew install candid82/brew/joker
# also: nix-env -i joker, or a binary from the GitHub releases page. No account needed.
```

## Try this

```
joker -e '(println "Hello, world!")'
```
Evaluates one expression, prints the greeting and exits, which shows the startup speed.

```
joker --lint test.clj
```
Lints a file. The README's example, `(let [a 1])`, produces a Parse warning about an empty let body.

```
joker --hashmap-threshold -1 -e "(pprint (read))"
```
Reads an EDN data structure from stdin and pretty-prints it.

## What's unique

It is a separate Clojure-dialect implementation in Go, not a wrapper around the JVM, and it ships a linter, formatter and task runner in one binary.

## Caveats

It is single-threaded and lacks many Clojure features such as protocols, records, transducers and sorted maps, and the brief could not confirm how actively it is maintained.

## Links

- [Homepage](https://joker-lang.org/)
- [GitHub repository (README source)](https://github.com/candid82/joker)
- [Standard library reference](https://candid82.github.io/joker/)
