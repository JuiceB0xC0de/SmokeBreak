---
name: basex
title: BaseX
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, database, java, query-language, xml, xquery]
homepage: https://basex.org
scout_score: 6
status: draft
---

# BaseX

**TLDR;** A lightweight XML database and XQuery processor that lets you query XML, JSON and CSV with a functional query language most developers never meet.

BaseX is a database engine written in Java for storing and querying collections of XML, HTML, JSON, CSV and other text, plus binary resources. You can run XQuery expressions straight from the command line, use a console, or open a desktop GUI that the docs describe as an IDE with visualizations for exploring data.

The idea underneath it is XQuery, a query language built for tree-shaped documents rather than tables. Where SQL asks questions of rows, XQuery walks and reshapes nested structures, and it is a full functional language rather than only a way to filter. BaseX describes itself as a highly compliant processor, with XQuery 4.0 and the W3C Update and Full-Text extensions.

The README lists four entry points: a console, a server that waits for requests, a client that talks to that server, and the GUI. That maps to the executables brew installs, including `basexserver`, `basexclient` and `basexhttp`. BaseX also supports RESTXQ, which lets you build web applications in XQuery itself.

The project's tagline is "Lightweight and High-Performance Data Processing". It is a door into a corner of data processing that is old, well specified and still maintained.

## Install

```
brew install basex
# Java is required; the formula lists openjdk as a dependency
```

## Try this

```
basex -h
```
Lists the available command line options, as the README suggests.

```
basexgui
```
Opens the desktop GUI, where you can write queries and explore data visually.

```
basexserver
```
Starts a database server that waits for requests from clients such as basexclient.

## What's unique

Few XML databases ship an XQuery 4.0 processor with the Update and Full-Text extensions, RESTXQ and a visual GUI in one lightweight package.

## Caveats

The brief did not check what the brew install pulls in or how first run behaves, and the docs are the best place to learn XQuery itself.

## Links

- [BaseX homepage](https://basex.org)
- [Documentation](https://docs.basex.org)
- [GitHub repository](https://github.com/BaseXdb/basex)
