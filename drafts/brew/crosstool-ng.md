---
name: crosstool-ng
title: crosstool-NG
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, compiler, cross-compilation, embedded, toolchain, tui]
homepage: https://crosstool-ng.github.io/
scout_score: 6
status: draft
---

# crosstool-NG

**TLDR;** A menuconfig-driven generator that builds a complete cross-compiler toolchain (compiler, linker, C library) for a machine other than the one you're on.

Crosstool-NG builds cross toolchains: the compiler, assembler, linker and C library needed to produce code for a different target than the host it runs on. The homepage calls it "a versatile (cross) toolchain generator" that "supports many architectures and components and has a simple yet powerful menuconfig-style interface." You pick a target and the parts you want in a text menu, then it builds the whole stack.

The reason it exists is stated plainly in the README: toolchains are an essential component of a software development project, and the project aims at building them. Anyone targeting a router, a microcontroller board or an odd embedded Linux device needs one, and assembling the pieces by hand means matching versions of binutils, a compiler and a libc that all have to agree.

The idea underneath is that a toolchain is not a single program but a bootstrapped chain of them. Watching one get built shows how the pieces depend on each other. The docs index has sections on configuring, building, toolchain types and how a toolchain is constructed, though the brief did not cover their contents.

ct-ng is, in the README's words, a make script underneath. That explains its quirks and also makes it approachable if you want to read how it works.

## Install

```
brew install crosstool-ng
# The docs say not all host dependencies are detected by configure, so a missing package can make a later ct-ng build fail. Check the per-distro setup notes linked from the install docs.
```

## Try this

```
ct-ng help
```
Prints crosstool-NG's own help, best run inside a fresh work directory, per the install docs.

```
ct-ng --help
```
Prints make's help instead, because ct-ng is a make script. The README says there is no clean workaround.

## What's unique

It turns the assembly of an entire cross toolchain into a menuconfig-style choice list. It is also openly a make script, a quirk the README documents itself.

## Caveats

Configure does not detect every host dependency, so a build can fail later, and the install docs are Linux-oriented; other platforms were not checked.

## Links

- [Homepage](https://crosstool-ng.github.io/)
- [Documentation](http://crosstool-ng.github.io/docs/)
- [GitHub repository](https://github.com/crosstool-ng/crosstool-ng)
