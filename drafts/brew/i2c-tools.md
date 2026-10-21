---
name: i2c-tools
title: i2c-tools
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, eeprom, i2c, linux, needs-hardware, protocol]
homepage: https://i2c.wiki.kernel.org/index.php/I2C_Tools
scout_score: 6
status: draft
---

# i2c-tools

**TLDR;** Command-line tools for scanning I2C buses, dumping chip registers, and decoding the EEPROMs inside your RAM sticks and monitor.

I2C is a two-wire bus that sits inside nearly every computer, running between chips that never show up as files or network ports. i2c-tools talks to those chips from user space through the Linux kernel's I2C support. You give it a bus number and a chip address, and it prints what answers: detected devices, register or EEPROM dumps, or the result of a write.

The package is a toolkit rather than a single program. `i2cdetect` probes a bus, `i2cdump` dumps a chip, and `i2cget` and `i2cset` read and write single registers. `i2ctransfer` handles raw transfers. `eeprog` programs EEPROMs. Several decoders turn raw bytes into something readable: `decode-dimms` for memory module data, `decode-edid` for monitor identification, and `decode-vaio` for Sony Vaio laptops. `i2c-stub-from-dump` is also included, but the brief does not say how it is used.

The tools were split out of lm-sensors because, in the wiki's words, "not all hardware monitoring chips are I2C devices, and not all I2C devices are hardware monitoring chips, so having everything in a single package was confusing and impractical." The idea underneath is that a lot of your hardware has a small, quiet management channel, and with the right address you can read it.

## Install

```
brew install i2c-tools
# Linux only: the kernel must have I2C support enabled. Real buses usually need root or device permissions (not confirmed in the brief). You need a machine with I2C buses to do anything useful.
```

## Try this

```
i2cdetect --help
```
Shows the options for scanning an I2C bus for responding devices.

```
i2cdump --help
```
Shows how to dump the registers of a chip given a bus number and address.

```
decode-dimms --help
```
Shows how to decode the memory module EEPROM data on your machine.

## What's unique

Most I2C probing tools handle one chip at a time. This one bundles bus scanning, raw register access, and decoders for formats like DIMM SPD and EDID monitor data in one toolkit.

## Caveats

Linux only, needs kernel I2C support, and the archived wiki may be outdated. Writing to real chips can affect hardware, and the pages I read describe no safety limits.

## Links

- [Homepage (archived Linux i2c wiki)](https://i2c.wiki.kernel.org/index.php/I2C_Tools)
- [Git repository (cgit web view)](https://git.kernel.org/pub/scm/utils/i2c-tools/i2c-tools.git/)
- [Release downloads (kernel.org)](https://www.kernel.org/pub/software/utils/i2c-tools/)
