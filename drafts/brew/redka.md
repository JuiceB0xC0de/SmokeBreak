---
name: redka
title: Redka
source: brew
category: languages-and-oddities
commitment: quick
tags: [database, go, postgresql, quick, redis, sqlite]
homepage: https://github.com/nalgeon/redka
scout_score: 5
status: draft
---

# Redka

**TLDR;** Redis reimplemented on top of SQLite or PostgreSQL, speaking the Redis wire protocol so existing clients work while your data sits in ordinary SQL tables.

Redka is a Go project that reimplements the core of Redis: strings, lists, sets, hashes and sorted sets, plus key, server and transaction commands. It speaks RESP, the Redis wire protocol, so a normal Redis client can connect to it. Behind that, the data goes into SQLite or PostgreSQL instead of a custom in-memory store.

The interesting part is the mapping. Redis data types become a relational schema, so the data lives in ordinary tables, can grow past RAM, and can be inspected with SQL. The README mentions SQL views for analysis and reporting, and ACID transactions. It points to docs/persistence.md for the schema details.

The README pitches three uses: an embedded key-value store for Go apps that already use SQLite, a light stand-in for Redis test containers in local development and integration tests, and Redis-style data structures for teams that want everything in PostgreSQL. It runs as a standalone server or as an in-process Go module.

It is upfront about the trade. In its own words: "Redka is not about raw performance. You can't beat a specialized data store like Redis with a general-purpose relational backend like SQLite."

## Install

```
brew install redka
# Alternatives: Docker image `nalgeon/redka` (x86 and ARM), or a source build (needs Go 1.23+ and GCC).
```

## Try this

```
redka --help
```
Lists the server's options, so you can see how to start it and point it at a SQLite file.

```
docker pull nalgeon/redka
```
Pulls the official image if you would rather run the server in a container.

```
git clone https://github.com/nalgeon/redka.git
```
Fetches the source so you can read the schema and build the server yourself with `make setup build`.

## What's unique

It keeps the Redis API and wire protocol, so existing clients connect unchanged, while the data stays in a plain SQL database you can query directly.

## Caveats

The README says it is in maintenance mode with no new features planned, covers only part of Redis's commands, tops out at tens of thousands of operations per second, and is rated for non-critical production only.

## Links

- [Homepage / README (GitHub)](https://github.com/nalgeon/redka)
- [Install standalone server docs](https://github.com/nalgeon/redka/blob/master/docs/install-standalone.md)
- [Performance benchmarks](https://github.com/nalgeon/redka/blob/master/docs/performance.md)
