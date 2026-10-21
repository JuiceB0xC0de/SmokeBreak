---
name: tarantool
title: Tarantool
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, application-server, database, in-memory, lua]
homepage: https://tarantool.org/
scout_score: 5
status: draft
---

# Tarantool

**TLDR;** An in-memory database that runs your Lua code in the same process as the data, so logic and storage share one address space.

Tarantool keeps its data in RAM and still survives restarts. Every write goes to a write-ahead log, and the transaction returns only after the log is saved to disk. It offers HASH, TREE, RTREE and BITSET indexes, MessagePack for data and the client protocol, and ANSI SQL. The homepage also describes synchronous and asynchronous replication and an MVCC transaction mode.

The odd part is the second half of the name. Tarantool is also an application server running LuaJIT 2.1, with cooperative multitasking and non-blocking IO. In the README's words, "The database is a C extension of the application server and can be turned off." Code and data share one address space, so your logic runs next to the stored records instead of across a network hop.

That inverts the usual layout, where an application talks to a separate database. Here the database is a library inside your program. The project pitches it for "queue servers, caches, stateful Web applications", and it ships persistent queues, sharding and a cluster management framework.

The brief did not include any first-run steps, so the getting started guide is the place to learn the console and the Lua API.

## Install

```
brew install tarantool
```

## Try this

```
tarantool --help
```
Lists the command-line options for the executable, which is the starting point for running Lua scripts or an interactive console.

## What's unique

Most in-memory stores are a cache or a key-value server. This one puts a full Lua application runtime in the same process as the data, and the database itself is the optional part.

## Caveats

The homepage is vendor marketing for the Community Edition, with Enterprise products mixed into the navigation, and its replication and data-loss claims are not measured results.

## Links

- [Homepage](https://tarantool.org/)
- [GitHub repository and README](https://github.com/tarantool/tarantool)
- [Getting started documentation](https://www.tarantool.io/en/doc/latest/getting_started/)
- [Download instructions](https://www.tarantool.io/en/download/)
