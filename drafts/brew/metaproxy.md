---
name: metaproxy
title: Metaproxy
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, libraries, network, protocol, proxy, sru, z39.50]
homepage: https://www.indexdata.com/resources/software/metaproxy/
scout_score: 6
status: draft
---

# Metaproxy

**TLDR;** A router for Z39.50 and SRU library search protocols that fans one query out to many back-end databases and merges the results.

Metaproxy is server software with no user interface. It sits in front of several Z39.50, SRU, SRW and Solr search servers and presents them to a client as one searchable endpoint. A request comes in, passes through a chain of filters, and a single merged result set goes back. The homepage calls it a "metasearch server in-a-box."

Everything is wired together in an XML configuration file. The file defines routes that request packets take, and each step on a route is an instance of a filter. The manual lists filters such as sru_z3950 (SRU requests translated to Z39.50), z3950_client (a Z39.50 back-end client), virt_db and multi (virtual databases and multi-database search), load_balance, and cql_rpn (CQL to RPN query conversion). New filter types can be added as loadable modules through a filter API.

It exists to join multiple back-end databases, within one organization or across several, into what looks to the user like one resource. The manual describes it as "a universal router, proxy and encapsulated metasearcher for information retrieval protocols."

The door here is Z39.50, a library-world search protocol that most developers have never met. Reading a Metaproxy config shows how a federated search system is put together as a pipeline of small, swappable stages. It is built on the YAZ toolkit, which is where you would go next to talk to these servers directly.

## Install

```
brew install metaproxy

Installs two executables: metaproxy (the server) and metaproxy-config (a script that reports on the installation). Depends on boost, yaz and yazpp. You write an XML config file, and you need a Z39.50 or SRU client, plus back-end servers, to see anything happen.
```

## Try this

```
metaproxy --help
```
Prints the server's command-line options, including how to point it at an XML config file.

```
metaproxy-config --help
```
Shows what the installation-reporting script can tell you about your build.

## What's unique

It is a router, not a search front end: no UI, just a chain of filters in XML that can fan one endpoint out to many Z39.50 and SRU back ends. Few people outside libraries have met the protocols it speaks.

## Caveats

It has no user interface and needs an existing standards-based client and back-end servers to be useful, and the brief found no sample command lines, so expect to learn from the manual.

## Links

- [Homepage](https://www.indexdata.com/resources/software/metaproxy/)
- [User's Guide and Reference](https://www.indexdata.com/metaproxy/doc/)
- [GitHub repository](https://github.com/indexdata/metaproxy)
