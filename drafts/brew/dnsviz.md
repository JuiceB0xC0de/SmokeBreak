---
name: dnsviz
title: DNSViz
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, dns, dnssec, graphviz, network, protocol, visual]
homepage: https://github.com/dnsviz/dnsviz/
scout_score: 7
status: draft
---

# DNSViz

**TLDR;** Probes a domain's DNS and DNSSEC setup, then draws the chain of trust as a graph you can open, so you can see what resolvers check.

DNSViz is a suite of tools for analysing and visualising the Domain Name System, including its DNSSEC security extensions. One command, `dnsviz`, has subcommands that work as a pipeline. `probe` sends queries for one or more domain names to recursive servers (the default) or to authoritative ones, and writes everything it saw as JSON. `grok` assesses that data, and `graph` or `print` turn the result into an image, an interactive HTML page, or plain text. The README says the same suite powers the web analysis at dnsviz.net.

Keeping collection apart from analysis is the useful design choice. The raw queries and responses are saved, so one probe can be re-assessed or re-rendered later without touching the network again. `dnsviz query` wraps probe and print into a single dig-like step for quick looks.

The idea underneath is that DNSSEC is a chain of signatures from the root down through each delegation, and most people never see it. The graph makes that chain visible, and shows where it is intact, where it is broken, and which servers answered differently. There is also a pre-deployment mode: you supply zone files, server addresses, or future NS, glue and DS records on the command line, and check a change before it goes live. The README says it starts BIND's named to serve local zone files, so that mode needs BIND installed.

## Install

```
brew install dnsviz
Needs network access to send DNS queries. Testing zone files before deployment also needs ISC BIND. A Docker image is available as dnsviz/dnsviz.
```

## Try this

```
dnsviz probe example.com > example.com.json
```
Queries example.com through your configured resolvers and saves the queries and responses as JSON.

```
dnsviz graph -Tpng -o example.com.png example.com < example.com.json
```
Renders the analysis of the saved probe as a PNG graph.

```
dnsviz print < example.com.json
```
Prints the textual analysis of the same saved probe to the terminal.

## What's unique

It separates probing from analysis, so recorded DNS data can be re-graded later, and it can test future delegation and DS changes before they go live. The same code runs the public dnsviz.net service.

## Caveats

The README mainly covers Linux installs, Python 2.7 support is scheduled for removal, and Docker authoritative queries only work with --network host.

## Links

- [GitHub repository and README](https://github.com/dnsviz/dnsviz/)
- [DNSViz web analysis](https://dnsviz.net/)
- [Docker image](https://hub.docker.com/r/dnsviz/dnsviz)
