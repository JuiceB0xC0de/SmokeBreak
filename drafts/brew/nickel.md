---
name: nickel
title: Nickel
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, configuration, functional, language, nix]
homepage: https://nickel-lang.org/
scout_score: 6
status: draft
---

# Nickel

**TLDR;** A small lazy configuration language that is essentially JSON with functions, merging, and contracts, and exports to JSON, YAML, or TOML.

Nickel is a language for generating static configuration files. You write records (JSON-style objects) and functions, merge pieces together, and run `nickel export` to get JSON, YAML, or TOML that some other system consumes. The README describes the core as "in essence JSON with functions."

It exists because templating config with string substitution gets painful as configs grow. The authors call it "configuration templating, but done right," and present it as an evolution of the Nix language that tries to fix some of Nix's limitations. It targets complex config for apps, machines, infrastructure, and build systems.

The idea underneath is the merge operator. When records are merged, it also combines metadata such as docs, defaults, and type contracts, so a configuration can be built from modular layers that each carry their own rules. Contracts act as schemas: you annotate data with type-like checks, and violations are caught at evaluation time.

Typing is opt-in. A sound gradual type system lets you statically check functions while using runtime contracts to validate data, so you only annotate what needs checking. The language is lazy, so only the parts of a configuration that are actually used get evaluated.

## Install

```
brew install nickel
# alternatives: nix run nixpkgs#nickel, or build from source with Rust: cargo build -p nickel-lang-cli --release
```

## Try this

```
nickel eval <<< '["hello", "world"] |> std.string.join ", "'
```
Evaluates an expression from stdin and prints "hello, world".

```
nickel export --format json <<< '{content = "hello, world"}'
```
Turns a Nickel record into JSON output.

```
nickel repl
```
Starts an interactive session where you can try expressions; :help lists its commands.

## What's unique

It takes a middle path between Nix-style lazy functional power and schema-focused config languages, with optional typing and contracts. The README compares it against CUE, Dhall, Jsonnet, KCL, and Starlark, and it is designed to be embeddable in other languages.

## Caveats

The roadmap still lists unfinished work such as incremental evaluation, caching, a bytecode VM for performance, and custom merge functions, though the core language has been called stable since 1.0 in May 2023.

## Links

- [Nickel homepage](https://nickel-lang.org/)
- [GitHub repository (README)](https://github.com/tweag/nickel)
- [User manual](https://nickel-lang.org/user-manual/introduction)
