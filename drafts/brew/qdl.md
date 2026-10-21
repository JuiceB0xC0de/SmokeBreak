---
name: qdl
title: qdl
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, firmware, flashing, needs-hardware, protocol, qualcomm, usb]
homepage: https://github.com/linux-msm/qdl
scout_score: 8
status: draft
---

# qdl

**TLDR;** A command-line tool that talks to Qualcomm chips in USB Emergency Download mode, loading a programmer and flashing firmware even to devices that will not boot.

qdl speaks to Qualcomm devices in EDL, a special boot mode the README describes as providing "low-level access for firmware flashing and recovery". It first uploads a flash loader (the programmer, typically prog_firehose_ddr.elf) using the Sahara protocol. It then writes firmware images region by region using the Firehose protocol, guided by the rawprogram and patch XML files that ship with a build. It can also take an installer zip, flashmap.json or contents.xml, and it reads, writes, erases, dumps and lists devices.

It is maintained under the linux-msm project. The reason it exists is that EDL sits below the bootloader, so it is still reachable on unresponsive devices or ones with locked bootloaders. Instead of a vendor's proprietary flashing tool, you get a small open tool and two documented-in-the-open protocols you can watch go by with `--debug`, which prints timestamped SAHARA: and FIREHOSE: log lines.

The larger idea is that a phone or board is not one boot stage but a ladder. Below the OS and the bootloader there is a ROM-level door that accepts a signed loader over USB and then lets that loader write flash. Reading how qdl climbs through that door is a good way to learn how modern SoCs bring themselves up.

You do not need hardware to look around. A dry-run mode validates the XML descriptors and programmer arguments without touching a device, so you can see how a build is described before you ever plug anything in.

## Install

```
brew install qdl
# Needs a Qualcomm device in EDL mode to do anything real. How to enter EDL is device-specific; the README points to your device's own documentation. Dependencies: libusb, libzip.
```

## Try this

```
qdl list
```
Lists EDL devices visible through either USB backend, with their serial numbers.

```
qdl --dry-run prog_firehose_ddr.elf rawprogram*.xml patch*.xml
```
Validates the XML descriptors and programmer arguments without connecting to or flashing any device.

```
qdl --serial=0AA94EFD prog_firehose_ddr.elf rawprogram*.xml patch*.xml
```
Flashes a build to one specific board by serial number when several are connected.

## What's unique

It matches any device with Qualcomm's vendor ID 05c6 and ignores the Product ID, so it keeps working on new hardware without updates. It also has a hardware-free dry-run mode and an nbdkit plugin that exposes a physical partition as a block device.

## Caveats

Flashing needs a device already in EDL mode, which varies per device, and --finalize-provisioning performs irreversible UFS provisioning, so a wrong write can brick hardware.

## Links

- [GitHub repository (homepage)](https://github.com/linux-msm/qdl)
- [Installer packages and contents.xml docs](https://github.com/linux-msm/qdl/blob/main/docs/installer-packages.md)
- [Raw binary read/write docs](https://github.com/linux-msm/qdl/blob/main/docs/raw-io.md)
- [Homebrew formula](https://formulae.brew.sh/formula/qdl)
