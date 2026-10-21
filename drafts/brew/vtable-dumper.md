---
name: vtable-dumper
title: vtable-dumper
source: brew
category: take-things-apart
commitment: quick
tags: [abi, c++, elf, library, quick, reverse-engineering]
homepage: https://github.com/lvc/vtable-dumper
scout_score: 6
status: draft
---

# vtable-dumper

**TLDR;** Prints the C++ virtual tables inside a compiled shared library, showing the slot layout the compiler actually produced.

vtable-dumper takes a shared library and lists every C++ virtual table in it. Each vtable gets a header with its mangled symbol name and entry count, then one line per slot with a byte offset and what sits there: a virtual method, a destructor, `__cxa_pure_virtual`, or a typeinfo pointer. Options switch between mangled and demangled names.

It was written by Andrey Ponomarenko for library developers and Linux distribution maintainers. In the README's words, it is "intended for developers of software libraries and maintainers of Linux distributions who are interested in ensuring backward binary compatibility." Reordering or adding a virtual method can shift slots and break programs built against the older library, and this tool shows that layout directly.

The idea underneath is that virtual dispatch is just an array of function pointers at fixed offsets. Source code hides that. Here you see what the compiler and linker really emitted, including stubs and thunks. Reading the output takes some familiarity with the Itanium C++ ABI, which makes it a good excuse to learn it.

The README says the tool loads the target with `dlopen()`, and it lists libelf and libdl as requirements. It does not describe the internals beyond that.

## Install

```
brew install vtable-dumper
# The README itself gives a source install: sudo make install prefix=/usr
# Needs libelf, libdl and libstdc++. The target library's dependencies must be resolvable by ldd; add paths to LD_LIBRARY_PATH if dlopen() fails.
```

## Try this

```
vtable-dumper /usr/lib64/libstdc++.so.6
```
Dumps the vtables in the system C++ standard library, one slot per line with offsets and symbol names.

```
vtable-dumper SHLIB
```
The basic pattern: pass any C++ shared library path as the only argument.

## What's unique

It shows the vtable layout as shipped in a binary, with offsets, thunks and pure-virtual stubs, rather than what the source suggests. That makes it handy for comparing library versions.

## Caveats

The brew entry lists no executables and the README does not mention Homebrew, so the formula may not put a working command on your path. The tool is Linux-oriented, and its maintenance status is unknown.

## Links

- [GitHub repository (homepage)](https://github.com/lvc/vtable-dumper)
