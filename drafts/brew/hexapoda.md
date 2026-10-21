---
name: hexapoda
title: hexapoda
source: brew
category: take-things-apart
commitment: quick
tags: [binary, hex-editor, modal-editing, quick, tui]
homepage: https://simonomi.dev/hexapoda
scout_score: 5
status: draft
---

# hexapoda

**TLDR;** A terminal hex editor that colours each byte by value and edits the way Helix and Kakoune do: select first, then act.

Hexapoda opens a binary file and shows its bytes, each coloured by its value. The colour helps you spot structure, such as runs of zeros, text and repeated patterns, without reading every number. The homepage calls it "a colorful modal hex editor".

Editing is modal and selection-first, "like Kakoune and Helix". You select bytes, then act on them. Multiple selections work, and a selection can be split into fixed-size chunks. You can search, mark offsets, jump to an offset, and undo or redo. Replacing and deleting bytes work. Inserting does not yet.

The most interesting idea is the repeat action, bound to `*` by default. Instead of typing a count, it takes the count from the primary register, so a value read out of the file can decide how many times an edit repeats. The homepage example yanks a word at 0x4, goes to 0xc and selects that many words with `v*e`. That fits how binary formats are built, with length fields that say how much data follows.

The `<C-space>` key inspects the current selection as signed, unsigned, binary, fixed-point, UTF-8 and colour. That makes it a handy way to learn how the same bytes read under different interpretations. The homepage gives no stated motivation beyond the modal model and the colour.

## Install

```
brew install hexapoda
```

## Try this

```
hexapoda --help
```
Prints the command-line usage so you can see how to open a file.

```
v*e
```
From the homepage usage example: after yanking a word at 0x4 and jumping to 0xc, selects that many words, using a value from the file as the repeat count.

```
<C-space>
```
Inspects the current selection as signed, unsigned, binary, fixed-point, UTF-8 and colour.

## What's unique

Byte values are coloured, editing is selection-first like Helix, and the repeat count can come from data in the file itself. That combination is unusual among terminal hex editors.

## Caveats

Inserting bytes is not implemented and diffing is missing. The homepage says features are incomplete and shows no release dates, so behaviour may change.

## Links

- [homepage](https://simonomi.dev/hexapoda)
