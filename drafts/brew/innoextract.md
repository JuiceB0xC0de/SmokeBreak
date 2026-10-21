---
name: innoextract
title: innoextract
source: brew
category: take-things-apart
commitment: quick
tags: [file-formats, gog, installers, quick, reverse-engineering]
homepage: https://constexpr.org/innoextract/
scout_score: 7
status: draft
---

# innoextract

**TLDR;** Unpacks Windows Inno Setup installers on any OS without running them or needing Wine, so you can see what a setup.exe actually contains.

innoextract takes a setup .exe built with Inno Setup and writes the packaged files into the current directory. It reads the installer's data format directly instead of executing anything. That means it works on Linux, macOS, FreeBSD and Windows, with no Windows machine and no Wine.

Inno Setup installers are common for Windows apps and games, and normally the only way to reach the contents is to run the installer. innoextract skips that. The page says it supports Inno Setup versions 1.2.10 through 6.2.2, plus some modified variants such as GOG.com's game installers. For GOG it can reassemble GOG Galaxy split parts into the original files, and it can use unrar or unar for certain RAR-packed archives.

The idea underneath is that an installer is just a file format. Once someone has reverse-engineered the layout, you can open it like an archive and look at what it would have put on your disk, without trusting it to run. The format changes between Inno Setup versions, which is why each release lists the range it handles. The project's own caveat is that it "cannot guarantee good forward compatibility as the Inno Setup data format changes frequently."

It has also become plumbing for other projects. The page lists downstream users such as game-data-packager, play.it and the Arx Libertatis installers, which rely on it to pull game data out of GOG installers on Linux.

## Install

```
brew install innoextract
# For GOG multi-part RAR-packed installers, the --gog option needs unrar or unar installed.
```

## Try this

```
innoextract --help
```
Lists the available command-line options.

```
innoextract <file>
```
Extracts the given Inno Setup installer into the current directory, without running it.

```
man 1 innoextract
```
Opens the man page documentation.

## What's unique

It reads the installer's data directly and never runs the setup program, so it needs neither Windows nor Wine. It has also become the quiet foundation for GOG game extraction tools on Linux.

## Caveats

The homepage lists 1.9 (August 2020) as current, so it looks stable but slowly updated, it cannot extract individual components, and support for newer Inno Setup formats depends on future releases.

## Links

- [innoextract homepage](https://constexpr.org/innoextract/)
