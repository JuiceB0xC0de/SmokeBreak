---
name: pwnat
title: pwnat
source: brew
category: fundamentals
commitment: quick
tags: [icmp, nat, network, protocol, quick, udp]
homepage: https://samy.pl/pwnat/
scout_score: 7
status: draft
---

# pwnat

**TLDR;** A proxy that connects a client behind one NAT to a server behind another, with no port forwarding, no relay and no third party.

pwnat runs in two modes. The server sits behind its NAT and listens on a UDP proxy port (2222 by default). The client sits behind a different NAT, opens a local port, and names a remote host and port to reach. TCP services like HTTP or SSH can be tunnelled, because the traffic between the two ends travels as UDP. The README says the client can reach any host and port, or only a fixed destination the server chooses.

The trick is in how the two NATs learn about each other. The server repeatedly sends ICMP echo requests to 3.3.3.3, an address that will never answer, so its NAT keeps a translation entry for them. A client that wants in sends an ICMP Time Exceeded packet containing that same echo request. The server's NAT matches it to the entry and forwards it inward, and the server learns the client's public IP.

From there both sides send UDP packets to each other's public addresses. Each NAT sees inbound packets that look like replies to outbound ones, so the session opens from both directions. A zero-byte keep-alive goes out at least every 5 seconds when no other data is flowing. In the README's words, "The connection is entirely direct, client to server."

The project is a follow-on to Samy Kamkar's earlier chownat and to udptunnel by Daniel Meekins. It is worth reading as a short, plain-spoken case study in how stateful NATs can be talked into cooperating.

## Install

```
brew install pwnat
# the server needs a public address that clients can reach
```

## Try this

```
pwnat --help
```
Prints the usage line: pwnat <-s | -c> <args>, where -s is server mode and -c is client mode.

```
./pwnat -s
```
Starts the server side, allowing anyone to proxy through it since no allowed-host list is given.

```
./pwnat -c 8000 <pwnat.server.com> google.com 80
```
Starts a client listening on local port 8000 that forwards to google.com:80 through the pwnat server. Then browse to http://localhost:8000.

## What's unique

It gets NAT-to-NAT connectivity with no relay or helper server, by using an ICMP Time Exceeded packet to make the server's own NAT reveal the client's address.

## Caveats

The page is dated 2010, the README admits it works behind many NATs but not all, and it was only tested on Linux and OS X.

## Links

- [pwnat homepage and README (samy.pl)](https://samy.pl/pwnat/)
