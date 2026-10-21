---
name: cxgo
title: cxgo
source: brew
category: languages-and-oddities
commitment: quick
tags: [c, compilers, go, quick, transpiler]
homepage: https://gotranspile.dev
scout_score: 5
status: draft
---

# cxgo

**TLDR;** A C-to-Go source translator that parses C in pure Go and tries to emit readable, idiomatic Go rather than just code that compiles.

cxgo reads C source files, headers included, and writes Go. The README calls it a transpiler. The goals it lists are a practical C to Go translator, correct output, generated code that is "human-readable and as idiomatic as possible", and easy customization. C++ is out of scope for now.

It does not shell out to clang or gcc. It uses modernc.org/cc v3, a C preprocessor and parser written in Go, then runs its own type-checker and an AST translation layer to produce Go. The README says it "uses a few tricks" to ease the conversion, and a config doc covers options such as `identsflatten`, which is part of the workaround for `goto`, which Go forbids.

The idea underneath is that two languages with different memory models, type rules and control flow can be mapped onto each other mechanically, and the gaps show you what each language assumes. Unions must match C data layout, `setjmp` compiles but panics at runtime, and bitfields and packed structs are incomplete. The README says it has been used on real projects: Potrace, G722, PortableGL and Physac.

The homepage is a small web demo where you paste C and see a translation, so you can try it without installing anything.

## Install

```
go install github.com/gotranspile/cxgo/cmd/cxgo@latest
# needs the Go toolchain; no C compiler required. Prebuilt binaries are on the GitHub releases page. Homebrew is not mentioned in the README, so check `brew info cxgo` before relying on a formula.
```

## Try this

```
cxgo file main.c
```
Translates main.c, and its headers, into Go source. This is the README's fastest way to try it.

```
cxgo --help
```
Lists the available commands and flags.

## What's unique

It parses C with a pure-Go library instead of clang or gcc, and it aims for Go a human would want to keep editing.

## Caveats

The README calls it experimental, warns that bugs may change program behavior, and reports passing 62/89 TCC tests and 783/1236 GCC tests; comments are not preserved.

## Links

- [Homepage (web demo)](https://gotranspile.dev)
- [GitHub repository and README](https://github.com/gotranspile/cxgo)
- [Go package reference (pkg.go.dev)](https://pkg.go.dev/github.com/gotranspile/cxgo)
