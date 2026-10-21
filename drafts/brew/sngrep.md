---
name: sngrep
title: sngrep
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, network, protocol, sip, tui, voip]
homepage: https://github.com/irontec/sngrep
scout_score: 7
status: draft
---

# sngrep

**TLDR;** A terminal viewer that draws SIP call message flows, so you can see how a VoIP call is set up and torn down.

sngrep is a command-line tool for displaying SIP call message flows. SIP is the signalling protocol behind much of VoIP: the text messages that ring a phone, answer a call, and hang it up. sngrep shows those messages as calls and their flows in a terminal interface built on ncurses.

The idea underneath it is that VoIP signalling is plain, readable protocol traffic. Once you can see an INVITE, a ringing response, and an acknowledgement laid out in order, the machinery behind a phone call stops being a black box. It is also a practical way to see why a call failed to connect.

The brief could not read the project's README, so what input sngrep accepts (live capture, saved capture files, or both) and what permissions capture needs are unconfirmed here. Check `sngrep --help` after installing.

## Install

```
brew install sngrep
# Capturing live traffic usually needs elevated privileges; the brief could not confirm first-run details.
```

## Try this

```
sngrep --help
```
Prints the available options, including what input sources and filters the tool supports.

## What's unique

It turns SIP signalling into an interactive call-flow view in the terminal, rather than a pile of packet text.

## Caveats

The brief could not load the README or docs, so project status, input modes, and platform details are unverified.

## Links

- [GitHub homepage (irontec/sngrep)](https://github.com/irontec/sngrep)
