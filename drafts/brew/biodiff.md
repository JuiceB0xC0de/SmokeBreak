---
name: biodiff
title: biodiff
source: brew
category: take-things-apart
commitment: quick
tags: [bioinformatics, diff, hex, quick, reverse-engineering, rust, tui]
homepage: https://github.com/8051Enthusiast/biodiff
scout_score: 8
status: draft
---

# biodiff

**TLDR;** A terminal hex diff viewer that lines up two binary files using DNA sequence alignment, so inserted or deleted bytes don't scramble the comparison.

biodiff shows two binary files side by side in hex, with an ASCII column. Its alignment step pads the shorter side so that similar bytes sit at the same position in both columns. Bytes that exist in only one file show up as gaps.

The usual problem with comparing binaries is that one inserted byte shifts everything after it, and a byte-by-byte diff turns into noise. Bioinformatics solved the same problem for DNA, where sequences gain and lose letters over time. biodiff borrows those algorithms from the wfa2 library or from rust-bio, and applies them to executables and other byte streams.

In the default interactive mode it aligns block by block, starting near the cursor and then moving outward. Global alignment over the whole file is available with F4, but it takes quadratic time and space. The README says it "will not work well for files bigger than 64kB". A faster banded algorithm trades some accuracy for speed. You can also select a region and use it as a pattern for a semiglobal search in the other file.

The views go beyond hex. You can switch between several byte representations (bases 2, 8, 10, 16, braille, roman numerals), and search handles text, regex and hexagex. The configuration dialogs are built with the cursive TUI library.

## Install

```
brew install biodiff
```

## Try this

```
biodiff file_a file_b
```
Opens both files side by side in the interactive hex view. They start unaligned; press F3 or 3 to align them.

```
biodiff --print file_a file_b
```
Prints the diff straight to the terminal instead of opening the interactive view.

```
biodiff --help
```
Lists the available options, including the alignment choices.

## What's unique

It treats two byte streams like two DNA sequences, so insertions and deletions get padded out instead of ruining the rest of the comparison.

## Caveats

Global alignment is quadratic and impractical for files over about 64kB, and the README gives no maintenance status or date; it also leaves the installed git-biodiff executable undocumented.

## Links

- [GitHub repository (homepage)](https://github.com/8051Enthusiast/biodiff)
- [Releases](https://github.com/8051Enthusiast/biodiff/releases)
- [crates.io](https://crates.io/crates/biodiff)
