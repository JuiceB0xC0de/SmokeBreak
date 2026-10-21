---
name: gfxutil
title: gfxutil
source: brew
category: take-things-apart
commitment: quick
tags: [device-properties, firmware, macos, quick, reverse-engineering]
homepage: https://github.com/acidanthera/gfxutil
scout_score: 5
status: draft
---

# gfxutil

**TLDR;** A small macOS tool that converts Apple firmware Device Properties between text and binary form, a peek at how firmware describes hardware to the OS.

gfxutil works with Device Properties, the property data that Apple Mac firmware hands to the operating system to describe the hardware inside the machine. Per the README, it is "a tool to work with Device Properties commonly found in Apple Mac firmwares by mcmatrix." It converts property trees between a text form and a binary form, so you can read a binary blob or produce one.

The idea underneath is that hardware does not simply announce itself. Firmware builds a tree of named properties for each device, and the OS reads that tree to learn what it is running on. A tool that moves that tree between readable and binary form lets you see the handoff directly.

The README is thin. It does not spell out the input and output formats, and it points to forum posts for usage examples and changelogs. Those pages were unreachable when the brief was written, so expect to learn mostly from `gfxutil -h` and by experimenting. The build depends on the edk2 firmware development tree, which the README has you clone from acidanthera/audk.

## Install

```
brew install gfxutil
# macOS only. The README itself describes building from source with Xcode:
# git clone https://github.com/acidanthera/audk edk2
# git clone https://github.com/acidanthera/gfxutil gfxutil
# cd gfxutil && xcodebuild
```

## Try this

```
gfxutil -h
```
Prints the help text. The README points here for usage, so this is the quickest way to see the supported options.

## What's unique

It is a small, focused utility for one niche firmware format, and its source build pulls in the edk2 firmware tree rather than ordinary packages.

## Caveats

Documentation is minimal and the original usage forum appears unreachable; the brief could not confirm the project's maintenance status, and the README states no formal license.

## Links

- [GitHub repository (homepage)](https://github.com/acidanthera/gfxutil)
- [edk2 dependency (acidanthera/audk)](https://github.com/acidanthera/audk)
- [Usage examples and changelogs (netkas forum, may be gone)](http://forum.netkas.org/index.php?topic=64.0)
