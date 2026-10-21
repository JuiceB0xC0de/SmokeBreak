---
name: jbig2enc
title: jbig2enc
source: brew
category: take-things-apart
commitment: quick
tags: [compression, image-formats, jbig2, pdf, quick, scanning]
homepage: https://github.com/agl/jbig2enc
scout_score: 5
status: draft
---

# jbig2enc

**TLDR;** An open encoder for JBIG2, the format that quietly shrinks scanned PDFs by reusing one picture of each letter wherever it appears.

jbig2enc compresses monochrome (1 bits per pixel) images into JBIG2, a format most people only meet inside scanned PDFs. The `jbig2` program reads image files such as JPG or TIF and writes either a standalone JBIG2 stream or fragments meant for embedding in a PDF. A companion script, `jbig2topdf.py`, wraps the output into a PDF. It can handle multipage documents too.

The README says JBIG2 uses "a number of clever tricks to get better compression than G4" on bi-level images. The main trick is symbol mode. The encoder extracts connected components from the page, classifies them into symbol classes (roughly, which blobs look like the same letter), and stores one template per class. The page is then described as a list of where each template is placed. Optional refinement coding can patch small differences.

The newer `--emit-json` flag writes that classification to a JSON sidecar file: which class each instance was assigned to, and where it sits. Normally the encoder throws this information away once it has finished. Exposed as JSON, it works as a glyph clustering layer you can use for other things. The README says negative coordinates for components at the crop edge are expected.

The door here is lossy-looking compression built on pattern matching. Because scanned text is full of repeated shapes, a page can be stored as an alphabet plus a layout. That is also why JBIG2 is a famous place for odd bugs when two similar glyphs get merged.

## Install

```
brew install jbig2enc
# jbig2topdf.py needs Python. Leptonica 1.74 or later is required (brew pulls it in).
```

## Try this

```
jbig2 -s -a -p -v -T 100 -b imgs images/*.jpg && python jbig2topdf.py imgs >out.pdf
```
Encodes a set of JPGs in symbol mode with a shared output base, then builds a PDF from the result. This is the README's main example.

```
jbig2 -s -S -p -v -O out.png images/*.jpg
```
Encodes the images and also writes a viewable PNG, so you can check the result before making a PDF.

```
jbig2 -s -p -b output --emit-json output.json images/amoris.2.150.jpg
```
Runs symbol mode and writes output.sym, output.0000 and output.json, with per-instance glyph placement and class data.

## What's unique

It is an open encoder for a format most people only meet inside scanned PDFs. The `--emit-json` sidecar exposes the glyph classification that encoders normally discard.

## Caveats

The README warns that refinement coding makes Acrobat crash (it is unclear whether the bug is in Acrobat), and Windows Command Prompt does not expand `*.jpg`. I could not find a last-commit date.

## Links

- [GitHub repository (homepage)](https://github.com/agl/jbig2enc)
- [jbig2enc-samples (linked in README)](https://github.com/zdenop/jbig2enc-samples)
- [jbig2enc-minidjvu fork (linked in README)](https://github.com/ImageProcessing-ElectronicPublications/jbig2enc-minidjvu)
