---
name: fwupd
title: fwupd
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, firmware, linux, lvfs, needs-hardware, protocol]
homepage: https://github.com/fwupd/fwupd
scout_score: 6
status: draft
---

# fwupd

**TLDR;** The Linux firmware update daemon: it finds devices in your machine, pulls vendor firmware metadata from LVFS, and flashes updates live or at next boot.

fwupd is a daemon that detects devices with updatable firmware and applies vendor-supplied updates to them. By default it downloads metadata and firmware capsules from the Linux Vendor Firmware Service (LVFS), a service OEMs can publish to. Updates that can be applied live happen immediately. Others are staged for the next reboot. It can also report success or failure back to LVFS.

The project's stated aim is "to make updating firmware on Linux automatic, safe, and reliable." The idea underneath is that firmware, the code below your operating system, can be handled through one shared path instead of a separate vendor tool for every device.

The design has a few details worth reading about. Administrators can restrict updates to an approved list (ApprovalRequired in the remote config, ApprovedFirmware in fwupd.conf, holding container checksums), so only firmware tested inside the organisation gets installed. If the optional Passim service is installed, fwupd republishes downloaded metadata on the local network via mDNS/LLMNR so other machines can fetch it from a peer.

The Homebrew formula installs two executables, dbxtool and fwupdtool. The README does not discuss them, so this entry does not describe what they do. The README's own command-line client is fwupdmgr.

## Install

```
brew install fwupd
# Most users on Linux should instead use the fwupd package from their distro. The README advises against building from source.
```

## Try this

```
fwupdtool --help
```
Lists what the fwupdtool executable offers. The README does not cover it, so start here.

```
fwupdmgr get-devices
```
Lists every device fwupd detects on the system (the README runs this as root).

```
fwupdmgr get-updates
```
Shows any firmware updates available for those devices.

## What's unique

Firmware arrives through a vendor-facing service that OEMs publish to, and downloaded metadata can be shared over the LAN through Passim. An admin-controlled approved-firmware list lets an organisation limit updates to firmware it has tested.

## Caveats

The README steers users to distro packages rather than source builds, and Passim sharing is on by default if Passim is installed, so disable it with P2pPolicy=none in /etc/fwupd/daemon.conf if unwanted.

## Links

- [fwupd homepage (GitHub repository)](https://github.com/fwupd/fwupd)
- [fwupd website](https://fwupd.org/)
- [Building and Debugging guide](https://github.com/fwupd/fwupd/blob/main/docs/building.md)
- [Passim](https://github.com/hughsie/passim/blob/main/README.md)
