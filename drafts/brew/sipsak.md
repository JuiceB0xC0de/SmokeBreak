---
name: sipsak
title: sipsak
source: brew
category: fundamentals
commitment: quick
tags: [network, protocol, quick, sip, voip]
homepage: https://github.com/nils-ohlmeier/sipsak/
scout_score: 6
status: draft
---

# sipsak

**TLDR;** A command-line Swiss army knife for SIP, the signalling protocol behind VoIP calls, useful for poking at a SIP server from the terminal.

sipsak is a small C utility for talking SIP, the Session Initiation Protocol that sets up, rings, and tears down most VoIP calls. The project describes itself as a "SIP Swiss army knife". The scout's note says it is for probing VoIP servers, though the README read for this entry does not list features, inputs or outputs.

The README sends readers to the man page instead: "Please read the man page. It also contains some typical usage examples at the end." The man page could not be fetched for this entry, so the specific commands and options are unverified here. Start with the built-in help and the man page on your own machine.

The door it opens is SIP itself. Like HTTP, SIP is a text-based request and response protocol, so a tool that sends a single request and shows the reply is a good way to see how phone systems register, route, and answer. The optional build dependencies hint at the surrounding topics: OpenSSL or GnuTLS can supply MD5, which SIP digest authentication uses, and c-ares adds DNS SRV lookups, which SIP uses to find servers.

## Install

```
brew install sipsak
```

## Try this

```
sipsak --help
```
Prints the option summary, the quickest way to see what this tool can send.

## What's unique

It is a single small binary dedicated to SIP, so you can examine a VoIP server's behaviour without installing a softphone or a full telephony stack.

## Caveats

The README gives no release date or changelog, so maintenance status is unknown, and the sipsak.org domain now serves unrelated spam rather than the project.

## Links

- [GitHub repository (homepage)](https://github.com/nils-ohlmeier/sipsak/)
