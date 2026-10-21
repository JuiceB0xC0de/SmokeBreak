---
name: tsduck
title: TSDuck
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, broadcast, cli, dvb, mpeg-ts, protocol, streaming]
homepage: https://tsduck.io/
scout_score: 7
status: draft
---

# TSDuck

**TLDR;** A toolbox of small command-line tools for taking apart MPEG transport streams, the container that carries digital TV, from live broadcasts or recorded files.

TSDuck is a free C++ toolkit for MPEG transport streams, the format that carries digital television over satellite, cable, terrestrial and IP networks. It installs about forty small executables, each doing one elementary job: analysing a stream, dumping packets, fixing continuity counters, compiling and decoding signalling tables, and so on. There is no GUI. In its own words: "Each utility or plugin performs only one elementary feature but they can be combined in any order."

The centre of it is tsp, the Transport Stream Processor. It chains plugins so a stream flows through input, processing and output stages. Inputs can be live DVB, ATSC or ISDB tuners, UDP multicast, HTTP, HLS, SRT, RIST, recorded .ts files or pcap captures. Outputs can be reports, rewritten streams, or tables and descriptors in XML, JSON or binary. Underneath is a shared C++20 library covering MPEG, DVB, ATSC, ISDB and SCTE signalling, with Python and Java bindings if you would rather script it.

The author describes it as a general-purpose toolbox for digital TV engineers doing test, monitoring, integration, debug and lab work, and not a production application. The idea underneath is that broadcast television is a stream of tiny fixed-size packets with tables interleaved to say what is in them, and that those tables can be read, rewritten and inspected like any other protocol. A .ts file and a few of these tools are enough to start looking at that layer.

## Install

```
brew install tsduck
# Also on Windows via winget and FreeBSD via pkg. Tuner, Dektec and HiDes hardware support needs separate drivers and is Windows and Linux only. You do not need hardware to analyse recorded .ts files.
```

## Try this

```
tsp --help
```
Shows the syntax of the stream processor, the plugin pipeline engine at the heart of the toolkit.

```
tsanalyze --help
```
Lists the options of the analysis tool, which reports on the services, PIDs and bitrates inside a transport stream.

```
tsversion --check
```
Checks online whether a newer TSDuck release is available.

## What's unique

It is a Unix-style box of single-purpose tools plus a plugin pipeline, and it reaches real broadcast hardware and standards such as SCTE 35, SimulCrypt head-end emulation and ETSI TR 101 290 metrics. Few open projects cover digital TV signalling this broadly.

## Caveats

Maintained by one developer in spare time, described by the README as a toolbox rather than a production application, and tuner and modulator support is mostly Windows and Linux only.

## Links

- [Homepage](https://tsduck.io/)
- [User Guide](https://tsduck.io/docs/tsduck.html)
- [Builder Guide](https://tsduck.io/docs/tsduck-build.html)
- [GitHub repository](https://github.com/tsduck/tsduck)
