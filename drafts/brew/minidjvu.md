---
name: minidjvu
title: minidjvu
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, ancient, compression, djvu, file-format, scanned-documents]
homepage: https://minidjvu.sourceforge.net/
scout_score: 5
status: draft
---

# minidjvu

**TLDR;** A small encoder and decoder for the black-and-white layer of DjVu, which squeezes scanned pages by reusing shared letter shapes across a whole document.

minidjvu turns bitmaps (PBM, BMP or TIFF) into DjVu files and back again. It handles only the bitonal layer of DjVu, called JB2, and ignores the colour and photo parts of the format. It sits on top of DjVuLibre, the main DjVu support library.

Its interesting trick is multipage mode. Scanned text repeats the same shapes over and over: every lowercase e on a page looks much like every other e. The README says minidjvu compresses multiple pages together, "taking advantage from similarities between pages". Pages can be bundled into one file or kept as indirect files, named after their source images with a numeric suffix added on a name clash.

The author calls it an experiment: "Minidjvu is not going to support all DjVu functionality; the idea is rather to take the black-and-white part (also called JB2) and experiment with it." The 0.8 notes show where this gets tricky. The pattern-matching changes were made to stop unrelated shapes from being merged. That failure mode is a good way into how symbol-matching compression works, and what goes wrong when it matches too eagerly.

## Install

```
brew install minidjvu
```

## Try this

```
minidjvu --help
```
Prints the usage text and the list of options, including the encoding controls, so you can see what the tool exposes.

## What's unique

It is a deliberately narrow tool: just the JB2 layer of DjVu, built as a playground for cross-page symbol sharing rather than as a full DjVu toolkit.

## Caveats

Only black-and-white content is supported, input is limited to PBM, BMP and TIFF, and the project looks quiet, with 0.8 as the latest release and no date given on the homepage.

## Links

- [minidjvu homepage](https://minidjvu.sourceforge.net/)
