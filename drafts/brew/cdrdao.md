---
name: cdrdao
title: cdrdao
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, ancient, burning, cd, cd-text, needs-hardware, optical]
homepage: https://cdrdao.sourceforge.net/
scout_score: 5
status: draft
---

# cdrdao

**TLDR;** Burns CDs in disk-at-once mode from a plain-text description of the disc, giving control over pre-gaps and sub-channel data that most burners hide.

Cdrdao records audio or data CD-Rs from a textual description of the disc called a toc-file. The file lists the tracks, pre-gaps and sub-channel fields such as catalog number, ISRC, index marks and copy or pre-emphasis flags. Cdrdao then writes the whole disc, lead-in, tracks and lead-out, in a single pass. The homepage says it accepts WAVE and raw audio files as input, and it can also copy audio, data and mixed-mode discs.

The reason it exists is the difference between two recording modes. According to the homepage, track-at-once recording cannot define what goes in the pre-gaps, which rules out things like hidden bonus tracks or track intros. Disk-at-once gives full control of the disc. In the project's words: "DAO recording is the only way to write data to the unused R-W sub-channels for e.g. CD-G or CD-TEXT."

The idea underneath is that a CD is not a folder of files. It is a layout with a spiral of sectors, gaps between tracks, and hidden channels running alongside the audio. Here that layout is a text file you can edit, diff and keep in version control. It is a way to see what the disc format really contains.

The install also brings helper executables: cue2toc, toc2cddb, toc2cue and toc2mp3. Their names suggest conversions between toc-files, cue sheets, CDDB data and MP3, but the homepage does not describe them, so check each with its own help output.

## Install

```
brew install cdrdao
# Actually burning a disc needs a CD recorder drive and blank CD-R or CD-RW media.
```

## Try this

```
cdrdao --help
```
Lists the commands and options, which shows what the tool can do before any disc is involved.

```
cue2toc --help
```
Shows usage for the helper installed alongside cdrdao. Its name suggests it converts cue sheets to toc-files, though the homepage does not confirm this.

```
toc2cue --help
```
Shows usage for the helper whose name suggests it converts toc-files to cue sheets.

## What's unique

It treats the disc as an editable text description rather than a list of files, exposing pre-gap contents and sub-channel data that most burning tools hide.

## Caveats

It needs a real CD recorder drive, writing to CD-R is irreversible, and the homepage shows no release date or version, so how actively it is maintained is unclear.

## Links

- [Cdrdao homepage](https://cdrdao.sourceforge.net/)
