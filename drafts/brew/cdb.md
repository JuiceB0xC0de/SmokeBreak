---
name: cdb
title: cdb
source: brew
category: languages-and-oddities
commitment: quick
tags: [c, database, djb, file-format, key-value, quick]
homepage: https://cdb.cr.yp.to/
scout_score: 6
status: draft
---

# cdb

**TLDR;** D. J. Bernstein's constant database: a read-only key/value file built once, rewritten whole, and looked up in one or two disk accesses.

cdb is a small C package for creating and reading constant databases. A constant database is a key/value file you build in one pass and then only query. You never update it in place. The tools build a database from records, dump one back out in cdbmake-compatible format, and report statistics or run tests. A separate cdb64 set of tools handles the 64-bit variant.

The idea underneath is that giving up in-place updates buys a lot. The homepage says a successful lookup in a large database normally takes two disk accesses, and an unsuccessful one takes one. To change data, you write a whole new file and swap it into place. In the project's words: "Readers don't pause during a rewrite: they continue transparently using the old database until the new database is in place."

The format is old and widely reused. The homepage lists independent implementations in other languages, and well-known programs that use it, including djbdns, qmail, and Postfix. Reading about why this shape works is a good way into how lookup tables, atomic file replacement, and read-mostly data fit together. The pages the brief covers describe the behaviour and the C read API (cdb_init, cdb_find, cdb_read), not the internal hash layout, so that part is yours to dig into.

## Install

```
brew install cdb
```

## Try this

```
cdbmake --help
```
Prints whatever usage the database builder offers, a starting point for building your first constant database.

```
cdbget --help
```
Shows how the lookup tool is invoked, for fetching the record stored under a key.

```
cdbdump --help
```
Shows usage for the dump tool, which writes a database back out in cdbmake-compatible format.

## What's unique

It treats the database as an immutable file that is replaced whole, which gives lookups in one or two disk accesses and readers that never pause. Postfix, qmail, and djbdns use the format.

## Caveats

The brief did not confirm usage or flags for the command-line tools, and the documented API is C-level, so expect to read the homepage and the tools' own help.

## Links

- [cdb homepage](https://cdb.cr.yp.to/)
- [cdb read API](https://cdb.cr.yp.to/cdb.html)
