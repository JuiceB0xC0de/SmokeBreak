---
name: joern
title: Joern
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, graph, jvm, reverse-engineering, scala, security, static-analysis]
homepage: https://joern.io/
scout_score: 6
status: draft
---

# Joern

**TLDR;** Joern turns source code, bytecode and binaries into a queryable code property graph, so you can hunt bugs by asking questions of a program.

Joern is an open-source platform for analyzing source code, bytecode, and binary executables. Language frontends (the `*2cpg` tools) parse the input and build a code property graph, or CPG. The graph layers syntax, control flow, data flow and call information into one structure, held in a custom graph database. The frontends tolerate missing build environments, so a snapshot that won't compile can still be analyzed.

You explore the graph through the `joern` interactive shell, or through a server mode with a REST API. Queries are written in a Scala-based query language. Joern also includes a taint-analysis engine that tracks attacker-controlled data statically, and queries can be packaged into scanners (`joern-scan`) and run in CI.

The README says it is developed "with the goal of providing a useful tool for vulnerability discovery and research in static program analysis." The homepage calls it "The Bug Hunter's Workbench" and says it helps uncover attack surface, sloppy coding practices, and variants of known vulnerabilities.

The idea underneath is that a program is a graph you can ask questions of, rather than text to grep. One graph model and one query language cover many languages, instead of a one-off AST script for each. It is a door into static analysis research, where linters stop and program-analysis ideas begin.

## Install

```
brew install joern
# Needs a JDK (the formula pulls in openjdk@25; upstream documents JDK 21). Docker images also exist: ghcr.io/joernio/joern:master
```

## Try this

```
joern
```
Starts the interactive shell; it prints a banner and 'Type `help` to begin' at the joern> prompt.

```
joern-scan --list-query-names
```
Prints all the built-in queries that the scanner can run.

```
joern --help
```
Lists the shell's command-line options, including server mode.

## What's unique

One graph model and one query language cover source, bytecode and binaries across many languages, and the frontends cope with code that won't build. The taint engine and CPG passes go well beyond what a linter does.

## Caveats

The homepage is out of date and maturity varies by language (C/C++ and Java are rated Very High, Ruby and C# Medium-Low), and queries are written in Scala on a heavy JVM stack.

## Links

- [Homepage](https://joern.io/)
- [Documentation](https://docs.joern.io/)
- [CPG specification](https://cpg.joern.io)
- [GitHub repository](https://github.com/joernio/joern)
