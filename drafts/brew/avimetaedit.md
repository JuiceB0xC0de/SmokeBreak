---
name: avimetaedit
title: AVI MetaEdit
source: brew
category: take-things-apart
commitment: quick
tags: [avi, file-formats, metadata, preservation, quick]
homepage: https://mediaarea.net/AVIMetaEdit
scout_score: 5
status: draft
---

# AVI MetaEdit

**TLDR;** A preservation tool from the US National Archives project that reads, edits, validates and exports metadata inside AVI video files.

AVI MetaEdit takes an AVI file, Standard or OpenDML, and lets you embed, edit, import and export the metadata stored inside it. It can also check a file against file-structure and metadata recommendations from the U.S. National Archives, Microsoft and IBM.

The homepage frames it as a preservation tool. It was initially funded by NARA (the National Archives and Records Administration) through FADGI, designed and led by AVPreserve, and developed by MediaArea. The goal is for archived AVI files to carry correct, standards-conformant metadata.

The interesting idea is what "correct" means for an old container format. AVI is a chunked file layout, and the project's documentation covers views and reports (TECH, CORE, TRACE), LIST-INFO and IMIT metadata definitions, XML chunks, audio/video-only checksums, and validation rules with explained errors and warnings. Those pages are a way into how archivists decide what a well-formed file looks like. The brief did not cover the internals beyond those headings.

## Install

```
brew install avimetaedit
```

## Try this

```
avimetaedit --help
```
Prints the list of options the command-line tool supports, a starting point for reading, editing and exporting metadata.

## What's unique

It goes beyond reading tags: it checks AVI files against named archival specifications from NARA, Microsoft and IBM. It also began as a federally funded preservation project.

## Caveats

Homepage lists version 1.0.2 but I could not confirm a recent release date, the README has no command examples, and it only handles AVI.

## Links

- [Homepage](https://mediaarea.net/AVIMetaEdit)
- [GitHub repository (MediaArea)](https://github.com/MediaArea/AVIMetaEdit)
- [GitHub repository (usnationalarchives, linked from README)](https://github.com/usnationalarchives/AVI-MetaEdit)
