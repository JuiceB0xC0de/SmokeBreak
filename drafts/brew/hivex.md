---
name: hivex
title: hivex
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, file-formats, forensics, library, reverse-engineering, windows-registry]
homepage: https://libguestfs.org
scout_score: 7
status: draft
---

# hivex

**TLDR;** Reads Windows Registry hive files on any machine, with a shell, an XML exporter and a C library, built to survive malformed input.

A Windows Registry hive is a binary file, kept under C:\WINDOWS\SYSTEM32\CONFIG, that holds a tree of keys, subkeys and typed values. Hivex opens one of these files from disk and lets you walk the tree. It is a C library with bindings for OCaml, Perl, Python and Ruby. Three command-line tools sit on top of it: hivexget prints the values under a subkey or one named value, hivexml exports the whole hive as XML, and hivexsh is an interactive shell for browsing.

It exists as part of libguestfs, where it lets you examine or merge changes into the Registry of Windows guests inside disk images. The README says it deliberately avoids the textual .REG format, because "parsing that is as much trouble as parsing the original binary format." Its stated goal is to be secure against buggy or malicious registry files.

The interesting part is the format itself. Microsoft never documented it, so the parser rests on reverse engineering, and the docs are frank about it: there may be "nuances in the reverse-engineered format that we do not understand." Each value carries a type such as REG_SZ, REG_DWORD or REG_BINARY, but the docs warn that the type is often unrelated to the real contents. Reading is the default. Writing needs an explicit open flag and an explicit commit, and new blocks are appended to the end of the file rather than reusing freed space.

## Install

```
brew install hivex
# You also need a hive file to open, for example one pulled from a Windows disk image. The homepage does not describe hivex-specific setup.
```

## Try this

```
hivexget --help
```
Shows the options for the hivexget tool.

```
hivexget hivefile '\\Path\\To\\SubKey'
```
Lists all the (key, value) pairs under that subkey in a format similar to regedit. The path is relative to the top of the hive.

```
hivexget hivefile '\\Path\\To\\SubKey' name
```
Prints one named value raw. Use @ for the default value.

## What's unique

It is a small, defensive parser for an undocumented binary format, and its write path appends new blocks instead of rewriting structures in place, so it never has to risk corrupting the hive.

## Caveats

You must supply your own hive file, write support is limited and the docs call it risky, so back up hives first, and the format is reverse-engineered so some details may be wrong.

## Links

- [libguestfs homepage](https://libguestfs.org)
- [hivex(3) library man page](https://libguestfs.org/hivex.3.html)
- [hivexget(1) man page](https://libguestfs.org/hivexget.1.html)
- [libguestfs source repository](https://github.com/libguestfs/libguestfs)
