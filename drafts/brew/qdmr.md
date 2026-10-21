---
name: qdmr
title: qdmr
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, cli, dmr, file-formats, gui, ham-radio, needs-hardware, usb]
homepage: https://dm3mat.darc.de/qdmr/
scout_score: 7
status: draft
---

# qdmr

**TLDR;** A GUI and command-line tool that writes DMR radio configs as plain text files instead of vendor binaries, then uploads them to cheap handhelds over USB.

qdmr builds and writes "codeplugs", the configuration blobs that tell a DMR (Digital Mobile Radio) handset which channels, zones, contacts, scan lists and radio ID it has. You assemble these for a supported radio in a GUI, or work from the command line with `dmrconf`, which ships with a man page. It can also download the current config from a radio.

The author's complaint is that vendor programming software for cheap radios is hard to use, poorly documented, often Windows-only, and produces device-specific binaries that cannot be shared. Every operator ends up redoing the same regional setup for every model. qdmr cuts the feature set down to what amateur use needs and tries to make setup friendlier.

The interesting idea is the format. The codeplug is stored as a device-independent, human-readable text file, and the tool converts it to each radio's own format at upload time. In the author's words, it "can therefore be shared across multiple device and even across vendors". That also means configs can be diffed and kept in version control. The project is derived from Serge KK6ABQ's reverse-engineering of the codeplug formats and communication protocols of cheap Chinese DMR radios, so it is a door into how these radios store and talk about their settings.

The GUI can pull nearby repeater frequencies from repeatermap.de and fetch the DMR call-sign database, so contacts can be added by callsign instead of numeric DMR ID.

## Install

```
brew install qdmr
# Needs a supported DMR radio connected over USB to upload or download a codeplug.
# Repeater auto-completion needs an API key requested from the repeatermap.de maintainer.
```

## Try this

```
dmrconf --help
```
Lists the command-line tool's options for reading, writing and converting codeplugs.

```
qdmr
```
Opens the GUI, where you can start a new codeplug and add channels, zones and contacts without a radio attached.

## What's unique

The codeplug is a plain text file that works across models and vendors, not a binary blob, which makes sharing and diffing configs practical.

## Caveats

Only a small set of radios is supported (the author owns just three), some features only work on radios that offer them, and the support table marks the Baofeng DR-1801-A6 with "Stay away!".

## Links

- [qdmr homepage](https://dm3mat.darc.de/qdmr/)
