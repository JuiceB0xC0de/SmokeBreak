---
name: knock
title: knock
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, firewall, libpcap, network, protocol, security]
homepage: https://github.com/jvinet/knock
scout_score: 6
status: draft
---

# knock

**TLDR;** A port-knocking server that sniffs raw packets for a secret sequence of port hits, then runs a command such as opening a firewall port.

knockd is the server half of port-knocking. It watches a network interface with libpcap for a configured sequence of connection attempts, called knocks. When it sees the right sequence from a client, it runs a command bound to that sequence. The `knock` client is a small program that sends the hits.

The trick is that knockd reads raw interface traffic instead of listening on sockets. In the README's words, "These port-hits need not be on open ports, since we use libpcap to sniff the raw interface traffic." The knocks can land on closed ports, so a port scan finds nothing, and the service behind the door stays invisible until someone knocks.

The README's example is a firewall with a DENY policy. A client sends four TCP SYN packets to a fixed sequence of ports. The server runs an iptables command that opens port 22 for that client. A second four-port sequence closes it again.

The underlying idea is older than this project, and the README points to other implementations such as doorman. It is a small way into how firewalls, packet sniffing, and hiding in plain sight fit together. The README does not document the config file format, so expect to read the man pages or source to get a working setup.

## Install

```
brew install knock
# Needs a firewall to act on. The README's example assumes Linux iptables. Building from source needs libpcap and autoconf.
```

## Try this

```
knock --help
```
Prints the client's usage, so you can see how a knock is sent to a host and a list of ports.

```
knockd --help
```
Lists the server's options for the daemon that sniffs the interface and runs your commands.

## What's unique

It sniffs raw traffic instead of listening on sockets, so the knocks can hit closed ports and the protected service never shows up in a scan.

## Caveats

The README is short and dated 2004, does not document the config format or client options, and the example assumes Linux iptables.

## Links

- [Homepage / README (GitHub)](https://github.com/jvinet/knock)
- [doorman (other implementation, linked from README)](http://doorman.sourceforge.net/)
- [sendip (advanced knock client, linked from README)](http://freshmeat.net/projects/sendip/)
