---
name: dvanalyzer
title: DV Analyzer
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, dv, file-formats, needs-sample-files, preservation, video]
homepage: https://mediaarea.net/DVAnalyzer
scout_score: 6
status: draft
---

# DV Analyzer

**TLDR;** Reads a DV video file frame by frame and reports the tape-transfer errors most capture tools never mention, from concealed video blocks to timecode jumps.

DV Analyzer examines the raw DV stream you get when a miniDV, DVCam or DVCPro tape is copied to a file. It reports problems introduced in that transfer: video error concealment, invalid audio samples, timecode inconsistency, odd use of arbitrary bits in video DIF blocks, and structural DIF problems. It also reads patterns in the stream, such as changes in timecode, recording date and time markers, and the first and last frame of each recording.

The reason it exists is stated on the homepage: tape-to-file reformatting is a point where permanent errors are at particularly high risk, and "Most capture tools for DV only report errors if they are significant, such as a lost frame, whereas other documented errors are not reviewed." The tool aims to make automated quality control possible, checking the integrity of a transfer frame by frame. It was initially funded, designed and led by AVPreserve and is developed by MediaArea.

The idea underneath is that a DV frame carries more than picture and sound. Every frame holds its own temporal metadata, so a file is a long record of how the tape was recorded and how it was read back. That makes it a way into digital video preservation and into how a consumer tape format lays its data out in small blocks. The homepage links a case study with sample DV files covering concealment, audio errors, DIF incoherency and STTS fluctuation.

## Install

```
brew install dvanalyzer

It needs a DV file to analyze. Tape hardware is only needed if you want to capture your own.
```

## Try this

```
dvanalyzer --help
```
Prints the command-line options, which is the safest place to start since no usage examples were found in the project's pages.

## What's unique

Few tools look at the raw DV bitstream this closely. It is built for preservation QC and surfaces per-frame errors and temporal metadata that capture software usually ignores.

## Caveats

No README or usage examples were found, so the command syntax is unconfirmed, and the status and last release date are unknown, though the homepage lists version 1.4.2.

## Links

- [Homepage](https://mediaarea.net/DVAnalyzer)
- [GitHub repository](https://github.com/MediaArea/DVAnalyzer)
