---
name: ddcutil
title: ddcutil
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, i2c, linux, monitors, needs-hardware, protocol]
homepage: https://www.ddcutil.com
scout_score: 7
status: draft
---

# ddcutil

**TLDR;** A Linux command-line tool that changes your external monitor's brightness, colour levels and input source over DDC/CI, the same settings the buttons on the bezel control.

Most external monitors carry a small control interface called the Virtual Control Panel, which implements the Monitor Control Command Set (MCCS). ddcutil sends commands to it over an I2C bus that the video driver exposes as /dev/i2c-n devices. A few monitors offer the same controls over USB instead, and ddcutil handles those through the USB Monitor Control Class Specification. Its own summary: "Generally speaking, any setting that can be changed by pressing buttons on the monitor can be modified by ddcutil."

The project grew out of colour profile management. Calibration is relative to the monitor's current settings, such as red gain, so ddcutil can save those settings when a calibration is made and restore them when the profile is applied.

The door it opens is that your monitor is a small networked-style device with its own command protocol, running behind the cable you already have. Once you see that, brightness scripts, input switching and calibration become ordinary programming. It builds a command-line tool and a shared library, libddcutil, which KDE PowerDevil uses. A separate Qt GUI, ddcui, is described on the same site.

## Install

```
brew install ddcutil

Needs Linux, an external monitor that supports DDC/CI, and the i2c-dev driver loaded; see the Post-Installation Checklist on the project site.
```

## Try this

```
ddcutil --help
```
Prints the online help listing the commands and options.

```
ddcutil environment
```
Probes the I2C environment, which helps diagnose a build that succeeds but fails at run time.

```
sudo ddcutil interrogate
```
Collects a detailed report on your system and monitors, the output the project asks you to attach to issue reports.

## What's unique

It uses DDC/CI, a control channel already built into most external monitors, so no vendor app is needed. It also covers USB-connected monitor controls, and its library is maintained for use by KDE PowerDevil.

## Caveats

Linux only, laptop panels are not supported, it will not run in a VM without GPU passthrough, and Nvidia's proprietary driver may need special settings.

## Links

- [Project homepage and documentation](https://www.ddcutil.com)
- [GitHub repository](https://github.com/rockowitz/ddcutil)
- [Post-Installation Checklist](https://www.ddcutil.com/config_steps)
- [FAQ](https://www.ddcutil.com/faq)
