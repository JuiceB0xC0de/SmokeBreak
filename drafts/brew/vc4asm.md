---
name: vc4asm
title: vc4asm
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, assembler, disassembler, gpu, hardware, raspberry-pi, reverse-engineering]
homepage: https://maazl.de/project/vc4asm/doc/index.html
scout_score: 7
status: draft
---

# vc4asm

**TLDR;** An assembler and disassembler for the Raspberry Pi's VideoCore IV GPU, a barely documented processor you can write machine code for yourself.

vc4asm is a macro assembler for the QPU cores inside the Broadcom VideoCore IV, the GPU in the original Raspberry Pi. It reads `.qasm` source and writes a raw little-endian binary, an ARM ELF object for `ld` or `gcc`, or C/C++ source and header files. Its companion `vc4dis` goes the other way, turning hex or binary QPU machine code back into assembler source.

The author built it because, in their words, "this area is highly undocumented in the public domain." With little documentation to go on, the instruction encoding was worked out using the `hello_fft` sample as a Rosetta Stone. The project builds on earlier assemblers by Pete Warden (qpu-asm), Eman, and Herman H Hermitage, and adds macros, functions, and constraint checking.

The constraint checker (`-V`) catches hardware rules that are easy to break by hand, such as reading a register file address right after writing it. The disassembler's `-M` option suppresses emulated `mov` instructions, so disassembling and reassembling gives back the same binary. That round trip makes it a decent tool for taking apart existing GPU code.

The idea underneath is that the GPU is just another small processor with its own instruction set, and with an assembler you can program it directly instead of going through a graphics API. The homepage includes a hand-optimized FFT shader as proof, with about 40% less code and roughly 9% less run time than GPU_FFT 3.0.

## Install

```
brew install vc4asm
# Assembling and disassembling work anywhere. Running the sample GPU programs needs a Raspberry Pi with the vc4 display driver turned off.
```

## Try this

```
vc4asm --help
```
Prints the assembler's options, including `-V` for constraint checking and `-i` for include paths.

```
vc4asm -o code.bin -i vc4.qinc gpu_fft_1k.qasm
```
Assembles the homepage's FFT example into a raw binary, pulling in the platform definitions from vc4.qinc.

```
vc4dis --help
```
Prints the disassembler's options, including `-M` for reassemblable output and `-b` for a base address.

## What's unique

It gives you macros, functions, and constraint checking for a GPU that almost nobody documents, plus a disassembler that can round-trip. Its optimized FFT shader builds only with this assembler.

## Caveats

The author says there are too few test cases so bugs are likely, the release date is unclear, and the samples run only on Raspberry Pi hardware with the vc4 display driver off.

## Links

- [Homepage and documentation](https://maazl.de/project/vc4asm/doc/index.html)
- [Source on GitHub](https://github.com/maazl/vc4asm)
- [Changelog](http://www.maazl.de/project/vc4asm/doc/changelog.html)
