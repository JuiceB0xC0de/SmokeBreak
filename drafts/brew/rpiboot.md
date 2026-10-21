---
name: rpiboot
title: rpiboot
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, bootloader, needs-hardware, protocol, raspberry-pi, usb]
homepage: https://github.com/raspberrypi/usbboot
scout_score: 6
status: draft
---

# rpiboot

**TLDR;** Turns a Raspberry Pi's boot ROM into a USB file server, so a Compute Module's storage shows up as a plain USB drive on your computer.

rpiboot is a host-side tool that talks over USB to a Raspberry Pi sitting in its ROM USB boot mode. The Pi has no OS running at this point. The host acts as a file server and pushes boot firmware and a small image into the device's memory. By default, that payload makes the Pi appear as a USB mass-storage device. You can then write an OS image to it with Raspberry Pi Imager.

The README describes it as a tool that "provides a file server for loading software into memory on a Raspberry Pi for provisioning." The aim is to reach a Pi's storage or bootloader from another computer without needing a working system on the device. On Compute Module 4 and newer it also updates the bootloader EEPROM.

The default payload, the mass-storage-gadget, is a small Linux initramfs. It scans for SD/eMMC, NVMe and USB block devices and exposes them through configfs as USB mass-storage devices. It also gives a console over UART and USB CDC-UART. The older msd firmware does less: it exposes only the SD/eMMC device, with no console and slower writes.

The door here is the boot chain itself. Before any operating system exists, the chip's ROM can ask a host for code over USB. How you trigger that mode depends on the board: a jumper (nRPIBOOT/EMMC-DISABLE) on Compute Modules, a GPIO set in OTP on Pi 4B and Pi 400, or holding the power button on Pi 5 and the Pi 500 models.

## Install

```
brew install rpiboot
# Homebrew caveat: boot a Compute Module with the default mass storage gadget:
sudo rpiboot -d "$(brew --prefix rpiboot)"/share/rpiboot/mass-storage-gadget64
# Needs a Raspberry Pi or Compute Module put into USB boot mode, and a USB cable to the host. Depends on libusb.
```

## Try this

```
rpiboot --help
```
Lists the options the tool accepts, with no hardware attached.

```
sudo rpiboot -d mass-storage-gadget
```
Boots a connected Pi in USB boot mode with the Linux mass-storage-gadget, so its storage appears as a USB drive on the host.

```
sudo rpiboot -d msd
```
Boots the device with the legacy msd firmware instead, intended for Pi 4 and older.

## What's unique

The Pi's own boot ROM becomes a USB drive, with a small Linux initramfs doing the work. The same tool also updates bootloader EEPROM and can provision secure boot.

## Caveats

It does nothing without a Raspberry Pi in USB boot mode, it is mainly a Linux tool, and the Pi 4B/Pi 400 GPIO setup permanently modifies OTP and cannot be undone.

## Links

- [usbboot repository (homepage and README)](https://github.com/raspberrypi/usbboot)
