---
name: tinysparql
title: TinySPARQL
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, gnome, library, rdf, semantic-web, sparql, triple-store]
homepage: https://tinysparql.org/
scout_score: 5
status: draft
---

# TinySPARQL

**TLDR;** A small RDF triple store you query with SPARQL 1.1, built as a GObject C library and the successor to GNOME's Tracker.

TinySPARQL is a C library that holds RDF data and answers SPARQL 1.1 queries. Its homepage describes it as a "Low-footprint RDF triple store with SPARQL 1.1 interface". An application opens a TrackerSparqlConnection to a store, runs queries and updates through it, and reads results back through a cursor. Statements can be prepared, and a Notifier reports changes to the stored data.

The homepage describes it as the successor to Tracker (version 3.x), and it ships with a set of ontologies (Nepomuk, NIE, NFO, NCO and others) listed in the docs. The brief gives no stated motivation beyond the one-line description, so the why is best read off the API: a store that lives inside a program rather than in a separate database server.

The idea underneath is the triple: everything is a subject, a predicate and an object, and a query is a pattern matched against a graph. SPARQL is the standard language for those patterns. Stores can also be exposed to other processes over D-Bus, or to other hosts over HTTP, through the endpoint classes.

The brew formula installs a `tinysparql` executable. The brief did not capture its usage, so start with its help output. The homepage mentions a command-line reference page that was not fetched.

## Install

```
brew install tinysparql
```

## Try this

```
tinysparql --help
```
Lists the subcommands the command-line tool offers, which is the way into the rest of it.

## What's unique

It is a small, local SPARQL 1.1 store embedded as a GObject library, with a standard ontology set included, rather than a heavyweight graph database server.

## Caveats

It is mainly a library, so expect to use its C API (or GObject bindings) rather than a standalone database; the README is one line, docs live on the homepage, and sources disagree on the license wording.

## Links

- [TinySPARQL homepage](https://tinysparql.org/)
- [Source on GNOME GitLab](https://gitlab.gnome.org/GNOME/tinysparql/)
