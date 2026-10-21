---
name: libesedb
title: libesedb
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, file-formats, forensics, library, reverse-engineering, windows]
homepage: https://github.com/libyal/libesedb
scout_score: 6
status: draft
---

# libesedb

**TLDR;** A C library and two tools for opening ESE database files, the proprietary Microsoft format behind Active Directory, Exchange and Windows Search.

libesedb reads Extensible Storage Engine files, also called EDB files. ESE is a Microsoft database format that most people never see directly. According to the README, it is used in Windows Search, Windows Mail, Exchange and Active Directory. The library takes an ESE file as input and gives programs access to what is stored inside.

The Homebrew package also installs two command-line tools, `esedbinfo` and `esedbexport`. The names suggest inspecting a file and exporting its contents, but the README as fetched does not describe their output, so run them with `--help` to see what they actually do.

The interesting idea is what a closed format looks like once someone writes a reader for it. The project sits in the libyal family and has a companion knowledge base, the ESE Database File Knowledge Base, which documents the format. The project points to a forensic and investigative audience: people who need to look inside a database file without the software that created it.

## Install

```
brew install libesedb
```

## Try this

```
esedbinfo --help
```
Prints the usage text for the tool that inspects an ESE database file.

```
esedbexport --help
```
Prints the usage text for the export tool, showing which options it accepts.

## What's unique

It is one of the few open-source readers for a proprietary Windows database format, and it comes with a separate knowledge base documenting the format itself.

## Caveats

The README marks the project 'Status: experimental', databases over about 10G are listed as work in progress, and you need an ESE file of your own to try it on.

## Links

- [libesedb on GitHub](https://github.com/libyal/libesedb)
- [Project wiki (documentation)](https://github.com/libyal/libesedb/wiki/Home)
- [How to build from source](https://github.com/libyal/libesedb/wiki/Building)
- [Extensible Storage Engine (ESE) Database File Knowledge Base](https://github.com/libyal/esedb-kb)
