---
name: picotool
title: picotool
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, firmware, microcontroller, needs-hardware, rp2040, rp2350, usb]
homepage: https://github.com/raspberrypi/picotool
scout_score: 6
status: draft
---

# picotool

**TLDR;** Raspberry Pi's official command-line tool for inspecting, flashing and reading back RP2040/RP2350 microcontroller binaries and the chips running them, over USB.

picotool does two jobs. Pointed at a file (ELF, UF2 or BIN), it prints what is inside, converts between formats, and for the RP2350 can seal, encrypt, build partition tables and link binaries. Pointed at a board in BOOTSEL mode, it can show info, load, save, verify, erase and reboot the chip, and read or write config and OTP memory.

The interesting idea is Binary Information. The Pico SDK can embed compact metadata in a firmware image: program name, build details, pin assignments. picotool reads it back, either from a .uf2 on disk or from a device that is plugged in. A firmware file stops being an opaque blob and becomes something that describes itself.

The RP2350 side goes further. The tool can touch OTP fuses, secure-boot partition tables, signature and hash metadata, and a self-decrypting binary option (`encrypt --embed`). That is a gentle way into how a microcontroller boots and decides what code to trust. It also replaces older SDK tooling: the README says `uf2 convert` takes over from the elf2uf2 functionality.

## Install

```
brew install picotool
# Needs a Raspberry Pi RP2040 or RP2350 board for device commands (BOOTSEL mode, or SDK USB stdio firmware with -f).
# File-only commands such as `info` on a .uf2 need no hardware.
```

## Try this

```
picotool help
```
Prints the general help and the list of commands.

```
picotool info -a lcd_1602_i2c.uf2
```
Reads a UF2 file you already have and shows its program, pin, and build info, with no board needed.

```
picotool save spoon.uf2
```
With a board in BOOTSEL mode, saves the installed program from its flash to a UF2 file.

## What's unique

It is the official tool, so it reads the SDK's embedded Binary Information and reaches RP2350 internals such as OTP, partition tables and signing that most people never see.

## Caveats

Most device commands need a board in BOOTSEL mode, and the README says the binary must be installed through cmake rather than copied onto PATH for the Pico SDK to find it.

## Links

- [GitHub repository (homepage)](https://github.com/raspberrypi/picotool)
- [Get started docs](https://rptl.io/pico-get-started)
- [pico-sdk-tools releases (pre-built binaries)](https://github.com/raspberrypi/pico-sdk-tools/releases)
