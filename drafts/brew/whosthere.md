---
name: whosthere
title: whosthere
source: brew
category: fundamentals
commitment: quick
tags: [arp, go, mdns, network, protocol, quick, ssdp, tui]
homepage: https://github.com/ramonvermeulen/whosthere
scout_score: 6
status: draft
---

# whosthere

**TLDR;** A terminal UI that lists every device on your LAN by combining mDNS, SSDP and the ARP cache, with no root needed.

Whosthere is a LAN discovery tool written in Go. Run it and a terminal interface fills with the devices on your local network: phones, TVs, printers, laptops, whatever answers. Each one is tagged with a manufacturer name looked up from its MAC address prefix (the OUI). You can give devices aliases, search with regex, and switch themes.

Under the hood it runs three kinds of discovery at once. The mDNS and SSDP scanners listen for multicast announcements, the chatter devices make to advertise themselves. For the ARP part, it opens ordinary TCP and UDP connections to every address in the subnet. That makes the operating system resolve each address with ARP, and whosthere then reads the OS ARP cache to see which hosts are alive. In the README's words: "This technique populates the ARP cache without requiring elevated privileges."

That trick is the door into something larger. Tools like this normally send raw packets and need root. Here you can watch the same protocols from the outside: which devices announce themselves, which only show up in the ARP table, and what your home network says when nobody is asking. The README says it was made mainly for education and home network exploration.

Beyond the TUI there is a one-shot scan that prints results (optionally as JSON), and a daemon mode with a small HTTP API. Optional port scanning checks a configurable list of TCP ports on the devices it finds.

## Install

```
brew install whosthere
# alternatives: go install github.com/ramonvermeulen/whosthere@latest, or pre-built binaries from the GitHub releases page
# no elevated privileges needed; clipboard copy needs pbcopy, clip.exe, xsel/xclip or wl-copy
```

## Try this

```
whosthere
```
Opens the interactive TUI and starts discovering devices on your local network.

```
whosthere scan -t 5
```
Runs a single five-second scan and prints the devices it found.

```
whosthere scan -t 5 --json --pretty > devices.json
```
Does the same scan and saves the results as pretty-printed JSON.

## What's unique

It finds devices without root by letting the OS fill its ARP cache through ordinary connections, then reading the cache instead of sending raw ARP packets. It puts that together with mDNS and SSDP in a single TUI.

## Caveats

The README says results may not be comprehensive and it is not a professional monitoring tool; only scan devices you have permission to scan, and the maintenance status is unclear from the README.

## Links

- [Homepage and README (GitHub)](https://github.com/ramonvermeulen/whosthere)
- [Releases and pre-built binaries](https://github.com/ramonvermeulen/whosthere/releases)
- [Available themes (theme.go)](https://github.com/ramonvermeulen/whosthere/blob/main/internal/ui/theme/theme.go)
