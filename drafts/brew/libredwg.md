---
name: libredwg
title: LibreDWG
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cad, dwg, file-formats, gnu, library, reverse-engineering]
homepage: https://www.gnu.org/software/libredwg/
scout_score: 5
status: draft
---

# LibreDWG

**TLDR;** A free C library and set of command-line tools that read and write AutoCAD's proprietary DWG format, converting it to DXF, JSON and SVG.

LibreDWG is a GNU project for handling DWG files, the native binary format of AutoCAD. The library reads DWG, and can also read DXF and JSON. The writer converts from DWG, DXF or JSON, or builds a drawing from scratch. The command-line programs are examples built on top of that library.

The tools cover conversions to DXF, JSON, and an initial SVG and PostScript output. They also rewrite DWG files (saveas) and include text search and layer listing (dwggrep and dwglayers). The brew formula installs a dozen executables, including dwgread, dwgwrite, dwg2dxf, dxf2dwg and dwg2SVG.

The project exists because DWG is a closed format, and the homepage says LibreDWG "aims to be a free replacement for the OpenDWG libraries." It is based on LibDWG, originally written by Felipe Castro. Reading a proprietary binary format that someone else controls is the larger idea here: every entity type and version difference has to be worked out and decoded by hand.

The decoder is described as done, while the writer is only good enough for versions R1.1 through R2000. That gap shows how much harder it is to produce a file a vendor's own software accepts than to read one.

## Install

```
brew install libredwg
```

## Try this

```
dwgread --help
```
Prints the options for the reader, the main tool for decoding a DWG file.

```
dwg2dxf --help
```
Shows how to convert a DWG file into the text-based DXF format, which is easier to inspect.

```
dwglayers --help
```
Shows how to list the layers inside a DWG drawing.

## What's unique

It is a free reimplementation of a proprietary CAD file format, shipped as a small family of single-purpose command-line tools under the GNU umbrella.

## Caveats

The project calls itself beta: some very advanced R2010+ entities fail to read and are skipped, and the writer only covers R1.1 through R2000.

## Links

- [GNU LibreDWG homepage](https://www.gnu.org/software/libredwg/)
