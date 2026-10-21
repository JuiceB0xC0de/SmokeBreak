---
name: packetq
title: PacketQ
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, dns, network, pcap, protocol, sql]
homepage: https://www.dns-oarc.net/tools/packetq
scout_score: 6
status: draft
---

# PacketQ

**TLDR;** Run SQL queries straight against PCAP files, so a packet capture becomes a table you can group, sort and count without a database.

PacketQ is a C++ command-line tool from DNS-OARC that treats a PCAP or DNSTAP capture as a queryable table. You hand it a capture file and a SQL-style query, and it prints the results as JSON by default, or as formatted or compact CSV or XML. Gzipped captures work too. The homepage also mentions a very simple web server for inspecting PCAP files remotely.

The idea underneath it is that a packet trace is already structured data. It is usually read through tools that show one packet at a time. Asking questions like which names were queried most, or how many responses were sent, is a different way of looking at the same bytes. PacketQ lets you ask in SQL, which most developers already know, and sorts the results in memory.

It began life as DNS2db and was renamed in 2011 when it was rebuilt to handle protocols other than DNS. Built-in decoding covers ICMP and DNS, and the decoding is extensible. The project describes DNS as its focus, with a built-in DNS resolver function and DNSTAP input. For large, uniform captures there is sampling, and queries can be cached by pre-processing PCAPs into static JSON files.

The brief's sources do not document the query engine beyond this, so the FIELDS and FUNCTIONS docs on the project site are the place to learn which columns and functions exist.

## Install

```
brew install packetq
# You need a PCAP file to query. The optional MaxMindDB support is only for the CC() and ASN() functions.
```

## Try this

```
packetq -s "select * from dns limit 10" sample.pcap
```
Returns the first 10 packets that carry DNS information from sample.pcap, as JSON.

```
packetq --help
```
Lists the available options, including the output format choices.

## What's unique

It queries capture files directly with SQL, with no import step into a database. Its decoding is DNS-focused and it reads DNSTAP as well as PCAP.

## Caveats

You need your own capture file to get anything interesting, and the README gives only one usage example, so expect to read the field and function docs.

## Links

- [Project homepage (DNS-OARC)](https://www.dns-oarc.net/tools/packetq)
- [Source repository (Codeberg)](https://codeberg.org/DNS-OARC/PacketQ)
- [Demo video](http://www.youtube.com/watch?v=70wJmWZE9tY)
