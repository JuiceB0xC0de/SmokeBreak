---
name: msdf-atlas-gen
title: msdf-atlas-gen
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [cli, fonts, graphics, library, quick, signed-distance-fields, textures]
homepage: https://github.com/Chlumsky/msdf-atlas-gen
scout_score: 5
status: draft
---

# msdf-atlas-gen

**TLDR;** Turns a font file into a packed texture of multi-channel distance fields, so game text stays sharp at any scale.

msdf-atlas-gen takes a TTF or OTF font, picks a set of glyphs (a character set, glyph indices, or everything), and generates a distance field for each one. It then packs them into a single bitmap and writes out the image plus layout data as JSON, CSV, or an Artery Font file. It runs as a console program or as a C++ library.

The reason for it: games and other real-time renderers keep text in texture memory. Ordinary bitmap glyphs go blurry or blocky when scaled. A distance field stores, for each pixel, how far it is from the glyph edge, and a shader can turn that back into a crisp outline at nearly any size. In the author's words, "This is a utility for generating compact font atlases using MSDFgen."

The multi-channel trick is the interesting part. In MSDF mode, glyph edges are coloured across three channels so that sharp corners survive upscaling, which a single-channel distance field rounds off. The README lays out six atlas types (hardmask, softmask, sdf, psdf, msdf, mtsdf) and the trade-offs between them. Generating the same font in a few types and looking at the images is a good way to see the idea.

The library side also offers a dynamic atlas that grows as new glyphs are needed, for programs that cannot know their text ahead of time.

## Install

```
brew install msdf-atlas-gen
```

## Try this

```
msdf-atlas-gen --help
```
Lists the options for atlas type, size, pixel range, packing and output formats.

```
msdf-atlas-gen -font <fontfile.ttf/otf> -imageout atlas.png
```
Generates an MSDF atlas (the default type) for the font and saves it as a PNG you can open and inspect.

```
msdf-atlas-gen -font <fontfile.ttf/otf> -type sdf -imageout atlas.png -json atlas.json
```
Writes a single-channel SDF atlas plus a JSON file with font metrics, per-glyph layout and kerning pairs.

## What's unique

It uses three-channel MSDF encoding to keep glyph corners sharp when scaled up. It is also both a command-line tool and a library, with a dynamic atlas that grows on demand.

## Caveats

The README documents only a Windows binary and does not state a maintenance status. The tool is aimed at real-time graphics, and the README warns that colour values must be read as linear, not sRGB.

## Links

- [GitHub repository and README](https://github.com/Chlumsky/msdf-atlas-gen)
- [MSDFgen, the underlying distance-field library](https://github.com/Chlumsky/msdfgen)
- [Changelog (linked from README)](https://github.com/Chlumsky/msdf-atlas-gen/blob/master/CHANGELOG.md)
