---
name: sispmctl
title: sispmctl
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, http, libusb, needs-hardware, power-strip, usb]
homepage: https://sispmctl.sourceforge.net/
scout_score: 6
status: draft
---

# sispmctl

**TLDR;** A small C tool that switches Gembird and Energenie USB power strips on and off from the command line, with schedules and a tiny web panel.

sispmctl talks to Gembird SIS-PM power strips over USB and switches their outlets. You give it an outlet number (1 to 4, or all) and a verb such as on, off, toggle or status, and it prints the result. Models with a power meter can report readings too. With several strips plugged in, you pick one by index, serial number or USB bus address.

The project exists so these strips can be run from Linux instead of a vendor GUI. The homepage calls it "an application for managing USB controlled powerstrips produced by GEMBIRD LTD." Newer units sold under the Energenie name work as well, if they appear in the supported device table.

The interesting part is what a cheap strip becomes once it has a command line. The strip can hold on/off schedules in the device itself, set with options like --Aat, --Aafter, --Ado and --Aloop. The -l option turns sispmctl into a minimal HTTP server on port 2638. It looks up page files in a skin directory and replaces `$$command(n)?yes:no$$` sequences with live outlet status or actions. The result is a scheduled, network-reachable outlet controller.

Underneath, this is plain userspace USB: libusb sends control requests to a device with a known vendor and product ID. That makes it a gentle first look at talking to physical hardware. You identify the device with lsusb, fix permissions with a udev rule, and then a shell script can flip a real switch.

## Install

```
brew install sispmctl
# Needs a supported Gembird/Energenie SIS-PM strip (vendor ID 04b4). By default only root can access the device; see the udev rule note in the README to allow a group.
```

## Try this

```
lsusb
```
Lists USB devices so you can spot the strip by its vendor and product ID (the README's example shows 04b4:fd13, an Energenie EG-PMS).

```
sispmctl -s
```
Scans for supported Gembird devices and reports what it finds.

```
sispmctl -nqg 4
```
Prints the status of outlet 4 as a bare 0 or 1, handy for scripts.

## What's unique

It is a dependency-light C tool that also carries its own device-side schedule language and a small HTTP control panel. A cheap USB strip becomes a networked, scheduled switch without extra software.

## Caveats

Only the listed Gembird and Energenie models work, the web interface has no authentication (the README says so), and the homepage was last modified in 2023.

## Links

- [Project homepage](https://sispmctl.sourceforge.net/)
- [Git repository](https://git.code.sf.net/p/sispmctl/git)
