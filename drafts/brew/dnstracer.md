---
name: dnstracer
title: dnstracer
source: brew
category: fundamentals
commitment: quick
tags: [debugging, dns, network, protocol, quick]
homepage: https://www.mavetju.org/unix/dnstracer.php
scout_score: 6
status: draft
---

# dnstracer

**TLDR;** Walks the DNS delegation chain from the root servers down to the authoritative one, printing every server it asks along the way.

dnstracer takes a domain name and follows the trail of referrals that DNS uses to find an answer. It starts at a resolver (127.0.0.1 by default), then asks the root servers, then the top-level domain servers, then the zone's own servers. Each server becomes a branch in a printed tree, with its name, its IP, and what kind of answer it gave.

The usual way to look up a name hides all of this: you ask one resolver and get one answer. Here you see the delegation happen. Each branch is marked as an authoritative answer, cached data, a lame server (one that is supposed to know the zone but does not), or nothing at all, shown as `* * *`. The author's own wording: "The *'s in the output means that there wasn't an answer on the request. By default there is three retries."

The author built it for debugging: finding where a server gets its information, and which server in a chain is broken or stale. As a side effect it works as a small lesson in how the DNS hierarchy is put together. Queries are not limited to A records. PTR, SOA and CNAME lookups work too, and `-s` lets you start the trace at a server you choose, where a dot means A.ROOT-SERVERS.NET.

## Install

```
brew install dnstracer
```

## Try this

```
dnstracer www.mavetju.org
```
Runs a full trace from your resolver through the root, .org and the zone's own servers. The author's example produced about 480 lines, so expect a lot of output.

```
dnstracer -o -s m.gtld-servers.net www.mavetju.org
```
Starts the trace at a named server and prints an overview of the answers received at the end, which keeps the output short.

```
dnstracer -q soa -o mavetju.org
```
Asks for the SOA record and shows the overview, which adds serial number, mname and rname fields.

## What's unique

Instead of asking one resolver for an answer, it shows the whole referral tree, with every server tried at each level and whether it answered authoritatively, from cache, or as a lame server.

## Caveats

The documentation is a single personal page whose examples date from around 2002, so the server names in them are old and output on a modern network will differ; current maintenance is unconfirmed.

## Links

- [Homepage and documentation (author's page)](https://www.mavetju.org/unix/dnstracer.php)
