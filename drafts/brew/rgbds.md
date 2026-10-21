---
name: rgbds
title: RGBDS
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, assembler, assembly, game-boy, homebrew, linker, retro]
homepage: https://rgbds.gbdev.io
scout_score: 7
status: draft
---

# RGBDS

**TLDR;** An assembler and linker toolchain for the Game Boy and Game Boy Color: write assembly and PNG art, get a ROM that runs on the console.

RGBDS, the Rednex Game Boy Development System, is a set of small programs that turn assembly source and PNG images into a playable Game Boy ROM. RGBGFX converts images into the console's tile formats. RGBASM assembles source into object files. RGBLINK links those into a ROM. RGBFIX patches the ROM header and checksum so the hardware will accept it. The brew formula also installs rgbobj.

The project's own pitch is control: "Gain complete control over the console; with no middle-man, debugging is made simpler." There is no engine or runtime in between. You write native assembly for the console's CPU and decide what happens on every cycle and in every byte of memory.

The idea underneath is that a whole computer can be small enough to hold in your head. The Game Boy has tight limits on memory, graphics and sound, and fitting a game inside them teaches how assemblers, linkers, object files and ROM headers fit together. Each stage is a separate program, and the project says each can be replaced with a custom one or used standalone in another process.

The project dates back to 1997 and is maintained through the GBDev homebrew community. The homepage links to a full manual and a version history. The brief does not describe the assembly syntax in detail, so the documentation is the place to start.

## Install

```
brew install rgbds
```

## Try this

```
rgbasm --help
```
Prints the assembler's options, a first look at how source files become object files.

```
rgblink --help
```
Shows how the linker turns object files into a ROM.

```
rgbgfx --help
```
Lists the options for converting PNG images into Game Boy tile data.

## What's unique

The toolchain is split into small single-purpose programs that can be swapped out or used on their own. It also includes RGBGFX, which handles the art conversion step that many hobby assemblers leave to you.

## Caveats

It is assembly-first and covers only the Game Boy and Game Boy Color, so expect to learn the hardware as well as the tools.

## Links

- [Homepage](https://rgbds.gbdev.io)
- [Full documentation](https://rgbds.gbdev.io/docs/)
- [Install instructions](https://rgbds.gbdev.io/install/)
- [Version history](https://rgbds.gbdev.io/versions)
