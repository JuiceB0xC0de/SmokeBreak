---
name: liblcf
title: liblcf
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, easyrpg, file-formats, library, reverse-engineering, rpg-maker, xml]
homepage: https://easyrpg.org/
scout_score: 5
status: draft
---

# liblcf

**TLDR;** A library and two small tools that turn RPG Maker 2000/2003 binary game data into XML and back, and pull out every string.

liblcf reads and writes the data files used by RPG Maker 2000 and 2003, the LCF formats (LMU, LMT, LDB, LSD and similar). It can also convert them to and from XML. Those files are binary and tied to an editor from the early 2000s, so the contents are normally locked inside it.

Two command-line tools come with it. lcf2xml converts between the RPG Maker formats and XML, so a map or database can be opened in a text editor. lcfstrings lists the text and filename strings stored in the files, which is a quick way to see a game's dialogue without playing it.

It exists as part of the EasyRPG Project, a community effort to build a free, open source tool compatible with RPG Maker 2000/2003 games. The EasyRPG Player needs a way to load those games, and this library is that part. The README does not go into the internals and points to the EasyRPG wiki for technical documentation. It uses Expat for XML and ICU for character encoding detection and conversion.

The larger idea is that a closed binary format from a dead editor can be understood, documented and made readable by a community. Converting to XML is a handy way to learn what a format holds.

## Install

```
brew install liblcf
# depends on icu4c@78 and inih; installs the lcf2xml and lcfstrings tools
```

## Try this

```
lcf2xml --help
```
Shows how to convert RPG Maker 2000/2003 data files to XML and back.

```
lcfstrings --help
```
Shows how to list the text and filename strings from LMU, LMT, LDB and LSD files.

## What's unique

It turns opaque binary data from an old game-making tool into readable XML, so you can inspect and edit it without the original editor. It is also the format layer of a community reimplementation.

## Caveats

It is a library first, with only two small tools, and you need RPG Maker 2000/2003 data files of your own to use them; without ICU only Windows-1252 text is supported, and the README gives no warning about round-trip data loss, so check converted output.

## Links

- [EasyRPG project homepage](https://easyrpg.org/)
- [liblcf source repository](https://github.com/EasyRPG/liblcf)
- [EasyRPG wiki (documentation)](https://wiki.easyrpg.org)
- [Released versions download archive](https://easyrpg.org/downloads/)
