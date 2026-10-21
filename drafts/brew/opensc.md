---
name: opensc
title: OpenSC
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, apdu, crypto, needs-hardware, pkcs11, protocol, smart-cards]
homepage: https://github.com/OpenSC/OpenSC/wiki
scout_score: 5
status: draft
---

# OpenSC

**TLDR;** A toolkit of about two dozen command-line tools and libraries for talking to cryptographic smart cards, from listing their files to signing with their keys.

OpenSC is a set of libraries and utilities for working with smart cards, mainly cards that do cryptographic operations. Its stated aim is to make those cards usable in security applications such as authentication, mail encryption and digital signatures. It does this by implementing the standard smart card APIs: PKCS#11, the Windows Smart Card Minidriver, and macOS CryptoTokenKit.

The Homebrew formula installs a long list of tools. Some are general, like `opensc-tool`, `opensc-explorer`, `pkcs11-tool` and `pkcs15-tool`. Others are named for a specific card family, like `piv-tool`, `openpgp-tool`, `sc-hsm-tool` and `gids-tool`. The names suggest a toolbox for looking at what is on a card and what it can do, but the brief did not confirm the exact behavior of each tool.

The door it opens is the world under the card slot. A smart card is a tiny computer that answers structured commands (APDUs) and exposes a file system and key slots. The project's security history is tied to how that command and response data is handled, which shows how much parsing happens at that boundary. OpenSC is written by an international team of volunteers and is open source.

It is also a family. Sub-projects such as libp11, pkcs11-helper, PAM-PKCS#11, pam_p11, OpenCT and OpenSC-Java can be used on their own. The README lists a card support matrix covering CAC, SmartCard-HSM, PIV, OpenPGP, GIDS and Pico HSM.

## Install

```
brew install opensc
# Needs a smart card and a USB card reader to do anything interesting.
# Brew caveat: OpenSSH PKCS11 smartcard integration will not work with this formula. For that, unlink it and install the OpenSC cask.
```

## Try this

```
opensc-tool --help
```
Prints the options of the general-purpose card tool, a first look at what it can ask a reader and card.

```
pkcs11-tool --help
```
Lists the options for working with a card through the PKCS#11 interface.

```
opensc-explorer --help
```
Shows how to start the interactive explorer for browsing a card's contents.

## What's unique

It is a whole family of tools and libraries rather than one program, covering several platform smart card APIs and many card types at once.

## Caveats

It needs a smart card and reader to be worth much, versions before 0.27.0 have several security advisories, and the brew build lacks OpenSSH PKCS11 support.

## Links

- [OpenSC wiki (homepage)](https://github.com/OpenSC/OpenSC/wiki)
- [Repository and README](https://github.com/OpenSC/OpenSC)
- [Latest release](https://github.com/OpenSC/OpenSC/releases/latest)
