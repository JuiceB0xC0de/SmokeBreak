---
name: babl
title: babl
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, color, gimp, library, pixels]
homepage: https://www.gegl.org/babl/
scout_score: 5
status: draft
---

# babl

**TLDR;** A C library that converts pixels between any two formats by assembling a chain of conversions at runtime, and the engine under GIMP's color handling.

babl converts pixel data between formats: different bit depths, data types, color models, color spaces and component orders. You describe a source format and a destination format, and babl builds a "fish", a conversion object for that pair. You run the fish over a buffer and get converted pixels out.

The idea underneath is that it does not store a converter for every pair of formats. Formats are assembled from registered color models and data types, and every conversion has a reference implementation in 64-bit floating point. Fast paths (SIMD, lookup tables) are registered as shortcuts, and babl can use them as intermediate steps when it builds a fish. Runtime profiling and validation pick the code path, and the results are cached between runs. The project's design rule is that the 64-bit reference conversions decide what is correct for any extension.

It exists because GEGL's GeglBuffer stores image tiles and converts pixels implicitly through babl formats, so GIMP can handle many pixel layouts without a hand-written converter for each. In the project's words, "Most users of babl do not know they are using babl and it is GIMP itself which uses babl". Color spaces can be built from chromaticity coordinates or ICC v2/v4 profiles, and new formats and conversions can be added as shared-object extensions.

It is a door into how image software thinks about color: why alpha handling loses precision, why conversion paths matter, and how a graph of small transforms beats a table of every pair.

## Install

```
brew install babl
# optional: lcms2 (installed as a dependency here) is what enables CMYK ICC profiles
```

## Try this

```
babl --help
```
Prints usage for the command-line tool the formula installs. The homepage documents no usage for it, so this is the way in.

```
git clone https://gitlab.gnome.org/GNOME/babl.git/
```
Clones the source from GNOME's GitLab, so you can read the reference conversions and the fast-path extensions.

## What's unique

It builds a chain of conversions from a small set of primitives instead of storing a converter for every format pair, and it treats a 64-bit float reference implementation as the arbiter of correctness.

## Caveats

Mostly a library for other programs. The homepage shows no usage for the CLI tool, and spectral formats and data types that are not a multiple of 8 bits are not yet implemented.

## Links

- [babl homepage](https://www.gegl.org/babl/)
- [Git repository (GNOME GitLab)](https://gitlab.gnome.org/GNOME/babl.git/)
- [Release tarballs (download.gimp.org)](https://download.gimp.org/pub/babl/)
