---
name: elfx86exts
title: elfx86exts
source: brew
category: take-things-apart
commitment: quick
tags: [cpu, disassembly, quick, reverse-engineering, rust, x86]
homepage: https://github.com/pkgw/elfx86exts
scout_score: 7
status: draft
---

# elfx86exts

**TLDR;** Disassembles a compiled binary and reports which CPU instruction set extensions it uses, plus a guess at the minimum Intel generation needed to run it.

elfx86exts reads an executable, works out its container format (ELF, Mach-O, and per the changelog PE), and disassembles the code with the Capstone engine. It then checks the decoded instructions against known extension families and prints the ones it sees. It picks the x86/x86-64 or ARM64 path from the binary's CPU architecture, and exits if the architecture is neither.

The idea underneath is that a binary carries a record of the hardware it assumes. SSE, AVX and friends are not abstract; a compiler emits them, and if one lands in your program, older CPUs will crash on it. Since version 0.3.0 the tool also prints a best guess at the minimum Intel CPU generation required, using an internal table of which extensions arrived in which CPU model.

The name is a running joke. The README calls it 'utterly misleading', since it now handles far more than ELF and x86, and the changelog keeps noting that each addition makes the name 'ever more inaccurate'. The author's tone is loose too: 'I have no idea what I'm doing here, but it seems to work.'

It is a small door into how compilers target CPUs, what `-march` flags actually change in the output, and how to inspect a binary without running it.

## Install

```
brew install elfx86exts
# Alternative: cargo install elfx86exts (needs a Rust toolchain and the Capstone C library)
```

## Try this

```
elfx86exts --help
```
Prints the tool's usage, since the README has no usage section.

## What's unique

Most disassemblers dump instructions. This one boils a whole binary down to which CPU features it needs, and guesses the oldest Intel generation that can run it.

## Caveats

The README has no usage section or sample output, ARM64 support is described as preliminary, and the last release seen was 0.6.2 in October 2023.

## Links

- [Project homepage (GitHub)](https://github.com/pkgw/elfx86exts)
- [CHANGELOG (release branch)](https://github.com/pkgw/elfx86exts/blob/release/CHANGELOG.md)
- [Arch Linux AUR package](https://aur.archlinux.org/packages/elfx86exts/)
