---
name: rtp2httpd
title: rtp2httpd
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, iptv, multicast, network, protocol, rtp, rtsp]
homepage: https://rtp2httpd.com
scout_score: 5
status: draft
---

# rtp2httpd

**TLDR;** A tiny C server that turns carrier multicast IPTV streams into plain HTTP, so any browser or player can watch what a set-top box would.

rtp2httpd joins multicast groups on an IPTV network, reads the RTP packets, puts out-of-order ones back in sequence, and re-serves the stream as ordinary HTTP unicast. It can also reverse-proxy HLS sources from an internal IPTV network out to a LAN or the internet. It ships with a web player, a status dashboard at `/status`, and M3U playlist generation at `/playlist.m3u`.

It exists because multicast television works nicely inside a carrier network and not at all in a browser. The README pitches it as a zero-dependency replacement for udpxy and msd_lite, small enough for routers, optical modems and NAS boxes. It is tuned for Chinese mainland IPTV, and the README is written in Chinese; English docs are at rtp2httpd.com/en/.

The idea underneath is how TV is delivered over IP. One sender, many receivers, with the network copying packets only where needed. The server also implements FCC (Fast Channel Change), where a carrier server hands the client an IDR frame at once so video appears without waiting for the next keyframe. That trick is usually locked inside set-top boxes. It can also apply Reed-Solomon FEC recovery when the upstream multicast supports it.

Internally it uses epoll-driven non-blocking IO, several worker processes sharing multicast subscriptions, and a preallocated buffer pool. The web player is pure front-end and does no transcoding, which keeps the server light.

## Install

```
brew install rtp2httpd
# Useful output needs a working multicast IPTV feed on your network. The brew install path was not verified; the project's own guides cover OpenWrt and other platforms: https://rtp2httpd.com/guide/installation
```

## Try this

```
rtp2httpd --help
```
Lists the server's command-line options so you can see how listening ports and config are set.

## What's unique

It carries carrier-grade fast channel change and Reed-Solomon FEC in a pure-C, zero-dependency binary of about 509KB with the web player bundled in. Most udpxy-style tools only forward packets.

## Caveats

Without a multicast IPTV feed there is nothing to watch, FCC needs a carrier FCC server, and the features are tuned for Chinese mainland IPTV; the benchmark figures are the author's own.

## Links

- [Project homepage and docs](https://rtp2httpd.com)
- [GitHub repository](https://github.com/stackia/rtp2httpd)
- [Performance benchmark report](https://rtp2httpd.com/reference/benchmark)
