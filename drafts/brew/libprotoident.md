---
name: libprotoident
title: libprotoident
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, dpi, flows, network, pcap, protocol]
homepage: https://github.com/LibtraceTeam/libprotoident
scout_score: 7
status: draft
---

# libprotoident

**TLDR;** A C library and three tools that name the application protocol of a network flow by looking at only the first four payload bytes in each direction.

Libprotoident labels each network flow with the application protocol it most likely carries: BitTorrent, SMTP, POP3, and so on. It does this from a very small sample. For each flow it looks at the first four bytes of application payload sent by each endpoint, and matches those against known patterns. The README calls this "a very limited form of deep packet inspection".

Three command-line tools come with it. `lpi_protoident` reads a libtrace URI, which can be a trace file or a live interface, and prints one line per flow: the protocol label, endpoints, ports, transport protocol, timestamps, byte counts, and the four leading bytes in each direction. `lpi_find_unknown` prints only the flows it could not identify. `lpi_arff` writes per-flow features in ARFF format for the Weka machine learning software.

The interesting idea is how much a conversation gives away in its opening bytes. Protocols tend to greet in recognisable ways, so four bytes each way can be enough to tell mail from file sharing, without reassembling streams. Labels can also be grouped into categories, so BitTorrent, Gnutella and eMule all count as P2P, and SMTP, POP3 and IMAP count as Mail.

The README also says some traffic in the WAND group's trace sets cannot be tied to any known protocol, and asks for help naming it. The `lpi_find_unknown` tool is the way into that puzzle: run it on a trace and look at what is left over.

## Install

```
brew install libprotoident
# Depends on libtrace and libflowmanager, which Homebrew pulls in. You need a packet trace file or a live interface to feed it.
```

## Try this

```
lpi_protoident --help
```
Shows the options for the main tool, which labels every flow in a trace.

```
lpi_protoident <input trace URI>
```
Prints one line per flow with the protocol label, endpoints, ports, timestamps, byte counts and the first four payload bytes per direction.

```
lpi_find_unknown <input trace URI>
```
Prints only the flows the library could not identify, the mystery traffic.

## What's unique

It deliberately uses only four payload bytes per direction, so it works on flow-level data without reassembling streams. It also ships an ARFF exporter so flow features can go straight into machine learning.

## Caveats

Identification happens only when a flow ends or expires, so it is poor for real-time use, and the four-byte method is inherently limited; the README does not give a release or last-commit date.

## Links

- [GitHub repository (homepage, README)](https://github.com/LibtraceTeam/libprotoident)
- [Supported protocols list (wiki)](https://github.com/wanduow/libprotoident/wiki/SupportedProtocols)
- [libtrace supported trace formats](https://github.com/LibtraceTeam/libtrace/wiki/Supported-Trace-Formats)
