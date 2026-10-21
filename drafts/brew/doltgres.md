---
name: doltgres
title: Doltgres
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, database, postgres, sql, version-control]
homepage: https://github.com/dolthub/doltgresql
scout_score: 6
status: draft
---

# Doltgres

**TLDR;** A Postgres-compatible database where tables are versioned like a Git repository, so you can commit, branch and merge your data using SQL.

Doltgres is a SQL server that speaks the Postgres wire protocol. You connect with psql or any Postgres client and create tables and rows as usual. The difference is that the data also has a history. You stage and commit changes, and you can branch, merge, fork, clone, push and pull the database the way you would a Git repository. The README puts it this way: "Git versions file, Doltgres versions tables. It's like Git and Postgres had a baby."

There is no Git-style command line for any of this. Version control is exposed through SQL: functions like `dolt_add` and `dolt_commit`, and system tables like `dolt.log` and `dolt.status`. Your commit history is something you query with `select`.

Under the hood, Doltgres emulates a Postgres server and parses Postgres SQL into an AST. That AST is converted into a form the Dolt engine can interpret. It shares the SQL engine and storage format of Dolt, the MySQL-flavored sibling from the same creators. The idea underneath is a database where history is a first-class part of the data rather than something bolted on with audit tables. That opens up questions about diffing, merging and reviewing changes to data, not just to code.

## Install

```
brew install doltgres
# You also need psql (from a Postgres install) as a client for the getting-started steps.
# Alternatives: the curl install script on Linux/Mac, an .msi on Windows, or the dolthub/doltgresql Docker image.
```

## Try this

```
doltgres
```
Starts the server. On first run it creates a postgres user and database in the current directory with the password 'password'.

```
PGPASSWORD=password psql -h localhost -U postgres
```
Connects to the running Doltgres server as the postgres user, in a second terminal.

```
select dolt_commit('-m', 'Created initial schema');
```
Creates a commit from staged changes (stage tables first with dolt_add) and returns the commit hash. Then run `select * from dolt.log;` to see the history.

## What's unique

Branch, merge, fork, clone, push and pull are all exposed as SQL on a database that existing Postgres clients can talk to. The version history lives in the same tables you query.

## Caveats

Some Postgres syntax, types, functions and extensions are not implemented yet, and the README's own benchmark shows overall latency about 2.7x Postgres's for release 1.0.0.

## Links

- [Homepage / GitHub repo](https://github.com/dolthub/doltgresql)
- [Documentation](https://doltgres.com/docs)
- [Docker image](https://hub.docker.com/r/dolthub/doltgresql)
