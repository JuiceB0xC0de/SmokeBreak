---
name: nmrpflash
title: nmrpflash
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, firmware, needs-hardware, network, protocol, reverse-engineering, router]
homepage: https://github.com/jclehner/nmrpflash
scout_score: 6
status: draft
---

# nmrpflash

**TLDR;** Rescues bricked Netgear routers by impersonating the recovery server their bootloader listens for, then pushing a firmware image over Ethernet.

nmrpflash is a command-line tool that speaks NMRP, the recovery protocol built into the bootloader of many Netgear devices. You wire a computer directly to the router's LAN port, start the tool on that network interface, then power the router on. The bootloader asks for configuration, and nmrpflash answers.

It advertises itself as an NMRP server and assigns the router a temporary IP (by default 10.164.183.252, with the host at 10.164.183.253). When the router sends its upload request, the tool sends the firmware over TFTP and prints progress and keep-alive messages. Afterward the router may spend many minutes writing to flash. The tool prints "Reboot your device now." only when it is actually done.

The idea underneath is that a device you think is dead is often still running a small, stubbed-down first stage that waits for a very specific conversation on the wire. Once you know that handshake, you can talk to hardware that has no working operating system. The project links an archived write-up of the NMRP protocol, which makes it a good starting point for reading about how vendor recovery modes work.

It runs on Linux, macOS, Windows, the BSDs and other POSIX systems. The README has a long troubleshooting section that explains each error message and what to do about it.

## Install

```
brew install nmrpflash
# Needs a Netgear router, an Ethernet cable, and a firmware image (.chk, .bin, .trx or .img) extracted from Netgear's download zip.
# On Windows, install Npcap with 'WinPcap Compatibility' enabled; prebuilt binaries are on the GitHub releases page.
```

## Try this

```
nmrpflash -L
```
Lists the network interfaces on your machine so you can find the one wired to the router.

```
nmrpflash -i eth2 -f EX2700-V1.0.1.8.img
```
Waits on eth2 for the router to appear, then uploads the firmware. Turn the router off first, then power it on when 'Waiting for Ethernet connection' appears.

```
nmrpflash --help
```
Prints the available options.

## What's unique

It turns a router's built-in recovery mode into a scripted, cross-platform push by impersonating the recovery server and assigning addresses on both ends. The README's troubleshooting section is unusually practical.

## Caveats

Only tested on a specific list of Netgear models (others are 'likely' to work), flashing can take 15 minutes or more, TFTP uploads are limited to about 32 MiB, and the README says the bootloader itself may be bricked or lack NMRP support.

## Links

- [GitHub repository and README](https://github.com/jclehner/nmrpflash)
- [Latest release (prebuilt binaries)](https://github.com/jclehner/nmrpflash/releases/latest)
- [NMRP protocol write-up (archived)](https://web.archive.org/web/www.chubb.wattle.id.au/PeterChubb/nmrp.html)
