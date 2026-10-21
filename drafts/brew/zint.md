---
name: zint
title: zint
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [barcodes, cli, encoding, images, qr-code, quick]
homepage: https://www.zint.org.uk/
scout_score: 5
status: draft
---

# zint

**TLDR;** A barcode generator that turns text into around ninety symbologies, from QR codes and Data Matrix to postal codes with bars of different heights.

Zint is a suite of programs for encoding data as barcodes. The Homebrew formula installs the command-line program, `zint`. It takes your data and a chosen symbology and writes an image file. The README lists BMP, EMF, EPS, GIF, PCX, PNG, SVG and TIF as output formats. The same codebase also produces a Qt-based GUI called Zint Barcode Studio and a C library, libzint, for embedding in other software.

The interest is in the range. Beyond the barcodes on a cereal box (Code 128, EAN-13), the list includes postal codes such as Royal Mail 4-State and USPS Intelligent Mail, and 2D codes such as QR Code, Data Matrix, PDF417, Aztec and MaxiCode. Each one is a different answer to the same question: how do you pack data into a printed pattern that a cheap scanner can read despite smudges, skew and bad printing?

The project's stated aim is "easy encoding of data in any of the wide range of public domain barcode standards" and to let you integrate that into your own programs. Trying several symbologies on the same string shows how differently each one spends its space.

## Install

```
brew install zint
```

## Try this

```
zint --help
```
Prints the list of options, including how to choose a symbology and an output file.

## What's unique

One open codebase covers dozens of obscure postal, pharmaceutical and industrial symbologies alongside the common ones, and ships as a CLI, a GUI and a library.

## Caveats

Support is volunteer-run and the README says answers may take up to a week; the CLI and GUI are GPLv3 or later while the library is BSD-3.

## Links

- [Homepage](https://www.zint.org.uk/)
- [Manual](https://zint.org.uk/manual/)
- [GitHub mirror](https://github.com/zint/zint)
- [SourceForge project](https://sourceforge.net/p/zint/)
