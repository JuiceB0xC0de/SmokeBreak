---
name: icarus-verilog
title: Icarus Verilog
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, compiler, digital-logic, hardware-design, simulation, verilog]
homepage: https://steveicarus.github.io/iverilog/
scout_score: 6
status: draft
---

# Icarus Verilog

**TLDR;** A free Verilog compiler and simulator runtime that lets you write digital circuits as code and run them on your laptop, no hardware needed.

Verilog is a hardware description language. Instead of writing instructions for a processor, you describe wires, registers and logic gates, and the circuit exists as text. Icarus Verilog takes that text, parses it, builds a netlist (a graph of the described hardware), runs optimization passes such as constant propagation, and hands the result to a code generator chosen with `-t`.

The default target produces a program for `vvp`, the runtime that actually steps through the simulation. So the workflow looks like a software compiler: `iverilog` compiles, then `vvp` (or the resulting `a.out`) runs. The README's example is a hello-world module that prints a message and calls `$finish`. The project's own framing is unusual: it is "not aimed at being a simulator in the traditional sense, but a compiler that generates code employed by back-end tools."

The idea underneath is that a chip is a program whose semantics are time and parallelism. Everything happens at once, and clock edges decide what changes when. Once you can simulate a counter, an adder or a small CPU on your own machine, the path to FPGAs and real silicon design opens up. Icarus appears to have started as a free toolchain for Verilog users on Linux, and the README calls it "a GPL Verilog for Linux".

## Install

```
brew install icarus-verilog
```

## Try this

```
iverilog hello.vl
```
Compiles the README's hello-world Verilog file into a.out, the program the vvp runtime executes.

```
./a.out
```
Runs the compiled design, which prints 'Hello World' and then calls $finish.

```
iverilog --help
```
Lists the compiler driver's options, including output naming and target selection.

## What's unique

It is a free, GPL-licensed compiler that covers IEEE 1364 Verilog and a growing slice of SystemVerilog, and it openly documents its quirks and unsupported constructs. Its pipeline is a real compiler with a netlist and selectable back ends.

## Caveats

SystemVerilog support is only a subset, specify blocks are ignored unless -gspecify is given, and trireg and `wire #N foo;` net delays are unsupported.

## Links

- [Icarus Verilog documentation (homepage)](https://steveicarus.github.io/iverilog/)
- [GitHub repository](https://github.com/steveicarus/iverilog)
- [Releases](https://github.com/steveicarus/iverilog/releases)
