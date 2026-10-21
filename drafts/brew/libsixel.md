---
name: libsixel
title: libsixel
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [graphics, images, quick, retro, sixel, terminal]
homepage: https://github.com/saitoha/libsixel
scout_score: 6
status: draft
---

# libsixel

**TLDR;** Converts images into SIXEL, a 1980s DEC terminal graphics format, so you can cat a picture straight into a compatible terminal window.

libsixel is an encoder and decoder for SIXEL, plus command-line tools. `img2sixel` reads an image (the README mentions JPEG, PNG and animated GIF) from a file or stdin and writes a stream of escape sequences. `sixel2png` goes the other way. Because the output is only escape sequences, the README puts it simply: "all you have to do is \"cat\" it to your terminal."

SIXEL dates from DEC printers and terminals of the 1980s, where drawing images was painfully slow. The README says modern CPUs and networks make the format practical again. This encoder was redesigned for terminal emulators rather than dot-matrix printers, to cut transport overhead while staying compatible with old SIXEL terminals.

Under the hood, the encoder quantizes colours (median-cut, with dithering choices such as Floyd-Steinberg, Atkinson and Stucki) and emits SIXEL's bands of six pixel rows. The idea underneath is that a terminal is not only a text grid: a few escape codes can turn it into a bitmap display, and any program that can write bytes can draw in it. The README lists many terminals and downstream projects that speak SIXEL, including mlterm, WezTerm, iTerm2, xterm, RetroArch and Neofetch. It also ships C APIs and bindings for Python, Perl, PHP and Ruby.

## Install

```
brew install libsixel
# You also need a SIXEL-capable terminal (e.g. mlterm, WezTerm, iTerm2, or xterm built with SIXEL support).
```

## Try this

```
img2sixel --help
```
Lists the encoder's options, including palette size, dithering and 8-bit output.

```
img2sixel -p 16 < images/egret.jpg > egret.sixel
```
Converts a JPEG from stdin to SIXEL with a 16-colour palette; cat the file in a SIXEL terminal to see it.

```
sixel2png < egret.sixel > egret.png
```
Decodes a SIXEL file back into a PNG.

## What's unique

It is an encoder tuned for showing images in modern terminals while staying compatible with old DEC SIXEL hardware. Many terminals and tools support the protocol beyond this one.

## Caveats

By default output is 7-bit (terminals in 8-bit mode need -8), many terminals limit you to 16 colours unless configured, and the brief could not confirm how recently the project was updated.

## Links

- [GitHub repository (homepage)](https://github.com/saitoha/libsixel)
- [Demo video (SIXEL on a VT330, and img2sixel)](https://youtu.be/0SasrQ7pnbA)
- [Low-level API header (include/sixel.h.in)](https://github.com/saitoha/libsixel/blob/master/include/sixel.h.in)
