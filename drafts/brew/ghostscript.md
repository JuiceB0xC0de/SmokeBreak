---
name: ghostscript
title: Ghostscript
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, converter, language, pdf, postscript, rendering]
homepage: https://www.ghostscript.com/
scout_score: 5
status: draft
---

# Ghostscript

**TLDR;** A PostScript and PDF interpreter that renders, converts and compresses documents from one command, and runs PostScript as the programming language it is.

Ghostscript is an open-source interpreter for the PostScript language and for PDF files. The main program is `gs`. It reads a document, runs it, and sends the result to an output device you pick with `-sDEVICE=`. The device might be `png16m` for raster images or `pdfwrite` for a new PDF. The same engine is also available as an embeddable library with Python, Java and C# bindings.

The repository is called GhostPDL, and Ghostscript is one part of it. In the README's words, it is "a unified package of interpreters and a shared graphics library for rendering, converting, and manipulating documents across every major page description language and many image formats." Besides PostScript and PDF, the family has interpreters for PCL (`gpcl6`) and XPS (`gxps`). They all sit on one shared graphics library. Run as GhostPDL, it detects the input language from file signatures and heuristics, so mixed job streams need no flag.

The idea underneath is that a page description is a program. PostScript is a real stack-based language, and a printer or viewer is just something that executes it. Once you see that, `gs` becomes a way to watch the language run. Many everyday tools, such as PDF compressors, print filters and converters, are built on this kind of interpreter.

The many wrapper scripts it installs, such as `ps2pdf`, `ps2ascii` and `pdf2ps`, are shortcuts for common `gs` invocations. The README's own examples are one-liners, so you can get useful results without reading the manual.

## Install

```
brew install ghostscript
# No account or runtime needed. Verify with: gs --version
```

## Try this

```
gs -dBATCH -dNOPAUSE -sDEVICE=png16m -r300 -sOutputFile=page_%03d.png input.pdf
```
Renders each page of a PDF to its own numbered 300 DPI PNG.

```
gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook -sOutputFile=compressed.pdf input.pdf
```
Rewrites a PDF with the /ebook preset (150 dpi images), often making it much smaller.

```
gs -h
```
Prints help and lists every output device your build supports.

## What's unique

One family of tools handles PostScript, PDF, PCL and XPS on a shared graphics engine, and it detects the input language on its own. It is also a real PostScript interpreter you can use to learn the language.

## Caveats

It is dual licensed: AGPL v3, or a commercial licence from Artifex for proprietary use. Unless built with GS_THREADSAFE, only one Ghostscript instance may be active at a time. Homebrew's compatibility symlinks for the old versioned path are due to be removed in 10.07.0.

## Links

- [Homepage](https://www.ghostscript.com/)
- [Command-line reference (docs)](https://ghostscript.readthedocs.io/en/latest/Use.html)
- [Source repository (GhostPDL README)](https://github.com/ArtifexSoftware/ghostpdl)
- [Binary downloads](https://ghostscript.com/releases)
