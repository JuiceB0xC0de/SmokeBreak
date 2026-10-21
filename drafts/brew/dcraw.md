---
name: dcraw
title: dcraw
source: brew
category: take-things-apart
commitment: quick
tags: [c, file-formats, image-processing, quick, raw-photos, reverse-engineering]
homepage: https://dechifro.org/dcraw/
scout_score: 6
status: draft
---

# dcraw

**TLDR;** A single-file C program that decodes raw sensor data from hundreds of camera models, built by reverse engineering formats the makers never documented.

dcraw reads the proprietary raw files cameras write (the page names CRW, CR2, MRW, NEF, RAF and many more) and turns them into ordinary images. It can also pull out embedded thumbnails and print camera metadata. The whole thing is one ANSI C source file of about 10,500 lines, using only standard C libraries.

The author wrote it because vendors' raw decoders were closed source and ran only on Windows and Mac. His stated mission: "Write and maintain an ANSI C program that decodes any raw image from any digital camera on any computer running any operating system." Each manufacturer's format had to be worked out from the cameras themselves, and the source file doubles as the documentation the camera makers refused to provide.

The idea underneath is that a camera sensor records only one colour per pixel. A raw file is closer to a measurement than a picture, and turning it into a photo means reconstructing the missing colours (demosaicing). dcraw lets you choose the method: Bilinear, VNG, PPG or AHD. Foveon X3 sensors get different handling. By default it also auto-brightens so that one percent of pixels come out white.

The author deliberately refuses to make it a library. It stays a standalone program that other tools wrap, and the page says many raw converters have done exactly that. It writes to stdout, so you pipe it into Netpbm tools or cjpeg to get other formats.

## Install

```
brew install dcraw
```

## Try this

```
dcraw -i -v crw_0001.crw
```
Reads the file's metadata quickly and prints it without decoding the image. The FAQ says it is faster than ExifTool but gives less.

```
dcraw -c crw_0001.crw | cjpeg > crw_0001.jpeg
```
Decodes the raw file to stdout and pipes it through cjpeg to produce a JPEG.

```
dcraw -T crw_0001.crw
```
Writes a TIFF with metadata instead of the default output.

## What's unique

Decades of reverse engineering of undocumented camera formats, packed into one portable C file that many commercial raw converters have reused. It is deliberately a program rather than a library.

## Caveats

The homepage shows no release date and its news items stop at 2006, though the camera list includes newer bodies. Output looks dark unless you read the FAQ about brightness options such as -W.

## Links

- [dcraw homepage (author Dechifro)](https://dechifro.org/dcraw/)
