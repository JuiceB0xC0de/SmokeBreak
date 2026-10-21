---
name: pmdmini
title: pmdmini
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, chiptune, fm-synthesis, pc-98, quick, retro]
homepage: https://github.com/mistydemeo/pmdmini
scout_score: 7
status: draft
---

# pmdmini

**TLDR;** A small C library and a pmdplay command that play PMD chiptunes, the music format written for Japan's PC-98 computers in the 1990s.

pmdmini plays back PMD music, the format made with the Professional Music Driver, a sound driver created by M. Kajihara for the NEC PC-98 line of computers. Many PC-98 games and fan songs were written in it. The project's own line is: "pmdmini allows playing back music written using PMD."

The PC-98 had a Yamaha YM2203 or YM2608 sound chip, which does FM synthesis. The files hold sequenced note data for that chip rather than recorded audio, so something has to emulate the chip to make sound. pmdmini does this by building on earlier engines, PMDXMMS and PMDWin, and using the OPNA FM sound generator from M88/cisc. It is a small, portable C reimplementation of a 1990s Japanese sound driver.

The README documents the C library, not the player. A caller initialises it, checks a file with pmd_is_pmd, sets a sample rate such as 48000 Hz, opens the file, then renders 16-bit samples in a loop. It can also report the song length, title and composer (both in Shift-JIS), track count, and the notes currently playing on each channel. Homebrew installs a pmdplay executable on top of it, but the README does not describe what pmdplay accepts or prints, so check its help output.

The door here is old Japanese computer music: sound chips, tracker-like sequencing, and a scene of files you can still download and hear. The linked Modland search and Zun's PMD page are places to find files.

## Install

```
brew install pmdmini
# depends on sdl2-compat, which brew pulls in; you also need a .m file in PMD format to play
```

## Try this

```
pmdplay --help
```
Prints the player's usage, since the README does not document its options.

## What's unique

It is a compact C reimplementation of the PMD sound driver that emulates the PC-98's FM chip, and it reports per-channel note data during playback.

## Caveats

The README covers only the C library, so pmdplay's usage is undocumented here, and the brief could not confirm when the project was last updated.

## Links

- [pmdmini homepage (GitHub)](https://github.com/mistydemeo/pmdmini)
- [Modland sample PMD music](http://www.exotica.org.uk/mediawiki/index.php?title=Special%3AModland&md=search&mod=&aut=&for=pmd&col=&ins=)
- [Zun's PMD music page](http://www16.big.or.jp/~zun/html/pmd.html)
