---
name: sipp
title: SIPp
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, network, protocol, sip, testing, voip]
homepage: https://sipp.sourceforge.net/
scout_score: 6
status: draft
---

# SIPp

**TLDR;** A traffic generator for SIP, the signalling protocol behind VoIP calls, that plays scripted XML call flows against real phone systems.

SIPp is a test tool for SIP, the protocol that sets up and tears down calls in VoIP systems and PBXes. It ships with basic user-agent scenarios that place calls with INVITE and end them with BYE. It can act as the caller, the callee, or both. It can also send RTP media, either by echoing it or by replaying a pcap file.

What it describes as its purpose: testing real SIP equipment such as proxies, B2BUAs, media servers, gateways and PBXes. In its own words, it is "very useful to emulate thousands of user agents calling your SIP system." It can also run one single call and exit with a passed or failed verdict, which makes it usable as a plain test.

The idea underneath is that a call is just a scripted conversation. Scenarios are XML files listing which messages to send and expect, over UDP, TCP, TLS or SCTP. Regular expressions pull fields out of received messages and feed them into later ones. CSV files supply per-user data. Reading a scenario file is a direct way to see what a phone call looks like on the wire.

While running, it shows live statistics in the terminal: call rate, round trip delay and message counts. It also writes periodic CSV dumps.

## Install

```
brew install sipp
```

## Try this

```
sipp --help
```
Prints the command line options, including the call rate, transport and scenario settings.

## What's unique

Call flows are plain XML with regex capture and re-injection, so one tool can play caller, callee, or load generator. It can also replay RTP media from pcap, and it doubles as a one-shot pass/fail test.

## Caveats

The homepage is dated and still lists v3.4 as current, while the GitHub master is 3.8.x; the brew formula's sipp-multi.py is not documented in what was reviewed, and you need a SIP system to test against to get much out of it.

## Links

- [Homepage](https://sipp.sourceforge.net/)
- [Documentation (html, readthedocs)](https://sipp3.readthedocs.io/en/latest/)
- [GitHub repository](https://github.com/SIPp/sipp)
- [Mailing list](https://lists.sourceforge.net/lists/listinfo/sipp-users)
