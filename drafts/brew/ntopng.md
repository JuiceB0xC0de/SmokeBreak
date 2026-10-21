---
name: ntopng
title: ntopng
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, dpi, network, protocol, traffic-analysis, web-ui]
homepage: https://www.ntop.org/products/traffic-analysis/ntop/
scout_score: 5
status: draft
---

# ntopng

**TLDR;** A web-based traffic monitor that shows which hosts and application protocols are crossing your network, live, from a browser tab on port 3000.

ntopng is a network traffic probe with a web interface built in. It reads packets from an interface, or takes in flows from NetFlow, sFlow and IPFIX exporters, and shows top talkers, hosts, flows and alerts. It also identifies Layer-7 application protocols through nDPI, so you see 'TLS' or 'DNS' or a named service rather than just a port number.

It is the successor to ntop, which was written in 1998. The README calls ntopng 'the new incarnation of the original ntop written in 1998, and now revamped in terms of performance, usability, and features.' So the idea is old: put a tap or mirror port on a network and look at what is actually on the wire.

Under the hood it captures with libpcap, or PF_RING on Linux. Alternatively it receives flows over ZeroMQ from nProbe, a companion tool that collects flow data from routers and switches. Redis is the backing store and must be running. The web UI is served by ntopng itself, and a REST API lives under /lua/rest/, so you can query it with curl.

The door it opens is the protocol layer of your own network. Pointed at a home router's mirror port, or even just your own interface, it turns invisible background chatter such as DNS lookups, mDNS, TLS sessions and update checks into something you can sort and click through.

## Install

```
brew install ntopng
# Redis must be installed and running on the same host, or pass --redis to point at a remote one.
# Capturing packets usually needs root. The default web login is admin / admin, so change it.
```

## Try this

```
ntopng --help
```
Lists the options, including interface selection (-i), the web port (-w) and the Redis address (-r).

```
ntopng -i eth0 -i eth1 -i view:eth0,eth1
```
Monitors two interfaces separately and adds a virtual 'view' interface that merges both. Substitute your own interface names.

```
curl --cookie "user=admin; password=admin" "http://127.0.0.1:3000/lua/rest/get/interface/data.lua?ifid=0"
```
Asks the running instance for interface 0's data through the REST API, with no browser involved.

## What's unique

One binary works as both a packet-capturing probe and a flow collector, with a built-in browser UI and nDPI application detection. It can also merge several interfaces into a single virtual view.

## Caveats

The Community edition is free and aimed at small networks; some features such as LDAP and historical reports are paid-only under EULA terms, and Redis is a hard dependency.

## Links

- [Homepage (ntop.org product page)](https://www.ntop.org/products/traffic-analysis/ntop/)
- [GitHub repository](https://github.com/ntop/ntopng)
- [User's Guide](https://www.ntop.org/guides/ntopng/)
- [API documentation](https://www.ntop.org/guides/ntopng/api/index.html)
