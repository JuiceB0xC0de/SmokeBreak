---
name: lensfun
title: Lensfun
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, image-processing, library, optics, photography]
homepage: https://lensfun.github.io/
scout_score: 5
status: draft
---

# Lensfun

**TLDR;** An open database of camera lens characteristics plus a library that uses it to undo distortion, colour fringing and vignetting in photos.

Lensfun is a C/C++ library with an XML database of photographic lenses and how they misbehave. Client code looks up a lens, then uses the stored model to correct three defects: geometric distortion, transversal chromatic aberration (colour fringes toward the frame edges), and vignetting (darkened corners). The C interface wraps the C++ classes, and GLib parses the database.

It exists because an earlier free lens database, PTLens, froze when its author went commercial. That author allowed Lensfun to build on the data, and the code was rewritten from scratch around a new XML format. The README's stated goal is "to provide a open source database of photographic lenses and their characteristics."

The idea underneath is that every lens has a measurable, repeatable fingerprint, and a photo can be corrected by inverting it. Most people meet Lensfun indirectly, when a raw converter quietly fixes a wide-angle shot. Here you can reach the pieces directly: the database, the update script, and `lenstool`, which the build options describe as the reference implementation.

The brief does not detail the correction math, so the library source and the online manual are the places to dig into how a lens model becomes a pixel remap.

## Install

```
brew install lensfun
```

## Try this

```
lenstool --help
```
Lists what the reference tool can do with the lens database and with images.

```
lensfun-update-data --help
```
Shows how to fetch the latest lens database updates; it needs CA certificates on the system.

```
lensfun-add-adapter --help
```
Shows the helper for adding lens adapter entries to the database.

## What's unique

The lens data is a community-maintained open database, licensed separately from the code, under CC BY-SA 3.0, with LGPL 3 for libraries and GPL 3 for apps. That split is unusual for a software project.

## Caveats

It corrects only distortion, lateral chromatic aberration and vignetting, and it is a library first, so most of the payoff comes from software built on it. The latest release on the homepage is a 0.3.4 maintenance release from July 2023.

## Links

- [Lensfun homepage](https://lensfun.github.io/)
- [GitHub repository](https://github.com/lensfun/lensfun)
- [Online user manual (latest)](https://lensfun.github.io/manual/latest)
