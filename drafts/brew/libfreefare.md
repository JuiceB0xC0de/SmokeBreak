---
name: libfreefare
title: libfreefare
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, c-library, mifare, needs-hardware, nfc, protocol, rfid]
homepage: https://github.com/nfc-tools/libfreefare
scout_score: 7
status: draft
---

# libfreefare

**TLDR;** A C library and set of command-line tools for talking to MIFARE contactless cards, the chips inside many access badges and transit tickets.

libfreefare is a C library for reading and manipulating MIFARE contactless smart cards. It sits on top of libnfc: an NFC reader is plugged in, a card is held to it, and libfreefare issues the card-specific commands. The README's feature matrix lists MIFARE Classic 1k and 4k, Mini, Ultralight and Ultralight C, DESFire (2k, 4k, 8k, EV1), FeliCa Lite and NTAG21x. MIFARE Plus is marked as not supported.

The Homebrew package installs a set of small tools named for the card family they target: `mifare-desfire-info`, `mifare-classic-format`, `mifare-classic-read-ndef`, `mifare-ultralight-info` and others. The names suggest they inspect cards, format them, and read or write NDEF data, plus a few DESFire EV1 configuration commands. The README does not document these tools, so the names are the best guide, along with their `--help` output.

The idea underneath is that the cards in your wallet are small, standardised computers with a command set, file layouts and key-based access control. The library also handles the Mifare Application Directory (MAD v1, v2 and v3), which is how several applications share one card. Building from source with `./configure --enable-debug` prints the traffic between the reader (PCD) and the card (PICC), which is a way to watch a card answer, byte by byte.

It is part of the wider nfc-tools family, and the README is short and points to the nfc-tools wiki for more.

## Install

```
brew install libfreefare
# Needs an NFC reader supported by libnfc, plus some cards to present to it. The README gives no reader model details.
```

## Try this

```
mifare-desfire-info --help
```
Shows the options for the DESFire inspection tool, the usual first step with a card on the reader.

```
mifare-ultralight-info --help
```
Shows how to query an Ultralight tag, the simple, cheap kind found in stickers and tickets.

```
mifare-classic-read-ndef --help
```
Shows how to read NDEF data from a MIFARE Classic card.

## What's unique

It covers the card side of the protocols, including DESFire, so you can work with the chips behind real access cards and tickets. A configure flag turns on reader-to-card transfer traces for studying how a card responds.

## Caveats

It needs an NFC reader that libnfc supports, the README has no usage docs for the command-line tools, MIFARE Plus is unsupported, and recent project activity could not be confirmed.

## Links

- [libfreefare on GitHub](https://github.com/nfc-tools/libfreefare)
- [nfc-tools project website and wiki](http://nfc-tools.org/)
- [libnfc (required dependency)](https://github.com/nfc-tools/libnfc)
