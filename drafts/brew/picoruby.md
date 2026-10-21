---
name: picoruby
title: PicoRuby
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, embedded, language, microcontroller, mruby, needs-hardware, ruby]
homepage: https://picoruby.org
scout_score: 6
status: draft
---

# PicoRuby

**TLDR;** A small Ruby implementation built for microcontrollers like the Raspberry Pi Pico, which also runs on your desktop as an interpreter, bytecode compiler and shell.

PicoRuby is an alternative implementation of mruby, itself a compact take on Ruby, aimed at boards such as the Raspberry Pi Pico and Pico 2 W. The README gives RAM targets of 512 KB or less for PicoRuby with networking, and 128 KB or less for FemtoRuby, a variant that uses the smaller mruby/c VM. Those figures depend on build configuration.

The brew formula installs three executables. `mrbc` compiles a Ruby file into `.mrb` bytecode for an mruby-compatible VM. `picoruby` runs Ruby source directly, the way the `ruby` command does. `r2p2` is a POSIX build of the R2P2 shell, so you can try the environment without a board.

The idea underneath is how little a high-level language needs from its host. The README says it depends only on a standard C library (glibc, Newlib or Newlib-nano, or emcc). It bundles its own compiler (mruby-compiler2), an allocator (Estalloc) and a filesystem (Littlefs). That portability is why the same codebase can run as firmware, a desktop tool, or WebAssembly. The homepage navigation also lists a WASM build and a browser framework called Funicular, though I could not read the prose behind them.

The README says the mruby VM version is the one mainly being developed. Following the bytecode path from `mrbc` to the VM is a good way to see how an embedded Ruby fits together.

## Install

```
brew install picoruby
# Real microcontroller use needs a board such as a Raspberry Pi Pico and a cross-compile build from the repo (see build_config/r2p2-picoruby-pico2.rb). The desktop binaries run without hardware.
```

## Try this

```
picoruby -e 'puts "Hello World!"'
```
Runs a one-line Ruby script on the tiny interpreter, as a smoke test.

```
mrbc path/to/source.rb
```
Compiles a Ruby file into path/to/source.mrb, the bytecode the VM executes.

```
r2p2 --help
```
Shows the options of the POSIX build of the R2P2 shell.

## What's unique

One Ruby codebase serves as a desktop interpreter, a shell, microcontroller firmware and a WebAssembly build. It is built to fit in a few hundred kilobytes of RAM.

## Caveats

The brief found no release or last-commit date, and building for boards from source needs CRuby 3.4+, a C toolchain, and on macOS an openssl workaround.

## Links

- [Project homepage and API docs](https://picoruby.org)
- [GitHub repository](https://github.com/picoruby/picoruby)
- [Project wiki](https://github.com/picoruby/picoruby/wiki)
