---
name: direwolf
title: Dire Wolf
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, aprs, audio, ax25, ham-radio, modem, needs-hardware, sdr]
homepage: https://github.com/wb2osz/direwolf
scout_score: 8
status: draft
---

# Dire Wolf

**TLDR;** A software modem that turns radio audio into AX.25 packets and APRS frames, replacing the 1980s hardware TNC with a soundcard and DSP.

Dire Wolf is a software TNC (terminal node controller) and packet modem for amateur radio. It listens to audio from a radio through a soundcard interface, or from SDR software such as gqrx, rtl_fm, or SDR#, and decodes AX.25 packets and APRS frames. It can also encode packets and send them back out through the radio. On its own it can act as an APRS tracker, digipeater, Internet gateway (IGate), or APRStt gateway. It can also serve as a virtual TNC for programs like Xastir, YAAC, and Winlink Express over KISS or AGW interfaces.

The README frames it as a replacement for the hardware TNCs of early packet radio: "Why waste $200 and settle for mediocre receive performance from a 1980's technology TNC using an old modem chip?" The modem work is done in software with digital signal processing. It supports 300 bps AFSK for HF, 1200 bps AFSK for VHF/UHF, 2400 and 4800 bps PSK, and 9600 bps GMSK/G3RUH, plus AIS and EAS SAME reception.

The idea underneath is that a modem is just a function from audio to bits. Once you see that, packet radio becomes something you can test and script. The package ships companion tools such as decode_aprs, gen_packets, atest, and kissutil, along with telemetry scripts and coordinate converters like ll2utm and utm2ll.

FX.25 is a notable design choice. It adds forward error correction in a way that ordinary AX.25 receivers simply ignore, so it stays backward compatible. Version 1.7 added IL2P, a different FEC scheme with less overhead, though it is not compatible with AX.25.

## Install

```
brew install direwolf
# The README itself documents a source build on macOS (brew install cmake portaudio hidapi, then git clone, cmake, make) and does not mention a brew install direwolf line. The Homebrew formula exists, but the source build is the README's recommended route.
# Real use needs a radio interface (a soundcard link or a USB adapter such as a SignaLink, DRAWS, or CM108-based interface) or SDR software feeding audio in.
```

## Try this

```
direwolf --help
```
Prints the command line options for the modem and its APRS functions.

```
gen_packets --help
```
Shows how to generate test packet audio, so you can hear what AX.25 sounds like without a radio.

```
decode_aprs --help
```
Shows how to decode APRS frames into readable fields.

## What's unique

It makes the case that soundcard DSP can beat dedicated TNC hardware at receiving packets. FX.25 adds error correction that plain AX.25 receivers can ignore.

## Caveats

Getting real packets needs a radio or SDR audio source, and the README says macOS support depends on volunteers and the author does not own a Mac. The benchmark claims are the author's own.

## Links

- [Project homepage (GitHub README)](https://github.com/wb2osz/direwolf)
- [Stable documentation (User Guide in doc directory)](https://github.com/wb2osz/direwolf/tree/master/doc)
- [Releases](https://github.com/wb2osz/direwolf/releases)
