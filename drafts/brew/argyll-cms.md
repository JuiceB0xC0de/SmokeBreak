---
name: argyll-cms
title: Argyll CMS
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, color, display, icc, needs-hardware, science]
homepage: https://www.argyllcms.com/
scout_score: 5
status: draft
---

# Argyll CMS

**TLDR;** A suite of 47 command line tools that measure colour with a sensor and build ICC profiles for monitors, printers, scanners and cameras.

Argyll CMS is an open source, ICC compatible colour management system. It is a collection of C source code that compiles into command line tools. They make ICC profiles for scanners, cameras and film recorders, and calibrate and profile displays and RGB and CMYK printers. It also builds device links, including 3D LUTs, and accepts spectral sample data with a choice of illuminants and observer types. Gamut mapping and profile linking use the CIECAM02 appearance model.

The author, Graeme Gill, says he wrote it to make serious colour management available on platforms other than Windows and OS X. The project is funded by donations, which he says are what let him keep working on it.

The tool names follow the workflow. `targen` generates a set of test colour patches. `dispread` or `chartread` measures them. `colprof` turns the measurements into a profile. `iccdump` and `viewgam` let you look inside the result. Each step is its own program, so the pipeline is visible and you can see where colour measurement ends and mathematics begins.

The door it opens is the question of what a colour actually is. A screen's RGB numbers mean nothing until someone measures what the device emits, and Argyll drives measurement instruments through its own driver code to do that. The measured light becomes a profile that other software uses to translate between devices.

## Install

```
brew install argyll-cms
A colorimeter or spectrometer is needed to measure real displays or prints. Without one, the profile inspection tools can still be run on existing ICC files.
```

## Try this

```
dispcal --help
```
Prints the usage for the display calibration tool, listing the options and instrument choices it supports.

```
targen --help
```
Shows how to generate a test chart of colour patches, the first step in profiling a device.

```
spotread --help
```
Shows the options for taking a single colour reading from a connected instrument.

## What's unique

It drives colour measurement instruments with its own driver code, so a sensor can profile a real monitor entirely from the command line. The homepage also claims the fastest portable 8 bit raster colour conversion engine available anywhere.

## Caveats

Most of the fun needs a colour measurement instrument; it is AGPL licensed, and the author says Wayland display calibration is unlikely and recommends X11 on Linux.

## Links

- [Argyll CMS homepage](https://www.argyllcms.com/)
