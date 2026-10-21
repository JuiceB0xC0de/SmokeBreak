---
name: mlkit
title: MLKit
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, language, memory-management, regions, standard-ml]
homepage: https://melsman.github.io/mlkit
scout_score: 6
status: draft
---

# MLKit

**TLDR;** A Standard ML compiler that decides memory allocation and freeing at compile time using region inference, so programs can skip or limit garbage collection.

MLKit compiles Standard ML to native executables (x64 on Linux, arm64 on Apple Silicon macOS). It covers all of the 1997 Definition of Standard ML and most of the Basis Library. Run `mlkit` with no arguments and you get an interactive REPL. Alongside the compiler it ships a region profiler, so you can see where memory went.

The idea underneath is region inference. In the project's words: "Memory allocation directives (both allocation and deallocation) are inferred by the compiler, which uses a number of program analyses concerning lifetimes and storage layout." Values are placed into regions that are freed all at once, with no programmer annotations. Region inference can be combined with reference-tracing garbage collection, or the collector can be turned off to avoid unbounded pauses in real-time work.

The repo also holds ReML, a variant of SML where you write regions and effects explicitly, which gives direct control over allocation. A sibling backend, SMLtoJs, compiles SML to JavaScript for browsers. Modules are removed at compile time by a scheme called Static Interpretation. The compiler bootstraps itself, at about 80,000 lines of SML.

This is a door into a different answer to the question of how a language manages memory, one that sits between manual freeing and a runtime collector.

## Install

```
brew install mlkit  # the README says MLKit is not currently available through Homebrew, so this may not work. The documented route: download mlkit-bin-dist-darwin.tgz (Apple Silicon macOS) or mlkit-bin-dist-linux.tgz (x64 Linux) from the latest GitHub release, unpack it, then run `make install` in the unpacked directory (optionally `PREFIX=... make install`). Intel macOS is not supported. Building from source needs an existing SML compiler (MLton, or MLKit 4.3.0 or newer) and gcc.
```

## Try this

```
mlkit
```
Starts the interactive REPL so you can type Standard ML directly.

```
mlkit helloworld.sml
```
Run inside a copy of the kitdemo directory (under /usr/share/mlkit), this compiles the example to a native executable called run.

```
./run
```
Runs the compiled program, which prints 'hello world'.

## What's unique

It infers region-based memory management for a full ML implementation, which the project says makes it unique among ML implementations. ReML lets you write regions and effects by hand.

## Caveats

Not on Homebrew despite the catalogue listing; install is a release tarball, Intel macOS is unsupported, and the published arm64 v4.7.23 binaries need macOS 26 or newer.

## Links

- [MLKit homepage](https://melsman.github.io/mlkit)
- [GitHub repository and README](https://github.com/melsman/mlkit)
- [Programming with Regions in the MLKit (PDF guide)](https://github.com/melsman/mlkit/raw/master/doc/mlkit.pdf)
