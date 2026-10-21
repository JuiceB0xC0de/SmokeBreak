---
name: dynamips
title: Dynamips
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, cisco, emulation, network, routing]
homepage: https://github.com/GNS3/dynamips
scout_score: 8
status: draft
---

# Dynamips

**TLDR;** Dynamips emulates whole Cisco routers, so a real IOS image boots as a virtual router on your laptop and you can poke at routing from the inside.

Dynamips is a command-line emulator for Cisco router hardware. The README lists the 7200, 3600, 3725, 3745, 2600 and 1700 families. You give it a Cisco IOS image file and it runs that software as a virtual router. The real IOS code executes on your machine instead of a imitation of its behaviour.

This project is a community continuation of the original Dynamips. It is based on the last development version plus patches from contributors, and it was renamed from Dynamips-community back to Dynamips at 0.2.9. The README gives no explicit motivation beyond that, but the GNS3 organisation hosts it and the project is still releasing.

The idea underneath is hardware emulation as a way to study network gear. A router is a computer with a particular CPU and set of interface cards. If you emulate those faithfully enough, the vendor's own firmware can't tell the difference, and you get a lab where you can break routing protocols without buying a rack.

The code builds in two variants, chosen with the DYNAMIPS_CODE CMake flag. 'Unstable' holds most of the development code. 'Stable' leaves out some mips64 optimisations and tcb code that the author says cause instability on some platforms. The README is blunt: "You should probably use stable unless you have a very good reason."

## Install

```
brew install dynamips
# You must supply your own legally obtained Cisco IOS image. None is included or downloaded.
```

## Try this

```
dynamips --help
```
Prints the list of options so you can see what the emulator can configure.

```
dynamips -P 7200 /ios/your-c7200-image.bin
```
Starts an emulated 7200-platform router from your IOS image. The README's image name is a placeholder, so substitute your own file.

```
nvram_export --help
```
Shows usage for the bundled helper that handles router NVRAM data.

## What's unique

It runs genuine Cisco IOS images rather than a lookalike, and it is the emulator underneath GNS3. The README also documents an ARM64 Docker script that builds it with a JIT.

## Caveats

You need your own Cisco IOS image, the README warns the unstable build has proved unstable outside 64-bit Mac, and its Windows and OS X instructions rely on old tooling such as WinPcap and GCC 4.9.

## Links

- [GitHub repository (homepage)](https://github.com/GNS3/dynamips)
- [Releases](https://github.com/GNS3/dynamips/releases)
- [Issue tracker](https://github.com/GNS3/dynamips/issues)
- [GNS3 community forum](https://gns3.com/community)
