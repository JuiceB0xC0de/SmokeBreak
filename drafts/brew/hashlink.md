---
name: hashlink
title: HashLink
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, bytecode, haxe, jit, language, vm]
homepage: https://hashlink.haxe.org/
scout_score: 5
status: draft
---

# HashLink

**TLDR;** A virtual machine for Haxe that runs typed bytecode through a JIT, or turns the same program into C for a native build.

HashLink is the runtime behind one of Haxe's compile targets. The Haxe compiler turns source into strictly typed bytecode with the `-hl` flag, and the `hl` program runs that bytecode through a just-in-time compiler. The runtime also ships standard library support for file I/O, regular expressions, networking and Unicode strings, plus optional libraries for image decoding, OS dialogs and SDL windowing with OpenGL.

The same bytecode can also be translated to C and built with gcc or a similar compiler into a native executable. Both paths share one runtime and the same semantics. The project's advice: "Use HL/JIT for daily development (fast compilation time)" and "Use HL/C for final release (best performance)." The homepage cites Northgard, a commercial 3D game that moved from Adobe AIR to HashLink, as its real-world example.

The door it opens is language implementation. Typed bytecode, a JIT, a C backend, a mark-and-not-sweep garbage collector, typed virtuals for fast access to anonymous objects, and static dispatch when nothing overrides a method are all visible in one codebase you can build and read. You also need the Haxe compiler, version 3.4 or later, to produce bytecode.

## Install

```
brew install hashlink
# Needs the Haxe compiler (3.4+) to produce bytecode. On ARM Macs, brew does not install the hl JIT VM, only the HL/C path is supported (see GitHub issue 557). The JIT supports x86 and x86-64 only.
```

## Try this

```
haxe -hl output.hl -main MyApp
```
Compiles a Haxe project whose main class is MyApp into HashLink bytecode in output.hl.

```
hl output.hl
```
Runs that bytecode file in the HL/JIT virtual machine.

```
haxe -hl out/main.c -main MyApp
```
Generates C source for the HL/C path, which you can then build with gcc and link against libhl.

## What's unique

One typed bytecode, one runtime, two ways to run it: a JIT for fast iteration and a C backend for release builds. Most Haxe targets go straight to JavaScript or native code instead.

## Caveats

On Apple Silicon and other ARM machines brew installs no `hl` JIT binary, only the HL/C route; the benchmarks against Adobe AIR and Node/V8 are the project's own and described as initial.

## Links

- [HashLink homepage](https://hashlink.haxe.org/)
- [GitHub repository](https://github.com/HaxeFoundation/hashlink)
- [HashLink wiki documentation](https://github.com/HaxeFoundation/hashlink/wiki)
- [VS Code debugger extension (haxe-hl)](https://marketplace.visualstudio.com/items?itemName=HaxeFoundation.haxe-hl)
