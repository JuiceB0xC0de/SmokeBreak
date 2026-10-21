---
name: beancount
title: Beancount
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [accounting, afternoon, language, plain-text, python]
homepage: https://beancount.github.io/
scout_score: 6
status: draft
---

# Beancount

**TLDR;** A double-entry bookkeeping language: you write your finances as plain text, and it parses and checks them like a compiler would.

Beancount treats a personal ledger as source code. You write transactions in a text file, and Beancount reads the file into memory as a list of directives. Reports and a web interface are generated from that parsed data. The docs also describe scripts and plugins that load the directives and transform them.

The author, Martin Blais, says he built it to do his own accounting first, "in the simplest, most durable manner", and polished it later so others could use it. Because the ledger is just text, you can edit it in any editor and keep its history in git, and it is not locked inside a spreadsheet or a database.

The idea underneath is double-entry bookkeeping, where every transaction moves value between accounts and everything has to balance. Once that rule is written down as a language, a file of your finances can be checked for errors the way a program is. It is a small way into how accounting actually works.

The brew formula installs a handful of small tools: a checker, a formatter, a diagnostic tool, an example-ledger generator, and a tree-printing helper. The docs also mention bean-query, but it is not in the brew executable list. In v3, most of the tools that v2 shipped have moved to separate projects.

## Install

```
brew install beancount
```

## Try this

```
bean-example
```
Prints a sample ledger file, which is a quick way to see what the syntax looks like.

```
bean-check --help
```
Shows the options for the checker, which parses a ledger file and reports errors.

```
bean-format --help
```
Shows the options for the formatter, which tidies the alignment of a ledger file.

## What's unique

It is a real parsed language with its own syntax rather than a spreadsheet or database, and your ledger stays plain text you can version. The author also writes the docs in Google Docs and mirrors them to Markdown.

## Caveats

Version 3 is the current stable release, v2 is obsolete, and many v2 tools now live in separate projects, so older tutorials may not match what you install.

## Links

- [Homepage](https://beancount.github.io/)
- [GitHub repository (README)](https://github.com/beancount/beancount/)
- [User documentation (Markdown mirror)](https://beancount.github.io/docs/)
- [Installation instructions](http://furius.ca/beancount/doc/install)
