---
name: codevis
title: codevis
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [code-visualization, images, quick, rust, visual]
homepage: https://github.com/sloganking/codevis
scout_score: 6
status: draft
---

# codevis

**TLDR;** Renders every source file in a folder into one large syntax-highlighted image, so you can see the shape and size of a codebase at a glance.

codevis walks a directory, picks up every source or UTF-8 encodable file, and draws them all into a single image. Files it recognizes are syntax-highlighted. The README puts it plainly: "These images show the shape and size of files, but not the exact characters inside the files."

The result is a kind of map. Big files look big, small files look small, and the colours hint at the language and structure. It is a different view from a file tree or a table of line counts, and it makes lopsided projects easy to spot.

There is also a readable mode. With --readable, the same image can be zoomed into until the text is legible, and --line-nums and --show-filenames add line numbers and labels. The README does not say why the author built it. It points to two sister projects, codemov for video output and codevis-gui, for related formats.

The underlying idea is treating source code as visual data rather than text. Once a codebase is a picture, you can compare projects, watch one grow, or just look at something you usually only read.

## Install

```
brew install codevis
# Homebrew builds and installs it with no extra caveats. Alternatively, install Rust and run: cargo install codevis
```

## Try this

```
codevis -i ./
```
Visualizes all files in the current directory and subdirectories, writing the image to ./output.png.

```
codevis -i ./ -o ./different_name.png
```
Does the same but saves the image under the name you choose.

```
codevis -i ./ -o ./output.png --bg-pixel-color style-checkerboard-darken --readable --line-nums --show-filenames
```
Renders a readable version with a checkerboard background, line numbers and filenames, which you can zoom into to read the text.

## What's unique

It turns a whole codebase into one zoomable picture instead of a file tree or stats table. The same image works as an overview and, in readable mode, as something you can read up close.

## Caveats

The default image shows shape and size rather than exact characters, only UTF-8 encodable files are included, and the README gives no release or maintenance information.

## Links

- [codevis homepage (GitHub)](https://github.com/sloganking/codevis)
- [codemov (sister project, video output)](https://github.com/sloganking/codemov)
- [codevis-gui](https://github.com/sloganking/codevis-gui)
