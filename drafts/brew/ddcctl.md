---
name: ddcctl
title: ddcctl
source: brew
category: radio-and-hardware
commitment: quick
tags: [ddc, macos, monitor, needs-hardware, quick]
homepage: https://github.com/kfix/ddcctl
scout_score: 6
status: draft
---

# ddcctl

**TLDR;** A macOS command-line tool that changes an external monitor's brightness, contrast and input source by sending DDC/CI commands down the display cable.

ddcctl sends commands to an external monitor over the same cable that carries the picture, and the monitor changes its own settings. Brightness and contrast are the starting point. The README says input source, speaker volume, RGB colors, color presets and reset may also work, depending on how well the monitor's firmware implements them. The output is a change on the monitor itself rather than any printed text.

The author wrote it so the monitor's on-screen menu and its row of fiddly buttons can be skipped. It grew out of a TonyMac-x86 forum thread, and the code (ddcctl.m, with DDC.c reworked from jontaylor/DDC-CI-Tools-for-OS-X) does the talking to the display. The README does not go into the mechanism beyond that.

The idea underneath is that your monitor is a small computer listening on a side channel you probably never use. Once the controls are a shell command, they can be scripted. The README suggests Alfred, ControlPlane or Karabiner calling a script to switch presets, for example flipping an input between two machines with a keystroke.

The README includes a table mapping input source values 1 to 27 to ports, such as HDMI-1 (17) and USB-C (27). It is a handy reference for any DDC tool, not just this one.

## Install

```
brew install ddcctl
# Alternatives: download ddcctl_binaries.zip from the GitHub releases page, or install Xcode and run make.
# Needs a real Mac (not a hackintosh) and an external monitor that supports DDC.
```

## Try this

```
ddcctl -h
```
Prints the available options, which shows what your build can ask a monitor to change.

```
ddcctl -d 1 -i 17
```
Switches display 1 to the HDMI-1 input (value 17), so the monitor changes what it shows.

## What's unique

It does one small thing on macOS: it turns the monitor's own buttons into shell commands. The README also ships a practical input-source value table and is unusually candid about the author's limits.

## Caveats

The project is in self-declared maintenance mode with no issue triage, which settings work depends on your monitor's firmware, and it is macOS-only with no hackintosh support.

## Links

- [GitHub repository (homepage)](https://github.com/kfix/ddcctl)
- [Releases (binaries zip)](https://github.com/kfix/ddcctl/releases)
- [Feature backlog (GitHub project)](https://github.com/kfix/ddcctl/projects/1)
