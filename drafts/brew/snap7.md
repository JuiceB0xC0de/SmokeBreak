---
name: snap7
title: Snap7
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, industrial, library, needs-hardware, network, plc, protocol]
homepage: https://snap7.sourceforge.net/
scout_score: 8
status: draft
---

# Snap7

**TLDR;** An Ethernet library that speaks the Siemens S7 protocol, so your own code can read and write memory in real factory PLCs, or in a fake one it hosts.

Snap7 is a native library that implements the S7 communication protocol over Ethernet. Siemens S7 PLCs are the industrial controllers that run assembly lines, pumps and building systems. Your program makes calls to read and write data blocks on the controller, and the library handles the network conversation.

It has three parts: Client, Server and Partner. The Client reads and writes a PLC. The Server pretends to be a PLC, so you can build and test without hardware. Partner is for peer-to-peer exchange, including the mode where the PLC pushes data when it chooses instead of waiting to be polled. Wrappers exist for C/C++, .NET/Mono, Pascal, LabVIEW and Python.

It exists so ordinary PC software can exchange data with S7 controllers without buying Siemens' own communication software. It is a community project by Davide Nardella, not an official Siemens product. The underlying idea is that industrial automation runs on documented-enough network protocols, and once you can speak one, a laptop or a Raspberry Pi becomes a peer of the machinery. The project says a full working server example is "not bigger than the 'Hello world'".

The Homebrew formula installs the library only. It has no executables, so you use it by writing code against it.

## Install

```
brew install snap7
# Installs the library only, with no executables. Talking to a real PLC needs a Siemens S7 controller reachable over Ethernet. The Server component can stand in for one.
```

## Try this

## What's unique

Client, Server and Partner live in one dependency-free library, so you can run both ends of an S7 conversation on a laptop. It also scales down to small ARM boards.

## Caveats

It talks to live industrial controllers, so test against the built-in server or a bench PLC first; the official homepage is an empty frameset, and Homebrew installs no command-line tools.

## Links

- [Snap7 homepage (frameset, no content)](https://snap7.sourceforge.net/)
- [SourceForge project page](https://sourceforge.net/projects/snap7/)
