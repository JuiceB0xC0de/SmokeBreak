---
name: imessage-exporter
title: imessage-exporter
source: brew
category: take-things-apart
commitment: quick
tags: [backup, ios, macos, quick, reverse-engineering, rust, sqlite]
homepage: https://github.com/ReagentX/imessage-exporter
scout_score: 5
status: draft
---

# imessage-exporter

**TLDR;** A read-only Rust tool that opens the local iMessage SQLite database, or an iPhone backup, and exports your conversations to plain text or HTML.

imessage-exporter reads the iMessage database on a Mac (chat.db) or inside an iOS device backup, and writes each conversation out as txt or html. It can copy attachments and convert them along the way: HEIC to JPEG, CAF or MOV to MP4. It also has a diagnostics mode that looks for problems in the database. The README says the binary only performs read-only operations.

The project exists so people can save, back up, archive and migrate their message history in open formats. The README puts it as "full ownership and control over your communication history", and its stated aim is "the most comprehensive and accurate representation of iMessage data available."

The interesting part is what sits underneath. A closed consumer app keeps your conversations in an ordinary SQLite file. Handles are phone numbers and emails, and the tool maps them to names through the Address Book or a backup's contacts database. Newer message features are stored in less obvious blobs. The README says the author reverse engineered the typedstream format and the payload_data plist format to decode them, crediting SQLiteFlow and Xplist. It covers tapbacks, edited messages, Digital Touch and handwritten messages.

It is also published as a library crate, so the same decoding work can be reused in other Rust programs.

## Install

```
brew install imessage-exporter
# The README recommends `cargo install --locked imessage-exporter` for normal use, since the Homebrew version may lag the latest release. Cargo needs a Rust toolchain.
# Needs a Mac's chat.db or an iOS backup to read. On non-macOS platforms, ImageMagick is needed for image conversion and ffmpeg for audio and video.
```

## Try this

```
imessage-exporter --help
```
Prints the full flag reference: formats, attachment copy methods, date filters, platform and path options.

```
imessage-exporter -f txt -o output -c clone
```
Exports every conversation as text into ./output, copying attachments in their original formats.

```
imessage-exporter -f txt -o ~/export-2020 -s 2020-01-01 -e 2021-01-01 -a macOS
```
Exports only messages from 2020 as text, using the start and end date filters.

## What's unique

It is a read-only exporter built on a reverse-engineered model of a closed Apple database, and it ships as both a CLI and a reusable Rust library. Its feature list is long and specific, down to tapbacks and handwritten messages.

## Caveats

On a Mac, the terminal needs Full Disk Access to read the database, PDF export does not work well (the README suggests printing to PDF from Safari), and a password passed with -x is visible in the process table and shell history.

## Links

- [GitHub repository (homepage)](https://github.com/ReagentX/imessage-exporter)
- [Binary documentation (flags and install)](https://github.com/ReagentX/imessage-exporter/blob/develop/imessage-exporter/README.md)
- [FAQ](https://github.com/ReagentX/imessage-exporter/blob/develop/docs/faq.md)
