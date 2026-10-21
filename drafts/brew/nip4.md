---
name: nip4
title: nip4
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, functional, gui, images, libvips, spreadsheet]
homepage: https://github.com/libvips/nip4
scout_score: 6
status: draft
---

# nip4

**TLDR;** A spreadsheet where cells hold images and formulas instead of numbers, built on libvips, so editing one input recalculates everything downstream.

nip4 is a graphical front end to the libvips image processing library, laid out like a spreadsheet. Cells are not pixels. Each cell is an object with a formula, and formulas refer to other cells. Change an input, such as a loaded image or a number, and every dependent cell recalculates. It also has a batch mode for running a workspace from the command line without the GUI.

The idea underneath is a functional, lazy model. In the README's words, "It is purely functional, meaning there is no assignment and there are no side effects, and it is fully lazy, meaning all computation is driven by the user interface, down to the pixel level." Only the pixels you actually need get computed, which is how a spreadsheet can sit on top of very large images without holding them in memory.

nip4 is a rework of an older tool, nip2, for the GTK4 toolkit and the vips8 library, and it can load workspaces saved by nip2. The README says the authors have built systems of more than 10,000 cells that analyse many hundreds of gigabytes of images. That makes it a door into dataflow thinking applied to images: describe the pipeline as connected formulas, then poke at the inputs and watch it update.

## Install

```
brew install nip4
# Needs a desktop session, since it is a GTK4 GUI. Flatpak (org.libvips.nip4 on Flathub) and Windows zip builds also exist.
```

## Try this

```
nip4 --help
```
Lists the command line options for the GUI and its batch mode.

```
snip --help
```
Shows the options for the second installed executable. The brief does not describe it, so check the help text.

## What's unique

Most image tools are a chain of destructive edits. This one is a spreadsheet of pure, lazy formulas, so the whole workflow stays editable and scales to huge images.

## Caveats

The GUI is the point, so it needs a desktop. On macOS the README says Ghostty may not launch GTK apps, so use Terminal.app. The Windows default renderer can show a blank window on some older versions.

## Links

- [GitHub repository (homepage)](https://github.com/libvips/nip4)
- [Introduction to nip4 (libvips news, 2025-03-20)](https://www.libvips.org/2025/03/20/introduction-to-nip4.html)
- [nip4 for nip2 users (libvips news, 2025-03-12)](https://www.libvips.org/2025/03/12/nip4-for-nip2-users.html)
- [Flathub page](https://flathub.org/en/apps/org.libvips.nip4)
