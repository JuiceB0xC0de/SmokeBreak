---
name: deark
title: deark
source: brew
category: take-things-apart
commitment: quick
tags: [file-formats, legacy, quick, retro, reverse-engineering]
homepage: https://entropymine.com/deark/
scout_score: 7
status: draft
---

# deark

**TLDR;** A command-line tool that decodes obscure legacy file formats, converting old images, icons, and archives into modern files or extracting what is inside.

Deark takes a file in an old or obscure format and either converts it to something modern or pulls out the files embedded inside. The inputs range widely: ANSI art, DOS executable packers, Macintosh resource forks, Palm OS and EPOC/Symbian files, calculator pictures, fonts, icons, disk images, and old archives. It autodetects the format and hands the file to a format-specific module. If detection fails, `-m` picks a module by hand.

Output usually lands in files named `output.*`, or in a ZIP or TAR archive with `-zip` or `-tar`. For archive formats such as ar or zoo, the README suggests `-zip -ka` so filenames and paths survive. The `-d` option goes the other way and prints the technical structure of the file: headers, fields, and metadata. That makes it a way to learn how a format is laid out by watching a decoder read it.

The author's stated motivation is turning files in forgotten formats into something modern or readable. The project also holds a lot of knowledge about third-party formats (structures, algorithms, tables, palettes) that is otherwise scattered. Each module is a small, readable record of how some vanished piece of software stored its data. Run it on a file you cannot open and you get a short lesson in how that format worked.

## Install

```
brew install deark
```

## Try this

```
deark -h
```
Prints usage and the list of options.

```
deark -modules
```
Lists the format modules Deark knows, a quick survey of the legacy formats it covers.

```
deark -d <input-file>
```
Prints technical details about the file's internal structure and metadata, instead of just converting it.

## What's unique

One tool covers a very wide spread of dead formats, from DOS packers to Palm OS to calculator pictures. Its `-d` mode doubles as a format explainer.

## Caveats

Misspelled or unrecognized `-opt` options are silently ignored, malformed input often still exits with status 0, and the README says features may change without notice.

## Links

- [Deark homepage](https://entropymine.com/deark/)
- [GitHub project (README, technical.md)](https://github.com/jsummers/deark)
- [Deark-extras (ancillary files for development)](https://github.com/jsummers/deark-extras)
