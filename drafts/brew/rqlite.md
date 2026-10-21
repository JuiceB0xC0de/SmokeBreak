---
name: rqlite
title: rqlite
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, database, distributed, http, network, raft, sqlite]
homepage: https://www.rqlite.io/
scout_score: 6
status: draft
---

# rqlite

**TLDR;** A SQLite database you reach with curl and replicate across machines, so a few nodes keep serving SQL if one dies.

rqlite runs SQLite behind an HTTP and JSON API. You start the rqlited server, POST SQL statements to /db/execute, GET queries from /db/query, and read JSON back. No driver is needed, and curl is enough as a client. It also ships a CLI, a built-in web console, and client libraries.

The twist is the cluster. Start more nodes with -join pointing at an existing one, and they keep their SQLite databases in sync. The homepage describes a Raft cluster, and the console shows Raft state. The idea is a database that stays up when a node fails, without a separate database server to deploy. Read consistency and write durability can be tuned per application.

The README pitches it as a SQLite that is highly available and easy to operate, aimed at resilient cloud services and edge applications. Its own shorthand is "think etcd, but with relational modeling available." It also mentions Change Data Capture and loadable SQLite extensions such as vector search.

It is a good door into replicated state and consensus. You can run a three-node cluster on one laptop with three data directories, then kill a node and watch what happens.

## Install

```
brew install rqlite
# alternatives: curl -fsSL https://rqlite.io/install.sh | sh, or docker run -p 4001:4001 rqlite/rqlite
```

## Try this

```
rqlited -node-id 1 data/
```
Starts the first node with ID 1, keeping its data in the data/ directory.

```
curl -XPOST 'localhost:4001/db/execute?pretty' -H 'Content-Type: application/json' -d '["CREATE TABLE foo (id INTEGER NOT NULL PRIMARY KEY, name TEXT)", "INSERT INTO foo(id, name) VALUES(1, \"fiona\")"]'
```
Creates a table and inserts a row in one request, using a JSON array of SQL statements.

```
curl -G 'localhost:4001/db/query?pretty' --data-urlencode 'q=SELECT * FROM foo'
```
Runs a SELECT over HTTP and prints the rows as JSON.

## What's unique

It turns SQLite into a replicated service you can talk to with plain curl, with no driver and no separate database server. Clustering is a matter of starting nodes with -join.

## Caveats

Surviving a node failure needs at least three nodes, and tuning read consistency or durability adds configuration choices; I did not confirm recent project activity.

## Links

- [Homepage](https://www.rqlite.io/)
- [GitHub repository](https://github.com/rqlite/rqlite)
- [Quick start docs](https://rqlite.io/docs/quick-start/)
- [HTTP API docs](https://rqlite.io/docs/api/)
