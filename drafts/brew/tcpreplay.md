---
name: tcpreplay
title: tcpreplay
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, network, packets, pcap, protocol, testing]
homepage: https://tcpreplay.appneta.com/
scout_score: 5
status: draft
---

# tcpreplay

**TLDR;** A suite that takes a saved packet capture, optionally rewrites its headers, and sends the packets back onto a live network at the speed you pick.

Tcpreplay reads a .pcap file from tcpdump, Wireshark or similar and puts the packets back on the wire. It can keep the original timing, send at a fixed rate in packets per second or Mbps, or go as fast as the hardware allows. The suite has seven executables, and the main tcpreplay binary is deliberately a lean engine that does no editing.

The reason it exists is that real network traffic is messy, bursty and hard to reproduce on demand. Capture a slice once, and you can replay the same packets with the same timing as often as you like. That makes it useful for benchmarking throughput, reproducing a bug, regression-testing a firewall rule, or pushing a NetFlow appliance hard.

The other tools fill in the pipeline. tcprewrite changes Layer 2 to 4 headers, tcpreplay-edit does the rewriting and replay in one pass, and tcpprep writes a cache file that classifies packets as client or server, which a two-NIC in-line test needs. tcpcapinfo inspects capture files, and tcpbridge bridges two networks.

tcpliveplay goes a step further. It replays a captured TCP session against a real server, so the whole stack up to the application answers instead of the traffic stopping at Layer 2. The 4.6 release also ships libtcpreplay, a static C library, so programs can embed the replay engine.

## Install

```
brew install tcpreplay
# Sending packets uses raw sockets, so run tcpreplay with sudo.
# You need a .pcap file to replay, for example one saved with tcpdump or Wireshark.
```

## Try this

```
tcpreplay --help
```
Lists the replay options, including timing, rate and interface controls.

```
sudo tcpreplay -i eth0 test.pcap
```
Replays test.pcap out of the eth0 interface. Substitute your own interface name and capture file.

```
sudo tcpreplay -i wg0 test.pcap
```
Replays onto a layer-3-only interface such as WireGuard. On Linux the Layer 2 headers are stripped automatically.

## What's unique

Replay is separated from editing, with tcprewrite, tcpprep and tcpliveplay as stages around it. tcpliveplay can make a real server answer a replayed TCP session, which plain replay tools usually cannot do.

## Caveats

Replaying needs root and puts real packets on a real network, so use a test interface, not the one you are SSHed in on. The netmap option in particular takes the interface's network stack offline while active.

## Links

- [Homepage and documentation](https://tcpreplay.appneta.com/)
- [GitHub repository](https://github.com/appneta/tcpreplay)
- [Releases](https://github.com/appneta/tcpreplay/releases)
