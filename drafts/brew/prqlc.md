---
name: prqlc
title: prqlc
source: brew
category: languages-and-oddities
commitment: quick
tags: [compiler, data, language, quick, rust, sql]
homepage: https://prql-lang.org
scout_score: 6
status: draft
---

# prqlc

**TLDR;** A compiler for PRQL, a pipelined query language where each line transforms the previous one, and the output is plain SQL for your database.

PRQL (Pipelined Relational Query Language, pronounced "Prequel") is a language for transforming data. You write a query as a top-to-bottom list of steps: from, filter, derive, group, aggregate, sort, take, join, select. `prqlc`, the Rust compiler and CLI, turns that pipeline into SQL for a chosen dialect. It can also format and annotate PRQL queries.

The idea underneath is that SQL's clause order (SELECT first, FROM second, WHERE and HAVING scattered around) does not match how people think about data. In PRQL, "each line of the query is a transformation of the previous line's result." The homepage example puts `filter` both before and after an aggregation, and the compiler works out which becomes WHERE and which becomes HAVING.

PRQL keeps SQL's declarative style but adds variables and functions. S-strings let you drop in raw SQL where PRQL has no equivalent. Because it compiles to SQL rather than replacing a database, it works with anything that speaks SQL. A header such as `prql target:sql.mssql` picks the dialect, for example producing TOP instead of LIMIT for SQL Server.

It was designed for analytical queries, with an emphasis on readability and development speed. Bindings exist for Python, JavaScript and R, and the homepage lists integrations such as a VS Code extension, a DuckDB extension and ClickHouse support.

## Install

```
brew install prqlc
```

## Try this

```
prqlc --help
```
Lists the compiler's subcommands, including the one that compiles PRQL text to SQL and the formatter.

## What's unique

Every query is a linear pipeline, so commenting out any one line still leaves a valid query, which the homepage pitches at analysts exploring data. It targets many SQL dialects instead of tying itself to one database.

## Caveats

The README says development has slowed while maintainers decide how to build a new resolver, and that PRQL still has bugs and missing features and suits fairly simple queries.

## Links

- [Homepage](https://prql-lang.org)
- [Playground (in-browser, compiles as you type)](https://prql-lang.org/playground)
- [PRQL Book (language docs)](https://prql-lang.org/book)
- [GitHub repo](https://github.com/PRQL/prql)
