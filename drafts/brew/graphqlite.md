---
name: graphqlite
title: GraphQLite
source: brew
category: languages-and-oddities
commitment: quick
tags: [cypher, database, extension, graph, quick, sqlite]
homepage: https://colliery-io.github.io/graphqlite/
scout_score: 5
status: draft
---

# GraphQLite

**TLDR;** A SQLite extension that lets you write Cypher graph queries and run graph algorithms like PageRank inside an ordinary .db file, with no server.

GraphQLite is a loadable extension for SQLite. Once loaded into a connection, a `cypher()` SQL function accepts Cypher text, the query language used by graph databases such as Neo4j. You can create nodes, match relationship patterns, and call graph algorithms, and the results come back as JSON rows through normal SQL. There are also Python and Rust bindings.

The pitch is that graph data does not need its own database server. The homepage says the graph lives in "a single .db file alongside the rest of your application data." That means no network configuration and no migration scripts, and your relational tables and your graph sit in the same file.

Under the hood, properties are stored in an EAV model, with separate tables for text, integer, real, boolean and JSON values. Algorithms such as PageRank are exposed as Cypher functions, for example `RETURN pageRank(0.85, 20)`. The project says it ships more than 15 of them, including Louvain, Dijkstra, A* and connected components.

The idea underneath is that a query language and a storage engine are separable. Cypher is a way of drawing patterns of nodes and edges, and here it is translated onto plain SQLite tables. That makes it a good way to see how graph queries relate to relational ones.

## Install

```
brew install graphqlite
# then, in the sqlite3 CLI:
# .load $HOMEBREW_PREFIX/opt/graphqlite/lib/sqlite/graphqlite
# Python: pip install graphqlite   Rust: cargo add graphqlite
# Requires sqlite (installed as a Homebrew dependency).
```

## Try this

```
SELECT cypher('CREATE (a:Person {name: "Alice", age: 30})');
```
Creates a Person node in the graph stored inside your SQLite database.

```
SELECT cypher('MATCH (a:Person)-[:KNOWS]->(b) RETURN a.name, b.name');
```
Runs a Cypher pattern match over KNOWS relationships and returns the names on each end.

```
SELECT cypher('RETURN pageRank(0.85, 20)');
```
Runs PageRank with damping 0.85 over 20 iterations; the homepage unpacks the JSON result with json_each.

## What's unique

It runs openCypher inside SQLite as a single file with no server, and the README reports 98.5% of 3,880 openCypher TCK scenarios passing. Most embedded graph options are not measured against a conformance suite like this.

## Caveats

Version numbers and Python API examples disagree between the homepage and README (v0.12.0 vs 0.4.4, g.connection.cypher vs g.query), and the README lists remaining gaps in timezone arithmetic, nested existential subqueries and multi-row MERGE.

## Links

- [Homepage and full documentation](https://colliery-io.github.io/graphqlite/)
- [Source code and issue tracker](https://github.com/colliery-io/graphqlite)
- [Conformance coverage matrix (in repo)](https://github.com/colliery-io/graphqlite/blob/main/docs/testing/semantic-coverage-matrix.md)
