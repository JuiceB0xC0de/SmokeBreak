---
name: bgpdump
title: bgpdump
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, bgp, mrt, network, protocol, routing]
homepage: https://github.com/RIPE-NCC/bgpdump/wiki
scout_score: 5
status: draft
---

# bgpdump

**TLDR;** Decodes MRT and Zebra/Quagga dump files into readable BGP messages, a way to see how the internet's routes are actually recorded and exchanged.

bgpdump reads files that routing daemons write when they record BGP traffic. BGP, the Border Gateway Protocol, is how networks tell each other which IP address ranges they can reach. The tool takes MRT RIB dumps (TABLE_DUMP and TABLE_DUMP_V2) and Zebra/Quagga BGP records, which can be gzipped or piped in through stdin. It turns them into decoded routing data: OPEN, UPDATE, NOTIFY and KEEPALIVE messages, plus BGP state changes.

It began as libbgpdump, a C library for analyzing these dump files, and the Homebrew formula also installs a `bgpdump` command. The project is maintained by the RIPE NCC and the internet researcher community. The MRT input format follows RFC 6396, which the wiki points to.

The idea underneath is that the internet's routing is observable. Collectors archive the BGP traffic they see, and researchers study those archives. A decoder like this is the first step from opaque binary files to questions such as who announced a prefix, or how a path changed. Wrappers exist for Python (PyBGPdump) and Perl (Net::BGPdump) if you want to script against the data.

The documentation is thin. The README is a short stub that sends you to the wiki, and the wiki covers building and input formats but gives no usage examples. You will need a dump file from a route collector and some willingness to read the output and work out its format yourself.

## Install

```
brew install bgpdump
# Upstream builds from source on Linux, FreeBSD, Solaris and Cygwin, needing zlib and bzip2 dev packages: sh ./bootstrap.sh && make
# You also need an MRT dump file to decode; none ships with it.
```

## Try this

```
bgpdump --help
```
Prints the usage text and options, the safest way to see what the tool accepts, since the wiki has no examples.

```
./bgpdump -T
```
Run from the source tree after building, this is the last line of the wiki's build steps. The wiki does not say what -T does.

## What's unique

It is a long-lived decoder for MRT and Zebra/Quagga dumps, maintained by the RIPE NCC, an organisation that works with real internet routing data. Python and Perl wrappers exist for scripting.

## Caveats

Project status is unclear, the README is a stub, the wiki has no usage examples, and macOS is not in the upstream list of supported platforms.

## Links

- [Project wiki (homepage)](https://github.com/RIPE-NCC/bgpdump/wiki)
- [GitHub repository](https://github.com/RIPE-NCC/bgpdump)
