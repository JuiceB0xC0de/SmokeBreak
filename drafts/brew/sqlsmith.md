---
name: sqlsmith
title: SQLsmith
source: brew
category: take-things-apart
commitment: quick
tags: [databases, fuzzing, postgresql, quick, sql, sqlite, testing]
homepage: https://github.com/anse1/sqlsmith
scout_score: 7
status: draft
---

# SQLsmith

**TLDR;** A random SQL generator that reads a database's schema, fires nonsense-but-valid queries at it, and reports which ones crash the server.

SQLsmith is a C++ command-line fuzzer for database engines. It connects to a target (PostgreSQL, SQLite 3, or MonetDB), reads the schema, builds random query syntax trees from a grammar, and sends them to the server. Each statement is rolled back, and the tool prints the outcome of every query as it goes.

The README names Csmith as its paragon, the random program generator that proved valuable for quality assurance in C compilers. The same idea applies here: instead of writing tests by hand, generate huge numbers of odd but legal inputs and watch for crashes. It is aimed at database developers, and at extension authors who want their code hit with a random workload.

Verbose output shows one symbol per query. `.ok` means the query ran, `t` is a timeout, and `C` is a broken connection, which usually means a query took the server down. `S` is a syntax error, which the README says points to a bug in SQLsmith itself. Productions that keep producing errors are blacklisted over time, so a new target gives a burst of errors at startup that then tapers off.

The project keeps a public score list of 118 bugs found since 2015 in alphas, betas, and releases of the supported products, including some security vulnerabilities, plus bugs in extensions and libraries such as orafce and glibc. To support another database, you implement two classes: one for schema information and one for connectivity.

## Install

```
brew install sqlsmith
# You also need a target database. The README says to connect as a suitably underprivileged database user, since generated queries can call functions with side effects.
```

## Try this

```
sqlsmith --verbose --sqlite="file:$HOME/.mozilla/firefox/places.sqlite?mode=ro"
```
Fuzzes a SQLite database opened read-only (the README's example uses a Firefox history file) and prints one status symbol per query.

```
sqlsmith --verbose --target="host=/tmp port=65432 dbname=regression"
```
Runs against a PostgreSQL database, with progress on stderr. Use a throwaway server.

```
sqlsmith --help
```
Lists the available options and target types.

## What's unique

It turns the Csmith idea of fuzzing compilers into fuzzing databases, and it comes with a public list of real bugs it has found in engines people trust.

## Caveats

The README warns: "Use it at your own risk. It may damage your database." It supports only PostgreSQL, SQLite 3, and MonetDB out of the box, and the brief could not confirm recent project activity.

## Links

- [GitHub repository and README](https://github.com/anse1/sqlsmith)
- [Score list of bugs found](https://github.com/anse1/sqlsmith/wiki#score-list)
