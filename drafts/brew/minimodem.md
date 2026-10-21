---
name: minimodem
title: minimodem
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, fsk, modem, protocol, quick, retro]
homepage: http://www.whence.com/minimodem/
scout_score: 9
status: draft
---

# minimodem

**TLDR;** A command-line software modem that turns text into audible FSK tones and decodes them back, using classic standards like Bell 103 and Bell 202.

Minimodem generates or decodes audio frequency-shift keying (FSK) tones at a baud rate you choose, with framing protocols layered on top. It can work in real time through the system audio device, or in batch mode on audio files. Text or data goes in and comes out as sound; sound goes in and text or data comes out.

The built-in protocols include Bell103, Bell202, RTTY, TTY/TDD, NOAA SAME and Caller-ID. These are the tones behind old dial-up modems, teletype machines, weather radio alerts and phone line caller display. One tool covers all of them.

The author describes it as a general-purpose software FSK modem for moving data between computers over an audio path: a cable, sound waves through air, radio, or a telephone line. The README leans on the Unix philosophy of simple tools that do one job, and a quoted user says minimodem "has all the boxes ticked."

The idea underneath is that any audio channel, even a speaker and a microphone, is a data pipe if you agree on how to encode bits as pitch. The README lists uses beyond serious comms, such as extracting Sega Saturn save games and decoding Arduino output. It also dares you to decode the modem data in a demo video yourself, with the hint to try 'pavucontrol'.

## Install

```
brew install minimodem
# Upstream targets GNU/Linux. On Debian: sudo apt-get install minimodem. Real-time use needs a working audio device (sound card, or a cable/speaker and mic).
```

## Try this

```
minimodem --help
```
Prints the option summary, where you can see how baud rate and protocol are chosen.

```
man minimodem
```
Opens the man page, which the README points to for usage since it gives no examples.

## What's unique

It packs a whole family of 1980s-era modem and teletype standards into one pipe-friendly command, and works over a plain speaker and microphone.

## Caveats

The README has no usage examples or flag reference, upstream is documented for GNU/Linux only so Homebrew on macOS may be less tested, and results depend on audio levels and noise.

## Links

- [Homepage](http://www.whence.com/minimodem/)
- [GitHub source](https://github.com/kamalmostafa/minimodem)
