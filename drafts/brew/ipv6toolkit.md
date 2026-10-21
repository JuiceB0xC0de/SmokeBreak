---
name: ipv6toolkit
title: ipv6toolkit
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, ipv6, network, packet-crafting, protocol, security]
homepage: https://www.si6networks.com/research/tools/ipv6toolkit/
scout_score: 7
status: draft
---

# ipv6toolkit

**TLDR;** Nineteen command-line tools that craft IPv6 packets by hand, so you can see how networks and devices react to Neighbor Discovery, fragments and extension headers.

The SI6 Networks IPv6 Toolkit is a set of small C programs, each built around one kind of IPv6 packet or test. There are tools for Neighbor Discovery (`ns6`, `na6`), Router Advertisements (`ra6`), ICMPv6 errors (`icmp6`), TCP and UDP (`tcp6`, `udp6`), fragmentation (`frag6`) and more. `addr6` analyses addresses, `scan6` scans for IPv6 hosts, and `path6` is a traceroute that understands extension headers and fragmentation.

It was written by Fernando Gont for SI6 Networks. The homepage says it is meant for security assessments of IPv6 networks, for testing device resilience "by performing real-world attacks against them", and for troubleshooting. The homepage also says development is partly funded by the company's IPv6 security training courses.

The idea underneath is that IPv6 moved a lot of work into protocols most people never look at: neighbour discovery replaces ARP, routers announce themselves unprompted, and extension headers chain together in ways middleboxes often mishandle. Each tool lets you send exactly one of those things and watch what comes back. `blackhole6`, for example, looks for where along a path packets with particular extension headers get dropped.

The tools send raw packets, so use them only on networks you are authorised to test.

## Install

```
brew install ipv6toolkit
# Upstream builds from source and needs libpcap. The brief did not confirm root requirements, but raw-packet tools will likely need elevated privileges.
```

## Try this

```
addr6 --help
```
Shows the options for the address analysis tool.

```
scan6 --help
```
Lists how to use the IPv6 address scanner.

```
path6 --help
```
Shows the options for the extension-header-aware traceroute.

## What's unique

It is built around protocol-level checks that general scanners and traceroutes rarely cover, such as Neighbor Discovery spoofing, Router Advertisement injection, and extension-header filtering. It is also the home of scan6, which the homepage calls "the most comprehensive IPv6 network scanning tool out there".

## Caveats

These are raw-packet security tools for networks you are authorised to test, and the brief could not confirm a last-release date, though the README lists tests on Ubuntu 24.04 and macOS 14.

## Links

- [SI6 Networks IPv6 Toolkit homepage](https://www.si6networks.com/research/tools/ipv6toolkit/)
- [GitHub repository (fgont/ipv6toolkit)](https://github.com/fgont/ipv6toolkit)
