---
name: z80dasm
title: z80dasm
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, assembly, disassembler, retro, reverse-engineering, rom, z80]
homepage: https://www.tablix.org/~avian/blog/articles/z80dasm/
scout_score: 7
status: draft
---

# z80dasm

**TLDR;** A disassembler for the Zilog Z80 that turns ROM dumps from 1980s micros into assembly source you can reassemble byte for byte.

z80dasm reads a binary file, such as a ROM dump or program image, and writes Z80 assembly source. It guesses label locations from jumps and similar instructions, or takes names from a symbol file you supply. You can also give it information about which regions are code and which are data, so the listing does not treat a text table as instructions.

The Z80 powered a lot of 1980s home computers, including the Sinclair ZX81 and Spectrum. The README says the tool can be used to reverse engineer programs and operating systems for those machines. The author developed it to produce the Galaksija ROM disassembly, so it was built for a real archaeology job rather than as an exercise.

The core is based largely on dz80 3.0 by Jan Panteltje. The README says z80dasm fixes multiple bugs in it and adds features. It also says a lot of attention went into unusual machine code: undocumented instructions, illegal sequences and partial opcodes.

The idea underneath is round-tripping. In the README's words, "Any disassembly by z80dasm is perfectly reversible with z80asm." The output can also be reassembled with zasm or the original Zilog assembler. That means you can disassemble a ROM, edit the source, reassemble it, and check that an untouched listing gives back the same bytes. This is how you start understanding or modifying old firmware.

## Install

```
brew install z80dasm
# No external libraries needed. To build from a release tarball you need GNU Make and a C compiler. A git checkout also needs GNU Autotools.
```

## Try this

```
z80dasm --help
```
Lists the options. The full list is also in the z80dasm(1) man page.

```
z80dasm -l -g 0x200 -o foo.asm foo.bin
```
Disassembles foo.bin into foo.asm, generating labels automatically (-l) and treating the code as sitting at address 0x200 (-g 0x200).

## What's unique

Its output is built to be reversible: a disassembly assembles back to the same binary, tested against z80asm. It also takes care over undocumented opcodes and partial opcodes.

## Caveats

The homepage gives no release or last-commit date, it was developed mainly on Debian, and you need your own Z80 binary to disassemble.

## Links

- [Project homepage](https://www.tablix.org/~avian/blog/articles/z80dasm/)
- [Source tarball downloads](https://www.tablix.org/~avian/z80dasm/)
- [Windows binary (outdated)](https://www.tablix.org/~avian/z80dasm/win32/)
