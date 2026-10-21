---
name: gql
title: GitQL
source: brew
category: languages-and-oddities
commitment: quick
tags: [git, query-language, quick, rust, sql]
homepage: https://amrdeveloper.github.io/GQL/
scout_score: 6
status: draft
---

# GitQL

**TLDR;** Write SQL-like queries against a git repository's commits, branches, tags and diffs, with no import step and no database file.

GitQL (the Homebrew formula is `gql`, the executable is `gitql`) reads a local git repository and exposes it as tables: `commits`, `branches`, `tags`, `refs` and `diffs_changes`. You write a statement such as `SELECT author_name, COUNT(author_name) FROM commits GROUP BY author_name`, and it prints rows. Keywords are case-insensitive, as in SQL.

The homepage describes it as "a query language with a syntax very similar to SQL with a tiny engine to perform queries on .git files instead of database files." Nothing is converted or stored. The engine builds the tables from the repository on the fly and evaluates the query in memory.

The idea underneath is that a repository is already structured data, and `git log` flags are just one fixed set of questions about it. With SQL you can ask your own: which files change most often, who commits from a given email domain, which branches are short. The same engine is also packaged as an SDK for running SQL-like queries over any data source. The README lists sibling tools built on it for LLVM IR, C/C++ source, file systems and Python source.

## Install

```
brew install gql
```

## Try this

```
gitql --help
```
Prints the available options, so you can see how to point it at a repository and run a query.

```
SELECT author_name, COUNT(author_name) AS commit_num FROM commits GROUP BY author_name, author_email ORDER BY commit_num DESC LIMIT 10
```
Counts commits per author and lists the top ten authors by commit count.

```
SELECT path, count() AS changes_count, SUM(insertions) AS additions, SUM(removals) AS removes FROM diffs_changes GROUP BY path ORDER BY changes_count DESC
```
Ranks file paths by how often they changed, with total insertions and removals for each.

## What's unique

It treats the repository itself as a table store with no import step, and the engine behind it is reusable as an SDK for querying other kinds of data.

## Caveats

Release and last-commit dates were not confirmed, though the project looks active, and I did not verify which of the README's more advanced query features the released binary supports.

## Links

- [Homepage (GQL documentation)](https://amrdeveloper.github.io/GQL/)
- [Install or Build](https://amrdeveloper.github.io/GQL/setup)
- [Tables reference](https://amrdeveloper.github.io/GQL/structure/tables)
- [GitHub repository](https://github.com/AmrDeveloper/GQL)
