---
name: dhcpdump
title: dhcpdump
source: brew
category: fundamentals
commitment: quick
tags: [dhcp, network, packet-capture, protocol, quick]
homepage: https://github.com/dhcpdump-org/dhcpdump
scout_score: 6
status: draft
---

# dhcpdump

**TLDR;** A packet decoder that shows the DHCP conversation on your network, with a full-screen view that groups traffic by client and labels each lease's state.

dhcpdump reads DHCP packets, either live from a network interface or from a saved capture, and prints the decoded options as readable text. It also handles traffic tagged with VLAN 802.1Q and QinQ 802.1ad headers. DHCP is the protocol that hands your laptop an address when it joins a network, and normally it happens out of sight.

This repository is a fork of dhcpdump 1.8 by Edwin Groothuis. The README says it "collects in a single place bug-fixes and improvements collected over the last 10+ years", since the original had gone quiet. Many of those fixes harden the parser against out-of-bounds reads and stack overflows on crafted packets. That is a useful reminder that a decoder is a program that trusts strangers' bytes.

The newer addition is a full-screen, colour-coded view started with -t. It groups traffic by client, then by transaction ID (XID), and shows the message flow: DISCOVER, OFFER, REQUEST, ACK. From the messages seen so far, it derives a state such as waiting, offered, bound, NAK, or timed out. A lease that never completes shows up on one screen instead of being buried in a scrolling dump.

The idea underneath is that DHCP is a small four-step conversation, and once you can watch it you can see what a device does when it plugs in, reboots, or renews. The README also says the parser was split into a reusable decoder library separate from the command-line tool.

## Install

```
brew install dhcpdump
# The TUI depends on the yascreen library. To build from source without it: make NO_TUI=1
# The README does not say whether live capture needs root.
```

## Try this

```
dhcpdump --help
```
Prints the usage text and the flags your build supports.

```
dhcpdump -t -i <interface>
```
Starts the full-screen session view on a live interface, grouping DHCP traffic by client and transaction. Check the manual page for exact syntax.

```
dhcpdump -t -r <capture.pcap>
```
Opens a saved capture in the same session view so you can browse the exchanges at your own pace.

## What's unique

Most DHCP tools just print packets. This one groups them into per-client sessions and per-XID transactions and labels each state, which makes a stuck or misbehaving lease easy to spot.

## Caveats

The TUI exists only in the unreleased 2.00pre1 line, release dates are unclear from the README, and it does not say what privileges live capture needs.

## Links

- [GitHub repository (homepage)](https://github.com/dhcpdump-org/dhcpdump)
- [yascreen (TUI dependency)](https://github.com/bbonev/yascreen)
