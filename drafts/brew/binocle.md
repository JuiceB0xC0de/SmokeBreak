---
name: binocle
title: binocle
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [binary, gui, quick, reverse-engineering, visual]
homepage: https://github.com/sharkdp/binocle
scout_score: 5
status: draft
---

# binocle

**TLDR;** A graphical viewer that turns any binary file into a colored pixel grid, so structure and hidden image-like regions show up by eye.

binocle opens a binary file and draws its bytes as pixels in a rectangular grid. Colors come from configurable rules, so a long run of zeros, a block of text, and a stretch of compressed data each look different. The README's examples include an ELF binary, an MS Teams memory dump, Doom assets, and perf record samples.

You control the offset into the file, the stride, and the width of the grid, and you choose how groups of bytes are colorized. Changing the width is the key move. When it matches the row length of some embedded bitmap, that region suddenly lines up into a recognizable picture. In the README's words, this lets you "identify interesting parts in large files and to reveal image-like regions."

The idea underneath is that you can look at a file before you parse it. Instead of reading a format spec, you let your eyes find the patterns first: headers, padding, tables, compressed blobs. The README lists binvis.io, veles.io, and cantor.dust as related tools that take the same visual approach.

## Install

```
brew install binocle
# Other routes from the README: cargo install binocle (needs a Rust toolchain), pacman -S binocle on Arch, or a .deb from the GitHub Releases page. It is a graphical program, so you need a desktop session.
```

## Try this

```
binocle --help
```
Lists the command-line options so you can see how to point it at a file.

## What's unique

It skips format parsing entirely and maps raw bytes to pixels, with adjustable offset, stride, and width so hidden images can be tuned into focus.

## Caveats

The README gives no release or commit dates, so whether it is actively maintained is unknown; it is also a GUI tool, not a terminal one.

## Links

- [GitHub homepage and README](https://github.com/sharkdp/binocle)
- [Screencast (MP4)](https://shark.fish/binocle.mp4)
- [Release page](https://github.com/sharkdp/binocle/releases)
