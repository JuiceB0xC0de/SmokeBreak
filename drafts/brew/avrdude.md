---
name: avrdude
title: avrdude
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, arduino, avr, flashing, microcontrollers, needs-hardware]
homepage: https://www.nongnu.org/avrdude/
scout_score: 6
status: draft
---

# avrdude

**TLDR;** A command-line tool that writes compiled programs into the flash memory of AVR microcontrollers, the chips inside Arduino boards, through a physical programmer.

AVRDUDE (AVR Downloader Uploader) reads and writes the on-chip memories of Atmel/Microchip AVR microcontrollers. You hand it a compiled file (Intel Hex, Motorola S-Record or raw binary, with the format detected automatically on input) or values typed on the command line, and it sends them to the chip through a programmer. It can program Flash and EEPROM, and fuse and lock bits where the protocol allows.

It began as Brian S. Dean's private in-system programmer for AVR chips, written for FreeBSD under the name avrprog and renamed to avoid confusion with Atmel's tool. The README says it dates from 2003 and has been maintained by Jörg Wunsch since 2006. Much of what Arduino-style toolchains do at the moment of upload is this program.

The idea underneath is that a chip is just memory behind a wire protocol. You pick a programmer with `-c` and a part with `-p`, and avrdude speaks AVR in-system programming (ISP) to the target. Supported adapters range from bare parallel-port or serial-port plugs to STK500, AVR910-style devices and JTAG ICE mkII. Adapters are described in a plain text config file, so new parallel-port ones can be added without recompiling.

It also has a direct instruction mode that issues any programming instruction to the chip, even for features avrdude does not wrap for that part. That makes it a way to learn how these chips are programmed and fused, and a way to recover one you have misconfigured.

## Install

```
brew install avrdude
# Needs real hardware to do anything useful: an AVR chip or board (an Arduino Uno works) and a programmer or serial connection.
```

## Try this

```
avrdude
```
Run with no arguments, it prints the list of options, which is the quickest tour of what it can do.

```
avrdude -c <programmer> -p <part> -U flash:w:<file>:i
```
The README's template for writing a HEX file to flash: -c picks the programmer, -p the chip, -U the memory operation.

```
avrdude -c arduino -P COM1 -b 115200 -p atmega328p -D -U flash:w:objs/blink.hex:i
```
Flashes blink.hex to an Arduino Uno on a serial port at 115200 baud, with -D skipping auto-erase. Swap COM1 for your port name.

## What's unique

It drives many kinds of programmer from a text config file rather than code. Its direct instruction mode lets you send raw AVR programming commands the tool itself does not implement.

## Caveats

Needs a physical AVR chip and a programmer to do anything. The nongnu.org homepage was last modified in 2010 and is stale, so the GitHub README and docs are the current source.

## Links

- [Project homepage (nongnu.org)](https://www.nongnu.org/avrdude/)
- [Documentation (GitHub Pages)](https://avrdudes.github.io/avrdude/)
- [Source repository (GitHub)](https://github.com/avrdudes/avrdude)
