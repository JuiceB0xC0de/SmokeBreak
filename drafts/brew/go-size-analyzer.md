---
name: go-size-analyzer
title: go-size-analyzer
source: brew
category: take-things-apart
commitment: quick
tags: [binary-analysis, go, quick, reverse-engineering, treemap, tui]
homepage: https://gsa.zxilly.dev/
scout_score: 5
status: draft
---

# go-size-analyzer

**TLDR;** gsa takes a compiled Go binary and shows which packages and sections take up its space, as a table, treemap, or terminal UI.

go-size-analyzer, run as `gsa`, reads a compiled Go executable (ELF, Mach-O, PE, and experimental WebAssembly) and attributes its bytes to packages and sections. The output can be a plain text table, JSON, HTML, or an SVG treemap. You can also explore it interactively in a local web UI or a terminal UI.

The README calls it "A simple tool to analyze the size of a Go compiled binary." Go binaries are statically linked and often surprisingly large, and the question of where the megabytes came from is hard to answer by looking at source code. This tool answers it from the finished artifact, not from the module list.

The README does not go deep on internals. It mentions disassembly, symbol, and DWARF passes, each of which can be skipped with `--no-disasm`, `--no-symbol`, or `--no-dwarf`. That is a small door into how a compiled binary keeps track of its own contents: symbol tables, debug info, and sections.

It can also diff two binaries, or two saved JSON results, and show which packages grew or shrank. That makes it a way to watch dependency bloat change between releases or Go versions.

## Install

```
brew install go-size-analyzer
# Windows: scoop install go-size-analyzer
# Or with Go: go install github.com/Zxilly/go-size-analyzer/cmd/gsa@latest
# You need a compiled Go binary to analyze. A browser version at gsa.zxilly.dev needs no install.
```

## Try this

```
gsa --tui golang-compiled-binary
```
Opens the terminal UI so you can browse package sizes interactively.

```
gsa bin-linux-1.21-amd64 bin-linux-1.22-amd64
```
Diff mode: shows old size, new size, and the difference for each package and section.

```
gsa cockroach-darwin-amd64 -f svg -o data.svg --hide-sections
```
Writes an SVG treemap of package sizes to data.svg, with sections hidden.

## What's unique

One binary covers text, JSON, HTML, SVG, a web treemap, a terminal UI, and a WebAssembly build that runs in the browser. It can also diff two builds.

## Caveats

Stripped binaries can be analyzed but may give inaccurate results, the WebAssembly version is about 10x slower and suits binaries under 30 MB, and the license is AGPL-3.0.

## Links

- [Homepage (WebAssembly treemap)](https://gsa.zxilly.dev/)
- [GitHub repository and README](https://github.com/Zxilly/go-size-analyzer)
- [Terminal UI demo (asciinema)](https://asciinema.org/a/1074190)
- [Development guide](https://github.com/Zxilly/go-size-analyzer/blob/master/DEVELOPMENT.md)
