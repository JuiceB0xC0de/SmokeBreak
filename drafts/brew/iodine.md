---
name: iodine
title: iodine
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, dns, network, protocol, tun-tap, tunnel]
homepage: https://code.kryo.se/iodine
scout_score: 8
status: draft
---

# iodine

**TLDR;** iodine carries IPv4 traffic inside DNS queries and replies, turning a protocol meant for looking up names into a point-to-point network link.

iodine has two halves. You run `iodined` on a server you control, which owns a delegated subdomain and listens for DNS on UDP port 53. You run `iodine` on the client, which creates a TUN/TAP interface. Both ends share a password. The result is an IPv4 link that rides on whatever DNS the client can reach, even through a relaying resolver.

The README says it is usable where internet access is firewalled but DNS queries are allowed. Upstream data is encoded into the labels of DNS queries, using Base32, Base64, Base64u or Base128 depending on what the relay accepts. Downstream data comes back in replies, mainly as NULL or PRIVATE records, which carry data without encoding. The README says that gives over a kilobyte of payload per reply.

The clever part is what the README calls lazy mode. DNS is strictly question and answer, so a server cannot speak first. iodined holds each reply until the next query arrives, so it always has a query to answer, and the client sends periodic pings to keep that supply going. The client also probes the relay to find a workable fragment size and request type on its own.

The name is a pun, and the README spells it out: "it starts with IOD (IP Over DNS) and since iodine has atomic number 53, which happens to be the DNS port number." The tool is a good way to see how much a resolver chain will carry for you, and how DNS delegation actually works.

## Install

```
brew install iodine
# Needs a TUN/TAP device on every platform. On macOS 10.6+, pass -d utunX to use the built-in utun.
# A real setup needs a domain you control, with an NS delegation for a subdomain pointing at a host with a public IP.
# Windows needs the OpenVPN TAP32 driver.
```

## Try this

```
iodine --help
```
Lists the client options, including the -f, -r, -P, -T and -M flags the README mentions.

```
./iodined -f 10.0.0.1 test.com
```
The README's quickstart server on a LAN: runs in the foreground with tunnel address 10.0.0.1 for domain test.com and asks for a password.

```
./iodine -f -r 192.168.0.1 test.com
```
The matching quickstart client: runs in the foreground, forces DNS tunnelling with -r, and points at the server at 192.168.0.1.

## What's unique

It sends downstream data in NULL records without encoding, and its lazy replies and automatic probing of fragment size and request type make it much faster than typical DNS tunnels, per the README.

## Caveats

The tunnel is not encrypted, so the README recommends running a VPN or SSH inside it. Client and server must run the same version, some relays break NULL or TXT records, and a real run needs a domain you control. The latest release, 0.8.0, is from April 2023.

## Links

- [iodine homepage (kryo.se)](https://code.kryo.se/iodine)
- [GitHub repository (yarrick/iodine, README)](https://github.com/yarrick/iodine)
- [DNS setup check tool](https://code.kryo.se/iodine/check-it/)
