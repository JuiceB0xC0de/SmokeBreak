---
name: scamper
title: scamper
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, measurement, network, protocol, traceroute]
homepage: https://www.caida.org/catalog/software/scamper/
scout_score: 6
status: draft
---

# scamper

**TLDR;** CAIDA's parallel traceroute and ping engine, built to probe thousands of Internet addresses at a set packet rate and map how the network connects.

Scamper is an active Internet prober from CAIDA, written by Matthew Luckie. It runs ping, traceroute and related measurements against lists of IPv4 or IPv6 addresses, taken from the command line, from files, or from commands sent to a running scamper process over a control socket. Results are saved in its own warts format, or as text or JSON.

It is the successor to skitter and is the prober deployed in CAIDA's Macroscopic Topology Project. The homepage describes it as built to probe destinations in parallel, at a packets-per-second rate you choose with `-p` (1 to 50000), so that bulk data can be collected in a timely fashion. That makes it a tool for surveying the network rather than debugging one host.

The idea underneath is that a measurement can be steered by earlier results. A driver program, written against the Python API or the C libraries libscamperctrl and libscamperfile, connects to a running scamper and decides the next probe from what came back. The many `sc_` programs include drivers for published research methods such as Ally, Speedtrap and bdrmap, so the install doubles as a reading list for how researchers infer routers, aliases and network borders from probe replies.

The warts files keep metadata about each measurement alongside the response detail. Converters such as `sc_warts2json`, `sc_warts2text` and `sc_warts2pcap` turn them into formats other tools can read.

## Install

```
brew install scamper
```

## Try this

```
scamper -?
```
Prints the usage summary: the options for probe rate, output file, daemon mode, and where targets come from.

```
scamper -c trace -i 8.8.8.8
```
Runs a traceroute to the one address you give with -i, using the trace command (the default when -c is omitted).

```
sc_wartsdump --help
```
Shows how to dump a warts result file in readable form, for inspecting the measurements scamper saved.

## What's unique

It is built for bulk, rate-controlled measurement rather than single-target troubleshooting, with a control socket that lets follow-up logic steer a live process. It also ships drivers that implement published research methods.

## Caveats

Not every module runs everywhere (sting and tbit need IPFW or PF), and probing other people's networks at high rates is a responsibility the project page does not discuss.

## Links

- [Scamper homepage (CAIDA catalog)](https://www.caida.org/catalog/software/scamper/)
- [CAIDA Resource Catalog entry for scamper](https://catalog.caida.org/software/scamper)
