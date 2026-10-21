---
name: clangql
title: ClangQL
source: brew
category: take-things-apart
commitment: quick
tags: [ast, c, clang, cpp, quick, sql, static-analysis]
homepage: https://amrdeveloper.github.io/ClangQL/
scout_score: 6
status: draft
---

# ClangQL

**TLDR;** ClangQL lets you query C and C++ source files with SQL, treating functions and globals as tables you can filter, count and select from.

ClangQL is a command-line tool that runs SQL-like queries against C and C++ source instead of a database. You hand it source files with `-f`, a query with `-q`, or a script file with `-s`. Results come back as a table, JSON, or CSV, and it can paginate output or print a query analysis.

Under the hood it parses the files with Clang and exposes the syntax tree as tables, such as `functions` and `globals`. Columns include things like `name`, `source_loc`, `return_type` and `is_volatile`. The query itself is evaluated by the GitQL SDK, so ClangQL does not ship its own query engine. Its README describes it this way: "ClangQL is a tool that allow you to run SQL-like query on C/C++ Code instead of database files using the GitQL SDK."

The interesting part is the idea underneath. Code is already structured data, and an AST is just a set of rows nobody usually gets to filter. Once functions are a table, questions like "which functions return int" or "which globals are volatile" become one-line queries. For declaration properties there are matcher functions such as `m_constructor()` and `m_pure_virtual()`, which you combine with `&&` and `||` inside `m_function(...)`. Keywords are case-insensitive, as in SQL, and plain expressions like `SELECT 1 + 2` work too.

## Install

```
brew install clangql
# Cargo or source builds need LibClang 17 installed first: cargo install clangql
```

## Try this

```
clangql --help
```
Lists the options: -f for files, -q for a query, -s for a script, plus output format and page size.

```
SELECT DISTINCT name AS function_name FROM functions
```
Run this as the query (via -q) against files given with -f to list each distinct function name under an alias.

```
SELECT name, source_loc FROM functions WHERE m_function(ast_function, m_pure_virtual());
```
Finds pure virtual functions and shows where each one is declared.

## What's unique

It points a SQL-style language at a C/C++ syntax tree, with matcher predicates like m_pure_virtual() for declaration properties, and borrows the GitQL engine instead of building its own.

## Caveats

The homepage is an unfilled MkDocs placeholder, the README is the only real documentation, and maintenance status could not be confirmed.

## Links

- [Homepage (MkDocs placeholder page)](https://amrdeveloper.github.io/ClangQL/)
- [GitHub repository and README](https://github.com/amrdeveloper/ClangQL)
