---
name: libnfc
title: libnfc
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, c, library, needs-hardware, nfc, protocol]
homepage: https://github.com/nfc-tools/libnfc
scout_score: 6
status: draft
---

# libnfc

**TLDR;** A C library and 21 command-line tools for talking directly to NFC readers, so you can list, poll, emulate and relay contactless tags yourself.

libnfc is a C library that gives userspace programs direct access to NFC reader hardware. A program opens a supported reader, sends it commands, and reads back what tags or other NFC devices answer. The README puts it plainly: "libnfc is a library which allows userspace application access to NFC devices."

The Homebrew formula also installs 21 tools built on the library. Some are simple: `nfc-list` finds tags in range, `nfc-poll` waits for them, and `nfc-scan-device` lists connected readers. Others go further: card emulation (`nfc-emulate-tag`, `nfc-emulate-uid`), relaying between devices (`nfc-relay`), MIFARE Classic and Ultralight tools, and `pn53x-tamashell`, a shell for the PN53x reader chip family.

The library talks to reader chips such as the PN53x/PN532 over USB, serial (for example `pn532_uart:/dev/ttyACM0`), or PC/SC middleware, depending on which drivers were built. A `libnfc.conf` file and a `devices.d` directory list the readers to use, and environment variables like `LIBNFC_DEVICE` and `LIBNFC_LOG_LEVEL` override them at runtime.

The idea underneath is that contactless cards and tags are small protocol endpoints you can speak to at the command level. Once you can send frames and see responses, access cards, transit tags and NFC stickers stop being opaque.

## Install

```
brew install libnfc

Requires a supported NFC reader (for example a PN53x/PN532-based USB or serial device, or a PC/SC reader). On Linux you may also need the udev rules from the source tree and to blacklist the kernel nfc/pn533 modules. Homebrew installs libusb-compat as a dependency.
```

## Try this

```
LIBNFC_AUTO_SCAN=true nfc-scan-device
```
Lists the names and connection strings of every NFC device it finds, which you need for configuration.

```
LIBNFC_LOG_LEVEL=3 nfc-list -v
```
Runs the tag lister with debug logging on, showing what the reader and library exchange.

```
nfc-poll --help
```
Shows the options for the tool that waits for a tag to appear at the reader.

## What's unique

It is a low-level reader SDK rather than a high-level wrapper, and its tools go past reading into card emulation, relay, MIFARE work and a PN53x diagnostic shell.

## Caveats

You need a supported NFC reader to do anything; the README covers POSIX only, the official website and forum are gone, and setup can involve udev rules, kernel module blacklisting and PC/SC tweaks.

## Links

- [GitHub repository (homepage)](https://github.com/nfc-tools/libnfc)
- [Releases](https://github.com/nfc-tools/libnfc/releases/)
- [Community page](http://www.libnfc.org/community)
