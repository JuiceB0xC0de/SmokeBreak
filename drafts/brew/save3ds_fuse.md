---
name: save3ds_fuse
title: save3ds_fuse
source: brew
category: take-things-apart
commitment: afternoon
tags: [3ds, afternoon, filesystem, fuse, needs-hardware, reverse-engineering, rust]
homepage: https://github.com/wwylele/save3ds
scout_score: 7
status: draft
---

# save3ds_fuse

**TLDR;** Mounts Nintendo 3DS save data, extdata and title databases as an ordinary folder you can browse and edit, then writes changes back on unmount.

save3ds_fuse is a Rust program that reads and writes the storage formats of the Nintendo 3DS. Point it at a save on an SD card, a NAND image, a cartridge dump or a standalone save file, and it can extract the contents, import a directory back in, or mount the archive through FUSE. In mount mode the archive shows up as a normal directory in your file manager, and unmounting writes the changes back.

The 3DS encrypts and signs its storage, so the tool needs material from your own console: boot9.bin for almost every archive type, otp.bin for some NAND and ticket work, movable.sed for SD archives, and extra key material for cartridge saves. The README gives no explicit motivation for the project. It describes itself as an "Extract, import and FUSE program for common save format for 3DS, written in rust."

The idea underneath is that a console's storage layer is a filesystem like any other, just wrapped in layers of crypto, hashing and odd allocation rules. The project also ships a library, libsave3ds, and the README records quirks found by experiment: a broken last block in title databases, and a workaround for resizing extdata. Reading it is a view into how a console organises its data.

## Install

```
brew install save3ds_fuse
# FUSE mounting needs macFUSE on macOS: brew install macfuse --cask
# You also need dumps from your own 3DS (boot9.bin, and for some archives otp.bin and movable.sed). Cartridge saves need more key material.
```

## Try this

```
save3ds_fuse --help
```
Prints the usage text: archive selectors, modes, and the options for pointing at your NAND and boot9.bin.

```
save3ds_fuse --boot9 /path/to/boot9.bin --sdsave ID /path/to/mountpoint -r
```
Mounts a game's SD save read-only, where ID is the 16-digit hex title ID. Other options such as --nand or --movable may be needed depending on setup.

## What's unique

It treats NAND, SD, cartridge and standalone 3DS storage as one browsable filesystem, and it documents hardware quirks found by experiment.

## Caveats

Needs console dumps you must make yourself, mount mode does not work on Windows, extdata editing is flaky (the README recommends --import), and the README says to back up before writing.

## Links

- [Save3DS repository (homepage, README)](https://github.com/wwylele/save3ds)
- [ninfs, a virtual filesystem layer for NAND FAT images](https://github.com/ihaveamac/ninfs)
