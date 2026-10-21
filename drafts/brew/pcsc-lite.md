---
name: pcsc-lite
title: pcsc-lite
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, apdu, needs-hardware, protocol, smartcard, usb]
homepage: https://pcsclite.apdu.fr/
scout_score: 6
status: draft
---

# pcsc-lite

**TLDR;** The open-source PC/SC daemon for smart card readers, with a spy mode that logs the raw APDU conversations between software and a card.

pcsc-lite is middleware that lets programs talk to smart card readers through the standard PC/SC API (the SCard functions). Applications call the API, and the pcscd daemon talks to the reader and its driver, usually over USB. What comes back are the card's responses to APDU commands, the small request and reply packets smart cards speak.

The project was started by David Corcoran in 1999, and Ludovic Rousseau has been the main author since 2001. The homepage presents it as a free, portable implementation of the PC/SC standard. Much Linux smart card tooling sits on top of it, so it is the layer between a card and whatever reads it.

The interesting part is the debugging. pcscd can run in the foreground with debug and APDU logging turned on, and pcsc-spy can watch the API calls an application makes. Together they show the conversation between software and a card, which most developers never see. The homepage also mentions that PC/SC clients and the server can run on two different hosts.

## Install

```
brew install pcsc-lite
Needs a USB smart card reader and a card to see anything real. On macOS the site says you should not need it, because Apple reimplemented PC/SC on top of CryptoTokenKit.
```

## Try this

```
pcscd --help
```
Lists the daemon's options, including the foreground and debug flags.

```
sudo LIBCCID_ifdLogLevel=0x000F pcscd --foreground --debug --apdu --color | tee -i log.txt
```
Runs the daemon in the foreground and prints every APDU exchange in color, saving it to log.txt. The site warns the log can contain your PIN.

```
pcsc-spy --help
```
Shows how to use the API spy that records the SCard calls an application makes.

## What's unique

It is the reference open-source PC/SC implementation on Linux, and it ships with a documented APDU logging mode and an API spy, so you can watch a smart card conversation directly.

## Caveats

You need a reader and a card for anything interesting to happen, the author does not test on the BSDs, and debug logs can leak your PIN.

## Links

- [Project homepage](https://pcsclite.apdu.fr/)
- [GitHub repository (README)](https://github.com/LudovicRousseau/PCSC)
