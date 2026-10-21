---
name: srgn
title: srgn
source: brew
category: languages-and-oddities
commitment: quick
tags: [cli, grep, quick, refactoring, rust, tree-sitter]
homepage: https://github.com/alexpovel/srgn
scout_score: 5
status: draft
---

# srgn

**TLDR;** A grep-like tool that understands source code grammar, so you can search and rewrite only the docstrings, comments, or struct definitions you mean.

srgn is a Rust command-line tool that sits somewhere between grep, tr, and sed. You give it a scope: a regular expression, a language scope such as "comments in Python" or "pub enums in Rust", or both. With no action it prints the matches. With an action it transforms them: replace, delete, squeeze repeats, change case, or swap ASCII arrows for Unicode symbols.

The language scopes are built on tree-sitter, which parses source into a syntax tree. The README describes scopes as queries that work "much like pattern matching against a tree data structure". The language scope is applied first, and the regex runs only inside the pieces it selects. That is how you can ask for "the word `age` only inside Python class bodies" without writing a parser or a fragile multi-line regex.

The author's stated reason is that regexes and IDE tools like "Rename all" cannot reach some precise places in code. srgn is meant to complement them, with a design goal of simplicity: if you know regex and the basics of the language, you are good to go. Several scopes are AND-ed left to right, and `-j` runs them independently and joins the results.

One deliberate choice is that the replacement is a positional argument placed last, after `--`. A forgotten quote then cannot quietly turn the command into a recursive, destructive one. The underlying idea, matching on syntax trees instead of text, is a door into how modern code-aware tooling works.

## Install

```
brew install srgn
```

## Try this

```
echo 'Hello World!' | srgn '[wW]orld' -- 'there'
```
Plain regex replacement, like tr or sed: prints "Hello there!".

```
cat birds.py | srgn --python 'class' 'age'
```
Searches only inside Python class definitions, so `age` in function bodies is not matched.

```
cat money.py | srgn --python 'function-calls' '^print$' -- 'logging.info'
```
Rewrites calls to print as logging.info, leaving names like print_more alone.

## What's unique

It puts a tree-sitter grammar scope in front of a regex, so the pattern only runs inside the syntax elements you pick. Its fixed `--` replacement slot guards against destructive typos.

## Caveats

The README calls it beta, so only run it on files you can restore with git, and only seven languages are supported.

## Links

- [GitHub repository (homepage)](https://github.com/alexpovel/srgn)
- [GitHub releases](https://github.com/alexpovel/srgn/releases)
- [Homebrew formula](https://formulae.brew.sh/formula/srgn)
