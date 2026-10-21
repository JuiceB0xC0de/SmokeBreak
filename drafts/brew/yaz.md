---
name: yaz
title: YAZ
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, library, marc, network, protocol, sru, z39.50]
homepage: https://www.indexdata.com/resources/software/yaz/
scout_score: 5
status: draft
---

# YAZ

**TLDR;** A C toolkit and set of command-line tools for talking to Z39.50 and SRU servers, the old protocols behind library catalogue search.

YAZ is a library for building clients and servers that speak Z39.50, SRW and SRU. These are the protocols libraries use to search each other's catalogues and exchange bibliographic records. Per its README, it supports Z39.50-2003 and SRU 1.1 through 2.0 in both client and server roles, plus the Solr webservice on the client side through the ZOOM API.

The homepage says YAZ has been the leading toolkit for these protocols since its first release in 1995, and that most library software vendors use it for protocol support. Others use it for interoperability testing and data conversion. It exists so nobody has to write the protocol layer from scratch.

The library comes with small command-line tools: `yaz-client` for talking to a server, `yaz-ztest` as a test server, `zoomsh` as a shell for the ZOOM API, `yaz-marcdump` for library records, and `yaz-iconv` for character conversion. You can poke at a catalogue protocol from a shell without writing any code.

The door it opens is a corner of internet infrastructure that predates the web's search habits. Library systems have federated search, record formats like MARC, and decades of interoperability work behind them, and almost nobody outside that world sees it.

## Install

```
brew install yaz
```

## Try this

```
yaz-client --help
```
Lists the options for the interactive Z39.50 client, which is the main way to explore a server from the shell.

```
zoomsh --help
```
Shows how to use the ZOOM API shell, the high-level route the docs recommend for client work.

```
yaz-marcdump --help
```
Shows the options for dumping and converting MARC library records.

## What's unique

It is the long-running reference implementation for a protocol most people never see, and it ships a full set of small tools for poking at Z39.50 and SRU servers with no programming.

## Caveats

It is a developer toolkit with no GUI, its command-line tools are aimed at testing and debugging, and the commercial MasterKey Connect service on the homepage is separate from the open-source code.

## Links

- [YAZ homepage (Index Data)](https://www.indexdata.com/resources/software/yaz/)
- [YAZ User's Guide and Reference (version 5.38.1)](https://www.indexdata.com/yaz/doc)
- [YAZ source on GitHub](https://github.com/indexdata/yaz)
