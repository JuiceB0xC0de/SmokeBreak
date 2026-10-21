---
name: rdap
title: rdap
source: brew
category: fundamentals
commitment: quick
tags: [dns, go, network, protocol, quick, rdap, whois]
homepage: https://www.openrdap.org
scout_score: 6
status: draft
---

# rdap

**TLDR;** A small Go client for RDAP, the JSON-over-HTTP successor to WHOIS, that finds the right registry server for a domain, IP or AS number on its own.

OpenRDAP is a command line client for the Registration Data Access Protocol. You hand it a domain, an IP address, an AS number or an entity tag, and it fetches the registration record over HTTP. Output can be text, raw JSON, or WHOIS-style text for domain queries.

RDAP exists as a replacement for WHOIS. In the project's words, it "provides domain name & IP address registration information in JSON format over HTTP." WHOIS is a plain-text protocol with no fixed format, so every registry words its answers differently. RDAP gives structured data that programs can read.

The interesting part is how the client knows who to ask. It detects the query type from your input, then looks up the authoritative server in bootstrap data published by IANA. That means `rdap example.com` works without you knowing which registry runs the zone. You can cache the bootstrap files on disk, or name a server yourself with `-s`.

The same project also offers a Go library and a public RDAP service at rdap.net. Using the tool is a quick way to see how the internet's registration data is split between registries, and how a lookup gets routed.

## Install

```
Homebrew lists a formula named rdap, but the project's own README installs with Go instead. It requires Go 1.20 or later:

go install github.com/openrdap/rdap/cmd/rdap@master

The binary lands in your Go bin directory (the README says $GOPATH/go/bin, for example ~/go/bin/rdap).
```

## Try this

```
~/go/bin/rdap google.com
```
Looks up a domain with default output, with the registry server found automatically through IANA bootstrap data.

```
rdap --json AS15169
```
Fetches the record for an autonomous system number and prints the raw RDAP JSON.

```
rdap -v -t nameserver -s https://rdap.verisign.com/com/v1 ns1.google.com
```
Queries a nameserver on an explicitly named server, as the README requires for advanced query types.

## What's unique

Automatic server discovery through IANA bootstrap data means you never need to know which registry to ask. One small binary covers the RDAP query types and can still print WHOIS-style text.

## Caveats

Maintenance status is unclear from the README and homepage, search queries like abc*.com need an explicit -s server, and not every server supports every query type.

## Links

- [OpenRDAP homepage](https://www.openrdap.org)
- [Live demo](https://www.openrdap.org/demo)
- [GitHub repository](https://github.com/openrdap/rdap)
- [Manual and docs](https://www.openrdap.org/docs)
- [Go package docs (godoc)](https://godoc.org/github.com/openrdap/rdap)
