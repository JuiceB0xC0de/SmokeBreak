---
name: solod
title: Solod
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c, compilers, go, language, transpiler]
homepage: https://solod.dev/
scout_score: 5
status: draft
---

# Solod

**TLDR;** Solod is a strict subset of Go that transpiles to readable C11 with no runtime, no garbage collector and explicit heap allocation.

You write ordinary Go source, but import Solod's own packages (`solod.dev/so/...`) instead of the standard library. The `so` tool translates each package into a C header and implementation file, and can call the C compiler to build a binary. The README lists structs, methods, interfaces, slices, maps, multiple returns and defer, with limited generics.

The author's pitch is that Go developers get systems-level control without learning a new language, and C programmers get Go's structure and tooling. The homepage headline is "Solod: Go can be a better C". The output carries no garbage collector and no reference counting. Memory lives on the stack unless you ask for the heap through the standard library.

The generated C is meant to be read. The README's example shows a Go method becoming a plain C function that takes a void pointer and a named struct type, with nothing hidden behind a runtime library. That makes it a good way to see what Go constructs look like when you strip the runtime away. Concurrency is a thread pool and atomics in the standard library, not language keywords. Go tests stay ordinary Go and are never transpiled, so `go test` still works next to `so test`.

C interop needs no CGO, and a companion tool called sobind can generate bindings from C headers.

## Install

```
go install solod.dev/cmd/so@latest
# needs a Go toolchain and a C compiler (default `cc`, override with the CC environment variable)
# supported compilers: GCC, Clang, Emscripten, zig cc. MSVC is not supported.
# the Homebrew formula installs the same `so` executable: brew install solod
```

## Try this

```
so --help
```
Lists the subcommands of the `so` tool.

```
so translate -o generated .
```
Transpiles the Go module in the current directory to C and writes the header and source files into `generated`, where you can read them.

```
so run .
```
Transpiles, compiles and runs the module without keeping the binary. It takes a module, not a single file, so use `.` rather than `main.go`.

## What's unique

Most Go-to-something projects bring a runtime along. Solod emits plain C11 with zero runtime and makes heap allocation explicit, and the C is written to be read.

## Caveats

The homepage says "Solod isn't ready for production yet", the roadmap says no more releases are planned, generics are limited, and the generated C depends on GCC/Clang extensions.

## Links

- [Homepage](https://solod.dev/)
- [GitHub repository (README)](https://github.com/nalgeon/solod)
- [Playground (run code or view translated C)](https://codapi.org/so/)
- [Solod by example](https://github.com/solod-dev/example)
