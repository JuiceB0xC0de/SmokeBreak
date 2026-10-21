---
name: flif
title: FLIF
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, compression, deprecated, file-format, image-format, lossless]
homepage: https://flif.info/
scout_score: 5
status: draft
---

# FLIF

**TLDR;** A dead but fascinating lossless image format whose files can be cut off at any byte and still decode into a usable, lower-quality picture.

FLIF, the Free Lossless Image Format, stores ordinary pixel images (greyscale, RGB, RGBA, palette, up to 16 bits per channel) in .flif files that decode back to the identical pixels. The package ships an encoder and decoder (`flif`), an example viewer (`viewflif`), converters from GIF and APNG (`gif2flif`, `apng2flif`), and a `dflif` tool. It also supports animation and has a lossy preprocessing option on the encoder side.

The pitch on the homepage: "FLIF does away with knowing what image format performs the best at any given task." The idea was one format that handles line art, photographs and everything between, instead of choosing PNG for one and JPEG 2000 for another. It was also built for progressive decoding, so a partial download gives a usable preview.

The interesting part is the model underneath. FLIF uses MANIAC (Meta-Adaptive Near-zero Integer Arithmetic Coding), a variant of CABAC in which the contexts are decision-tree nodes learned at encode time, rather than a fixed table of quantized local image information. Its interlacing generalizes PNG's Adam7 and is built into both the pixel estimation and the context model, so any prefix of a file works as a rough version of the whole image, with little size overhead.

Development has stopped. The project's own notice says FLIF was superseded by FUIF and then by JPEG XL. That makes FLIF a good specimen: a small, readable codec that shows ideas which carried forward into the format that replaced it.

## Install

```
brew install flif
# The brew formula is deprecated. The upstream README builds from source in FLIF/src: install libpng (plus SDL2 for the viewer), then run make. No hardware or accounts needed.
```

## Try this

```
flif --help
```
Prints the encoder/decoder options, including interlacing and lossy settings.

```
viewflif --help
```
Shows how to use the example viewer, which displays .flif files, including partially loaded ones.

```
gif2flif --help
```
Shows how to convert an animated GIF into an animated FLIF file.

## What's unique

Interlacing is part of the compression model rather than a bolt-on, and the context model is a decision tree learned per image instead of a fixed set of contexts.

## Caveats

Development has stopped and the README points readers to JPEG XL; the brew formula is deprecated, speed is described as only 'acceptable', and the homepage's compression figures come from an early development version.

## Links

- [FLIF homepage](https://flif.info/)
- [FLIF source repository (GitHub README)](https://github.com/FLIF-hub/FLIF)
- [JPEG XL reference implementation (libjxl), the successor](https://github.com/libjxl/libjxl)
