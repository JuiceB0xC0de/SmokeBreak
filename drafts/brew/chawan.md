---
name: chawan
title: Chawan
source: brew
category: languages-and-oddities
commitment: quick
tags: [browser, gemini, gopher, nim, quick, terminal, tui]
homepage: https://sr.ht/~bptato/chawan/
scout_score: 7
status: draft
---

# Chawan

**TLDR;** A terminal web browser with its own from-scratch engine that renders CSS, inline images and optional JavaScript, and also reads Gopher, Gemini and man pages.

Chawan is a text-mode browser that takes a URL or a local file and draws the page in your terminal. It lays out HTML with CSS, including flow, table and flexbox layouts, and it handles double-width CJK characters. Images can be shown inline through the Sixel or Kitty protocols if your terminal supports them. JavaScript is available but off by default.

The interesting part is the engine. The README says Chawan uses "its own small browser engine developed from scratch", written in Nim, which "can nevertheless display many websites in a manner similar to major graphical browsers." It names w3m as its main inspiration but shares no code with it. Building a layout engine is normally a huge job, so this is a small, readable place to see how one works.

It runs as several processes, loads documents incrementally, and applies syscall sandboxing on Linux, FreeBSD and OpenBSD (seccomp-bpf, capsicum and pledge). Beyond HTTP(S) it speaks (S)FTP, Gopher, Gemini, Finger and Spartan, so it doubles as a way to visit the small-web corners of the internet. It can also act as a pager, and the second executable, mancha, is a man page viewer.

## Install

```
brew install chawan
# JavaScript is off by default, and inline images need enabling; see doc/image.md in the repo
# Inline images need a terminal that supports Sixel or the Kitty protocol
```

## Try this

```
cha example.org
```
Opens the site directly in the terminal, rendered with CSS.

```
cha -V
```
Opens in visual mode, which shows a list of the default keybindings.

```
mancha cha
```
Reads the cha(1) man page in mancha, the bundled man page viewer.

## What's unique

It is a browser engine written from scratch in Nim, not a wrapper around an existing one, and it covers Gopher, Gemini and other small protocols alongside the web.

## Caveats

No native Windows support (WSL needed), and JavaScript and inline images are both disabled until you turn them on.

## Links

- [Chawan homepage (SourceHut)](https://sr.ht/~bptato/chawan/)
- [Homebrew formula](https://formulae.brew.sh/formula/chawan)
- [Nim compiler install](https://nim-lang.org/install.html)
