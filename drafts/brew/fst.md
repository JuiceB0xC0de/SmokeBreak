---
name: fst
title: fst
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, automata, data-structures, library, rust, search]
homepage: https://github.com/BurntSushi/fst
scout_score: 5
status: draft
---

# fst

**TLDR;** A Rust library that stores huge sorted sets and maps as compact finite state machines you can search directly, including typo-tolerant queries.

fst is a Rust crate, not a standalone program. You give it keys, usually already sorted, and it builds a finite state transducer: a small automaton in which each key is a path through the machine and each value is emitted as output along the transitions. The result is an ordered set or map that supports exact lookups, prefix and range queries, and can be memory-mapped from disk.

The compactness comes from sharing. Common prefixes and suffixes between keys are stored once, so a large pile of similar strings takes far less space than it would in a hash table or a tree of strings. The README frames this as a way to index very large key collections while keeping them easy to search, and points to the author's blog post, "Index 1,600,000,000 Keys with Automata and Rust", for the background and experiments.

The idea underneath is that a search can itself be an automaton. Run a Levenshtein automaton over the transducer and you get every key within a given number of edits of a query. The README's example asks a set of short words for everything within one edit of "foo". The same structure answers exact, range and fuzzy questions, which makes it a good way into automata theory and into how search indexes are built.

## Install

```
brew install fst
# Note: the README documents only a library. To use it, add `fst = "0.4"` under [dependencies] in Cargo.toml (needs a Rust toolchain and Cargo).
# Fuzzy search needs the `levenshtein` cargo feature, which is off by default.
```

## Try this

```
fst --help
```
Shows what the brew-installed executable offers, if anything. The README does not describe a command-line tool, so check this first.

## What's unique

Sorted keys become a compact, searchable automaton rather than a hash or tree, so one structure serves exact lookup, range queries and typo-tolerant search.

## Caveats

This is a library for Rust projects; the README shows no shell commands and never mentions the `fst` executable the brew formula lists, and the fuzzy search needs a feature flag.

## Links

- [GitHub repository (homepage)](https://github.com/BurntSushi/fst)
- [Author's blog post: Index 1,600,000,000 Keys with Automata and Rust](https://blog.burntsushi.net/transducers/)
- [API documentation on docs.rs](https://docs.rs/fst)
- [crates.io package](https://crates.io/crates/fst)
