---
name: jbig2dec
title: jbig2dec
source: brew
category: take-things-apart
commitment: quick
tags: [decoder, image-formats, jbig2, library, pdf, quick]
homepage: https://github.com/ArtifexSoftware/jbig2dec
scout_score: 5
status: draft
---

# jbig2dec

**TLDR;** A decoder for JBIG2, the monochrome image compression format hiding inside many scanned PDFs, with a command-line tool for unpacking streams.

jbig2dec is a decoder library plus a small example utility for JBIG2, the bi-level (black and white) image compression format, also known as ITU T.88 and ISO/IEC 14492. The `jbig2dec` command takes a JBIG2 file and decodes it. The `-o` option names the output file. The brief does not say what the default output format is.

The format matters because, per the README, JBIG2 is included by reference in Adobe's PDF 1.4 and later. Scanned documents in PDFs often carry JBIG2 images, so PDF tooling needs a decoder. This project exists to supply one.

The second invocation shows how JBIG2 lives inside other files. You can pass a global stream and a page stream separately, which the README says are generally extracted from some embedded format. JBIG2 is rarely a standalone file in practice. It is a pair of streams pulled out of a container.

The repository's file list suggests the structure of the spec. There are separate modules for arithmetic coding, generic regions, halftones, Huffman, MMR, refinement, symbol dictionaries, text regions, and page and segment handling, with PBM and PNG image writers. That makes the source a readable map of how a monochrome page can be split into symbols, regions, and halftones.

## Install

```
brew install jbig2dec
```

## Try this

```
jbig2dec --help
```
Prints the usage text and the options the decoder accepts.

```
jbig2dec -o page.png file.jbig2
```
Decodes a single JBIG2 file into the named output file. Whether the format follows the extension is not stated in the brief, so check the result.

```
jbig2dec -o page.png globals.jbig2 page.jbig2
```
Decodes a global stream and a page stream together, as extracted from an embedded source such as a PDF.

## What's unique

It is a small, focused decoder for a format that mostly hides inside PDFs, and its source is split along the spec's own building blocks.

## Caveats

The README says the program is only partially functional and should be useful only in limited contexts, and the brief found no release dates.

## Links

- [GitHub mirror (homepage)](https://github.com/ArtifexSoftware/jbig2dec)
- [Project site with updated versions](https://jbig2dec.com/)
- [Example JBIG2 test files](https://git.ghostscript.com/?p=tests.git;a=tree;f=jbig2)
- [Bug reports](https://bugs.ghostscript.com)
