---
name: idsgrep
title: idsgrep
source: brew
category: languages-and-oddities
commitment: quick
tags: [cjk, kanji, language, quick, search, unicode]
homepage: https://tsukurimashou.org/idsgrep.php.en
scout_score: 6
status: draft
---

# idsgrep

**TLDR;** Grep for Han characters by shape: ask for every character with 月 on the right and get 明, 朝 and 期 back.

IDSgrep searches databases of CJK character structure. Each character is stored as a tree in an extended form of Unicode Ideographic Description Sequences (IDS), which say how a character is built from smaller components and where each one sits in the layout. A query is matched against those trees instead of against strings of text.

The query language is inspired by traditional Unix regular expressions, so a search can say where a component sits in a character's layout. The homepage's own example: "a user might ask for all characters with 月 on the right, and get a result including the characters 明, 朝, and 期." That is the reverse of a normal dictionary lookup, which starts from a reading or a meaning. This starts from what the character looks like, which helps when you can see a character but cannot pronounce it or look it up.

It comes from the Tsukurimashou Project, which works on Japanese-style typefaces. The package includes, or can generate, dictionary data from Tsukurimashou, KanjiVG, CHISE and EDICT2. The homepage calls it "a general tree-matching utility whose main application is to querying databases of Han-script character structures", so the matching idea is not limited to kanji. The underlying idea is that writing systems have an internal grammar of parts and arrangements, and you can query it.

## Install

```
brew install idsgrep
```

## Try this

```
idsgrep --help
```
Prints the command's options. The brief did not confirm the query syntax, so start here and read the user's manual linked from the homepage.

## What's unique

It applies a regex-style query language to trees of character components rather than to strings, so you can search by where a part sits inside a character.

## Caveats

The latest release, 0.6, is from 2021, and I could not confirm query syntax or data setup because the manual is a PDF I did not read.

## Links

- [IDSgrep homepage](https://tsukurimashou.org/idsgrep.php.en)
- [KanjiVG](https://kanjivg.tagaini.net/)
- [CHISE](http://www.chise.org/)
- [EDICT](http://www.edrdg.org/jmdict/edict.html)
