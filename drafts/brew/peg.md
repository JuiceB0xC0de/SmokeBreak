---
name: peg
title: peg and leg
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c, code-generator, grammar, parsing, peg]
homepage: https://www.piumarta.com/software/peg/
scout_score: 6
status: draft
---

# peg and leg

**TLDR;** Two small tools that turn a parsing expression grammar into a C recursive-descent parser, with backtracking and ordered choice instead of lex and yacc.

peg and leg read a Parsing Expression Grammar from files or standard input and write C source for a parser. The generated file defines `yyparse()`, which returns non-zero when the input matches the grammar and zero when it does not. peg reads Ford-style PEG syntax. leg reads a variant with lex/yacc-style conventions. Rules can carry C actions that run after a successful match, with the matched text available as `yytext`.

The author presents leg as an attractive replacement for lex and yacc. In the manual's words: "Unlike lex and yacc, peg and leg support unlimited backtracking, provide ordered choice as a means for disambiguation, and can combine scanning (lexical analysis) and parsing (syntactic analysis) into a single activity."

The idea underneath is the PEG itself. A grammar is a set of named rules matched left to right, descending into sub-rules and backtracking on failure, so the parser does a depth-first search for the first path that succeeds. Choice is ordered, so there is no ambiguity to resolve. Predicates (`&` and `!`) are tested during the search, while actions run only after a complete match, in left-to-right order along the successful path.

The output is plain C with a `yy`/`YY` prefix on external symbols, which the manual says avoids namespace pollution. The generated parser needs no runtime and carries no license obligation. peg itself is MIT licensed.

## Install

```
brew install peg
# installs two executables: peg and leg. Building a parser from the output needs a C compiler.
```

## Try this

```
peg -o username.c username.peg
```
Reads the grammar in username.peg and writes a C parser to username.c, as in the manual's simple example.

```
peg --help
```
Prints the options. The manual's synopsis lists -h, -o, -P, -v and -V.

```
man peg
```
Opens the manual, which covers the grammar syntax, actions, and a candid BUGS section. It also covers leg.

## What's unique

It is a compact, old-school PEG-to-C generator that sits outside the modern PEG toolchains. Its leg dialect is meant as a conceptual drop-in for lex and yacc, and its quirks are documented openly.

## Caveats

Release activity is quiet (stable 0.1.19 from 2023-03-06), left recursion is not handled correctly, a grammar that accepts empty input loops forever, and output targets C only.

## Links

- [Project homepage (peg/leg)](https://www.piumarta.com/software/peg/)
- [Manual page (peg.1.html)](https://www.piumarta.com/software/peg/peg.1.html)
