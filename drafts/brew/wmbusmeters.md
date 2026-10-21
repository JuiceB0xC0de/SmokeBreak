---
name: wmbusmeters
title: wmbusmeters
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, mqtt, needs-hardware, protocol, radio, sdr, utility-meters]
homepage: https://github.com/wmbusmeters/wmbusmeters
scout_score: 8
status: draft
---

# wmbusmeters

**TLDR;** Decodes wired and wireless M-Bus utility meter telegrams from radio dongles into readable fields, so you can read your own water or heat meter.

wmbusmeters takes raw telegrams from a radio dongle (im871a, iu891a, amb8465, cul, rc1180, or an rtl-sdr stick), a serial M-Bus converter, or a file, pipe, stdin or MQTT topic. It matches each telegram to a meter by id, picks a driver, and prints named fields as text, CSV or JSON. From there the readings can go to MQTT, a REST API, a database or plain files.

The interesting part is the drivers. A telegram is just bytes, and the README points out that a 32-bit signed volume in storage slot 1 means nothing until you know whether it is last month's billing reading or last year's gas delivered. The drivers supply that meaning. Its example turns the hex telegram `1844AE4C4455223368077A55000000_041389E20100023B0000` into a line with a water meter's id, total m3, flow and timestamp.

Since version 2.0 many drivers are declarative xmq/ixml text files rather than C++, and the maintainer says new drivers must be written that way. You can also add calculated fields using formulas that track SI units, or run a shell command with METER_ environment variables for each reading.

You can decode a single hex telegram from the command line with no hardware at all, which makes a decent first look at how these meters talk.

## Install

```
brew install wmbusmeters
# Real use needs hardware: a supported wM-Bus dongle, an rtl-sdr stick, or a serial M-Bus converter. For rtl-sdr, the rtl_sdr and rtl_wmbus binaries must be in /usr/bin or next to the wmbusmeters binary. The README recommends building from source (./configure; make; sudo make install, GNU/Linux only) because development moves fast.
```

## Try this

```
wmbusmeters 234433300602010014007a8e0000002f2f0efd3a1147000000008e40fd3a341200000000
```
Decodes one hex telegram with no config or hardware, printing the meter id, manufacturer and recommended driver (lansenpu in the README's example).

```
wmbusmeters --listdrivers=water
```
Searches the built-in meter drivers by keyword.

```
wmbusmeters auto:t1
```
Probes for any attached dongle and listens for T1-mode telegrams from meters in range.

## What's unique

Meter drivers are moving to editable declarative text files instead of C++. The project also promises that if you pin a named driver, the JSON keys will not change incompatibly on upgrade.

## Caveats

Real readings need a dongle, and encrypted meters need their own key, so this reads meters you have keys for, not arbitrary neighbours' meters.

## Links

- [GitHub repository (homepage)](https://github.com/wmbusmeters/wmbusmeters)
- [FAQ / wiki / manual](https://wmbusmeters.github.io/wmbusmeters-wiki/)
- [Run in the browser (serial ports)](https://wmbusmeters.org/inbrowser)
- [Releases](https://github.com/wmbusmeters/wmbusmeters/releases)
