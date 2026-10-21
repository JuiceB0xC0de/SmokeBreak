---
name: msitools
title: msitools
source: brew
category: take-things-apart
commitment: quick
tags: [file-formats, installers, quick, reverse-engineering, windows]
homepage: https://wiki.gnome.org/msitools
scout_score: 5
status: draft
---

# msitools

**TLDR;** Open, dump, diff and extract Windows .MSI installers from a Mac or Linux terminal, or build new ones from XML without Windows.

msitools is a set of command-line programs for inspecting and building Windows Installer (.MSI) packages. The inspection side takes an existing MSI and shows its tables and streams (`msiinfo`, `msidump`), pulls out the embedded files (`msiextract`), or compares two packages (`msidiff`).

The build side goes the other way. `msibuild` is a low-level builder that works from MSI tables. `wixl` reads an XML description and writes an MSI, and tries to use the same syntax as Microsoft's WiX toolset. `wixl-heat` generates XML fragments from a list of files and directories. The README says the point is packaging and deploying cross-compiled Windows applications.

Underneath is libmsi, a portable library for reading and writing MSI files, itself a port of a subset of Wine's Windows Installer implementation. The README explains that an MSI is an OLE Structured Storage file, a container format msitools reads through libgsf. That makes an installer a small database of tables with files packed alongside, rather than an opaque executable. Most people never see inside one.

## Install

```
brew install msitools
```

## Try this

```
msiinfo --help
```
Lists what the inspection tool can show about an MSI file, such as its tables and streams.

```
msiextract --help
```
Shows how to unpack the files embedded in an MSI without running the installer.

```
wixl --help
```
Shows the options for building an MSI from a WiX-style XML file.

## What's unique

wixl accepts WiX-style XML, so Windows installers can be built on macOS or Linux without the Windows toolchain. The inspection tools open up a file format most people only ever double-click.

## Caveats

The README calls the project very early stage though usable, says wixl lacks many WiX features, and the homepage is a retired GNOME wiki, so current maintenance is unclear.

## Links

- [Homepage (GNOME wiki, retired)](https://wiki.gnome.org/msitools)
- [Source repository (GitLab)](https://gitlab.gnome.org/GNOME/msitools)
- [Release tarballs](https://download.gnome.org/sources/msitools/)
- [Issue tracker](https://gitlab.gnome.org/GNOME/msitools/issues)
