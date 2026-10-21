---
name: libwbxml
title: libwbxml
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, binary-format, library, mobile, protocol, wap, wbxml, xml]
homepage: https://github.com/libwbxml/libwbxml
scout_score: 5
status: draft
---

# libwbxml

**TLDR;** A C library and two converters for WBXML, the compact binary XML that WAP-era phones used for settings, sync and messages.

WBXML is a binary encoding of XML, defined by the WAP Forum. In the project's words, it is "used to reduce bandwidth in mobile communications." Instead of spelling out tags as text, it swaps them for single-byte tokens, which mattered a great deal on slow early mobile links.

libwbxml reads and writes that format. It ships two tools: wbxml2xml turns a WBXML file into readable XML, and xml2wbxml goes the other way. The library behind them covers many WAP-era document languages, including WML, SyncML and OTA settings.

The design is tidy. Input goes through either a WBXML parser or the Expat XML parser, and both build the same in-memory tree. An encoder then writes that tree out as WBXML or as XML. The README describes the parser as SAX-like, in the spirit of Expat but for WBXML.

The idea underneath is that a token table agreed in advance can stand in for text. Decoding a WBXML blob means knowing which document language it uses, and the tools let you force one with a flag when it is not obvious. It is a small window into how phones once synced contacts and received settings over very thin pipes.

## Install

```
brew install libwbxml
# XML-to-WBXML conversion depends on Expat being available
```

## Try this

```
wbxml2xml -o output.xml input.wbxml
```
Decodes a WBXML file into readable XML written to output.xml. The README example also shows a bare -i, but its usage is ambiguous there.

```
xml2wbxml -o output.wbxml input.xml
```
Encodes an XML file as WBXML.

```
xml2wbxml -k -n -v 1.1 -o output.wbxml input.xml
```
Encodes to WBXML version 1.1, keeping whitespace and skipping the string table.

## What's unique

It is a full round-trip toolkit for a niche protocol family, with a library API and command-line tools sharing one tree structure. Few tools can read or write this format at all.

## Caveats

The README gives no version or date and lists several document languages as only tested or partially tested; the -l option table also looks to have SI10 and SL10 swapped, so check before relying on it.

## Links

- [Homepage (GitHub repository)](https://github.com/libwbxml/libwbxml)
- [Releases](https://github.com/libwbxml/libwbxml/releases)
