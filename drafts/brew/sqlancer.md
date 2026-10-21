---
name: sqlancer
title: SQLancer
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, databases, fuzzing, java, science, testing]
homepage: https://github.com/sqlancer/sqlancer
scout_score: 7
status: draft
---

# SQLancer

**TLDR;** Fuzzes database engines like SQLite, DuckDB and PostgreSQL with generated queries, and uses clever oracles to catch cases where the database silently returns the wrong rows.

SQLancer is a Java command-line tool that tests database management systems for logic bugs: cases where the engine returns an incorrect result set, such as quietly dropping a row. It does not look at your queries. It looks for bugs in the DBMS implementation itself. The README says it has found hundreds of bugs in mature, widely used systems.

It works in phases. Hand-written generators create a schema, insert data, add indexes and views, then produce queries. Each query is checked by a test oracle. With TLP, a query is split into three partitions whose combined results must match the original. With NoREC, the query is compared against a rewrite that avoids the optimizer. Other oracles include PQS, DQP and CODDTest. There are also modes for performance issues (CERT) and crashes.

The idea underneath is metamorphic testing. You rarely know the correct answer to a random query, but you can know that two different formulations of it must agree. If they do not, one is wrong, and the log files contain the statements needed to reproduce it. Almost every oracle has a published paper behind it, and the README links to them, so the tool doubles as a reading list on how database correctness gets tested.

Optional extras include a feedback-guided mode (`--qpg-enable`) that mutates database state to reach new query plans, and an experimental reducer (`--use-reducer`) that shrinks bug-inducing inputs with delta debugging.

## Install

```
brew install sqlancer
# Needs Java (brew pulls in openjdk). The README's main route is instead: git clone the repo, then build with Maven (Java 11+ and Maven required).
# Embedded DBMSs (SQLite, DuckDB, H2) need nothing else. Others need a running server, and some expect a database named test.
```

## Try this

```
sqlancer --help
```
Lists the available options and general flags.

```
java -jar sqlancer-*.jar --num-threads 4 sqlite3 --oracle NoREC
```
Tests SQLite with the NoREC oracle on four threads, running until it finds a bug. General options like --num-threads go before the DBMS name.

```
java -jar sqlancer-*.jar --help
```
Prints the full option list from the built JAR.

## What's unique

Instead of looking for crashes or comparing against hand-written expected results, it uses metamorphic and differential oracles, so it can detect wrong answers with no known right answer. Nearly every oracle comes with an academic paper.

## Caveats

It targets specific DBMS versions, so newer releases can produce false alarms, and without a bug it runs forever unless you set --num-tries or --timeout-seconds.

## Links

- [GitHub repository (homepage)](https://github.com/sqlancer/sqlancer)
- [Video Guide](https://www.youtube.com/watch?v=lcZ6LixPH1Y)
- [Papers and .bib entries](https://github.com/sqlancer/sqlancer/blob/main/docs/PAPERS.md)
