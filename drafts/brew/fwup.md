---
name: fwup
title: fwup
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, embedded, firmware, images, needs-hardware, updates]
homepage: https://github.com/fwup-home/fwup
scout_score: 5
status: draft
---

# fwup

**TLDR;** fwup packs partitions, filesystems and update logic into one signed ZIP, then writes it to an SD card or image file. It shows how embedded devices update themselves.

fwup is a command-line tool for embedded Linux devices that replace a whole system image at once. You write a config file, fwup.conf, describing resources, an mbr or gpt partition table, and tasks. fwup packs all of it into a .fw file, which is a ZIP archive that can optionally be signed. Applying the archive writes it to an SD card, a device file, or a plain image file. A helper called img2fwup turns a raw image into a .fw file.

Each task has event handlers (on-init, on-resource, on-finish, on-error) and actions such as fat_write, raw_write and uboot_setenv. fwup stores a processed copy of the config and a BLAKE2b-256 hash of every resource in the archive. When applying, it streams through the archive in one pass and checks the writes as it goes. The README says the scripting is kept limited on purpose: "Scripts are intentionally limited to make failure scenarios easier to reason about."

The idea underneath is the A/B update pattern. Write the new system to the unused slot, then flip a flag at the very end, so a power cut halfway leaves the old system bootable. fwup is built around that, along with recovery partitions and trial-update/failback schemes. The README is blunt about scope: "Distribution of software update archives is not a feature." You fetch the file some other way and hand it to fwup. The stated goal is updates "fast enough for code development and reliable enough for production use," and it aims to beat dd on write speed and reliability.

You can learn a lot without a device. Build an archive, apply it to a plain image file, and inspect the result.

## Install

```
brew install fwup
# Linux: .deb and RPM packages are on the GitHub releases page. Windows: choco install fwup
# Writing to a real SD card needs sudo on Linux. Building archives and writing image files needs no hardware.
```

## Try this

```
fwup -c -f fwup.conf -o myfirmware.fw
```
Builds a firmware archive from your config file into myfirmware.fw.

```
fwup -a -d myimage.img -i myfirmware.fw -t complete
```
Applies the complete task to a regular image file instead of a card, so no hardware is needed.

```
fwup -g
```
Generates a signing key pair, fwup-key.pub and fwup-key.priv, in the current directory.

## What's unique

Unlike a general-purpose flasher, fwup centres on the archive. One ZIP can hold several tasks, and the first one whose conditions match the target is applied. Those conditions can be a file, a partition offset or a U-Boot variable. Archives can be signed and verified.

## Caveats

Delta updates are labelled BETA and may change incompatibly, some actions need --unsafe, and U-Boot support is limited (no big-endian targets or raw NAND writes).

## Links

- [GitHub repository and README](https://github.com/fwup-home/fwup)
- [Releases (v1.17.1 latest)](https://github.com/fwup-home/fwup/releases)
- [Nerves Project buildroot system (more examples, per README)](https://github.com/nerves-project/nerves_system_br)
