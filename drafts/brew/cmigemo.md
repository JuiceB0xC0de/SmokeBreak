---
name: cmigemo
title: cmigemo
source: brew
category: languages-and-oddities
commitment: quick
tags: [emacs, japanese, library, quick, regex, search, vim]
homepage: https://www.kaoriya.net/software/cmigemo
scout_score: 6
status: draft
---

# cmigemo

**TLDR;** Turns a romaji query like 'ai' into a regex matching 愛, 相, 藍 and 合, so ordinary search tools can find Japanese text typed in Latin letters.

C/Migemo is a C library and command-line tool that takes a romaji query and a dictionary and prints a regular expression. In the README's own notation, `ai → [愛相藍合]`. Type 'koi' and the pattern covers 鯉, 濃 and 恋. The search tool never needs to know anything about Japanese input; it just receives a bigger regex.

The original Migemo, by Satoru Takabayashi, was written in Ruby and Emacs Lisp so Emacs users could do incremental search in Japanese text while typing romaji. The author of C/Migemo rewrote it from scratch in C so it could be used from Vim, and the README adds that C makes it easier to plug into the large body of existing C software.

The idea underneath is to move the hard part out of the matcher. Japanese has many words that share a reading, and typing them normally means converting romaji into kana and then choosing a kanji. Migemo skips the choosing and matches all the candidates at once, using a dictionary derived from SKK-JISYO.L. The README also describes a precompiled 'sdict' binary dictionary format that the author says cuts startup from about 50ms to about 4ms and memory from about 18MB to about 8MB. Those figures are the author's and were not measured here.

## Install

```
brew install cmigemo
# Emacs users: also get https://github.com/emacs-jp/migemo, save it as migemo.el and put it in your load-path (from the brew caveats)
```

## Try this

```
cmigemo --help
```
Lists the options the binary accepts, including dictionary selection.

```
./build/bin/cmigemo --save build/dict/utf-8/migemo-sdict -w ''
```
From a source build, converts the dictionary to the precompiled sdict format, saves it, and exits immediately because of the empty -w argument.

```
./build/bin/cmigemo --sdict build/dict/utf-8/migemo-sdict
```
Launches cmigemo using the saved sdict file instead of loading the dictionaries dynamically.

## What's unique

It is a from-scratch C rewrite of a Ruby and Emacs Lisp tool, so C programs and editors like Vim can use it directly. It also offers a precompiled dictionary format to cut startup time and memory.

## Caveats

The library is MIT but the generated dictionary is GPL because it comes from SKK-JISYO.L, and the brief could not confirm a recent release date or version.

## Links

- [Homepage (KaoriYa, Japanese)](https://www.kaoriya.net/software/cmigemo)
- [GitHub repository and README](https://github.com/koron/cmigemo)
- [Latest releases](https://github.com/koron/cmigemo/releases/latest/)
- [vim-migemo (Vim plugin)](https://github.com/haya14busa/vim-migemo)
