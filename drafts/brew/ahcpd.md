---
name: ahcpd
title: ahcpd
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, autoconfiguration, ipv6, mesh, network, protocol]
homepage: https://www.irif.fr/~jch/software/ahcp/
scout_score: 7
status: draft
---

# ahcpd

**TLDR;** A daemon that hands out IPv4, IPv6, DNS and NTP settings on mesh networks where DHCP and router discovery cannot reach every link.

ahcpd implements the Ad-Hoc Configuration Protocol (AHCP), an autoconfiguration protocol for IPv6 and dual-stack IPv6/IPv4 networks. One or more servers hold prefixes, name servers, NTP servers and a lease database. Clients on the link ask for settings and receive addresses within seconds.

It exists because, in the project's words, AHCP is meant to be used in place of router discovery and DHCP "on networks where it is difficult or impossible to configure a server within every link-layer broadcast domain, for example mobile ad-hoc networks." Wireless meshes break the assumption that one broadcast domain has one DHCP server. AHCP is built for that case, though it could also run on wired networks.

The design splits the work. ahcpd does not set default routes, because it is meant to run beside a routing protocol such as Babel or OLSR. Addressing is one problem, routing is another, and each gets its own protocol.

There is also a time-aware lease rule. The server checks the kernel for time synchronisation. Without it, the server hands out only short leases and is very conservative about releasing them. Leases depend on a trustworthy clock, and the daemon enforces that.

## Install

```
brew install ahcpd
# Servers need a config file at /etc/ahcpd.conf (mode server, prefix lines, lease-dir, name-server, ntp-server) and a writable lease directory. Clients must run as root. A routing protocol such as Babel or OLSR is needed alongside it for default routes.
```

## Try this

```
ahcpd --help
```
Prints the daemon's usage and options.

```
ahcpd -c /etc/ahcpd.conf wlan0
```
Runs ahcpd as an authoritative server on wlan0 using your configuration file.

```
# ahcpd wlan0
```
Runs ahcpd as a client on wlan0 with no config file, and should yield IPv4 and IPv6 addresses in a few seconds.

## What's unique

It lets a few servers in a mesh hand out addresses, DNS and NTP settings without router advertisements, and leaves routing to a separate protocol. Its rule that servers must show kernel time sync before granting long leases is unusual.

## Caveats

The protocol is a draft specification, no release or commit dates were found, and the author hopes to replace it with HNCP on his own network, so expect a quiet project.

## Links

- [AHCP homepage (author's software page)](https://www.irif.fr/~jch/software/ahcp/)
- [ahcpd source on GitHub](https://github.com/jech/ahcpd)
