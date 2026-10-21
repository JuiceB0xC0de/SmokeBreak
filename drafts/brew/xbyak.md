---
name: xbyak
title: Xbyak
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, assembler, c++, jit, library, x86]
homepage: https://github.com/herumi/xbyak
scout_score: 5
status: draft
---

# Xbyak

**TLDR;** A header-only C++ library that turns method calls like mov(eax, x) into x86 machine code in memory, then lets you call it as a function.

Xbyak is a JIT assembler. You write C++ calls that mirror assembly mnemonics, and it encodes the instructions into a buffer. Ask for a function pointer with `getCode<T>()`, call it, and your program is running machine code it wrote a moment earlier.

The usual route is to subclass `Xbyak::CodeGenerator` and emit instructions in the constructor. Labels, jumps and memory operands such as `ptr[...]` are supported, so you can build loops and branches and not only straight-line code. The syntax follows MASM/NASM closely, with parentheses around operands. The AVX-512 example in the README shows the NASM form `vaddpd zmm2{k5}{z}, zmm4, zmm2` next to the Xbyak form `vaddpd(zmm2 | k5 | T_z, zmm4, zmm2)`.

The idea underneath is that code can be data. If you know a matrix size, a filter length or a CPU feature only at runtime, you can emit a routine specialised for exactly that, instead of one general routine full of branches. It is also a good way to learn how instructions are encoded, since you can write one and look at the bytes it produces.

The name comes from the Japanese word kaibyaku, meaning 'the beginning of the world' or 'creation'. The README says it supports recent extensions such as AVX10.2, APX and ACE.

## Install

```
brew install xbyak
# Installs headers only, no executables. You need a C++ compiler and an Intel CPU to use it.
# Alternatively copy xbyak.h, xbyak_mnemonic.h and xbyak_util.h into your include path.
```

## Try this

```
mov(eax, x);
```
Inside a CodeGenerator subclass, emits mov eax, x. Follow it with ret() to build a function that returns x.

```
int (*f)() = c.getCode<int (*)()>();
```
Gets a callable function pointer to the generated code, which you invoke as f().

```
vaddps(xmm1, xmm2, xmm3);
```
Emits an AVX packed-float add, xmm1 = xmm2 + xmm3.

## What's unique

It is header-only and writes instructions as ordinary C++ method calls in MASM-like syntax, and it tracks very new x86 extensions. Forks exist for AArch64 and RISC-V.

## Caveats

Intel CPUs only on Windows, Linux and macOS. It is a library with no command-line tool, and generated code lives in writable and executable memory by default.

## Links

- [GitHub repository and README](https://github.com/herumi/xbyak)
- [Usage guide (doc/usage.md)](https://github.com/herumi/xbyak/blob/master/doc/usage.md)
- [Install guide (doc/install.md)](https://github.com/herumi/xbyak/blob/master/doc/install.md)
- [Xbyak_aarch64 derived project](https://github.com/fujitsu/xbyak_aarch64/)
