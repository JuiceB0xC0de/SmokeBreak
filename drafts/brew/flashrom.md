---
name: flashrom
title: flashrom
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, bios, firmware, needs-hardware, reverse-engineering, spi]
homepage: https://flashrom.org/
scout_score: 8
status: draft
---

# flashrom

**TLDR;** A command-line tool that identifies, reads, writes, verifies and erases the flash chips holding BIOS and firmware, on hundreds of boards and programmers.

flashrom talks to the firmware chip itself rather than to the operating system. Its README says it is built to flash BIOS, EFI, coreboot, firmware and option ROM images on mainboards, network, graphics and storage controller cards, and other programmer devices. It supports parallel, LPC, FWH and SPI interfaces and chip packages such as SOIC8, DIP8, TSOP and BGA. The README counts more than 627 flash chips, 407 chipsets and 539 mainboards.

The project pitches itself as a way to reflash firmware at scale without physical access: "No keyboard or monitor needed. Simply reflash remotely via SSH." You write and verify the image on a running machine, and the new firmware takes effect on the next boot. It also describes crossflashing and hotflashing as recovery techniques, and says it is faster than most vendor flash tools.

The idea underneath is that the firmware on your machine is just bytes on a small chip, and those bytes can be dumped, inspected and replaced. That is the starting point for firmware archaeology: read an image off a chip, back it up, and then open it in whatever binary analysis tools you like. The README does not explain the internals beyond naming the protocols. Root is usually enough, though some programmers do not need it.

## Install

```
brew install flashrom
Most real use needs hardware: either a supported mainboard (internal programmer) or an external programmer such as a USB device, plus root access in most cases. The formula pulls in libftdi, libjaylink, libusb and openssl.
```

## Try this

```
flashrom --help
```
Lists the available options and programmers, a quick way to see how wide the tool's hardware support is.

```
meson setup builddir
```
Configures a source build, the first step of the README's build path, if you want to compile flashrom yourself.

```
meson test -C builddir
```
Runs the project's test suite from a configured build directory, with no flash chip required.

## What's unique

It works on the firmware chip, not the OS, and one tool covers a very wide range of chips, chipsets and boards. The project's emergency instructions for a failed flash are unusually explicit for a command-line tool.

## Caveats

Writing to a flash chip can brick a machine; the README says to back up the chip first and not to use flashrom on laptops yet, since the embedded controller may interfere.

## Links

- [flashrom homepage (README)](https://flashrom.org/)
- [Official website](https://www.flashrom.org/)
- [Platform packaging list (repology)](https://repology.org)
