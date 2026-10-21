---
name: cdpr
title: cdpr
source: brew
category: fundamentals
commitment: quick
tags: [cdp, cisco, network, pcap, protocol, quick]
homepage: https://www.monkeymental.com/
scout_score: 7
status: draft
---

# cdpr

**TLDR;** Listens for the Cisco Discovery Protocol chatter your switch already broadcasts and tells you which switch and port your machine is plugged into.

CDPR (Cisco Discovery Protocol Reporter) passively listens on a network interface for CDP frames. Cisco switches broadcast these constantly so that neighbouring devices can learn who they are. CDPR decodes them and prints the neighbour's device ID, its IP address, and the port you are connected to.

In verbose mode it decodes the whole CDP packet, including details such as native VLAN and device capabilities. It can also report what it hears to a server, which lets you keep a running database of which devices sit on which switch ports, with no agent on the switches.

The idea underneath is that a lot of network gear announces itself all day to anyone who listens. Nothing needs to be probed or configured. Once you see one of these discovery protocols decoded, you start noticing how much of a LAN is neighbours quietly introducing themselves. The project's own line: "This software will tell you which switch and port your device is plugged into."

It is old. The SourceForge page was registered in 2003 and last updated in 2013. It comes from MonkeyMental, a small group writing tools for sysadmins, and the homepage says it has been extended at Cisco's request and is used in their labs.

## Install

```
brew install cdpr
# packet capture needs root: run it as `sudo cdpr`, or you get 'No interfaces found! Make sure pcap is installed.'
# you need to be on a network with a Cisco switch (or other gear sending CDP) to see anything
```

## Try this

```
cdpr --help
```
Prints the list of options, including the verbose and server-reporting modes.

```
sudo cdpr
```
Listens on the network interface and prints the neighbouring device ID, its IP address, and the port once a CDP frame arrives.

## What's unique

It answers one practical question, which switch port am I on, by reading broadcasts the switch was already sending. It can also log the answers centrally to build a device-to-port map.

## Caveats

Last updated in 2013, needs root and pcap, and only shows anything on networks where the switches actually send CDP; I could not confirm it works with current switch firmware.

## Links

- [MonkeyMental homepage](https://www.monkeymental.com/)
- [CDPR project page on SourceForge](https://sourceforge.net/projects/cdpr/)
