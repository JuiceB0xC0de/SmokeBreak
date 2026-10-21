---
name: unixcw
title: unixcw
source: brew
category: sound-and-live-coding
commitment: quick
tags: [ancient, audio, morse, quick, tui]
homepage: https://unixcw.sourceforge.net/
scout_score: 7
status: draft
---

# unixcw

**TLDR;** A Morse code tutor for the terminal: a small library and a few programs for learning to send and receive Morse.

unixcw is a project that provides a library, libcw, and a set of programs built on it: cw, cwgen, cwcp and xcwcp. The programs are, in the project's words, "intended for people who want to learn receiving and sending Morse code." Brew installs three of them: cw, cwgen and cwcp. The fourth, xcwcp, is an X11 front-end.

The project was started by Simon Baldwin. Kamil Ignacak took over maintenance in 2011. The homepage lists version 3.6.1, published November 2023, so it is old but still being looked after.

The idea underneath is that Morse is a small, learnable code you can pick up by drilling at a prompt, and that a library plus several front-ends is a reasonable way to build a trainer. The homepage does not describe exactly how each program takes input or produces output, so run each with --help to see what it does. Brew pulls in pulseaudio as a dependency, which suggests sound plays a part, though the homepage does not say so.

## Install

```
brew install unixcw
# The homepage says it is developed and tested on GNU/Linux; other platforms are unverified. Brew pulls in pulseaudio and gettext.
```

## Try this

```
cw --help
```
Lists the options for the main command-line Morse program.

```
cwgen --help
```
Shows the options for the generator tool, which is part of the practice toolset.

```
cwcp --help
```
Shows the options for the terminal-based Morse program.

## What's unique

It is a long-running GPL Morse trainer that ships a reusable library (libcw) alongside several front-ends, including an X11 one.

## Caveats

The homepage says it is developed and tested on GNU/Linux only, and I could not confirm install steps, options or audio behaviour elsewhere.

## Links

- [Project homepage](https://unixcw.sourceforge.net/)
