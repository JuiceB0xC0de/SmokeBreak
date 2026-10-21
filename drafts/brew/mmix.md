---
name: mmix
title: MMIX
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, architecture, assembly, knuth, risc, simulator, teaching]
homepage: https://mmix.cs.hm.edu/
scout_score: 8
status: draft
---

# MMIX

**TLDR;** Donald Knuth's 64-bit RISC teaching computer, with an assembler and simulator, so you can write and run assembly for a machine that never existed.

MMIX is an instruction set architecture designed by Donald Knuth. The homepage describes it as a teaching architecture that is easy to learn yet representative of modern machines. MMIXware is the software around it: an assembler (mmixal) and a simulator (mmix). You write MMIX assembly, assemble it, and run it on the emulated machine. The package also installs mmmix and mmotype, which the homepage does not describe in detail.

Knuth built MMIX to replace the older MIX machine in volumes 1 to 3 of The Art of Computer Programming, and to use it in later volumes starting with volume 4. The MMIX Supplement provides MMIX versions of every MIX program in those volumes. The software is therefore a companion to a book, and it makes the book's programs runnable.

The idea underneath is that a whole computer, with its instruction set, assembler and simulator, can be small enough to learn completely. Nothing is hidden behind an operating system or a vendor manual. You see what a program does at the level of registers and instructions, which is a good way into how real machines execute code.

Version 1 is frozen. The homepage calls it "permanently frozen" and "bug-free by definition." The software is a fixed reference, not a moving project.

## Install

```
brew install mmix
```

## Try this

```
mmixal --help
```
Shows the assembler's usage, the first step in turning MMIX assembly source into something the simulator can run.

```
mmix --help
```
Shows the simulator's usage and options for running an assembled program.

```
mmotype --help
```
Shows usage for mmotype, one of the extra tools installed alongside the assembler and simulator.

## What's unique

Knuth designed a whole machine, instruction set and toolchain for teaching, and tied it to a landmark book series. The software is a frozen reference, not a moving target.

## Caveats

The architecture is frozen at Version 1 with the last named tarball dated 2013, much of the documentation is in PDF, and the homepage gives no quick-start commands.

## Links

- [MMIX homepage](https://mmix.cs.hm.edu/)
- [MMIX sources (git, LRZ GitLab)](https://gitlab.lrz.de/mmix)
