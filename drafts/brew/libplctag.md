---
name: libplctag
title: libplctag
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, c-library, ethernet-ip, industrial, modbus, needs-hardware, plc, protocol]
homepage: https://github.com/libplctag/libplctag
scout_score: 5
status: draft
---

# libplctag

**TLDR;** A small C library that reads and writes tags on Allen-Bradley and Omron PLCs over Ethernet, a way into how industrial controllers talk.

libplctag is a pure C library that talks to programmable logic controllers over EtherNet/IP or Modbus TCP. You give it a tag name and a PLC address, and it hands back the value as an integer, float, bit, or an array of those. It supports Rockwell/Allen-Bradley ControlLogix, Micro850, PLC-5, SLC 500 and MicroLogix, plus Omron NX/NJ series.

The README frames it as a portable, simple API that avoids tying you to vendor tooling. It has been in production since early 2012, and the README says the API has seen almost no changes other than feature additions since then. It depends on nothing beyond libc (or musl) and pthreads on some platforms, and it is designed to be wrapped. Wrappers exist for .NET (libplctag.NET), Go, Java and Julia.

The idea underneath is that factory-floor equipment exposes its state as named variables on a network. Once you can read a tag, you can log it, graph it, or write it back. The README says it uses protocol-specific features for speed, including multiple requests per packet and packet size negotiation with newer ControlLogix firmware.

The Homebrew formula installs two executables, modbus_server and tag_rw2. The README does not describe either one, so check their `--help` output before assuming what they do.

## Install

```
brew install libplctag
# Talking to a real PLC needs one reachable on your network. Building and running the library itself does not.
```

## Try this

```
tag_rw2 --help
```
Prints the usage for the tag read/write tool so you can see what it expects.

```
modbus_server --help
```
Prints the usage for the bundled Modbus server executable.

## What's unique

It has been in production for over a decade with a very stable API, and it is the base for several language wrappers. It is dual licensed under MPL 2.0 or LGPL 2+, so it can go into both open and closed projects.

## Caveats

The README warns that PLCs control equipment and mistakes can cause loss of property, production or life, and the authors can't test every hardware model, so real use needs a PLC and care.

## Links

- [GitHub repository (homepage)](https://github.com/libplctag/libplctag)
- [Releases (pre-built binaries)](https://github.com/libplctag/libplctag/releases)
- [Examples directory (simple.c is the suggested start)](https://github.com/libplctag/libplctag/tree/release/src/examples)
- [API wiki](https://github.com/libplctag/libplctag/wiki/API)
