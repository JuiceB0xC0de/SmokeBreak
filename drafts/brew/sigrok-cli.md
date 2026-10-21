---
name: sigrok-cli
title: sigrok-cli
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, logic-analyzer, needs-hardware, protocol-decoding, scripting]
homepage: https://sigrok.org/
scout_score: 8
status: draft
---

# sigrok-cli

**TLDR;** A command-line front end to sigrok that captures and decodes signals from logic analyzers, oscilloscopes and multimeters, built with scripting in mind.

sigrok-cli is a C program that gives the terminal access to sigrok, a free, cross-platform signal analysis suite. It sits on top of two libraries: libsigrok, which talks to the devices, and libsigrokdecode, which decodes captured signals. The README describes the result as "the basic sigrok functionality from the command-line."

Sigrok covers more than logic analyzers. The README names oscilloscopes and multimeters too, so the same tool is a door into a whole family of lab instruments. The README says it is "useful for scripting purposes," which points at capture and decode steps you can chain into automated pipelines instead of clicking through a GUI.

The idea underneath is protocol decoding. A logic analyzer records raw high and low voltages on wires; a decoder layer turns those into the bytes and messages that devices were actually exchanging. Seeing a real signal become readable data is the interesting part, and this is the terminal way in.

The brief could not confirm the command syntax or output format from the README, so the project's wiki page is the place to learn those.

## Install

```
brew install sigrok-cli

Pulls in libsigrok, libsigrokdecode, glib and gettext. To capture anything real you need a supported device, such as a logic analyzer, connected over USB or similar.
```

## Try this

```
sigrok-cli --help
```
Prints the options the tool supports, the quickest way to see what it can do.

## What's unique

It is a scriptable front end for a whole suite covering many instrument types, with protocol decoding built in rather than just raw capture.

## Caveats

Doing anything useful needs supported hardware, and the README gives no usage examples, so you will be reading the sigrok wiki to learn the commands.

## Links

- [Homepage](https://sigrok.org/)
- [sigrok-cli wiki page](http://sigrok.org/wiki/Sigrok-cli)
- [Building wiki page](http://sigrok.org/wiki/Building)
