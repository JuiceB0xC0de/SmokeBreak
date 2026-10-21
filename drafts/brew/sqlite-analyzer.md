---
name: sqlite-analyzer
title: sqlite3_analyzer
source: brew
category: take-things-apart
commitment: quick
tags: [database, deprecated, file-formats, quick, sqlite]
homepage: https://www.sqlite.org/
scout_score: 6
status: draft
---

# sqlite3_analyzer

**TLDR;** A small tool that reads an SQLite file and reports where every page went, table by table and index by index, as a report that is also valid SQL.

sqlite3_analyzer takes the path to an SQLite database and prints a plain-text report on how space is used inside it. For each table and index it gives page counts, unused bytes and payload percentages. The SQLite documentation describes it as a TCL program that reads the dbstat virtual table and formats what it finds.

The odd part is the output. The report is also valid SQL: most of the text sits in a header comment, and the end of the file holds statements that create and fill a database with the raw measurements. Pipe it into the SQLite shell and you get a database about your database, which you can query to find which index wastes the most space.

The idea underneath is that an SQLite file is a sequence of fixed-size pages, and a table or index is a set of those pages with some left empty. Seeing that breakdown shows why a file is the size it is, and why deleting rows does not shrink it.

The tool is deprecated. As of SQLite 3.54.0 the docs say it has been replaced by the CLI's .diskused command and the diskused() SQL function. It is still a quick way to see the report format and the layout it describes, and the replacement is one command away.

## Install

```
brew install sqlite-analyzer
```

## Try this

```
sqlite3_analyzer database.sqlite
```
Prints the space-utilization report for each table and index in the file.

```
sqlite3 database.sqlite .diskused
```
Runs the CLI dot-command the docs name as the replacement, on the same file.

```
sqlite3_analyzer --help
```
Shows what the tool says about its own usage.

## What's unique

Its report doubles as a SQL script that rebuilds the measurements as a database, so you can query the layout of your database with SQL.

## Caveats

Deprecated as of SQLite 3.54.0 in favour of the CLI's .diskused command and the diskused() SQL function.

## Links

- [SQLite homepage](https://www.sqlite.org/)
- [sqlite3_analyzer documentation](https://www.sqlite.org/sqlanalyze.html)
