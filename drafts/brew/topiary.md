---
name: topiary
title: Topiary
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, formatter, language-tools, parsing, rust, tree-sitter]
homepage: https://topiary.tweag.io/
scout_score: 6
status: draft
---

# Topiary

**TLDR;** A code formatter engine from Tweag, built on Tree-sitter, where a language's style is written in a small DSL instead of a hand-built formatter.

Topiary is a uniform formatter for what its README calls "simple languages", written in Rust by Tweag. It sits on top of Tree-sitter, the incremental parsing library with grammars for a large number of languages. Instead of writing a parser and a formatting engine for each language, a formatter author describes the style in a simple DSL and Topiary's engine applies it.

The problem it aims at is familiar: personal style preferences that eat review time. The README's pitch is that "Authors can create a formatter for a language without having to write their own formatting engine or even their own parser." The one precondition is that a Tree-sitter grammar already exists for the language.

The idea underneath is that formatting can be treated as data rather than code. The listed design goals are idempotency ("formatting of already-formatted code doesn't change anything"), respecting the author's line-spanning choices, and keeping diffs local to the lines that changed. Reading how those goals shape the engine is a good way into how formatters work. There is also an in-browser playground on the homepage, so you can try it before installing anything.

## Install

```
brew install topiary
# The brief found no install steps in the README or homepage; the Topiary Book is the place to check usage and setup.
```

## Try this

```
topiary --help
```
Lists the subcommands and options, which is the safest way to see what the tool can do.

## What's unique

Most formatters ship their own parser and engine per language. Topiary keeps one engine and moves each language's style into a small DSL over an existing Tree-sitter grammar.

## Caveats

It is aimed at simple languages, not complex ones. I could not confirm the supported language list or recent release activity from the pages I read.

## Links

- [Homepage](https://topiary.tweag.io/)
- [Topiary Book](https://topiary.tweag.io/book/index.html)
- [Playground](https://topiary.tweag.io/playground)
- [GitHub repository](https://github.com/tweag/topiary)
