---
name: gphoto2
title: gphoto2
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, cameras, gpl, needs-hardware, ptp, usb]
homepage: http://www.gphoto.org/
scout_score: 6
status: draft
---

# gphoto2

**TLDR;** A command-line program that talks to over 2700 digital cameras and media players through libgphoto2, built so free systems don't need vendor software.

gphoto2 is the command-line front end to libgphoto2, the library that does the actual device communication. The project's homepage calls gPhoto2 "a free, redistributable, ready to use set of digital camera software applications for Unix-like systems, written by a whole team of dedicated volunteers around the world." The homepage claims support for more than 2700 cameras and media players.

The project exists because many camera makers do not publish their communication specifications. Without them, free operating systems have no official way to talk to the camera. gPhoto fills that gap with community-maintained drivers, so a camera plugged into a Unix machine can be driven from a shell rather than a vendor app.

The idea underneath is a protocol door. The homepage notes that newer libgphoto2 versions also support MTP media players, because MTP is based on PTP, the Picture Transfer Protocol. Cameras and players are small devices speaking a defined protocol over USB, and this tool is a way to see that conversation from the command line.

The README and homepage that were read do not list subcommands or usage examples, so the `--help` output and the man page are the place to learn what it can do. The README also mentions optional extras at build time: EXIF and JPEG support, an ncurses configuration UI via CDK, and ASCII-art previews via AALIB.

## Install

```
brew install gphoto2
Needs a camera or media player supported by libgphoto2 and a USB connection to do anything useful. The README gives no first-run or hardware setup steps.
```

## Try this

```
gphoto2 --help
```
Prints the list of options, which is the quickest way to see what the tool can do with a connected camera.

## What's unique

Most camera tools are built around a GUI or a vendor app. This one is a plain command-line front end to a broad, community-maintained camera library, with a clear free-software purpose.

## Caveats

Unix-like systems only according to the homepage, the 2700-camera figure may not be current, and you need a supported device to get anything out of it.

## Links

- [gPhoto project homepage](http://www.gphoto.org/)
- [gphoto2 GitHub repository (README)](https://github.com/gphoto/gphoto2)
