---
name: bgpq4
title: bgpq4
source: brew
category: fundamentals
commitment: quick
tags: [bgp, irr, network, protocol, quick, routing]
homepage: https://github.com/bgp/bgpq4
scout_score: 6
status: draft
---

# bgpq4

**TLDR;** Turns Internet Routing Registry data into router filter configs, a way to see how the internet decides which networks to believe.

bgpq4 takes an AS number, an AS-SET, or a route-set, asks an IRRd server what prefixes belong to it, and prints a filter list. The default server is rr.ntt.net, and `-h` points it elsewhere. Output is Cisco IOS by default. Flags switch it to Juniper, OpenBGPD, BIRD, Arista EOS, Mikrotik, Nokia, Huawei or IOS XR syntax.

The idea underneath is how BGP, the protocol that stitches networks together, stays sane. Anyone can announce anything, so operators filter what they accept from customers and peers. The README describes the tool as being used to generate configurations "based on IRR data", meant to replace hand-built customer filters with lists generated from registry route objects. AS-SETs are expanded recursively into their member prefixes, then optionally aggregated or trimmed by prefix length.

The interesting part is trust. The README notes that "By default bgpq4 trusts data from all databases mirrored into NTT's IRR service", and says the RIR-maintained databases should be trusted more than the others. The `-S` flag limits which sources are used, and `SOURCE::OBJECT` notation sets the source for a single object. It warns against ARIN-NONAUTH and RIPE-NONAUTH. Running the same query with different sources shows how much routing data is stale or self-asserted.

The `-F` format option takes a template, so output does not have to be router config. The README's example emits FreeBSD ipfw rules.

## Install

```
brew install bgpq4
# Needs network access to an IRRd server (default rr.ntt.net). No account or hardware needed.
```

## Try this

```
bgpq4 -Jl eltel AS20597
```
Prints a Juniper prefix-list named eltel for the prefixes registered to AS20597.

```
bgpq4 -6l as-retn-6 AS-RETN6
```
Expands the AS-RETN6 AS-SET and prints an IPv6 Cisco prefix-list.

```
bgpq4 -S RIPE AS-VOSTRON
```
Restricts all lookups to the RIPE database, so the list reflects only RIPE route objects.

## What's unique

It covers a long list of router vendors plus a free-form template, and its documentation spends real effort on which registry data to trust.

## Caveats

Results are only as good as the registry data, which can be stale or wrong, and they depend on the IRR server you query.

## Links

- [GitHub repository and README](https://github.com/bgp/bgpq4)
- [NLNOG BGP Filter Guide](http://bgpfilterguide.nlnog.net/)
- [Container image on GitHub Container Registry](https://github.com/bgp/bgpq4/pkgs/container/bgpq4)
- [BGPQ4 mailing list](https://tcp0.com/cgi-bin/mailman/listinfo/bgpq4)
