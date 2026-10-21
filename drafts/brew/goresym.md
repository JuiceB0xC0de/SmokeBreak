---
name: goresym
title: GoReSym
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binary, go, reverse-engineering, symbols]
homepage: https://github.com/mandiant/GoReSym
scout_score: 7
status: draft
---

# GoReSym

**TLDR;** Reads a compiled Go binary, even a stripped one, and prints its function names, source paths, and types as JSON by pulling them out of Go's own runtime metadata.

GoReSym is a command-line parser from Mandiant for compiled Go programs. Point it at an ELF, Mach-O or PE file and it reports the CPU architecture, OS, endianness and compiler version. It also lists functions with start and end addresses, names and source locations, file and line-number data, and the type and interface structures embedded in the binary. Output is JSON by default, or a flat text listing with `-human`.

It exists because reverse engineers lose a lot when a Go binary is stripped or packed with something like UPX. The usual symbol table is gone. But every Go binary carries its own runtime metadata, because the runtime needs it for stack traces and reflection. GoReSym reads that instead of the symbol table.

Under the hood it extends the Go toolchain's own `debug/gosym` and runtime code. It locates the pclntab and moduledata structures even when section layout is unusual, can scan for the pclntab by a signature near `runtime_modulesinit`, and can repair a modified pclntab magic. Type recovery walks the typelinks from the moduledata table.

The idea underneath is that a compiled program still describes itself. Go has to keep enough of a map of its own code to run, and stripping the obvious names does not remove that map. Reading it is a good way into how a language runtime lays out its internals. The README also describes an optional IDAPython script that feeds the JSON into IDA Pro to set symbols and labels.

## Install

```
brew install goresym
# Alternatively, pre-built linux, macos and windows binaries are on the GitHub Releases tab, or build from source with `go build` and a recent Go compiler. No accounts or extra runtimes needed. You need a compiled Go binary to point it at.
```

## Try this

```
goresym --help
```
Lists the available flags so you can see what the tool can extract.

```
goresym -t -d -p /path/to/input.exe
```
Recovers type names (-t), includes standard Go package names alongside user packages (-d), and prints file paths embedded in the pclntab (-p), as JSON.

## What's unique

Most symbol tools depend on intact symbol tables. GoReSym reads the Go runtime's own metadata, so it still works on stripped binaries, UPX-mangled files and binaries with split data sections.

## Caveats

Type parsing needs the Go version detected correctly; on some stripped binaries you must pass -v with the version string, and a wrong one makes type parsing fail, and types cannot be extracted from Go versions before 1.5.

## Links

- [GitHub repository (homepage)](https://github.com/mandiant/GoReSym)
- [Mandiant blog: Golang internals symbol recovery](https://www.mandiant.com/resources/blog/golang-internals-symbol-recovery)
- [IDAPython rename script](https://github.com/mandiant/GoReSym/blob/master/IDAPython/goresym_rename.py)
