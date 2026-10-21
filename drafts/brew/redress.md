---
name: redress
title: redress
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binary-analysis, go, radare2, reverse-engineering]
homepage: https://github.com/goretk/redress
scout_score: 7
status: draft
---

# redress

**TLDR;** Redress rebuilds package names, types, and approximate source layout from stripped Go binaries, so you can read compiled Go programs and malware samples.

Redress is a command-line tool, written in Go, that reads a compiled Go binary and recovers what the build tried to remove. Stripping a binary deletes the usual symbol table, but Go embeds a lot of its own bookkeeping for the runtime. Redress pulls that data out and uses it to reconstruct symbols, packages, types, and a rough picture of the original source files. The README's phrase for this is that it tries to "re-dress" a "stripped" binary.

It has subcommands for different views: `info` for a summary of the build (OS, architecture, compiler version, main package path), `packages` for what was linked in, `types` for structs and interfaces with their methods, and `source` for a per-file list of functions with estimated line numbers. The README's examples run against a macOS malware sample called pplauncher, which makes the purpose concrete: you have a binary you did not write, and you want to know what is inside.

It also runs inside radare2 through r2pipe. The README says "The binary is aware of its environment and behaves accordingly." Inside an r2 session, `redress r2 init` creates flags for functions and methods, marks the type symbols, and analyzes main.init and main.main. Given the address of a type flag, it prints the Go struct definition for that type.

The larger idea is that a compiled language still carries a lot of metadata for its own runtime, and that metadata is a way back into the program. It is a good small door into reverse engineering.

## Install

```
brew install redress
# radare2 mode additionally needs radare2 and r2pipe installed
```

## Try this

```
redress -h
```
Lists the subcommands: info, packages, types, source, moduledata, gomod, r2, and others.

```
redress info <binary>
```
Prints OS, architecture, compiler version, build ID, GoRoot, main package path, and package counts for a Go binary.

```
redress source <binary>
```
Reconstructs the source layout: each file with its functions and estimated start and end lines.

## What's unique

The same binary runs standalone or as a radare2 plugin through r2pipe, turning recovered Go type information into flags and annotations inside the disassembler.

## Caveats

The README does not say which Go versions are supported, its examples come from a Go 1.10 macOS binary, and it calls some output, such as line numbers, an estimate.

## Links

- [redress on GitHub](https://github.com/goretk/redress)
