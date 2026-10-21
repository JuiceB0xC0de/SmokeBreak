---
name: certgraph
title: certgraph
source: brew
category: fundamentals
commitment: quick
tags: [certificates, dns, network, protocol, quick, tls]
homepage: https://lanrat.github.io/certgraph/
scout_score: 7
status: draft
---

# certgraph

**TLDR;** Give it one hostname and it follows the names inside TLS certificates from site to site, building a graph of domains that share certificates.

CertGraph is a command-line crawler written in Go. You hand it a hostname, it fetches that host's TLS certificate, reads the Subject Alternative Names listed inside, and then visits each of those names in turn. Each domain becomes a node, and each certificate name becomes an edge to another node. New domains print as they are found. With `-details`, it ends by printing the adjacency list: node, depth, status, and certificate fingerprint.

The README says it was designed for host name enumeration via SSL certificates, but it can also show "a chain of trust between domains and the certificates that re-used between them." A certificate is usually thought of as a lock on one site. Here it is a link between sites, and following the links shows which hostnames an operator has tied together, sometimes including ones nobody advertises.

By default it connects to each host over HTTPS, or over SMTP with STARTTLS. Two other drivers, crtsh and censys, query Certificate Transparency logs instead. The README says no packets are sent to the target domains with those drivers, so you can map a domain from public records alone. The crawl is breadth-first, to a depth of 5 by default, with 10 fetches at a time.

The README also applies the graph to dangling certificates, the BygoneSSL problem, where a certificate still names a domain that has since changed hands. It gives recipes for checking your own domains.

## Install

```
brew install certgraph
# The censys driver needs Censys API credentials (-censys-appid and -censys-secret). The default http driver needs nothing.
```

## Try this

```
certgraph -details eff.org
```
Crawls eff.org through certificate names and prints one line per domain with depth, status, and certificate fingerprint.

```
certgraph --serve 127.0.0.1:8080
```
Starts the embedded web server so you can use the graph UI locally.

```
certgraph --help
```
Lists the drivers and options, including depth, parallelism, and the Certificate Transparency drivers.

## What's unique

Most certificate tools inspect one host. This one treats the SAN list as edges in a graph and crawls it, and it can do so from Certificate Transparency logs without touching the targets.

## Caveats

The default http and smtp drivers connect to every host they find, which can be noticed, and the project's status is unconfirmed since the fetched pages showed no release date.

## Links

- [Web UI homepage (GitHub Pages)](https://lanrat.github.io/certgraph/)
- [Source repository and README](https://github.com/lanrat/certgraph)
- [Blog post with more information](https://lanrat.com/certgraph/)
