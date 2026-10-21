---
name: ctl
title: CTL
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, color, dsl, image, language, vfx]
homepage: https://github.com/aces-aswf/CTL
scout_score: 7
status: draft
---

# CTL

**TLDR;** A deliberately tiny language for color transforms: write pixel math as a program, run it on an image, and share it as plain text.

CTL, the Color Transformation Language, describes a digital color transform as a small program. An interpreter loads the program, runs it on every pixel of an input image, and writes the transformed image. The command-line tool `ctlrender` does this for image files, and parameters such as exposure can be set to adjust a transform.

The reason it exists is about sharing. The README argues that C, C++ or Python are poor vehicles for passing color transforms around: the recipient may have to compile code, portability is hard to guarantee, a bug can crash the host application, and malware is difficult to rule out. CTL is restricted to the operations color transforms need, which the author says improves portability, protects host applications and users, and allows efficient interpreters.

The idea underneath is that a language gets safer and more useful by being able to say less. CTL only handles single-pixel operations, so it cannot blur, sharpen or compute whole-image statistics. In exchange, two parties with the same program and the same parameters get identical results, and the transform can travel as program text. Color management in film and VFX leans on exactly that guarantee.

The README is explicit that CTL is not the same thing as ACES, the film color framework that uses it for its reference transforms: "CTL's utility extends far beyond its usage in the ACES framework." The language is documented in SMPTE RDD 15.

## Install

```
brew install ctl
# Installs the ctlrender, exr_ctl_exr and exrdpx tools. Dependencies (imath, libtiff, openexr) come along via brew. You will need an EXR image and a .ctl program of your own to do anything useful.
```

## Try this

```
ctlrender -help
```
Prints the help menu and confirms the tool is installed and working.

```
ctlrender -ctl transform.ctl input.exr output.exr
```
Runs your CTL program over every pixel of input.exr and writes the result to output.exr.

```
exrdpx --help
```
Shows the options for the bundled tool that converts between EXR and DPX image files.

## What's unique

It is a scripting language locked down by design: only single-pixel color math, so a transform can be shared as plain text with predictable results and no arbitrary code running in a host application.

## Caveats

It cannot do blurs, sharpening or any neighborhood operation, and the brief could not confirm how recently the project was updated.

## Links

- [GitHub repository (homepage)](https://github.com/aces-aswf/CTL)
- [INSTALL.md (install guide)](https://github.com/aces-aswf/CTL/blob/master/INSTALL.md)
- [SMPTE RDD 15 (CTL syntax and functions)](https://pub.smpte.org/doc/rdd15/20070924-pub/)
