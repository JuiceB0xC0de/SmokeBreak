---
name: dolt
title: Dolt
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, database, git, mysql, sql, versioning]
homepage: https://www.dolthub.com
scout_score: 6
status: draft
---

# Dolt

**TLDR;** A MySQL-compatible SQL database you can branch, merge, diff, push and pull like a Git repository, with history down to individual cells.

Dolt is a SQL database with Git's verbs. You can fork, clone, branch, merge, push and pull it. Connect with any MySQL-compatible client and read or change schema and data as usual. The version control layer sits alongside, reachable from a Git-like `dolt` command line and from inside SQL itself.

The README puts it this way: "Git versions files. Dolt versions tables. It's like Git and MySQL had a baby." The CLI has the same commands as `git`, with some extras. It can import CSV files, commit, push to a remote and merge a teammate's changes.

Inside SQL, reads are system tables named `dolt_<thing>`, such as `dolt_log`, `dolt_status` and `dolt_diff_<table>`. Writes are stored procedures named after the CLI command, such as `dolt_add` and `dolt_commit`, with options passed as arguments just as on the command line. A Dolt commit is distinct from a SQL transaction COMMIT.

The idea underneath is that data, not just code, can have a history you can branch and merge. Test a schema change on its own branch and merge it when it works. Ask which commit changed a given cell. Undo an accidental `DROP TABLE`. The project also pitches it for agent memory in multi-agent and multi-machine workflows, which is the author's own claim.

## Install

```
brew install dolt
# then set the commit author, like git config:
dolt config --global --add user.email YOU@DOMAIN.COM
# also set user.name the same way
```

## Try this

```
dolt sql-server
```
Starts the built-in MySQL-compatible server on localhost:3306. The terminal stays occupied while it runs.

```
mysql --host 127.0.0.1 --port 3306 -uroot
```
Connects the standard MySQL client to the running Dolt server.

```
call dolt_commit('-m', 'Created initial schema');
```
Run inside a SQL session, this creates a Dolt commit of your staged changes, the SQL equivalent of `dolt commit -m`.

## What's unique

It is a real MySQL-compatible database, not a versioned file store, with commits, branches, merges and cell-level history exposed through plain SQL.

## Caveats

The binary is about 103 MB, MySQL 9.0 clients need extra auth configuration (the README recommends 8.4), and the brief could not confirm how actively the project is maintained.

## Links

- [Homepage (DoltHub)](https://www.dolthub.com)
- [GitHub repository and README](https://github.com/dolthub/dolt)
- [Documentation: What is Dolt](https://dolthub.com/docs/introduction/what-is-dolt)
- [Explainer video](https://www.youtube.com/watch?v=H2iZy0Cme10)
