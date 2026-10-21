---
name: kimwitu++
title: Kimwitu++
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, c++, code-generation, compilers, term-rewriting]
homepage: https://savannah.nongnu.org/projects/kimwitu-pp
scout_score: 5
status: draft
---

# Kimwitu++

**TLDR;** A tree-processing generator from the compiler-toolkit era: describe a syntax tree and rewrite rules in a small language, get C++ classes back.

Kimwitu++ is a meta tool for processing trees, which it calls terms. You write an input file that defines a tree structure and the functions that work on it. Kimwitu++ turns that into a set of C++ files, which you compile and link into your own program. It is the successor to Kimwitu, and it is released under GPL v2 or later.

The intended home is compiler building. A parser, for example one made with lex and yacc, handles the grammar. Kimwitu++ takes over from there and builds the abstract syntax tree that later passes walk over. Each node type becomes a C++ class, and you can extend those classes with your own methods and embed C++ code directly in the rules.

Two mechanisms process the tree. Unparse rules are for code generation. Rewrite rules are for transformations. Both are written as pattern matches on node structure, and they are applied recursively over the tree. Views let different rules apply to the same kind of node in different contexts, so one tree can be printed several ways or transformed in separate passes.

The idea underneath is term rewriting: treat a program as a tree and express each compiler pass as patterns over that tree. It is the same idea behind pattern matching in modern functional languages, reached here through a code generator rather than a language feature. Reading about it is a way into how compilers were assembled before frameworks took over.

## Install

```
brew install kimwitu++
You also need a C++ compiler, since the generated files are compiled and linked into a program. The brief lists no installed executables, so check what the formula puts on your path.
```

## Try this

## What's unique

It is a generator, not a library: a small input language describes the tree and its pattern-matched rules, and C++ classes come out. It belongs to the lex and yacc lineage of compiler toolkits.

## Caveats

The most recent news on the project page is from 2008, the brief found no usage examples or documentation, and the formula lists no executables, so expect to read the manual from the download area.

## Links

- [Savannah project homepage](https://savannah.nongnu.org/projects/kimwitu-pp)
