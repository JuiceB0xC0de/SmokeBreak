---
name: treecc
title: treecc
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, c, code-generation, compilers, dotgnu, yacc]
homepage: https://gnu.org/software/dotgnu/treecc/treecc.html
scout_score: 6
status: draft
---

# treecc

**TLDR;** A compiler-compiler from DotGNU that generates C tree-building and tree-walking code from a declarative spec, and errors if any node type lacks a case for an operation.

Treecc sits next to yacc. Yacc turns a grammar into a parser, then leaves you to write the tree code that does type checking, code generation and everything else after parsing. Treecc generates that tree layer. You write a spec listing node types, their fields and their abstract parents, then declare operations, such as type inference, with code for each node type. Embedded C supplies the details.

From the spec, treecc emits the node structures, a `*_create` constructor for each node, and the dispatch code for each operation. The yacc grammar's actions call those constructors, with parameters matching the node's fields in type and order. Abstract types such as `binary` let one case cover every subclass, and a more specific case, say for `power`, overrides the inherited one.

The manual's complaint is that in a hand-written tree, adding a node type means hunting down every walker that should handle it. The Visitor pattern makes adding node types painful. Treecc checks coverage at translation time instead. In the manual's words: "If it detects a lack, it will immediately raise an error to the user."

The idea underneath is that each operation is a cross-cutting concern, an aspect, woven across all node types, with the generator checking the whole grid for gaps. It is a small, concrete look at how compilers get structured, and at the expression problem.

## Install

```
brew install treecc
Needs a C compiler, and a yacc-style parser generator if you follow the manual's example.
```

## Try this

```
treecc --help
```
Prints the command-line usage, since the brief did not capture the manual's invocation section.

## What's unique

It applies aspect-oriented ideas to compiler trees and checks globally that every operation covers every node type. It stays declarative and yacc-like rather than inventing a whole new language.

## Caveats

The manual is dated 2009 and the project looks quiet; this entry is based on only the first two manual sections, so check the current command-line syntax yourself.

## Links

- [Homepage (treecc manual index)](https://gnu.org/software/dotgnu/treecc/treecc.html)
- [Manual section 1: Overview (rationale for treecc)](https://gnu.org/software/dotgnu/treecc/treecc_1.html)
- [Manual section 2: A simple example for expressions](https://gnu.org/software/dotgnu/treecc/treecc_2.html)
