---
name: rrdtool
title: rrdtool
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, database, graphing, monitoring, old-school, time-series]
homepage: https://oss.oetiker.ch/rrdtool/
scout_score: 6
status: draft
---

# rrdtool

**TLDR;** A time-series database whose files are created at full size and wrap around like a ring buffer, so a decade of graphs never outgrows its disk space.

RRDtool logs numbers over time and draws graphs from them. You define a database up front: one or more data sources (each a GAUGE, COUNTER, DERIVE or ABSOLUTE, with a heartbeat and optional min and max) and a set of round robin archives. The file is created at its final size and pre-filled with UNKNOWN. New values overwrite the oldest ones as the archives wrap, so storage stays bounded.

Updates can arrive at irregular times. RRDtool folds them into primary data points on each step interval, then consolidates those into archives using AVERAGE, MIN, MAX or LAST. You might keep fine-grained recent data and coarser data for older periods, all in one file. Counter-type sources are stored as per-second rates, not running totals. In the project's words: "RRDtool stores rates in amount/second for COUNTER, DERIVE, DCOUNTER, DDERIVE and ABSOLUTE data."

The idea underneath is that monitoring data has a natural decay. You want detail about now and a summary of last year, and you do not want to manage retention jobs. Deciding that at create time makes the database a fixed-size object you can reason about. The rrdcreate docs are frank about the trade-offs, such as COUNTER versus DERIVE and how a counter reset can be mistaken for a wrap.

There is more inside. It has built-in Holt-Winters forecasting and failure flagging (HWPREDICT, FAILURES), and COMPUTE data sources that act like virtual columns. The install also includes rrdcached, a caching daemon for batching writes, and rrdcgi, which builds web pages from graph templates. The homepage says it can be called from shell scripts and from perl, python, ruby, lua or tcl.

## Install

```
brew install rrdtool
```

## Try this

```
rrdtool --help
```
Lists the subcommands (create, update, fetch, graph and others) so you can see the whole workflow.

```
rrdtool create temperature.rrd --step 300 \
```
Starts the doc example for a file that accepts one temperature value every 300 seconds. Follow it with a DS line and RRA lines from the rrdcreate docs.

```
rrdtool create power.rrd \
```
Starts the doc example for a file collecting power values once per second. The docs show the scaled-duration form there, such as --step 1s and RRA durations like 10d.

## What's unique

The database never grows, because old data is overwritten by design. It also ships forecasting with Holt-Winters and graphing in the same tool.

## Caveats

Maintenance status is unclear from the pages read (docs are dated between 2012 and 2019), and the Holt-Winters features need a matched set of RRAs to work.

## Links

- [RRDtool homepage](https://oss.oetiker.ch/rrdtool/)
- [rrdcreate documentation](https://oss.oetiker.ch/rrdtool/doc/rrdcreate.en.html)
- [Documentation index](https://oss.oetiker.ch/rrdtool/doc/index.en.html)
