---
name: libdsk
title: libdsk
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cp/m, disk-images, file-formats, floppy, library, retrocomputing]
homepage: https://www.seasip.info/Unix/LibDsk/
scout_score: 6
status: draft
---

# libdsk

**TLDR;** A C library and set of utilities that read, convert and write floppy disc images across dozens of obscure formats, from CP/M and Amstrad to Commodore 64.

LIBDSK puts one API in front of a long list of floppy formats. Its drivers cover raw image files, emulator formats such as .DSK, IMD, CopyQM, TeleDisk, APRIDISK, JV3, D88, SAP, D64 and dc42, and real floppy drives on Linux, DOS and Windows. You can point a utility at an image or a physical drive and get the same data back out in a different format or on a different medium.

The project page says it exists for the job CPCTRANS and PCWTRANS did under DOS: moving data between real discs and disc images. It also lets other programs, such as CPMTOOLS and emulator floppy controllers, read .DSK files and real discs without carrying format-specific code of their own.

The idea underneath is that a floppy is a layout of tracks, sectors and headers, and each image format is a different way of freezing that layout in a file. Per the page, newer 1.5.x versions store intermediate data in a common format called LDBS, which several drivers now share. The rcpmfs driver goes further and presents an ordinary directory as a CP/M disc image. A separate package, Lib765, runs the other way, turning uPD765A floppy controller commands into LIBDSK calls.

The project is the work of John Elliott, and the page was last updated in November 2024. The installed utilities include dskdump, dskform, dskid, dskscan, dsktrans and dskutil, which are small tools for looking at and moving disc data.

## Install

```
brew install libdsk
# Reading or writing real floppy drives on Linux needs a kernel with FDRAWCMD support; the page says it is deprecated since 5.18 and due for removal. Image-file work does not need it.
```

## Try this

```
dskid --help
```
Shows the options for the tool that identifies what format and geometry a disc image has.

```
dsktrans --help
```
Shows how to convert a disc or image from one format to another.

```
dskdump --help
```
Lists the options for dumping the contents of a disc image, sector by sector.

## What's unique

Its range of formats is much wider than most floppy tools, and it treats CP/M, Amstrad, Commodore 64 and TRS-80 discs as first-class. It also bridges emulators and real drives through one API.

## Caveats

Real-drive access on modern Linux depends on FDRAWCMD, which the kernel is dropping, and rcpmfs users with files over 16k should use 1.5.18 or later to avoid corruption.

## Links

- [LIBDSK homepage (John Elliott)](https://www.seasip.info/Unix/LibDsk/)
