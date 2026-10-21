---
name: openslide
title: OpenSlide
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, image-formats, library, microscopy, pathology, science]
homepage: https://openslide.org/
scout_score: 6
status: draft
---

# OpenSlide

**TLDR;** A C library and small toolset for reading gigapixel pathology slide scans from many vendor formats without loading the whole image into memory.

Whole-slide images are digitised microscope slides. Uncompressed, they often run to tens of gigabytes, which is more than most machines have in RAM. OpenSlide gives programs one consistent interface for reading them: ask for a region at a chosen resolution and get just those pixels back. It also exposes metadata, ICC profiles, and associated images such as the slide label and a thumbnail.

The harder problem is the formats. Per the project, "Vendors typically do not document their formats," and the files were often readable only with the vendor's own Windows software. OpenSlide reads Aperio .svs, Hamamatsu .ndpi, Leica .scn, MIRAX .mrxs, Zeiss .czi, DICOM, and generic tiled TIFF, among others. The aim is that doctors and researchers are not tied to one vendor's viewer, and that non-Windows platforms can read these files too.

The door here is digital pathology and the quirks of huge tiled, multi-resolution images. Python and Java bindings are published separately. The Python one includes a Deep Zoom generator and a simple web viewer, which is an easy way to see how a gigapixel image is served as pyramids of tiles. The project comes from Satyanarayanan's group at Carnegie Mellon, and a 2013 Journal of Pathology Informatics paper linked from the homepage describes the design.

## Install

```
brew install openslide
# You need a whole-slide image file to do anything useful. Sample slides are linked from the formats page on the website.
```

## Try this

```
slidetool --help
```
Prints usage for the bundled slide tool. The brief does not document it, so read the help text to see what it offers.

```
openslide-show-properties --help
```
Shows how to dump a slide's metadata properties. Usage is unverified in the brief, so check the help output.

```
openslide-write-png --help
```
Shows the options for writing a region of a slide out as a PNG. Usage is unverified in the brief, so check the help output.

## What's unique

It reads gigapixel pathology scans that ordinary image libraries cannot open, using support built by reverse-engineering undocumented vendor formats. One API covers many of them.

## Caveats

Vendors do not endorse the format support, which may be incomplete, and per the README it reads brightfield slides only. The four bundled executables are not documented in the pages the brief drew on.

## Links

- [OpenSlide homepage](https://openslide.org/)
- [Supported formats](https://openslide.org/formats/)
- [C API reference](https://openslide.org/api/openslide_8h.html)
- [GitHub repository](https://github.com/openslide/openslide)
