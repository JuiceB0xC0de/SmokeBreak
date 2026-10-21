---
name: mdbtools
title: mdbtools
source: brew
category: take-things-apart
commitment: afternoon
tags: [access, afternoon, databases, file-formats, reverse-engineering]
homepage: https://github.com/mdbtools/mdbtools/
scout_score: 6
status: draft
---

# mdbtools

**TLDR;** A set of command-line tools that read Microsoft Access database files on Unix, turning a proprietary binary format into tables, CSV and JSON.

mdbtools reads Microsoft Access .mdb files without Access, Windows or Microsoft's libraries. Its executables cover the usual questions you would ask of an unfamiliar database: list the tables, dump the schema, export a table, count rows, run SQL against it. There are also exports to JSON and a hexdump tool for looking at the raw pages.

The interesting part is the format underneath. Access files are a closed, undocumented binary layout, so a tool like this exists only because someone worked out how the pages, tables and data types are stored. That makes it a small, practical example of format reverse engineering, with real files you can test against.

It also fills a plain need. Old Access databases turn up in archives, in small-business data and in government downloads, and getting the data out on a Mac or Linux machine is otherwise awkward. The brief for this entry was empty, so details beyond the executable names and the project description are not covered here.

## Install

```
brew install mdbtools
```

## Try this

```
mdb-tables yourfile.mdb
```
Lists the tables in an Access database file you supply.

```
mdb-schema yourfile.mdb
```
Prints the schema of the database, so you can see how it is laid out.

```
mdb-export yourfile.mdb TableName
```
Writes the named table out as CSV.

## What's unique

It is a long-standing open implementation of a closed file format, split into small single-purpose tools that fit in shell pipelines.

## Caveats

You need an .mdb or .accdb file of your own to try it on, and support for newer Access formats may be partial.

## Links

- [mdbtools on GitHub](https://github.com/mdbtools/mdbtools/)
