---
name: msdfgen
title: msdfgen
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [cpp, distance-fields, fonts, graphics, quick, shaders]
homepage: https://github.com/Chlumsky/msdfgen
scout_score: 5
status: draft
---

# msdfgen

**TLDR;** Turns a font glyph or SVG shape into a three-channel distance field texture that keeps sharp corners crisp when a shader scales it up.

msdfgen is a C++ command-line tool and library. Give it a glyph from a font, an SVG file, or a text description of a shape, and it writes an image (PNG, BMP, TIFF or raw float formats). The default mode is `msdf`, a multi-channel signed distance field. It can also write a plain `sdf`, a perpendicular `psdf`, or `mtsdf`, which puts a true distance field in the alpha channel.

The problem it addresses is that a single-channel distance field rounds off sharp corners when magnified. The author's approach assigns each edge of the shape a colour (c, m, y or w), so that two edges meeting at a corner land in different channels. In the fragment shader, the median of the three channels gives back a signed distance, which is then used like an ordinary SDF to get anti-aliased edges. In the README's words, these fields "have the ability to reproduce sharp corners almost perfectly by utilizing all three color channels."

The idea underneath is that a texture can hold geometry instead of pixels. A 32x32 image of a letter can be scaled up to fill a screen and still look sharp. Once you have seen the three channels pulled apart, the trick is easy to follow. The method is described in the author's master's thesis, linked below.

## Install

```
brew install msdfgen
# Depends on freetype, libpng and tinyxml2, which brew pulls in. The README documents a prebuilt binary only for Windows.
```

## Try this

```
msdfgen msdf -font C:\Windows\Fonts\arialbd.ttf 'M' -o msdf.png -dimensions 32 32 -pxrange 4 -autoframe -testrender render.png 1024 1024
```
The README example: writes a 32x32 multi-channel field of the letter M to msdf.png, plus a 1024x1024 render rebuilt from it in render.png. Swap in any font path on your machine.

```
msdfgen msdf -font C:\Windows\Fonts\arialbd.ttf 'M' -o msdf.png -dimensions 32 32 -pxrange 4 -autoframe -testrendermulti render.png 1024 1024
```
Using -testrendermulti instead of -testrender leaves the colour channels uncombined, so you can see how the multi-channel field works.

```
msdfgen --help
```
Lists the modes, input types and options, including -exportshape, which saves a shape with its edge colouring as editable text.

## What's unique

The per-edge colouring trick lets one ordinary RGB texture carry sharp corners, and the shader needs only a median to read it. The tool's own test renders let you check the result without writing any shader code.

## Caveats

The README documents a prebuilt binary only for Windows, and building from source defaults to vcpkg. The SVG loader reads only the last vector path in a file. Treat the output channels as linear, not sRGB.

## Links

- [Project homepage (GitHub)](https://github.com/Chlumsky/msdfgen)
- [Master's thesis describing the method (PDF)](https://github.com/Chlumsky/msdfgen/files/3050967/thesis.pdf)
- [MSDF-Atlas-Gen, for generating whole font atlases](https://github.com/Chlumsky/msdf-atlas-gen)
