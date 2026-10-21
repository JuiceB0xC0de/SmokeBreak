---
name: immudb
title: immudb
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, cryptography, database, go, merkle-tree, sql, tamper-evident]
homepage: https://immudb.io/
scout_score: 5
status: draft
---

# immudb

**TLDR;** A database that only appends, and hands back cryptographic proofs that its history has not been altered, which clients check without trusting the server.

immudb is a database written in Go that works as a key-value store, a document store, or a SQL database. Writes only add new versions. Existing records are never changed or deleted. A read can come back with a proof, and the client checks that proof itself.

The README's argument is that ordinary database transactions and logs are mutable, so there is no way to know for sure whether data has been compromised. immudb is positioned as a practical alternative to a blockchain or a hosted ledger service, without the throughput cost.

Underneath is a cryptographic commit log with a parallel Merkle tree, indexed with an extended B-tree. That is the same family of structure behind certificate transparency logs and similar tamper-evident systems. The proofs are also exposed in plain SQL through functions such as `immudb_verify_row`, `immudb_verify_tx` and `immudb_history`, so you can poke at them from any PostgreSQL client.

It runs as a standalone server with gRPC, PostgreSQL wire protocol and REST access, or embedded in a Go program as a library with no separate process. The Go embedding guide is in `docs/EMBEDDING.md` in the repo.

## Install

```
brew install immudb
# Docker also works: docker run -d -p 3322:3322 -p 8080:8080 -it --name immudb codenotary/immudb:latest
```

## Try this

```
immudb
```
Starts the server in the foreground so all output is visible.

```
immuclient
```
Opens the interactive client shell, where you can write records and ask for verified reads.

```
immudb --audit-log --audit-log-events=write
```
Starts the server with structured audit logging of write, admin, auth and system operations, stored in immudb's own KV store under the audit: prefix.

## What's unique

Verification happens on the client, so you do not have to trust the server, and the proofs are reachable through ordinary SQL and a PostgreSQL-compatible endpoint. The same engine runs as a server or embedded as a Go library.

## Caveats

The license is Business Source License 1.1 (source available, not OSI open source), the PostgreSQL compatibility has known gaps, and benchmark figures come from the authors' own tests.

## Links

- [Homepage](https://immudb.io/)
- [Documentation](https://immudb.io/docs/)
- [GitHub repository](https://github.com/codenotary/immudb)
- [Online demo](https://demo.immudb.io)
