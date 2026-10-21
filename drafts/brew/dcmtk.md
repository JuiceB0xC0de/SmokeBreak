---
name: dcmtk
title: DCMTK
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cli, dicom, file-formats, medical-imaging, protocol]
homepage: https://dcmtk.org/en/dcmtk/
scout_score: 5
status: draft
---

# DCMTK

**TLDR;** About 80 command-line tools for reading, converting and sending DICOM, the file and network format behind medical imaging, from one long-running open toolkit.

DCMTK is the OFFIS DICOM toolkit. The project's own words: "source code, documentation and installation instructions for a set of software libraries and applications implementing part of the DICOM/MEDICOM Standard." The Homebrew formula installs the command-line tools built on those libraries, roughly 80 of them.

The tool names suggest the range. There are dump and convert utilities (`dcmdump`, `dcm2img`, `dcm2json`, `dcm2xml`, `img2dcm`, `xml2dcm`), structured report converters (`dsr2html`, `dsr2xml`), and networking tools named after DICOM operations (`echoscu`, `storescu`, `storescp`, `findscu`, `movescu`). There is also a modality worklist server (`wlmscpfs`). What each one takes in and emits is inferred from the names here, so check the docs before relying on it.

The idea underneath is that medical imaging has its own world: a binary file format and a network protocol, both defined by one large standard, that most developers never touch. The README describes layered libraries, with a base of config and utility code, then `dcmdata` for encoding and decoding, `dcmimgle` for images, and `dcmnet` for networking. The command-line tools are thin programs over those layers. Reading the tools is a way into the standard.

The README gives no motivation and no usage examples. It points to a wiki, API docs and a forum for the rest.

## Install

```
brew install dcmtk
```

## Try this

```
dcmdump --help
```
Prints the options for the DICOM file dumper, a first look at how the toolkit describes its own file format.

```
echoscu --help
```
Shows the options for the DICOM network ping client, the simplest way into the protocol side.

```
img2dcm --help
```
Lists how an ordinary image can be wrapped into a DICOM file.

## What's unique

It is one of the few open implementations of both the DICOM file standard and its networking, with clients, servers and converters in one package.

## Caveats

The README has no usage examples and the homepage could not be read when this entry was researched, so expect to learn from the wiki and API docs.

## Links

- [Homepage](https://dcmtk.org/en/dcmtk/)
- [API documentation](https://support.dcmtk.org/docs/)
- [Wiki (HOWTOs and further information)](https://support.dcmtk.org/wiki/)
- [Public discussion forum and FAQ](https://forum.dcmtk.org/)
