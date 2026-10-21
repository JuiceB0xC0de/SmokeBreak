---
name: dns2tcp
title: dns2tcp
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, dns, network, protocol, tunnel]
homepage: https://packages.debian.org/sid/dns2tcp
scout_score: 8
status: draft
---

# dns2tcp

**TLDR;** A client and server pair that wrap a TCP session inside DNS queries and replies, showing how a name lookup can carry arbitrary traffic.

dns2tcp is a set of tools that encapsulate a TCP session in DNS packets. Homebrew installs two executables: `dns2tcpc`, the client, and `dns2tcpd`, the server. The Debian description notes that the client does not need root privileges.

The design choice the package text highlights is carrying TCP directly, rather than tunnelling whole IP packets over DNS. In its words, "This type of encapsulation generates smaller packets than IP-over-DNS, improving throughput." The brief does not explain the mechanism in more detail, so how data is packed into queries and replies is something to find out by reading the source or running it.

The idea underneath is that DNS is a protocol almost every network lets through, and that its queries and answers are just structured bytes that can hold something else. Poking at a tunnel like this is a good way to learn what DNS messages look like on the wire and why a resolver chain can end up relaying traffic it was never meant to. The usual motivation is getting past restrictive networks, though the package text does not say so directly.

The homepage listed is a Debian package page with no usage docs, so expect to work from the man pages and source after install.

## Install

```
brew install dns2tcp
```

## Try this

```
dns2tcpc --help
```
Prints the client's options so you can see what it needs to reach a server.

```
dns2tcpd --help
```
Prints the server's options, showing how it is started and configured.

## What's unique

It tunnels a TCP session directly instead of full IP-over-DNS, which the Debian description says gives smaller packets and better throughput. The client runs without root.

## Caveats

The only source behind this entry is the Debian package description; no usage docs were found, the upstream site could not be confirmed, and upstream activity is unknown.

## Links

- [Debian package page (homepage)](https://packages.debian.org/sid/dns2tcp)
