---
name: dovi_tool
title: dovi_tool
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, hdr, hevc, metadata, reverse-engineering, rust, video]
homepage: https://github.com/quietvoid/dovi_tool/
scout_score: 6
status: draft
---

# dovi_tool

**TLDR;** A command-line tool that reads, plots, edits and generates the hidden Dolby Vision metadata inside HEVC video streams.

Dolby Vision video carries a second stream of information alongside the picture: RPU (Reference Processing Unit) metadata, stored as NAL units inside the HEVC bitstream. It tells a display how to map brightness and colour frame by frame. dovi_tool reads that metadata from raw HEVC files, and from Matroska files for RPU extraction, and lets you look at it directly.

You can print a single frame's parsed RPU as JSON, export the whole list, or plot the L1 brightness metadata to a PNG. Beyond reading, it rewrites. It converts between Dolby Vision profiles (for example to 8.1 or 8.4), demuxes dual-layer files into base and enhancement layers, muxes them back, and injects or removes RPU data. The `generate` and `editor` commands take JSON config files, or exported Dolby Vision XML, and build or alter metadata from scratch.

The README calls it "a CLI tool combining multiple utilities for working with Dolby Vision" and credits a Python tool by yusesope that it ported to Rust. The door it opens is how HDR video is structured: a plain picture stream with a layer of per-frame instructions riding along, and that layer can be inspected like any other file format. The repo also hosts the `dolby_vision` Rust crate and a C-compatible library, `libdovi`.

## Install

```
brew install dovi_tool
# Alternatively build from source: needs Rust 1.88.0 or newer, then `cargo build --release`. On Linux, fontconfig is required, or build with `--no-default-features --features internal-font`. You need an HEVC or Matroska file with Dolby Vision content to do anything interesting.
```

## Try this

```
dovi_tool --help
```
Lists the subcommands: info, export, plot, convert, demux, extract-rpu, generate, editor and more.

```
dovi_tool extract-rpu video.hevc
```
Pulls the Dolby Vision RPU out of an HEVC file into a binary RPU file. Matroska input such as video.mkv also works.

```
dovi_tool plot RPU.bin -t "Dolby Vision L1 plot" -o L1_plot.png
```
Draws the L1 brightness metadata across the video as a PNG with your title.

## What's unique

Most Dolby Vision tools only show the metadata. This one rewrites it, converting profiles, generating RPUs from JSON or XML, and splitting and remuxing dual-layer streams.

## Caveats

You need your own Dolby Vision HEVC material to try it, the README gives no maintenance dates, and it says conversions such as FEL to MEL have side effects, so check output before relying on it.

## Links

- [Homepage (GitHub repository)](https://github.com/quietvoid/dovi_tool/)
- [Editor documentation](https://github.com/quietvoid/dovi_tool/blob/main/docs/editor.md)
- [Generator documentation](https://github.com/quietvoid/dovi_tool/blob/main/docs/generator.md)
