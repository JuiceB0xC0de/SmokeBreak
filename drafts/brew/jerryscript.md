---
name: jerryscript
title: JerryScript
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c, embedded, iot, javascript, language, microcontrollers]
homepage: https://jerryscript.net
scout_score: 5
status: draft
---

# JerryScript

**TLDR;** A JavaScript engine written in C99 that is meant to run in under 64 KB of RAM on microcontrollers, with a `jerry` command for trying it on a desktop.

JerryScript is a JavaScript engine for devices where a normal engine will not fit. The homepage says it can run with under 64 KB of RAM and under 200 KB of ROM. It takes JavaScript source, or precompiled snapshots of it, and executes it. The homepage also says it can reach peripherals from JavaScript. Brew installs a single executable, `jerry`.

The project exists for the Internet of Things. The README describes it as "a lightweight JavaScript engine for resource-constrained devices such as microcontrollers" and says it is "heavily optimized for low memory consumption". It is a C library with a C API, meant to be embedded in other programs, and the README calls that API mature.

The idea underneath is snapshots. Parsing JavaScript is costly for a tiny chip, so the source can be compiled to byte code ahead of time on a bigger machine. The device then loads and runs the byte code only. This turns a dynamic language into something closer to a firmware blob.

The language coverage is a trade-off too. The README claims full ECMAScript 5.1 compliance and about 70% of ECMAScript 2025. That makes it a good way to see which parts of JavaScript you can drop and still have a working language.

## Install

```
brew install jerryscript
# Building from source instead needs Python and a C99 toolchain.
# Running it on a real microcontroller needs a target device.
```

## Try this

```
jerry --help
```
Lists the options the `jerry` command line runner accepts, including how it runs scripts and snapshots.

```
git clone https://github.com/jerryscript-project/jerryscript.git
```
Fetches the sources, the README's first Quick Start step, so you can read the docs and build it yourself.

```
python tools/build.py
```
Run inside the cloned repository, this builds the engine from source. The README points to docs/00.GETTING-STARTED.md for more options.

## What's unique

Most JavaScript engines are built for speed on big machines. This one is built to fit in kilobytes, and it can precompile scripts to byte code so the device never has to parse source.

## Caveats

The brief could not confirm recent release or commit activity, and ES2025 support is only partial at about 70%.

## Links

- [Homepage](https://jerryscript.net)
- [GitHub repository and README](https://github.com/jerryscript-project/jerryscript)
- [Getting Started docs](https://github.com/jerryscript-project/jerryscript/blob/master/docs/00.GETTING-STARTED.md)
- [Wiki](https://github.com/jerryscript-project/jerryscript/wiki)
