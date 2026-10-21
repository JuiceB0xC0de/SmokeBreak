---
name: oclgrind
title: Oclgrind
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, debugger, gpu, llvm, opencl, simulator]
homepage: https://github.com/jrprice/Oclgrind
scout_score: 6
status: draft
---

# Oclgrind

**TLDR;** A virtual OpenCL device that runs GPU kernels in a bounds-checking interpreter, catching memory errors, data races and barrier bugs a real device would ignore.

Oclgrind presents itself to an OpenCL application as the only platform and device available. Behind that facade there is no GPU and no vendor driver. Kernels are compiled to LLVM IR and interpreted, with every memory access checked. You run an unmodified OpenCL host program under it, and the program's normal output is joined by diagnostics on stderr.

When something goes wrong, the report names the kernel, the work-item (Global, Local and Group IDs), the offending IR instruction and the source line. The README also lists data-race detection, barrier-divergence detection and instruction histograms. These are the kinds of bugs that often pass silently on real hardware and then surface as wrong answers on someone else's machine.

It was created by James Price and Simon McIntosh-Smith at the University of Bristol. In the README's words, the goal is "to provide a platform for creating tools to aid OpenCL development." The idea underneath is that a GPU program can be run on a simulated device where every step is observable, so the interpreter becomes a place to build analysis tools.

With `-i` or `OCLGRIND_INTERACTIVE=1`, execution stops at the start of each kernel invocation and at any invalid access, and drops you at a GDB-style prompt where `help` lists the commands. This is a CPU-side interpreter, so it is a debugger for kernel logic, not a view of what the GPU silicon does.

## Install

```
brew install oclgrind
# You also need an OpenCL application or a kernel file to run under it. Homebrew pulls in llvm@19.
```

## Try this

```
oclgrind ./application
```
Runs your OpenCL program with Oclgrind as the only visible platform and device, reporting invalid memory accesses and other errors on stderr.

```
oclgrind --help
```
Lists the options, including the interactive debugging mode and the checks you can switch on.

```
oclgrind-kernel --help
```
Shows the options of the standalone kernel runner, which executes a kernel file without a host program.

## What's unique

It runs unmodified OpenCL host programs and checks every memory access, race and barrier against the kernel's IR, so it finds bugs a real device would let through.

## Caveats

It is slow, typically a couple of orders of magnitude slower than a regular CPU implementation, so keep problem sizes small, and you need your own OpenCL program to test.

## Links

- [GitHub repository (homepage)](https://github.com/jrprice/Oclgrind)
- [Wiki](https://github.com/jrprice/Oclgrind/wiki/)
- [Releases](https://github.com/jrprice/Oclgrind/releases)
