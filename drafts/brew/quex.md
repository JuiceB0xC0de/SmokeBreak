---
name: quex
title: Quex
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, code-generation, compilers, lexer, unicode]
homepage: https://quex.sourceforge.net/
scout_score: 5
status: draft
---

# Quex

**TLDR;** Quex generates lexical analyzers from pattern definitions, producing directly coded code instead of lookup tables, with Unicode queries and state graph drawing built in.

A lexical analyzer, or lexer, is the first stage of a compiler or parser. It reads a stream of characters and groups them into tokens, which the Quex homepage calls the 'atomic chunks of meaning'. Quex takes pattern definitions, which the homepage describes as regular expressions, plus mode and token definitions, and generates the analyzer for you.

The notable design choice is that the generated engines are directly coded rather than table based. The homepage lists modes that can be inherited and switched by transitions, and buffer handling that supports seek and tell on character indices even for variable-width encodings such as UTF-8 and UTF-16. It also mentions path and template compression to keep the generated code small.

The homepage also lists a few unusual extras. The command line can answer Unicode property and regular expression queries, and it can draw state transition graphs of the generated engines, which makes it a way to look at how a regular expression turns into a state machine. Indentation-based tokens (INDENT, DEDENT, NODENT), include stacks, and fuzzy matching with edit distance operators such as Levenshtein are also described as built in.

The homepage gives no origin story, so why it was built is not stated. It is a way into compiler construction: once you see a pattern become a state machine, parsers and language tooling make more sense.

## Install

```
brew install quex
```

## Try this

```
quex --help
```
Prints the command line options, the starting point since the homepage shows no usage examples.

## What's unique

It generates directly coded analyzers rather than table-driven ones, and it builds in fuzzy matching, indentation tokens, and Unicode property queries. It is also MIT licensed, which the brief calls unusual in this niche.

## Caveats

The homepage shows no release date or version, so project activity is unknown, and the target languages of the generated code were not confirmed.

## Links

- [Homepage](https://quex.sourceforge.net/)
