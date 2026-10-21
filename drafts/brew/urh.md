---
name: urh
title: Universal Radio Hacker (urh)
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, gui, needs-hardware, protocols, reverse-engineering, sdr]
homepage: https://github.com/jopohl/urh
scout_score: 6
status: draft
---

# Universal Radio Hacker (urh)

**TLDR;** A GUI suite that turns raw SDR captures into readable bits, then helps you work out what the protocol fields mean.

Universal Radio Hacker, or URH, is a desktop application for figuring out how wireless devices talk. You feed it a signal from a software defined radio, or a saved capture, and it demodulates the signal. It detects the modulation parameters automatically, so you end up looking at bits and bytes rather than a waveform.

Once you have bits, the harder part starts. Transmitters often encode data before sending it, and URH has customizable decodings to undo that. The README names CC1101 data whitening as one example. From there you can label protocol fields and message types by hand, or let URH infer them with what the README calls rule-based intelligence. That inference is described in a USENIX WOOT'19 paper.

The idea underneath is that the radio side of reverse engineering is a pipeline: capture, demodulate, decode, find structure, then test your guess. URH puts each step in one place. It includes a fuzzing component for stateless protocols and a simulation environment for stateful ones, so you can replay and probe what you learned. The WOOT'18 paper describes it as a suite for analyzing and attacking stateful wireless protocols.

The Homebrew formula is marked deprecated, with a disable date of 2027-07-17. That is a packaging status, and the brief does not say the upstream project is dead. The PyPI install is the fallback.

## Install

```
brew install urh
# The formula is deprecated. On Linux the README recommends: pipx install urh
# Capturing live signals needs a supported SDR (the brew formula pulls in hackrf). Non-root access on Linux needs the udev rules from the wiki.
```

## Try this

```
urh
```
Launches the GUI, where you can open a capture file or connect an SDR and start demodulating.

```
urh_cli --help
```
Lists the options of the command-line binary that the formula installs alongside the GUI.

```
pipx install urh
```
Installs from PyPI with the native extensions precompiled, the README's recommended route on Linux.

## What's unique

Most tools in this space handle one step, such as capturing or decoding. URH covers demodulation, decoding, automatic field inference, fuzzing and stateful simulation in a single GUI.

## Caveats

The Homebrew formula is deprecated (disable date 2027-07-17), and live capture needs a supported SDR; you can still explore without one.

## Links

- [Homepage / GitHub repository](https://github.com/jopohl/urh)
- [Official userguide (PDF)](https://github.com/jopohl/urh/releases/download/v2.0.0/userguide.pdf)
- [Supported devices (wiki)](https://github.com/jopohl/urh/wiki/Supported-devices)
- [WOOT'18 paper](https://www.usenix.org/conference/woot18/presentation/pohl)
