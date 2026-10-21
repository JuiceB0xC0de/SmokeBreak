---
name: silk
title: SiLK
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, ipfix, netflow, network, security]
homepage: https://tools.netsa.cert.org/silk/
scout_score: 6
status: draft
---

# SiLK

**TLDR;** A suite of about 70 piped command-line tools from CERT for querying huge archives of network flow records, the NetFlow-style telemetry most developers never see.

SiLK, the System for Internet-Level Knowledge, comes from the CERT Network Situational Awareness Team. It does not look at packets. It works on flow records, the summaries a router or probe emits for each conversation: who talked to whom, on which ports, how many bytes, and when. A packing system takes IPFIX, NetFlow v9, or NetFlow v5 input and converts it into compact binary flat files.

The analysis side is a family of terse `rw`-prefixed commands that read those files and talk to each other through Unix pipes. In the project's words, "the analysis tools interoperate using pipes, allowing a user to develop a relatively sophisticated query from a simple beginning." `rwfilter` selects records, `rwcut` prints fields, `rwstats` and `rwuniq` summarize, and `rwsort` orders. The executables list also shows tools for building and combining IP sets and bags.

The idea underneath is that network history can be treated like a text corpus, searchable with the same stage-by-stage habits as grep and sort. It was built so analysts could rapidly query large historical traffic data sets for security work. The homepage says it is best suited to backbone or border traffic for a large distributed enterprise or mid-sized ISP.

The brief did not cover setup or configuration, so the Documentation link on the homepage is the place to learn how to get flow data in.

## Install

```
brew install silk
# No sample data ships with the formula as far as the brief shows. You need flow records (IPFIX, NetFlow v5/v9) packed by SiLK's own tools before the query commands have anything to read.
```

## Try this

```
rwfilter --help
```
Prints the options for the main record-selection tool, which is where most SiLK queries begin.

```
rwcut --help
```
Shows how to choose and format the fields printed from flow records.

```
rwstats --help
```
Lists the options for computing top-N style statistics over flow data.

## What's unique

Flow data is stored in a compact binary format and queried with classic Unix-style pipelines, so large NetFlow/IPFIX archives become something you can explore from the shell.

## Caveats

It is aimed at large networks and needs real flow data to be interesting; the brief found no release date and no install walkthrough.

## Links

- [SiLK homepage](https://tools.netsa.cert.org/silk/)
