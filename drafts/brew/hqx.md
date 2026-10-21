---
name: hqx
title: hqx
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [emulators, image, pixel-art, quick, upscaling]
homepage: https://github.com/grom358/hqx
scout_score: 6
status: draft
---

# hqx

**TLDR;** A command-line pixel-art enlarger that scales sprites 2x, 3x or 4x using a hand-built lookup table, the way classic console emulators smoothed their graphics.

hqx is a C library and command-line tool that enlarges pixel art by a factor of 2, 3 or 4 (hq2x, hq3x, hq4x). It reads an image such as a PNG and writes a bigger one with smoothed diagonal edges instead of the chunky blocks plain scaling gives you. The library form works on 32-bit RGB buffers that the caller allocates.

The algorithm is one of Maxim Stepin's pixel-art scalers, the family used in emulators such as Nestopia, bsnes, ZSNES, Snes9x and FCE Ultra. It was designed to be fast enough to process 256x256 images in real time, which is why it is built around a table and not around heavy maths.

For each source pixel, the filter looks at the 3x3 neighbourhood and compares the centre with its 8 neighbours in YUV colour space, tolerating more difference in brightness than in colour. Each neighbour is marked 'close' or 'distant', which yields 256 possible patterns. A 256-entry lookup table maps each pattern to a precomputed way of blending the source pixels into the output. The table was made by working out the most probable edge shape for each pattern and rasterising it at 3x resolution with anti-aliasing.

That is the idea worth taking away: upscaling does not have to be interpolation. It can be pattern recognition, a small fixed set of guesses about what the artist meant. The README says the filter was made for "images with clear sharp edges, like line graphics or cartoon sprites."

## Install

```
brew install hqx
# depends on the DevIL image library, which brew installs for you
```

## Try this

```
hqx --help
```
Prints the usage text so you can see the options before running anything.

```
hqx -s 4 test.png out.png
```
Scales test.png by 4x with hq4x and writes the result to out.png.

```
hqx -s 2 test.png out.png
```
Does the same at 2x, so you can compare the smoothing at different magnifications.

## What's unique

It is a fixed, hand-derived lookup table over 3x3 pixel patterns, not a parametric resampler, so sharp sprite edges stay crisp where general-purpose upscalers blur them.

## Caveats

It is not meant for photographs, and the brief could not confirm release dates or recent maintenance; the README's notes on 16-bit pixels and MMX look dated.

## Links

- [Homepage / GitHub repository](https://github.com/grom358/hqx)
- [DevIL image library (required dependency)](http://openil.sf.net/)
