---
name: cayley
title: Cayley
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, go, graph-database, linked-data, query-languages]
homepage: https://cayley.io
scout_score: 5
status: draft
---

# Cayley

**TLDR;** A graph database for Linked Data, modeled on the one behind Google's Knowledge Graph, queryable in Gremlin-style, GraphQL-style or Freebase MQL languages.

Cayley stores graph data, including RDF formats such as NQuads and JSON-LD, and sits on top of a backend you may already run. The homepage lists SQL, NoSQL and key-value stores. Rather than replace your database, it adds a graph layer over it.

You query the same data through one of three languages: Gizmo, a dialect of Gremlin; a GraphQL-inspired language; or MQL, a simplified query language from Freebase. The README also lists a built-in query editor, a visualizer and a REPL.

The idea underneath is the one behind Freebase and Google's Knowledge Graph: facts stored as linked nodes and edges, where a question is a walk through the graph. The README's own example is a multi-hop intersection, films starring two given actors. It reports about 150ms on 134 million quads in LevelDB, on 2014 consumer hardware.

Cayley is modular. The homepage says new formats, backends, query languages or custom logic can be added. It is also built to be embedded in applications as a Go library.

## Install

```
brew install cayley
# The brief did not confirm first-run setup. See the Install and Quick Start pages in the docs.
```

## Try this

```
cayley --help
```
Lists the subcommands and flags, the safest way to see how to load data and start the server or REPL.

## What's unique

Few graph databases offer Freebase's MQL alongside a Gremlin-style language and a GraphQL-style language over the same data. It is also designed to sit on top of a store you already run.

## Caveats

Activity is unclear: the homepage copyright reads 2021, the docs say 'Last updated 4 years ago', and the README's performance figures come from 2014 hardware.

## Links

- [Homepage](https://cayley.io)
- [GitHub repository and README](https://github.com/cayleygraph/cayley)
- [Documentation](https://cayley.gitbook.io/cayley/)
