---
name: hesiod
title: Hesiod
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, c-library, dns, historical, naming, protocol]
homepage: https://github.com/achernya/hesiod
scout_score: 5
status: draft
---

# Hesiod

**TLDR;** A 1980s naming service that stores plain-text lookups as ordinary DNS TXT records, so any DNS server can double as a tiny directory.

Hesiod is a small C library. A program hands it a name and a type, and the library turns that into a normal DNS query under a configured domain. The answer comes back as a text string, stored in a TXT record or in a CNAME that points at one. The README says it "can provide general name service for a variety of applications" and that it is based on BIND.

Setup is mostly DNS zone work. Each client reads a `hesiod.conf` with two settings: `rhs`, the domain suffix, and `lhs`, a label that defaults to `.ns`. The `HES_DOMAIN` environment variable can override `rhs`. Administrators make their name servers authoritative for `ns.your.domain` and load a zone file with records like `haynes.group` (TXT) and `2638.gid` (CNAME pointing at it).

The idea underneath is reuse. Instead of inventing a new server protocol for looking up things like users and groups, Hesiod treats DNS as a distributed key-value store that already runs everywhere. The README admits that the `.ns` label is "an unfortunate historical convention" and that ".hs" or "hesiod" would have been better.

The Homebrew package installs one executable, `hesinfo`. The README does not describe it, so treat it as something to explore with `--help`.

## Install

```
brew install hesiod
# Depends on libidn. No account or hardware needed.
# Real lookups need a hesiod.conf on the client and a DNS zone serving Hesiod TXT/CNAME records.
```

## Try this

```
hesinfo --help
```
Prints usage for the one executable Homebrew installs, which the README leaves undocumented.

```
./configure --help
```
If building from source, lists the configure options, including where hesiod.conf is expected.

## What's unique

It is a naming scheme that needs no new server protocol: the data lives in plain TXT and CNAME records on stock DNS servers. The README is candid about its own historical naming mistakes.

## Caveats

Release 3.2.1 shows no visible date, the README still references a retired Travis CI host and BIND-era named.boot configuration, and hesinfo is undocumented.

## Links

- [Project homepage (GitHub)](https://github.com/achernya/hesiod)
