---
name: caire
title: caire
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [algorithms, go, image, quick, seam-carving, visual]
homepage: https://github.com/esimov/caire
scout_score: 5
status: draft
---

# caire

**TLDR;** Shrinks an image by repeatedly carving out its least interesting pixel paths, so the subject stays put while the empty space collapses.

Caire is a Go implementation of the seam carving paper, "Seam Carving for Content-Aware Image Resizing". Ordinary resizing either scales everything uniformly, which squashes the subject, or crops, which throws away the edges. Seam carving does neither. It finds a connected line of pixels running top to bottom (or left to right) that matters least to the picture, deletes it, and repeats until the image reaches the target size.

The idea underneath is small enough to hold in your head. An edge-detection pass (Sobel, after a blur) gives each pixel an energy value. A dynamic programming pass then computes the cheapest connected path across the image, and that path is the seam to remove. Sky, walls and blank backgrounds have little energy, so they get eaten first. Faces and sharp edges survive.

The `caire` binary takes a file, URL, stdin or a whole directory, and picks the output format from the file extension (jpg, jpeg, png or bmp). Width and height can be absolute pixels or percentages. You can also supply protective and removal masks, which are binary images the same size as the input. White areas mark where no seams should be carved. Face detection uses the embedded Pigo library so seams do not cut through people, and no separate model file is needed.

The debug mode is the best way in. It draws the chosen seams in a configurable colour (red by default), so you can see exactly which pixels the algorithm decided were expendable.

## Install

```
brew install caire
# alternative, needs a Go toolchain with $GOPATH/bin on PATH:
# go install github.com/esimov/caire/cmd/caire@latest
# the optional GUI preview needs Gio's system dependencies
```

## Try this

```
caire --help
```
Lists all supported flags, including the debug, mask and face detection options.

```
caire -in input.jpg -out output.jpg -perc=1 -width=20 -height=20 -debug=false
```
Shrinks both dimensions of the image by 20 percent by carving seams instead of scaling.

```
caire -in input.jpg -out output.jpg -face=1 -perc=1 -width=20
```
Shrinks the width by 20 percent while face detection keeps detected faces from being deformed.

## What's unique

Debug mode draws the removed seams over the image, so the algorithm becomes visible. Embedded face detection avoids the classic seam carving failure of slicing through faces, with no extra files to download.

## Caveats

The README is thin on limitations and quality trade-offs, and I could not confirm a recent release date; it describes itself as a library even though it ships a CLI.

## Links

- [Homepage (GitHub)](https://github.com/esimov/caire)
- [Seam Carving for Content-Aware Image Resizing (paper)](https://inst.eecs.berkeley.edu/~cs194-26/fa16/hw/proj4-seamcarving/imret.pdf)
- [Pigo face detection library](https://github.com/esimov/pigo)
