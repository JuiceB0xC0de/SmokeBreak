---
name: gmic
title: G'MIC
source: brew
category: quick-weird-payoffs
commitment: afternoon
tags: [afternoon, filters, gimp, image-processing, scripting-language, visual]
homepage: https://gmic.eu/
scout_score: 5
status: draft
---

# G'MIC

**TLDR;** A scripting language for image pipelines with over a thousand built-in filters, usable from the shell, GIMP, Krita, or a webcam.

G'MIC is an image processing framework built around its own small scripting language. The `gmic` command-line tool is one front end. The same engine also runs inside editors such as GIMP, Krita and digiKam, through the G'MIC-Qt plug-in, and in a C++ library, a web service and a real-time webcam tool called ZArt. The homepage counts more than 1000 predefined algorithms and pipelines.

It works on lists of images rather than one image at a time, so a command can apply to a whole group or to chosen items in it. The data is generic: 1D signals, 2D colour images, 3D volumes and 3D+t multi-spectral sets, in 8/16-bit or float pixel types. The core is built on the CImg library and is multi-threaded with OpenMP.

The idea underneath is that filters are written in the language itself. Custom command files add new commands to the interpreter, so users build their own libraries on top of it. In the project's words: "G'MIC is an open framework: the default language can be extended with custom G'MIC-written commands, thereby adding new image filters and effects to the language." The homepage pitches the CLI as a companion to ImageMagick or GraphicsMagick, and the pipeline-and-extension model is what sets it apart from them.

## Install

```
brew install gmic
```

## Try this

```
gmic --help
```
Prints the built-in help for the command-line interface, a first look at the command vocabulary.

## What's unique

It is a full scripting language for image pipelines, not just a filter collection, and one engine serves the shell, GIMP, Krita and a webcam tool. Command files extend the language itself.

## Caveats

The project does not officially maintain macOS builds (Homebrew packages them), and the homepage has no command-level tutorial, so you will need the Scripting Tutorial and Technical Reference.

## Links

- [G'MIC homepage](https://gmic.eu/)
- [Download page (packages and source build instructions)](https://gmic.eu/download.html)
- [JOSS article (Tschumperlé, Fourey, Osgood, 2025)](https://doi.org/10.21105/joss.06618)
