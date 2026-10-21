---
name: vttest
title: vttest
source: brew
category: take-things-apart
commitment: quick
tags: [ancient, escape-sequences, quick, terminal, tui, vt100]
homepage: https://invisible-island.net/vttest/
scout_score: 6
status: draft
---

# vttest

**TLDR;** A decades-old interactive test suite that puts your terminal emulator through DEC VT100-and-later escape sequences, showing how 'compatible' it really is.

vttest runs inside a terminal and shows a menu of test screens. Most of them draw something, such as cursor movement, screen modes or character sets, and you look at the result and judge whether your terminal got it right. Some tests send query sequences and check the replies automatically, but most need a person who knows what the screen should look like.

The author describes it as a way to test, and demonstrate the non-compatibility of, so-called "VT100-compatible" terminals. He began this version in 1996 to test colour changes he was making to xterm. The program goes well beyond the VT100: it covers the VT220 through VT520 and xterm extensions. Extra menus appear only when the terminal identifies itself as a VT220 or higher, and rectangle tests only at VT420 or higher.

The idea underneath is that a terminal is not a window that prints text. It is a state machine driven by escape sequences, and every terminal emulator you use is someone's reading of DEC's hardware from the late 1970s. vttest makes the gaps in those readings visible. Its history is documented in detail: rxvt, KDE's Konsole and the Linux and FreeBSD console drivers have carried or used copies of it, and modern terminals such as Terminal.app and Zutty have been checked against it.

The homepage notes that vttest can re-read its own log file as a command script, which the author used to measure coverage. Menus are built from tables rather than case statements, which makes adding entries simple.

## Install

```
brew install vttest
```

## Try this

```
vttest
```
Opens the main menu of test screens; pick a number to run a test and judge by eye whether your terminal drew it correctly.

```
vttest --help
```
Lists the program's command-line options.

## What's unique

It is a roughly forty-year-old conformance suite, still maintained, that has been used to validate real terminals and whose author documents its history in detail.

## Caveats

Most results need a human who knows what the screen should look like, and the only documentation is the source code and DEC's VT100 manual.

## Links

- [vttest homepage](https://invisible-island.net/vttest/)
