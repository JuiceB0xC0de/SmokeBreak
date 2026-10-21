---
name: vgmstream
title: vgmstream
source: brew
category: take-things-apart
commitment: quick
tags: [audio, cli, decoder, game-audio, quick, reverse-engineering]
homepage: https://vgmstream.org
scout_score: 8
status: draft
---

# vgmstream

**TLDR;** Decodes hundreds of proprietary video game audio formats, so streamed music and sound pulled from old game files plays or converts to .wav.

vgmstream is a library with a set of players and converters built on top of it. Feed it a game's streamed audio file, in one of hundreds of formats, and it decodes the sound. `vgmstream-cli` writes the result out as a .wav, and `vgmstream123` plays it from the terminal. Other front ends include plugins for Winamp, foobar2000, XMPlay and Audacious.

Game audio is a mess of formats. Some are typical engine containers, and some are obscure codecs used by a single game. The README says the project aims for "high accuracy and compatibility". It reads the loop points and sample counts stored in the files, so looped background music repeats seamlessly instead of clicking at the seam.

Two features let you handle files nobody has written support for. TXTH lets you describe a raw or unknown audio layout in a small text file. TXTP sets per-file options, such as forcing a loop, removing channels, or fusing several files into one. Neither needs code.

The door underneath is that a game's audio is data with a structure you can learn. Each format in the supported list is someone's reverse-engineering work, written down so the rest of us can hear it. It only decodes. In the README's words: "vgmstream cannot *encode* (convert from `.wav` to a game format), it only *decodes* (plays game audio)."

## Install

```
brew install vgmstream
```

## Try this

```
vgmstream-cli --help
```
Lists the decoder's options, including how to write a game audio file out as a .wav.

```
vgmstream123 --help
```
Shows the options for the terminal player, which plays game audio files directly.

## What's unique

It treats each game's quirks, such as loop points, subsongs and companion files, as part of the format. Looped music plays the way the game intended. TXTH lets you teach it a new layout without code.

## Caveats

It decodes only and cannot encode. The format list is described as "not always current", and the brief could not confirm recent commits.

## Links

- [Homepage (nightly builds, web player, downloads)](https://vgmstream.org)
- [Source on GitHub](https://github.com/vgmstream/vgmstream)
- [Supported formats list](https://github.com/vgmstream/vgmstream/blob/master/doc/FORMATS.md)
- [Usage guide](https://github.com/vgmstream/vgmstream/blob/master/doc/USAGE.md)
- [Numbered releases](https://github.com/vgmstream/vgmstream/releases)
