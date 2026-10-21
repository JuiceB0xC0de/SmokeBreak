---
name: gnirehtet
title: gnirehtet
source: brew
category: radio-and-hardware
commitment: quick
tags: [adb, android, needs-hardware, network, quick, tunneling, usb]
homepage: https://github.com/Genymobile/gnirehtet
scout_score: 6
status: draft
---

# gnirehtet

**TLDR;** Gives an Android phone your computer's internet connection over USB, tethering in reverse, with no root and no UI on the phone.

Gnirehtet is the word tethering spelled backwards, and the README's own joke is `rev <<< tethering`. Ordinary tethering shares a phone's connection with a computer. This does the opposite: a phone plugged in over USB uses the computer's network, with no root on either side.

The computer runs a relay server, written in Rust or Java. It sets up an adb reverse tunnel (`adb reverse localabstract:gnirehtet tcp:31416`) to the phone. A small APK the tool installs has no interface of its own. It captures the phone's TCP and UDP traffic and pushes it through that tunnel to the relay, which sends it out over the computer's connection. A key icon shows in the status bar while the tunnel is up.

The idea underneath is that adb is more than a debugging shell. Its port-forwarding features can carry a whole network stack's worth of traffic, and nothing special is needed on the phone besides the app. It is a small, readable example of tunneling and relaying packets, and it can help when a device has no Wi-Fi or you are on a restricted network.

## Install

```
brew install gnirehtet
# adb must be on your PATH at runtime:
brew install --cask android-platform-tools
# Needs an Android phone (Android 5.0 / API 21+) with USB debugging enabled, connected by USB.
```

## Try this

```
gnirehtet run
```
Installs the app if needed and turns on reverse tethering for one device. It stays active until you press Ctrl+C. Accept the permission popup on the phone the first time.

```
gnirehtet autorun
```
Enables reverse tethering for every connected device, now and in the future.

```
gnirehtet --help
```
Lists the subcommands, including the relay, start, stop and tunnel steps for running things manually.

## What's unique

It needs no root and no special driver, only adb, and the whole tunnel is built on `adb reverse`. It comes in two implementations: a Rust build the README recommends and a Java build for anywhere Java 8 runs.

## Caveats

The README says the project is not actively maintained and only build blockers are fixed. It is IPv4 only, and the macOS Rust download is the older v2.2.1.

## Links

- [GitHub repository (homepage)](https://github.com/Genymobile/gnirehtet)
- [Gnirehtet rewritten in Rust (author's blog)](https://blog.rom1v.com/2017/09/gnirehtet-rewritten-in-rust/)
- [Introducing gnirehtet (author's original article)](https://medium.com/@rom1v/gnirehtet-reverse-tethering-android-2afacdbdaec7)
