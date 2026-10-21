---
name: augeas
title: Augeas
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, config, dsl, library, linux, parsing]
homepage: https://augeas.net/
scout_score: 5
status: draft
---

# Augeas

**TLDR;** Augeas parses config files into a tree and writes them back, so scripts edit structured data instead of patching text with sed.

Augeas reads configuration files in their native formats and turns them into a tree. You change the tree, then save it, and Augeas writes the native config text back out. It ships as a C library, a shell tool for scripts (`augtool`), and bindings for scripting languages. The Homebrew formula also installs `augmatch`, `augparse`, `augprint` and `fadot`.

The homepage states the motivation plainly: manipulate config files "safer than the ad-hoc techniques generally used with grep, sed, awk and similar mechanisms in scripting languages". It also aims to provide a local configuration API for Linux.

The idea underneath is the lens. A lens is a small program in Augeas's own domain-specific language that describes one file format and maps it to and from a canonical tree. Because the same description drives both parsing and writing, the tool can save a file back out as native text. Supporting a new file means writing a new lens, which the project says it wants to make easy.

That makes it a door into bidirectional parsing: treating every config file, whatever its quirks, as the same kind of structured data.

## Install

```
brew install augeas
# Lenses are installed to $HOMEBREW_PREFIX/share/augeas/lenses/dist
```

## Try this

```
augtool --help
```
Lists the options of the interactive shell for browsing and editing the config tree.

```
augparse --help
```
Shows how to run and test lenses, the format descriptions at the core of Augeas.

```
augmatch --help
```
Shows how to query a config file's parsed tree from the command line.

## What's unique

Most config tools patch text with regular expressions. Augeas parses each file with a per-format lens and writes it back, and the lens language is what makes new formats pluggable.

## Caveats

The homepage shows no release date or version, and it frames the Linux focus as a goal, so how well it works on macOS is unclear.

## Links

- [Augeas homepage](https://augeas.net/)
