---
name: ser2net
title: ser2net
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, gensio, needs-hardware, network, protocol, serial]
homepage: https://ser2net.sourceforge.net/
scout_score: 6
status: draft
---

# ser2net

**TLDR;** A daemon that puts a serial port on the network, so a UPS, router console or old instrument can be reached with a TCP connection instead of a cable.

ser2net reads a YAML file that pairs an accepter with a connector. The accepter is something like a tcp or telnet listener on a port number. The connector is something like a serialdev with a device path and line settings such as 115200N81. When a client connects, ser2net opens the serial device and relays bytes both ways. The README says this generally means network connections to serial ports, or IPMI Serial Over LAN connections.

The author, Corey Minyard, started it in 2001 because, in his words: "I tried all the other ones I could find and found them lacking, so I wrote my own." The practical aim is to reach serial devices such as UPS units and old equipment from across a network without running a cable to your machine.

The idea underneath is the gensio library. The README calls ser2net "just a veneer over gensio (with a bunch of added features)". Gensio stacks connection layers, so the strings in the config pass almost directly into it. One line can add RFC 2217 remote control of baud and stop bits, TLS with client certificates, mDNS advertisement, or multiplexing. A serial line becomes something you can compose with the rest of the network stack.

The tool is a door into how serial links, telnet option negotiation and layered transports fit together. Following it leads to gensio itself, which is useful beyond serial work.

## Install

```
brew install ser2net
# then edit $HOMEBREW_PREFIX/etc/ser2net/ser2net.yaml
# you need a real serial device (USB adapter, console cable) to see anything useful
```

## Try this

```
ser2net --help
```
Lists the daemon's options, a quick look before you write any config.

```
gensiot tcp,host,3001
```
Connects from the command line to a plain TCP ser2net port. The README says not to use the telnet command for this.

```
gtlssh -m my-console
```
Connects by mDNS name to a connection called my-console on the local network, with no host or port needed.

## What's unique

It is not just a socket-to-tty bridge. It sits on a connection-stacking library, so one YAML line can add RFC 2217 control, TLS with client certificates, mDNS, or IPMI Serial Over LAN.

## Caveats

You need a serial device to get anything out of it, and ordinary ssh and telnet clients will not work with its encryption or RFC 2217 control; use gensiot or gtlssh.

## Links

- [Homepage](https://ser2net.sourceforge.net/)
- [GitHub repository and README](https://github.com/cminyard/ser2net)
- [SourceForge project page](https://sourceforge.net/projects/ser2net/)
- [gensio library (GitHub)](https://github.com/cminyard/gensio)
