---
name: ssldump
title: ssldump
source: brew
category: fundamentals
commitment: quick
tags: [fingerprinting, json, network, pcap, protocol, quick, tls]
homepage: https://adulau.github.io/ssldump/
scout_score: 5
status: draft
---

# ssldump

**TLDR;** A passive TLS analyzer that reads live traffic or a pcap and prints every handshake and record as text or JSON, with fingerprints included.

ssldump watches TCP connections on a network interface, or reads a saved pcap file, and tries to interpret them as SSLv3/TLS. It decodes the record layer and the handshake and prints what it sees to stdout. With the right keying material it can also decrypt the sessions and show application data. It never sits in the middle of a connection. It only listens.

This repository is a maintained fork of the original SSLDUMP 0.9b3, which is old and was left unmaintained. The maintainer gathers Debian and other distribution patches plus pull requests into one place. In the maintainer's words: "Because it's a mess. The software maintenance process for old free (unmaintained) software like ssldump is a complete chaotic process." The contributing policy is just as short: if a patch works for the maintainer, it is merged.

The fork adds a JSON output mode (-j). In that mode it computes JA3 and JA3S fingerprints from ClientHello and ServerHello messages, skipping GREASE values. It also computes FAN/1 feature strings for TLS handshakes and for X.509 certificates. A TLS fingerprint is a compact summary of how a client or server chooses to talk: which versions, ciphers and extensions it offers, and in what order. That is why a pcap can tell you which software made a connection even though the payload is encrypted. The JSON pipes straight into jq, so the handshake becomes something you can filter and query.

## Install

```
brew install ssldump
# live capture needs elevated privileges, so run it with sudo; reading a pcap file does not
```

## Try this

```
ssldump --help
```
Lists the capture, decryption and output options.

```
./ssldump -j -ANH -n -i any | jq
```
Captures on all interfaces and pretty-prints each handshake as JSON, with JA3 and FAN/1 fingerprints where present.

```
./ssldump -r yourcapture.pcap -j | jq 'select(.fan1_tls_fp != null or .cert_chain != null) | {handshake_type, fan1_tls_features, fan1_tls_fp, cert_chain}'
```
Reads a saved pcap and pulls out just the TLS and certificate fingerprint fields.

## What's unique

Most TLS tools show a decoded handshake or compute a fingerprint, not both. This fork gives a record-level view and JA3/FAN/1 fingerprints in one pass, as JSON.

## Caveats

It is old code (SSLDUMP 0.9b3 plus patches) and the homepage's own brew line is a build recipe, not a documented formula. The homepage's ja3er.com example has nested single quotes that will not parse as written, and decrypting traffic needs keying material you supply.

## Links

- [Project homepage](https://adulau.github.io/ssldump/)
- [GitHub repository](https://github.com/adulau/ssldump)
- [ja3er.com (JA3 hash lookup used in the homepage example)](https://ja3er.com)
