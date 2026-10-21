---
name: snort
title: Snort
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, ids, network, packets, pcap, rules]
homepage: https://www.snort.org
scout_score: 5
status: draft
---

# Snort

**TLDR;** Snort reads network packets, checks them against written rules, and raises alerts, a hands-on way to see how intrusion detection actually works.

Snort is an open source network intrusion detection and prevention system. It takes packets, either live from a network interface or from a saved pcap file, and compares them against rules that describe malicious activity. When a packet matches, it writes an alert. It can also run inline and drop matching packets, or act as a plain packet sniffer or logger for debugging traffic.

The idea underneath is that a rule is a small, readable description of what bad traffic looks like. Reading and writing those rules shows you how packets are structured, how services are recognised, and how detection gets tuned. Rules come as a free Community ruleset checked by Cisco Talos, a free Registered ruleset, and a paid Subscriber ruleset delivered in real time.

Snort 3 is configured with a Lua file, snort.lua, rather than the old Snort 2 config format. It supports multiple packet threads, detects services without needing port-based configuration, and has pluggable components. The Homebrew formula also installs snort2lua, which converts Snort 2 configs and rules to the new format, plus helpers for unified2 output (u2boat, u2spewfoo) and show_flows.

A good first session is offline: take a pcap you already have, run Snort over it, and see what it reports. No live network or privileges are needed for that.

## Install

```
brew install snort
# On macOS, Snort needs read access to the BPF devices for live capture:
sudo chmod o+r /dev/bpf*
# Rules: sign up at snort.org for an Oinkcode (the Registered ruleset is free).
```

## Try this

```
snort --help
```
Lists the command-line options of the installed binary.

```
snort -r a.pcap
```
Reads and examines a pcap file; replace a.pcap with your own capture.

```
snort -c $my_path/etc/snort/snort.lua -R $my_path/etc/snort/sample.rules -r a.pcap -A alert_test -n 100000
```
Runs in IDS mode over a pcap with the config and sample rules, writing alerts with the alert_test output. Set $my_path to your Snort install prefix, since the config and rules paths depend on it.

## What's unique

Snort 3 pairs a long-established rule-based IDS with a scriptable Lua config, multithreaded packet processing, and portless service detection. Its README even ships a libFuzzer setup, which is uncommon for an IDS.

## Caveats

The README looks dated in places, still citing a 3.0.0 alpha tarball, and the most current rules need a paid Subscriber ruleset; rule syntax also changed from Snort 2.

## Links

- [Snort homepage](https://www.snort.org)
- [Snort 3 source and README (GitHub)](https://github.com/snort3/snort3)
- [Snort 3 releases (GitHub)](https://github.com/snort3/snort3/releases)
