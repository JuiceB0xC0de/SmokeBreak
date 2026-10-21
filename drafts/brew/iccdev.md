---
name: iccdev
title: iccDEV
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cli, colour, file-formats, icc, images]
homepage: https://github.com/InternationalColorConsortium/iccDEV
scout_score: 5
status: draft
---

# iccDEV

**TLDR;** The International Color Consortium's own toolkit for opening, validating, editing and applying ICC colour profiles, including the newer iccMAX model, from the command line.

Every photo, monitor and printer carries or assumes an ICC profile, a small binary file that says how its numbers map to real colour. iccDEV is the ICC's open source toolkit for reading and writing those files. Its tools dump a profile's tags, validate it, run colour values or TIFF images through a chain of profiles, and report round-trip error.

The useful trick is the text round trip. `iccToJson` and `iccToXml` turn a binary profile into something you can read and edit, and `iccFromJson` and `iccFromXml` turn it back. The graphical viewer is read-only, and the README says so: to change a profile, convert it, edit the text, and convert it back.

Underneath is the question of how colour is described across devices: profile connection spaces, rendering intents, and a CMM that applies them. Most ICC utilities handle the classic v2 and v4 profile model. iccDEV also covers iccMAX, the newer and more flexible specification. The project was formerly known as DemoIccMAX.

The same libraries ship as a Python module, a MATLAB package, a WebAssembly npm package, a Docker image and an MCP server for AI assistants. The README's own line is: "You do not need to build iccDEV to use it."

## Install

```
brew install iccdev
# Homebrew installs the tools but not the sample profiles. Get sRGB_v4_ICC_preference.icc from the repository's Testing/ directory, or use the Docker image, which includes the samples: docker pull ghcr.io/internationalcolorconsortium/iccdev:latest
```

## Try this

```
iccDumpProfile -v sRGB_v4_ICC_preference.icc
```
Prints the contents of the sample sRGB profile, with a Validation Report appended at the end.

```
iccToJson sRGB_v4_ICC_preference.icc srgb.json
```
Converts the binary profile into editable JSON; iccFromJson converts it back to a binary ICC file.

```
iccRoundTrip sRGB_v4_ICC_preference.icc
```
Reports round-trip Delta E statistics for the profile.

## What's unique

It comes from the ICC itself and targets the iccMAX profile model as well as v2/v4. A round-trip and PAWG assessment report is built in, so checking a profile's quality needs no separate tool.

## Caveats

Binaries are attached to a rolling latest build rather than version tags, and the Docker image is large and slow because its tools are sanitizer-instrumented and it has no display for the GUI.

## Links

- [iccDEV repository (homepage)](https://github.com/InternationalColorConsortium/iccDEV)
- [Using iccDEV guide](https://github.com/InternationalColorConsortium/iccDEV/blob/master/docs/using-iccdev.md)
- [CLI tool reference](https://github.com/InternationalColorConsortium/iccDEV/blob/master/docs/tools-cli-reference.md)
- [Latest release page](https://github.com/InternationalColorConsortium/iccDEV/releases/latest)
