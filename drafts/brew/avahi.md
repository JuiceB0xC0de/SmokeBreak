---
name: avahi
title: Avahi
source: brew
category: fundamentals
commitment: quick
tags: [dns-sd, linux, mdns, network, protocol, quick, zeroconf]
homepage: https://avahi.org
scout_score: 6
status: draft
---

# Avahi

**TLDR;** Avahi is the Linux implementation of mDNS and DNS-SD, the Bonjour-style protocols that let machines announce and find printers, shares and .local names.

Avahi is a free, LGPL implementation of DNS Service Discovery (RFC 6763) over Multicast DNS (RFC 6762). It is compatible with Apple Bonjour and aimed mainly at Linux. A daemon, avahi-daemon, listens to the local network, hears what other machines announce, and makes it visible to programs on your machine. It also announces what your machine offers.

The homepage describes the goal as plugging a laptop into a network and instantly seeing other people to chat with, printers to print to, and shared files, the way Bonjour does on macOS. It ships by default in most Linux distributions, so it is probably already running on a Linux machine near you.

The idea underneath is that discovery needs no central server. Hosts ask questions to a multicast address and answer for themselves. That is why `.local` names and "find a printer" menus work on a home network with no configuration. Avahi exposes this through D-Bus, which is its primary API, and through a set of command-line tools such as avahi-browse and avahi-publish-service.

You can also advertise a service with no code at all: drop an XML service definition into /etc/avahi/services. For `.local` lookups to work in ordinary programs, the separate nss-mdns project hooks into nsswitch.

## Install

```
brew install avahi
# Needs D-Bus for most uses. Linux is the primary target; the formula depends on systemd. For .local lookups in ordinary programs, the separate nss-mdns project is also needed.
```

## Try this

```
avahi-browse --help
```
Shows the options for browsing services announced on the local network.

```
avahi-publish-service --help
```
Shows how to advertise a service of your own over mDNS/DNS-SD.

```
avahi-resolve-host-name --help
```
Shows how to resolve a host name through mDNS.

## What's unique

It is a plain, open implementation of the discovery protocols Apple markets as Bonjour, already present on most Linux systems. Services can be advertised from a static XML file with no code.

## Caveats

Primarily for Linux and the main API needs a running D-Bus; the latest release, 0.8, is from 2020, and the README has no usage examples.

## Links

- [Avahi homepage](https://avahi.org)
- [Avahi source on GitHub](https://github.com/avahi/avahi)
- [nss-mdns project](https://github.com/avahi/nss-mdns)
