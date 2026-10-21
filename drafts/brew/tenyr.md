---
name: tenyr
title: tenyr
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, assembly, cpu, fpga, simulation, verilog]
homepage: https://kulp.github.io/tenyr/
scout_score: 8
status: draft
---

# tenyr

**TLDR;** A deliberately small 32-bit computer you can assemble, link and run in a simulator, with Verilog that also runs on real FPGA boards.

tenyr is a complete tiny computer, not just a program. It has three parts: an instruction set architecture, a Verilog hardware definition for FPGAs, and a set of software tools. The tools are an assembler (`tas`), a linker (`tld`) and a simulator (`tsim`). Assembly source goes through the assembler and linker, and the resulting image runs on the simulated CPU.

The README describes it as "a 32-bit computer architecture and computing environment that focuses on simplicity of design and implementation." It does not say more about why it was built. The project ships a standard library of tenyr code and example programs, including Conway's Game of Life, a random snakes screensaver and a recursive Fibonacci generator.

The idea underneath is that you can see the whole stack at once: the instruction set, the toolchain, the simulator and the hardware description. The same design has been demonstrated on a Lattice ECP5 FPGA (ULX3S board) and a Xilinx Spartan6 FPGA (Nexys3 board), with VGA text output at 64x32. The ISA is documented in the project wiki. If you have ever wondered what sits between assembly and gates, this is a small enough system to read through.

## Install

```
brew install tenyr
# installs tas, tld and tsim; depends on sdl2-compat and sdl2_image
# running on real hardware needs an FPGA board (ULX3S or Nexys3 have been demonstrated); the simulator needs none
```

## Try this

```
tas --help
```
Shows the assembler's options, the first step from assembly source to an object file.

```
tld --help
```
Shows the linker's options, which combine objects into a runnable image.

```
tsim --help
```
Shows the simulator's options. Run the example programs from the repository's ex/ directory with it, following the wiki.

## What's unique

The whole stack is small and self-contained: a custom ISA, an assembler, linker and simulator, and Verilog that has run on real FPGA boards. The homepage calls it a simple environment, not a toy.

## Caveats

No input devices are implemented in the hardware (the README asks for help), hardware output is VGA text at 64x32 only, and recent maintenance activity could not be confirmed.

## Links

- [Project homepage](https://kulp.github.io/tenyr/)
- [GitHub repository](https://github.com/kulp/tenyr)
- [Wiki (documentation, assembler, linker, simulator)](https://github.com/kulp/tenyr/wiki)
- [Example programs (ex/)](https://github.com/kulp/tenyr/tree/develop/ex)
