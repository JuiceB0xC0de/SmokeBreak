---
name: tracebox
title: tracebox
source: brew
category: fundamentals
commitment: quick
tags: [icmp, lua, middlebox, needs-root, network, protocol, quick, traceroute]
homepage: https://github.com/tracebox/tracebox
scout_score: 7
status: draft
---

# tracebox

**TLDR;** A traceroute that reports what changed your packets on the way, revealing hidden middleboxes like NATs, firewalls and proxies rewriting headers.

Tracebox sends probes with increasing TTL, the same trick traceroute uses. The difference is in what it reads back. When a router drops a packet because its TTL ran out, it sends an ICMP error that often quotes the original packet. Tracebox compares that quoted packet with the one it sent. Any difference in the headers or payload shows that something between you and that hop modified, added or removed fields.

The README says this works because some systems (Linux, Cisco IOS-XR) and MPLS routers return the full original datagram, rather than the minimum RFC 792 asks for. The ICMP Multi-Part Messages extension is another route to the same information. In the project's words, "Tracebox can be viewed as a tool similar to traceroute as it uses ICMP replies to identify changes in the packets."

The idea underneath is that the network path is not transparent. Devices in the middle quietly rewrite TCP options, sequence numbers and other fields, and you normally never see it. Tracebox gives a per-hop view of that, with no cooperation needed from the middlebox. It also ships a Lua API, exposed as the luatracebox executable, for scripting your own probes.

## Install

```
brew install tracebox
# needs root to run: use sudo. On older macOS (Yosemite, El Capitan) run xcode-select --install first.
# On Linux, build from source: ./bootstrap.sh, ./configure, make, make install (distro packages listed in the README).
```

## Try this

```
tracebox --help
```
Lists the options, including -j for JSON output, -m for maximum hops and -v for verbose detail.

```
man tracebox
```
Opens the manual page installed with the tool.

```
luatracebox --help
```
Shows how to run the Lua-scriptable version of the tool.

## What's unique

Ordinary traceroute tells you which routers are on the path. Tracebox tells you what was done to your packets along it, by reading the quoted copy that routers send back.

## Caveats

Needs root, and the README is dated: it mentions Yosemite, Fedora 24 and a possibly broken CircleCI link, while the OpenWRT package is marked unmaintained.

## Links

- [Project homepage (tracebox.org)](http://www.tracebox.org)
- [GitHub repository](https://github.com/tracebox/tracebox)
- [Lua API documentation](http://tracebox.org/lua_doc)
- [OpenWRT package repository](http://github.com/tracebox/openwrt)
