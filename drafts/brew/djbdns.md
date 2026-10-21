---
name: djbdns
title: djbdns
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, dns, network, old, protocol, unix]
homepage: https://cr.yp.to/djbdns.html
scout_score: 6
status: draft
---

# djbdns

**TLDR;** D. J. Bernstein's DNS suite: a caching resolver, authoritative servers and lookup tools, built as small separate programs with security as the stated concern.

djbdns is a set of DNS programs written by D. J. Bernstein. `dnscache` is a caching resolver. `tinydns` is an authoritative server, fed by `tinydns-data` and `tinydns-edit`. `axfrdns` and `axfr-get` handle zone transfers. `walldns` and `rbldns` are narrower servers. A pile of small command-line tools (`dnsq`, `dnsip`, `dnsmx`, `dnstxt`, `dnstrace`) lets you ask DNS questions and watch the answers.

The homepage is a table of contents with no summary, but the page titles show what the author cared about: 'The djbdns security guarantee', 'The importance of separating DNS caches from DNS servers', and 'The libresolv security disaster'. The suite splits the jobs of resolving and serving into different programs instead of one daemon doing everything. The brief did not cover the mechanism in detail, so read those pages for the argument.

The door here is the structure of DNS itself. Because the roles are separate, you can learn what a cache does, what an authoritative server does, and what a zone transfer is, one executable at a time. The servers run as services under `daemontools` and `ucspi-tcp`, which are the dependencies, and which are a small tour of the author's way of building Unix software.

It is old. The install page calls djbdns-1.05 the 'latest published' package, and the pages carry no release date. That does not stop it from being readable as a design.

## Install

```
brew install djbdns
# pulls in daemontools and ucspi-tcp. The upstream install is a manual source build (make, then make setup check as root) under /usr/local, and the install page says it works only under UNIX.
```

## Try this

```
dnsq --help
```
Prints usage for the low-level query tool, which sends a single DNS query and shows the raw answer.

```
dnsip --help
```
Shows usage for the tool that looks up IP addresses for host names.

```
dnstrace --help
```
Shows usage for the tool that traces how a name is resolved down from the root servers.

## What's unique

It splits DNS into small single-purpose programs with the security argument written up on the project's own site, including pages critiquing other DNS software.

## Caveats

Old and quiet, with no release date on the pages read, UNIX only, no warranty beyond its security guarantee, and the upstream install is manual rather than through a package manager.

## Links

- [djbdns homepage](https://cr.yp.to/djbdns.html)
- [How to install djbdns](https://cr.yp.to/djbdns/install.html)
