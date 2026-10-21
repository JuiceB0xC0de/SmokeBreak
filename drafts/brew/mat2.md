---
name: mat2
title: mat2
source: brew
category: take-things-apart
commitment: quick
tags: [file-formats, metadata, privacy, python, quick]
homepage: https://github.com/jvoisin/mat2
scout_score: 6
status: draft
---

# mat2

**TLDR;** Strips hidden metadata from images, PDFs, Office files, audio, video and archives, and admits it cannot promise the result is fully clean.

mat2 takes files and writes cleaned copies next to the originals. A photo named `myfile.png` becomes `myfile.cleaned.png`. It handles images, PDFs, Office documents, audio, video, archives and SVGs. It ships as a Python library (libmat2), a command line tool, and a Dolphin file manager service menu.

The reason it exists is that files quietly record who made them and when. Cameras note when and with what a picture was taken. Office and PDF tools add author and company names. mat2's stated job is "getting rid, as much as possible, of metadata."

Under the hood, each file goes to a format-specific cleaner. Those lean on helpers such as ExifTool, FFmpeg, mutagen, and GObject bindings for Poppler, GdkPixbuf and librsvg. The `--show` flag lists the metadata it can detect without removing anything, which is a quick way to see what your own files give away.

The idea underneath is that a file format is a container with more rooms than you see. Cleaning one means learning where each format hides things. By default mat2 may re-encode or alter content to strip more, so a cleaned PDF can lose selectable text. The `-L` lightweight flag removes less and leaves the data alone.

## Install

```
brew install mat2
# Needs Python 3 and several helpers (exiftool, ffmpeg, poppler, gdk-pixbuf, librsvg); Homebrew pulls these in as dependencies.
```

## Try this

```
mat2 --help
```
Lists the options, including show, lightweight mode, in-place cleaning and how to handle unknown archive members.

```
mat2 --show myfile.png
```
Prints the metadata mat2 can find in the file without changing it. Substitute any file of your own.

```
mat2 myfile.png
```
Writes a cleaned copy named myfile.cleaned.png and leaves the original untouched.

## What's unique

It says plainly that it cannot prove a file is clean, so an empty `--show` result should not be trusted. It also gives you an explicit choice between thorough stripping that may alter content and a lightweight mode that does not.

## Caveats

Cleaning is best effort and the README warns that not every metadata field can be detected; the default mode can alter file content, and `--inplace` overwrites with no backup.

## Links

- [mat2 GitHub repository (homepage)](https://github.com/jvoisin/mat2)
- [Metadata Cleaner (GTK GUI built on mat2)](https://gitlab.com/metadatacleaner/metadatacleaner)
- [mat2-web (web interface)](https://0xacab.org/jvoisin/mat2-web)
- [Issues](https://github.com/jvoisin/mat2/issues)
