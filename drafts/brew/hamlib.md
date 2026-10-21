---
name: hamlib
title: Hamlib
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, ham-radio, library, needs-hardware, radio, serial, tcp]
homepage: http://www.hamlib.org/
scout_score: 6
status: draft
---

# Hamlib

**TLDR;** One shared API and a set of command-line tools for controlling ham radio transceivers, rotators and amplifiers over serial, USB or a plain TCP socket.

Hamlib is a C library that gives programs one consistent way to talk to amateur radio gear. Each manufacturer has its own control protocol, usually spoken over a serial port. Hamlib puts a generic front-end API over per-model backends, one per protocol family, and maps common calls like "set frequency" onto whatever the device expects. Control can go over RS-232, USB-to-serial, or network connections.

The executables that Homebrew installs are the front ends. `rigctl` sends commands to a radio, `rotctl` does the same for antenna rotators, and `ampctl` for amplifiers. `rigctld` and `rotctld` are daemons that expose the same control over a TCP socket. The README says the daemon works with any language that can open a socket, "even netcat!" So a radio can be driven from a shell script.

The project exists so application authors can write radio-control software once instead of learning every vendor's protocol. In its own words, the aim is "stable, flexible, shared libraries that enable quicker development of amateur radio equipment control applications." The README also mentions distance, bearing and grid-square conversion helpers, and bindings for Perl, Python and TCL.

The idea underneath is that a radio is just a device with a serial protocol, and once that protocol is abstracted, a hobby becomes scriptable. The contributor model is part of the design too: support is added by writing backends and model definitions, and the project wants a device's protocol documentation to be public before it will support it.

## Install

```
brew install hamlib
# Controlling a real radio needs a supported transceiver, rotator or amplifier and a serial, USB or network connection to it.
```

## Try this

```
rigctl --help
```
Prints the options for the command-line radio controller, including how to pick a rig model and port.

```
rigctld --help
```
Shows how to start the TCP daemon that lets any program or netcat talk to a radio.

```
rotctl --help
```
Lists the options for controlling antenna rotators from the command line.

## What's unique

Radios, rotators and amplifiers sit behind a single API, and a plain TCP daemon makes them reachable from any language. The project also declines to support devices whose protocols are not publicly documented.

## Caveats

The README warns that Hamlib 5 changes on master will break compatibility with existing software, so stick with the 4.x releases; you also need compatible radio hardware and per-radio serial setup to do anything real.

## Links

- [Hamlib homepage](http://www.hamlib.org/)
- [GitHub repository](https://github.com/Hamlib/Hamlib)
- [API documentation (wiki)](https://github.com/Hamlib/Hamlib/wiki/Documentation)
- [Supported radios (wiki)](https://github.com/Hamlib/Hamlib/wiki)
