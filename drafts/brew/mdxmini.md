---
name: mdxmini
title: mdxmini
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, c-library, chiptune, fm-synthesis, quick, retro, x68000]
homepage: https://github.com/mistydemeo/mdxmini/
scout_score: 6
status: draft
---

# mdxmini

**TLDR;** A small C library and the mdxplay player that render MDX chiptunes, the FM-synth music format of Sharp's X68000 home computer, into audio.

mdxmini plays MDX files, a music format from the Sharp X68000, a Japanese 16-bit home computer. In the README's words, its "8-channel YM2151 sound chip and 1-channel PCM chip gave it excellent music support." A large archive of MDX songs from that era still exists, and this library is a way to hear them without the original machine.

It is built as a library first. A caller opens an MDX file, optionally with a directory of .pdx sample files, reads the title, length and track count, then repeatedly asks for chunks of raw 16-bit audio at a chosen sample rate. Each chunk can also report which note is sounding on each of the eight FM channels and which sample is playing on the PCM channels, which is handy if you want to draw a visualizer.

The lineage is traced in the README's credits: the original X68000 MXDRV player, then Daisuke Nagano's Unix mdxplay, then BouKiCHi's library. The Homebrew formula installs an executable called mdxplay. The README does not describe it, so treat its options as something to discover with --help.

The larger door here is the sound itself. FM synthesis on a chip like the YM2151 shaped a lot of 1980s and 90s game and computer music, and a small, readable C API makes this a convenient place to see how a tracker-style song file turns into samples.

## Install

```
brew install mdxmini
# installs the mdxplay executable; depends on sdl2-compat
# some songs need matching .pdx sample files on disk, and you must supply your own MDX files
```

## Try this

```
mdxplay --help
```
Prints the player's usage, since the README does not document the executable.

## What's unique

It is a reusable playback library with live per-channel note data, not only a player. The same core is used in an Android player and in the Modizer music-module player.

## Caveats

The README documents only the library API, with no build steps or description of mdxplay, and I could not confirm the project's recent activity or that titles display correctly, since they are Shift-JIS encoded.

## Links

- [mdxmini homepage (GitHub)](https://github.com/mistydemeo/mdxmini/)
- [Fossil of FM-sound era MDX archive](http://www42.tok2.com/home/mdxoarchive)
- [ruby-mdxplay demo program](https://github.com/mistydemeo/ruby-mdxplay)
