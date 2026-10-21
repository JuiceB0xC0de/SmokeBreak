---
name: gammu
title: gammu
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, daemon, library, needs-hardware, phones, sms]
homepage: https://wammu.eu/gammu/
scout_score: 5
status: draft
---

# gammu

**TLDR;** A command-line toolkit for controlling a mobile phone: read and send SMS, export contacts and calendars, and browse the phone's files from a terminal.

Gammu is a C library (libGammu) with a command-line tool on top. According to its README, the tool can list and handle calls, retrieve, back up and send SMS, retrieve MMS, export and import the phonebook (including vCard), export and import calendar and tasks (vCalendar or iCalendar), report phone and network information, and reach the phone's file system. How much of that works depends on the handset.

The package is more than one utility. It also ships an SMS daemon (`gammu-smsd`) with helpers to inject messages and monitor it, plus Python bindings, so other programs can drive a phone through the same library. `gammu-detect` and `gammu-config` are there to find a phone and set up a connection. The scout's notes say the phone is reached over AT commands, serial, or Bluetooth. The pages behind this entry do not confirm that, so treat it as a lead to check in the manual.

The project forked from Gnokii and was called MyGnokii2 up to version 0.58. When it needed a better name, it became Gammu, short for 'Gammu All Mobile Management Utilities'. The homepage admits the author did not know that Gammu is also a character in Heretics of Dune.

The larger idea is that a phone is a device you can talk to from a script, not only through its own screen. Gammu turns old handsets into scriptable message gateways and gives a way into how phones were managed before apps took over.

## Install

```
brew install gammu
# Needs a phone or a GSM modem that Gammu supports, connected to your machine. Check the Gammu Phone Database for your model.
```

## Try this

```
gammu --help
```
Lists the commands the tool offers for talking to a connected phone.

```
gammu-detect --help
```
Shows the options for the helper that looks for connected phones.

```
gammu-config --help
```
Shows how the interactive configuration helper is invoked.

## What's unique

It is a long-running toolkit with a library, an SMS daemon and Python bindings, not just a single utility. It also keeps a per-phone compatibility database, a sign of how uneven handset support is.

## Caveats

Support depends on the phone model, and the homepage says phones that present themselves as USB storage cannot be reached through Gammu.

## Links

- [Homepage](https://wammu.eu/gammu/)
- [Gammu manual (online docs)](https://docs.gammu.org/)
- [Source code and issue tracker (GitHub)](https://github.com/gammu/gammu)
