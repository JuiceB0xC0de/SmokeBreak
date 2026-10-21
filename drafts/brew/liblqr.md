---
name: liblqr
title: liblqr
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, images, library, seam-carving]
homepage: https://liblqr.wikidot.com/
scout_score: 6
status: draft
---

# liblqr

**TLDR;** A C/C++ library for seam carving, the content-aware resizing trick that shrinks a picture by quietly removing paths of boring pixels.

Liquid Rescale Library (liblqr) is a free, open source implementation of the algorithm from a paper by Shai Avidan and Ariel Shamir. You hand it an image and a target size, and it resizes the image non-uniformly while trying to keep the important parts from distorting. Per the homepage, it also supports saving and loading carving information, real-time scaling, manual feature selection, and customizable progress reporting.

The idea underneath is that an image is not uniform. Some regions carry the subject and others are sky, wall, or blur. Seam carving treats resizing as a question of what to remove rather than how much to squash. The wiki names the paper but does not explain the mechanism, so the paper is the place to start if you want the details.

This is a library, not a program, and it installs no executables. Its reach comes from who uses it: the wiki lists the GIMP Liquid Rescale plug-in, digiKam, ImageMagick, and Photivo. If you have ever used content-aware scaling in one of those tools, this code may have been doing the work. The wiki says the API aims to be 'powerful, yet fast and easy to use'.

## Install

```
brew install liblqr
# Installs the library only, with glib and gettext as dependencies. There is no command to run; you link against it from C/C++ code.
```

## Try this

## What's unique

It is a reusable seam carving library rather than a feature locked inside one app, which is why several unrelated image tools can share it.

## Caveats

It has no command-line tool, and I could not verify the API, build steps, or platform support because only the wiki homepage loaded; the latest release listed is 0.4.3 from August 2024.

## Links

- [Homepage (Liquid Rescale Library wiki)](https://liblqr.wikidot.com/)
