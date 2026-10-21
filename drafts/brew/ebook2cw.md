---
name: ebook2cw
title: ebook2cw
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, cw, ham-radio, morse, quick, text-to-speech]
homepage: https://fkurz.net/ham/ebook2cw.html
scout_score: 8
status: draft
---

# ebook2cw

**TLDR;** Turns a plain text file into Morse code audio, MP3 or OGG, so you can listen to a whole book sent in CW at the speed you choose.

ebook2cw reads a text file (ASCII, ISO 8859-1 or UTF-8) and writes Morse code audio files. You choose the speed, tone frequency, waveform and bitrate. It can split the output into numbered files at chapter markers, or by duration or word count, and it can add ID3 tags so the result behaves like an audiobook on a player.

It was written by Fabian Kurz (DJ5CW, formerly DJ1YFK) so that anyone could make a CW audiobook to their own liking. Earlier hams had already made Morse audiobooks, but shipping finished audio files was inflexible and used a lot of bandwidth. His answer was to distribute the converter and let people generate the audio themselves. The author "claims no credit for the original idea to convert books to morse."

Inline commands in the text change things mid-stream: `|f400` shifts the tone, `|w60` changes the speed, `|S1000` inserts silence, and prosigns can be written like `<AR>`. There is also Farnsworth spacing, which sends characters fast but stretches the gaps, a common way to learn Morse. It can mix in background noise at a chosen signal-to-noise ratio to simulate a real band.

The program can also be built as a CGI that returns a sound file from a URL. The Learn CW Online site uses this to generate Morse on demand.

## Install

```
brew install ebook2cw
```

## Try this

```
ebook2cw --help
```
Lists the options for speed, tone, output format, chapter splitting and noise.

```
ebook2cw -w 40 -c Chapter -o Book- Book.txt
```
Converts Book.txt at 40 wpm, splits it at the word Chapter, and writes Book-0000.mp3, Book-0001.mp3 and so on.

```
ebook2cw -X
```
Runs in test mode without generating any files.

## What's unique

It writes ordinary MP3 or OGG files from whole books, with inline commands to change pitch and speed mid-text. It can also be built as a CGI that generates Morse on demand.

## Caveats

Input must be plain text, so ebooks in other formats need converting first; UTF-8 support covers only Latin, Cyrillic, Greek, Hebrew and Arabic, and the optional GUI dates from 2013.

## Links

- [ebook2cw homepage](https://fkurz.net/ham/ebook2cw.html)
- [Source repository](https://git.fkurz.net/dj1yfk/ebook2cw)
- [Learn CW Online (lcwo.net), uses the CGI build](https://lcwo.net)
