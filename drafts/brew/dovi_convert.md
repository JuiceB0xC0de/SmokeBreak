---
name: dovi_convert
title: dovi_convert
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, dolby-vision, hdr, mkv, remux, video]
homepage: https://docs.doviconvert.com
scout_score: 5
status: draft
---

# dovi_convert

**TLDR;** Converts Dolby Vision Profile 7 MKV rips to Profile 8.1 without re-encoding, after scanning each file to decide whether that is safe.

dovi_convert takes UHD Blu-ray style MKV files and rewrites their Dolby Vision structure. Profile 7 carries a base layer, an Enhancement Layer and dynamic metadata (the RPU). Profile 8.1 keeps the base layer and the RPU, and drops the Enhancement Layer. The tool does this by extracting and remuxing, so the video is never re-encoded.

The reason it exists is device support. Per the README, "Most streaming devices (Apple TV, Shield, Amazon Fire*, etc.) don't support Profile 7's Enhancement Layer." They either fall back to plain HDR10 or strip the layer blindly and damage the picture. The author wanted a conversion that keeps the dynamic metadata so Dolby Vision still plays properly.

The interesting part is the scan step. Some Profile 7 files have a Complex FEL, where the enhancement layer carries real brightness expansion rather than being nearly empty. The tool flags these and skips them by default, since dropping that layer changes the picture. It is a small look at how HDR video is layered inside a container, and at why "just strip the extra layer" is not always harmless.

Originals are backed up automatically. A `--delete` flag removes them permanently. It leans on dovi_tool, ffmpeg, mkvtoolnix and mediainfo, and credits dovi_scripts as the earlier tool that inspired it.

## Install

```
brew install dovi_convert
# Needs Python 3 plus ffmpeg, mkvtoolnix, mediainfo and dovi_tool; the README says missing ones are detected and can be installed automatically.
# Windows is supported only through WSL2 or Docker.
```

## Try this

```
dovi_convert --help
```
Lists the available commands and options.

```
dovi_convert scan
```
Analyzes the files in the current directory and reports which are Profile 7 and which have a Complex FEL, without changing anything.

```
dovi_convert convert Movie.mkv
```
Converts one Profile 7 MKV to Profile 8.1, keeping the dynamic metadata and backing up the original.

## What's unique

It analyzes before converting and refuses files whose enhancement layer carries real picture information, instead of stripping every Profile 7 file. The work is metadata extraction and remuxing, with no re-encoding.

## Caveats

The README opens with "Development is paused for now" and says bug fixes have ceased; film grain and other FEL data are dropped, and it only makes sense if your player cannot handle Profile 7 FEL.

## Links

- [Documentation homepage](https://docs.doviconvert.com)
- [GitHub repository](https://github.com/cryptochrome/dovi_convert)
- [Development pause announcement (GitHub discussion)](https://github.com/cryptochrome/dovi_convert/discussions/54)
