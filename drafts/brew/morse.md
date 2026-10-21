---
name: morse
title: morse
source: brew
category: sound-and-live-coding
commitment: quick
tags: [ancient, audio, ham-radio, morse, quick, trainer]
homepage: http://www.catb.org/~esr/morse/
scout_score: 7
status: draft
---

# morse

**TLDR;** A command-line Morse code trainer that adapts to your mistakes, plus a QSO generator that pipes simulated radio contacts into it for copying by ear.

morse-classic plays text as Morse beeps. The text can come from standard input, from command-line arguments, from a random letter generator (-r), or from what you type yourself (-i). The README describes it as "a Morse-code training program for aspiring radio hams", aimed at the 5-words-per-minute Element 1 test.

The training modes are what make it more than a beeper. In random mode it starts with easy letters and leans toward the ones you get wrong. In the type-along modes (-t, -T, -s) you type back what you hear, and the program keeps right and wrong counts per character. It uses them to decide when to prompt you, and with -d when to change speed. Farnsworth spacing (-F) keeps the characters fast while stretching the gaps, which targets hearing whole letters as sounds rather than counting dots and dashes.

The companion QSO program prints a simulated amateur radio contact, resembling those used in the ARRL test. Because it writes to standard output, you can pipe it into morse and copy a conversation that does not exist. This is the Unix idea doing something unexpected: text streams become a listening skill.

The README lays out a progression: learn the alphabet slowly, drill, do real-time drills with hints, take a simulated test, then push to 13 wpm with 24 wpm spacing. It is written by Eric S. Raymond and the homepage shows recent maintenance. It is an old-school tool and says so in its plain interface.

## Install

```
brew install morse
```

## Try this

```
morse -r -s -T -d -w 5 -F 15 -p 5 -E -10
```
Starts the README's alphabet-learning drill: random letters at 5 wpm with 15 wpm spacing, where you type back each character you hear.

```
QSO | morse -e -T -d -w 5 -F 15
```
Generates a simulated radio contact and plays it as Morse while you type along.

```
morse -r -T -d -w 13 -F 24
```
The README's speed-building step: random letters at 13 wpm with 24 wpm Farnsworth spacing.

## What's unique

The QSO generator pipes straight into the trainer, so a fake radio contact becomes audio you copy by ear. Random mode adapts to the letters you miss.

## Caveats

The docs do not say which audio backend it needs; Homebrew lists pulseaudio as a dependency, so sound output on your machine may take some sorting out.

## Links

- [Homepage](http://www.catb.org/~esr/morse/)
- [Manual page](http://www.catb.org/~esr/morse/morse.html)
- [Source repository (GitLab)](https://gitlab.com/esr/morse-classic)
