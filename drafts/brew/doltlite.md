---
name: doltlite
title: DoltLite
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, database, embedded, prolly-tree, sql, sqlite, version-control]
homepage: https://github.com/dolthub/doltlite
scout_score: 6
status: draft
---

# DoltLite

**TLDR;** A SQLite fork that swaps the B-tree for a prolly tree, so a single-file SQL database gets Git-style branches, commits, diffs and merges.

DoltLite keeps SQLite's parser, query planner and virtual machine, but replaces the storage engine beneath them. Instead of pages in a B-tree, each database is one content-addressed chunk-store file holding prolly trees: immutable nodes whose boundaries are chosen by a rolling hash. Because identical content produces identical nodes, two versions of a table can share almost all their storage, and comparing them is cheap.

Version control is exposed through SQL. You call functions such as `dolt_commit`, `dolt_branch`, `dolt_checkout` and `dolt_merge`, and query virtual tables such as `dolt_log` and `dolt_diff_<table>`. Each connection sits on its own branch, and uncommitted work belongs to that branch. Merge conflicts live only inside the transaction that produced them and never reach disk.

It comes from the team behind Dolt, a versioned database that runs as a server. The README's pitch for DoltLite is that it "can be embedded in any language enabling local-first use cases for Dolt." The package ships a `doltlite` shell, a `doltlite-remotesrv` sync server, and a C library with bindings for Python, Ruby, Node, Rust, Go and others. Stock SQLite files still open on the original B-tree engine.

The underlying idea is worth the visit even if you never use the tool: if a database's storage is a Merkle-style tree of content-addressed chunks, then history, diff and merge stop being bolted-on features and become properties of the data structure.

## Install

```
brew install doltlite
# Alternatives from the README: a curl-piped install.sh (macOS arm64/Linux, needs sudo), .deb packages, a Windows zip, or build from source with: cd build && ../configure && make
# Language bindings install via each ecosystem's package manager, e.g. pip install doltlite
```

## Try this

```
doltlite :memory:
```
Opens the shell on a throwaway in-memory database, where you can create a table and try the dolt_* functions.

```
SELECT dolt_commit('-m', 'Add users');
```
Inside the shell, commits your staged changes with a message, the start of the commit loop.

```
SELECT dolt_branch('feature');
```
Creates a branch named feature; follow it with dolt_checkout('feature') to switch this connection onto it.

## What's unique

It puts Git-style branching, merging and conflict resolution inside an ordinary single-file embedded SQL database rather than a separate server. Even the built-in vec1 vector index is versioned and merges like the rest of the data.

## Caveats

It is labelled Beta, a write transaction may touch only one file-backed database, and the brief could not confirm recent maintenance activity.

## Links

- [GitHub homepage and README](https://github.com/dolthub/doltlite)
- [Detective demo (tutorial, per README)](https://github.com/dolthub/doltlite/blob/main/doc/doltlite/demo.md)
- [Why DoltLite? (DoltHub blog)](https://www.dolthub.com/blog/2026-04-27-why-doltlite/)
