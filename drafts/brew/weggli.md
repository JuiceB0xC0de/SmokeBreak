---
name: weggli
title: weggli
source: brew
category: take-things-apart
commitment: quick
tags: [c, code-search, cpp, quick, rust, security, tree-sitter]
homepage: https://github.com/weggli-rs/weggli
scout_score: 6
status: draft
---

# weggli

**TLDR;** A grep for C and C++ that matches code by structure, not text, so you can search for patterns like a memcpy into a stack buffer.

weggli is a command-line search tool for C and C++ source. You write a query in a C-like pattern language, point it at a file or directory, and it prints the snippets whose syntax tree matches. It finds code by shape, so spacing, line breaks and variable names do not get in the way the way they do with plain grep.

It was built to help security researchers find interesting functionality in large codebases. The README names Semgrep, Coccinelle, joern and CodeQL as inspirations and says it makes different choices: first-class C++ support, minimal setup, interactive speed, and greedy matching. It works on incomplete code and does not need the project to build.

Underneath, it uses the tree-sitter parser library and its C and C++ grammars. The query is parsed with an extended grammar, turned into a set of tree-sitter queries, and run against the parsed source. The query language looks like C with a few additions: `_` is a wildcard for any AST node, `$var` binds an identifier so it can be reused within the query, and `not:` and `strict:` modify matching.

The door it opens is treating source code as a tree you can query. Once you write a pattern like "a buffer declared, then copied into", you start to see how bug classes are really shapes in a syntax tree. As the README puts it, matching is greedy: "While this increases the risk of false positives it simplifies query creation." For example, `$x = 10;` matches both assignments and declarations.

## Install

```
brew install weggli
# alternative from the README: cargo install weggli (needs a Rust toolchain)
```

## Try this

```
weggli '{
    _ $buf[_];
    memcpy($buf,_,_);
}' ./target/src
```
Finds calls to memcpy that write into a stack buffer, the README's first example.

```
weggli -R 'func=^mem' '$func(_);'
```
Finds calls to functions whose names start with mem, using a regex to constrain the $func variable.

```
weggli -X 'DCHECK(_!=_.end());' ./target/src
```
Runs in C++ mode to find debug-only iterator validation.

## What's unique

Queries are written as C or C++ code rather than a separate rule language, and it runs fast enough for interactive use without needing the target project to build.

## Caveats

The README says it is not an official Google project and is unsupported. Greedy matching means false positives by design, and the README does not say how actively it is maintained.

## Links

- [GitHub homepage and README](https://github.com/weggli-rs/weggli)
- [tree-sitter](https://tree-sitter.github.io/tree-sitter/)
- [CONTRIBUTING.md](https://github.com/weggli-rs/weggli/blob/main/CONTRIBUTING.md)
