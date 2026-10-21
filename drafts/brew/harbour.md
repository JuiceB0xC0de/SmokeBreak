---
name: harbour
title: Harbour
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, clipper, compiler, dbase, language, xbase]
homepage: https://harbour.github.io
scout_score: 6
status: draft
---

# Harbour

**TLDR;** A free, Clipper-compatible xBase compiler that turns .prg source into native apps, keeping the dBASE-era language alive on modern systems.

Harbour is a free-software implementation of the xBase language family, the line of database-centred languages that grew out of dBASE and Clipper. You write `.prg` source files and the compiler turns them into C-level output, which a C compiler then builds into a native program. The project describes itself as "multi-platform, multi-threading, object-oriented, scriptable", and says it is "100% compatible with Clipper compilers".

It exists so that old xBase applications can keep running. Clipper was a commercial DOS-era compiler, and a great deal of business software was written in it. Harbour lets that code move to current platforms from one code base. The listed targets run from MS-DOS and OS/2 to Linux, macOS, iOS and Android.

The install brings a whole toolchain. `harbour` is the compiler, `hbmk2` is the build tool driven by `.hbp` and `.hbc` project files, `hbrun` runs scripts, and `hbformat` tidies source. The runtime has native database drivers (RDDs), SQL and ODBC support, JSON, SSL, TCP/IP and XML, with console, text-UI, GUI, daemon and web targets.

The door it opens is a language design from before SQL servers were the default. Database tables, records and screen handling sit close to the core of the language, and a whole generation of software was built that way. Harbour is a working way to read and run it.

## Install

```
brew install harbour
# The Homebrew formula is marked deprecated. The upstream README builds from source and needs an ANSI C compiler and GNU Make.
```

## Try this

```
hbmk2 --help
```
Shows the options of the Harbour build tool, which compiles and links .prg projects.

```
hbmk2 hello.prg
./hello
```
Compiles the hello example from the source tree's tests directory and runs it. The README expects it to print 'Hello, world!'.

```
hbrun --help
```
Shows how to run Harbour scripts directly without a separate compile step.

## What's unique

It carries a complete xBase toolchain forward, with its own compiler, build system, formatter and scripting runner, and keeps Clipper compatibility as its explicit goal. It is both a time capsule and a working modern environment.

## Caveats

The Homebrew formula is flagged deprecated, and the homepage still lists 3.0.0 as the latest stable release while the GitHub README says 3.2.0.

## Links

- [Harbour homepage](https://harbour.github.io)
- [GitHub repository and README](https://github.com/harbour/core)
- [GitHub releases](https://github.com/harbour/core/releases)
