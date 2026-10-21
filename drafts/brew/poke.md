---
name: poke
title: GNU poke
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binary-formats, editor, language, reverse-engineering]
homepage: https://jemarch.net/poke
scout_score: 9
status: draft
---

# GNU poke

**TLDR;** An interactive editor where you describe a binary format in a small language, then map it onto a file and edit its fields as typed values.

GNU poke is an editor for binary data that goes past bits and bytes. It ships with a procedural, interactive programming language "designed to describe data structures and to operate on them." You write down what a format looks like, point it at a spot in a file, and poke shows parsed fields instead of raw hex.

The homepage example opens an ELF binary, loads the ELF pickle, and maps an `Elf64_Ehdr` struct at offset 0. Printing a member such as `e_ident` gives a struct with fields like `ei_mag` and `ei_class`. Because the fields are typed objects, you can inspect them and also change them.

Format descriptions are called pickles. GNU poke comes with many pre-written ones, and separate packages such as poke-elf and poke-dwarf extend the coverage. The underlying idea is that a file format is a program you can run against bytes. Once you have written the description, hex dumps and ad hoc scripts become unnecessary for that format.

The homepage says the Poke Virtual Machine is based on Jitter by Luca Saiu. It does not explain the internals beyond that, or what the extra executables in the brew package do.

## Install

```
brew install poke
```

## Try this

```
poke --help
```
Lists the command-line options for starting the editor.

```
(poke) load elf
```
Inside the poke prompt, loads the ELF pickle so types like Elf64_Ehdr become available.

```
(poke) var ehdr = Elf64_Ehdr @ 0#B
```
Maps an ELF header struct at byte offset 0 of the open file; then `ehdr.e_ident` prints its fields.

## What's unique

It treats a binary file as a typed, programmable object with its own interactive language, rather than as a grid of hex you read by eye.

## Caveats

The homepage does not cover platform support or the full list of pickles, and it does not explain the extra pk-* tools that brew installs.

## Links

- [poke homepage](https://jemarch.net/poke)
