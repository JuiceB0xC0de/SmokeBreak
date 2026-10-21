---
name: lisette
title: Lisette
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, go, language, rust, transpiler]
homepage: https://lisette.run
scout_score: 5
status: draft
---

# Lisette

**TLDR;** A small Rust-flavoured language that compiles to readable Go, adding pattern matching, Option and Result, and a linter aimed at Go's footguns.

Lisette is a language with Rust-like syntax that turns `.lis` files into Go source. The `lis` compiler emits Go the README calls readable, so the result runs on Go's runtime and links against Go packages. On top of Go it adds algebraic data types, pattern matching, immutability by default, a `|>` pipeline operator, and try blocks. Option and Result take the place of nil and bare error returns.

The homepage calls it "A love letter to Go written in Rust". The idea is to keep Go's ecosystem and deployment story while borrowing the type-system habits people miss from Rust. Go packages come in with `import "go:..."`, and Go's standard library signatures are described in `.d.lis` declaration files. Attributes like `#[json(...)]` generate tagged Go structs.

The second half of the pitch is a compile-time checker for Go pitfalls. The homepage shows messages for an unchecked Result, a non-exhaustive match, a sort on an immutable binding, and a `defer` skipped by `os.Exit`. The README claims 500+ diagnostics, a figure not verified here.

The door it opens is transpiler design: what you gain and lose by targeting another language's source instead of building a new runtime. Reading the generated Go next to the Lisette source shows the mapping directly.

## Install

```
Install Go 1.26 or newer first. Then: brew install lisette
(Alternatives from the quickstart: mise use -g lisette, cargo install lisette, or the official curl install script.)
Editor support is a separate step: extensions for VSCode, Zed or JetBrains, or the language server via `lis lsp` for Neovim and Helix.
```

## Try this

```
lis --help
```
Lists the compiler's subcommands, a quick way to see what the toolchain offers.

```
lis add google/uuid
```
Adds a Go module dependency to a Lisette project and records it in lisette.toml.

```
lis lsp
```
Starts the language server, which is how editors like Helix get diagnostics and completion.

## What's unique

Most Go-targeting languages are new runtimes or thin wrappers. Lisette emits readable Go, imports Go packages directly, and ships a linter built around Go's common mistakes.

## Caveats

Requires Go 1.26 or newer, and the README gives no stability or production-readiness statement, so treat it as young.

## Links

- [Homepage](https://lisette.run)
- [Quickstart](https://lisette.run/docs/intro/quickstart/)
- [Language reference](https://lisette.run/docs/lexemes/)
- [GitHub repository](https://github.com/ivov/lisette)
