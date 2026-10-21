---
name: pngcheck
title: pngcheck
source: brew
category: take-things-apart
commitment: quick
tags: [file-formats, image, png, quick, reverse-engineering]
homepage: https://github.com/pnggroup/pngcheck
scout_score: 6
status: draft
---

# pngcheck

**TLDR;** Walks a PNG file chunk by chunk, printing offsets, lengths and decoded fields, and flags anything invalid, misplaced or obsolete.

pngcheck is a command-line tool that checks PNG files, including animated PNG, for validity and prints the metadata inside them. It reads one or more files and prints a report for each chunk: where it sits in the file, how long it is, what its header fields decode to, and any warnings or errors. The image data itself is not shown. A file with problems ends with `ERRORS DETECTED`.

The interesting part is what the report reveals. A PNG is a signature followed by a list of typed chunks, such as the header, palette, color profile, pixel data and metadata. Nothing is hidden, and pngcheck lays that list out in order. You can see the structure the format is built on, and see which tools wrote what into a file.

It also tracks the format as it changes. According to the README it supports all registered extension chunks, including newer ones like cICP, mDCV and cLLI, the animated PNG chunks, caBX content credentials and Apple's iDOT. It flags a chunk that is misplaced, such as an eXIf chunk after the image data, which the README says browsers ignore and PNG Third Edition no longer allows. It also flags deprecated chunks. In the README's sample, an old cLLi chunk is marked 'do not use'.

The Homebrew description also mentions JNG and MNG, the related JPEG and multi-image formats. The README text focuses on PNG.

## Install

```
brew install pngcheck
```

## Try this

```
pngcheck --help
```
Prints the usage summary and the list of options.

```
pngcheck -c -v test_pattern-PQ.png
```
Prints a colorized, verbose chunk-by-chunk dump of the file, ending with ERRORS DETECTED if it finds a problem. This is the README's own example.

## What's unique

It is a chunk-level dissector that keeps up with the newest PNG specification chunks. The output doubles as a readable map of how a PNG file is laid out.

## Caveats

The README gives no release date or platform notes, so how recently it was updated is unclear, though it is at version 4.0.1 and covers PNG Fourth Edition features.

## Links

- [GitHub repository (homepage)](https://github.com/pnggroup/pngcheck)
- [PNG Fourth Edition specification (W3C)](https://w3c.github.io/png/)
- [PNG Third Edition chunk definitions (W3C)](https://w3c.github.io/png/#cICP-chunk)
