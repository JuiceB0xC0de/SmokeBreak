---
name: ssocr
title: ssocr
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [c, image-processing, ocr, quick, seven-segment]
homepage: https://www.unix-ag.uni-kl.de/~auerswal/ssocr/
scout_score: 7
status: draft
---

# ssocr

**TLDR;** Reads the digits off a photo of a seven-segment display and prints them as text, using plain deterministic image rules instead of machine learning.

ssocr takes an image of a single row of seven-segment digits, the kind on clocks, multimeters and old tokens, and writes the number it sees to standard output. It accepts a file, or image data piped in with `-` as the name. Before recognising anything it can run cleanup commands on the image: threshold, crop, invert, shear, rotate and filters.

The author wrote it to read the number on an RSA SecurID 600 token through a USB camera. General OCR software struggled because the segments of a seven-segment digit are not connected to each other. The homepage says it began as a proof of concept to test the recognition algorithm.

The method is small enough to hold in your head. The image is thresholded to monochrome, then scanned by columns to find digit-shaped stretches. Each digit is classified by checking the three horizontal segments and the vertical segments at fixed positions, and a table lookup maps the lit pattern to a character. In the author's words: "The algorithm used by ssocr is quite simple and completely deterministic." It also prints debug images showing how it segmented and read the picture, so you can see why it got a digit wrong.

That makes it a good door into classic image processing: thresholding, segmentation and rule-based classification, with every step inspectable and tunable by hand.

## Install

```
brew install ssocr
# The author ships source only (C, needs Imlib2 and a compiler); Homebrew and some distro packages are maintained by third parties.
```

## Try this

```
ssocr --help
```
Lists the options and image-cleanup commands so you can see what can be tuned.

```
ssocr -T six_digits.png
```
Recognises the digits in your image using iterative (k-means) thresholding and prints the number.

```
ssocr -Dillustrate_algo.png -T six_digits.png
```
Also writes a debug image illustrating how the algorithm segmented and read the digits.

## What's unique

It uses no machine learning, so results are repeatable and explainable through debug images. It has a concrete origin: a camera pointed at a security token, feeding a login script.

## Caveats

It reads only a single row of seven-segment digits, skewed digits often break it (a missed 7 is common), and the author develops only on GNU/Linux.

## Links

- [ssocr homepage](https://www.unix-ag.uni-kl.de/~auerswal/ssocr/)
