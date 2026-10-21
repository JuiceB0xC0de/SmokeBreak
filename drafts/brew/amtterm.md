---
name: amtterm
title: amtterm
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, intel-amt, needs-hardware, network, protocol, serial]
homepage: https://www.kraxel.org/blog/linux/amtterm/
scout_score: 8
status: draft
---

# amtterm

**TLDR;** A serial-over-LAN client for Intel AMT, the out-of-band management channel built into some business PCs, with terminal and GTK front ends.

amtterm is a serial-over-LAN (SOL) client for Intel AMT, a management feature found in some Intel-based machines. SOL carries a machine's serial console over the network, so you can see and type into it without being at the keyboard.

The package installs four programs: amtterm, the terminal client; gamt, the graphical GTK version; amttool, a Perl script that, per the homepage, gathers information about AMT-managed computers and controls them remotely; and amtider, which the homepage does not describe.

The idea underneath is out-of-band management: a second, separate channel to a computer that exists apart from the operating system running on it. Reading how this client talks to that channel is a way into a corner of the network that most people never look at. The homepage is a short blurb and gives no motivation, so what follows is the shape of the idea rather than the author's own account.

## Install

```
brew install amtterm
Needs a target machine with Intel AMT enabled and reachable on the network. The homepage does not say what credentials or setup that requires.
```

## Try this

```
amtterm --help
```
Prints the terminal client's usage, the quickest way to see what it expects.

```
amttool --help
```
Shows what the information-gathering and remote-control script can do.

```
gamt --help
```
Shows the options for the graphical GTK client.

## What's unique

One package covers a terminal client, a GTK client and a scripting tool for the same management channel, which is rare for something this obscure.

## Caveats

Without an AMT-enabled machine you can only read help text, and the homepage gives no usage examples, supported hardware list or maintenance dates.

## Links

- [Homepage (kraxel's news, amtterm entry)](https://www.kraxel.org/blog/linux/amtterm/)
