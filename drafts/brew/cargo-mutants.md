---
name: cargo-mutants
title: cargo-mutants
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cargo, mutation-testing, rust, testing]
homepage: https://mutants.rs/
scout_score: 5
status: draft
---

# cargo-mutants

**TLDR;** Breaks your Rust code on purpose, one small change at a time, and reports which breakages your tests never noticed.

cargo-mutants is a mutation testing tool for Rust. It reads a source tree, automatically makes small changes that act like inserted bugs (the mutants), and runs your tests against each one. The output is a list of bugs the tests failed to catch, which marks the places where the tests may not check much.

The idea underneath is a gap in coverage numbers. In the README's words: "Coverage measurements can be helpful, but they really tell you what code is _reached_ by a test, and not whether the test really _checks_ anything about the behavior of the code." A line can run during a test and still be unverified. Mutation testing asks a different question: if this code were wrong, would anything fail?

You run it as a Cargo subcommand from inside a Rust project, and you can narrow it to a single file. It needs a tree whose non-flaky tests run under `cargo test` or `cargo nextest run`. The README says the goal is to be easy to run on any Rust tree and to tell you something interesting, not just produce a number. The README links a guide for running it incrementally on pull requests in CI.

The README does not go deep on internals. The author's design notes and the user guide at mutants.rs are where to look next.

## Install

```
cargo install --locked cargo-mutants
# needs a Rust toolchain; the README also mentions cargo-binstall and prebuilt binaries on GitHub releases
# Homebrew users: brew install cargo-mutants
```

## Try this

```
cargo mutants
```
Run from inside a Rust source directory, it generates mutants and runs your tests against each one, then reports the ones that survived.

```
cargo mutants -f src/something.rs
```
Limits mutation to one file, which keeps a first run short and the results readable.

```
cargo-mutants --help
```
Lists the available options.

## What's unique

It inverts the usual testing question. Instead of asking whether code is covered, it deliberately breaks the code and asks whether any test notices.

## Caveats

Rust only, and it needs non-flaky tests under cargo test or cargo nextest; it is a semi-actively-maintained spare-time project, and some noise from false positives is expected.

## Links

- [Homepage / user guide (mutants.rs)](https://mutants.rs/)
- [GitHub repository](https://github.com/sourcefrog/cargo-mutants)
- [Comparison with other tools (GitHub wiki)](https://github.com/sourcefrog/cargo-mutants/wiki/Compared)
