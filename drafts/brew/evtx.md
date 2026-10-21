---
name: evtx
title: evtx
source: brew
category: take-things-apart
commitment: quick
tags: [file-formats, forensics, quick, reverse-engineering, rust, windows]
homepage: https://github.com/omerbenamram/evtx
scout_score: 6
status: draft
---

# evtx

**TLDR;** A Rust parser that turns Windows binary .evtx event logs into XML or JSON on any platform, plus a browser viewer that runs locally.

Windows writes its event logs in a binary format, .evtx, that most people on other systems never open. `evtx_dump` reads those files and prints each record as XML, JSON, or JSON Lines. It runs on Linux and macOS as well as Windows, so you can inspect a log file someone sent you without a Windows machine.

The README says XML and JSON are both built straight from one shared intermediate representation, so there is no XML-to-JSON conversion step. Parsing is multithreaded by default, which means records can come out of order unless you pass `-t 1`. It also has some basic recovery when records or chunks are missing.

The interesting door is the format itself. A log record is a compact binary encoding of XML, built on templates and substitutions. An optional feature can pull message templates out of provider DLL, EXE, and SYS files into an offline cache, and use them to render records whose templates are missing or corrupt. That is a close look at how Windows stores structured events.

The project also ships Python bindings and EVTX Web, a browser viewer that runs the same Rust core as WebAssembly. Per the README, "Everything happens locally – files never leave your machine."

## Install

```
brew install evtx
# You need an .evtx file to parse. The browser viewer needs no install: https://omerbenamram.github.io/evtx/
```

## Try this

```
evtx_dump <evtx_file>
```
Prints every record in the log as XML to stdout.

```
evtx_dump -o json <evtx_file>
```
Prints the same records as JSON.

```
cat <evtx_file> | evtx_dump -o jsonl -
```
Reads the log from stdin and emits JSON Lines, ready to pipe into other tools.

## What's unique

It parses a Windows-only binary format anywhere Rust runs, written in 100% safe Rust. A WebAssembly viewer lets you open logs in a browser without installing anything.

## Caveats

CDATA nodes and the EVTHandle node type are not implemented yet, output order is not guaranteed without `-t 1`, and the speed claims come from the author's own benchmarks.

## Links

- [GitHub repository (homepage)](https://github.com/omerbenamram/evtx)
- [EVTX Web viewer (in browser)](https://omerbenamram.github.io/evtx/)
- [Crate on crates.io](https://crates.io/crates/evtx)
- [WEVT template docs](https://github.com/omerbenamram/evtx/blob/master/docs/wevt_templates.md)
