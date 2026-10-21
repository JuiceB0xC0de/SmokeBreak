---
name: libgphoto2
title: libgphoto2
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, cameras, library, needs-hardware, ptp, usb]
homepage: http://www.gphoto.org/proj/libgphoto2/
scout_score: 5
status: draft
---

# libgphoto2

**TLDR;** A C library that lets programs talk to digital cameras over USB using PTP and other protocols, and the engine under gphoto2, digiKam and Darktable.

libgphoto2 is the backend that other photo programs use to reach a camera. A calling application asks it to list files, fetch images or change settings, and the library turns those requests into whatever protocol the camera speaks, mainly PTP, with MTP also covered. It has no window of its own. The project says: "Unlike the original gphoto, libgphoto2 is not a standalone graphical user interface (GUI) application. Instead, it is a backend library."

The design splits two concerns. Physical links live in libgphoto2_port, and camera families live in camlibs that provide a set of required callbacks. A new link or a new camera family can be added without changing the programs on top. Frontends such as the gphoto2 command-line tool, digiKam, gThumb and Darktable never need to know which camera or cable is underneath.

The door it opens is the camera as a protocol device rather than a disk. Cameras that use USB Mass Storage are simply mounted by the OS and need none of this. PTP cameras that the library does not know fall back to a generic PTP driver, which usually works with no configuration. Reading how that fallback and the camlib interface work is a good way into how cameras expose controls over USB.

The Homebrew formula installs two small helpers, gphoto2-config and gphoto2-port-config. These report build and configuration details for programs compiling against the library. For anything interactive you want the separate gphoto2 frontend.

## Install

```
brew install libgphoto2
# This installs the library only. For a command-line tool, install the separate gphoto2 frontend.
# A USB camera is needed to do anything real. The gphoto2 manual covers USB hotplug setup if the camera is not detected.
```

## Try this

```
gphoto2-config --help
```
Prints the options of the helper that reports how libgphoto2 was built, used by programs that compile against it.

```
gphoto2-port-config --help
```
Prints the options of the matching helper for the port layer, which handles the physical links.

```
env LC_ALL=C gphoto2 --debug-logfile=logfile.log --debug <options>
```
With the separate gphoto2 frontend installed, runs a command with English messages and writes a debug log of the camera conversation to logfile.log.

## What's unique

Ports for physical links and camlibs for camera protocols are separate, so new hardware plugs in without touching client programs. Unknown PTP cameras fall back to a generic driver that often just works.

## Caveats

Needs a camera that speaks PTP or another supported protocol to do anything real, will not talk to undocumented proprietary protocols, is aimed at Unix-like systems, and the brief could not confirm how recently it was released.

## Links

- [libgphoto2 homepage](http://www.gphoto.org/proj/libgphoto2/)
- [Supported camera list with protocol status](https://gphoto.sourceforge.io/proj/libgphoto2/support.php)
- [gphoto2 Manual](http://www.gphoto.com/doc/manual/)
- [GitHub repository](https://github.com/gphoto/libgphoto2)
