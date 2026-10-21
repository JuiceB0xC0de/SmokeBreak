---
name: open-babel
title: Open Babel
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, chemistry, cli, file-formats, library, science]
homepage: https://github.com/openbabel/openbabel
scout_score: 6
status: draft
---

# Open Babel

**TLDR;** A chemical toolbox that converts, searches and analyzes molecular data across dozens of file formats, as command-line programs and a programmer's library.

Open Babel reads, writes and converts chemical file formats. The README says over 90 and the website says over 110, so the exact count depends on which page you trust. It can also filter and search molecular files with SMARTS patterns and other methods, and generate 2D and 3D coordinates from inputs such as SMILES and InChI.

It exists because chemical data is scattered across many formats, each from a different tool, field or era. The project describes itself as "designed to speak the many languages of chemical data", and as an open, collaborative effort so that anyone can search, convert, analyze or store data from molecular modeling, chemistry, solid-state materials, biochemistry and related fields.

The idea underneath is that a molecule is a graph of atoms and bonds, and every format is a different way of writing that graph down. Some formats are a line of text, like SMILES. Others are full 3D coordinate tables. Converting between them means deciding what to keep, what to compute and what to guess. That is a way into cheminformatics.

Brew installs a set of executables, including obabel, obgen, obminimize, obenergy and obprop. The names come from the package metadata, and the pages that were read do not describe them, so use `--help` on each to see what it does.

## Install

```
brew install open-babel
```

## Try this

```
obabel --help
```
Prints the main converter's usage, including its input and output format options.

```
obgen --help
```
Shows the help for the 3D coordinate generator.

```
obminimize --help
```
Shows the help for the geometry minimizer.

## What's unique

One toolbox spans a very wide range of chemical formats and fields, and it ships both as ready-made command-line programs and as a full library. The website says it has been downloaded over 700,000 times and is used by over 40 related projects.

## Caveats

Licensed under GPL-2.0, so anything built on it inherits those terms, and the format count differs between the README and the website.

## Links

- [GitHub repository](https://github.com/openbabel/openbabel)
- [Open Babel website](http://openbabel.org/)
