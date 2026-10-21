---
name: blink
title: blink
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cosmopolitan, debugger, emulator, reverse-engineering, tui, x86-64]
homepage: https://github.com/jart/blink
scout_score: 8
status: draft
---

# blink

**TLDR;** A 221kb x86-64 Linux emulator for any POSIX host, with blinkenlights, a terminal debugger that animates memory as you step through assembly.

Blink is a user-mode emulator written in ANSI C11. It takes a Linux x86-64 ELF binary, or a Cosmopolitan Actually Portable Executable, and runs it on another POSIX system such as macOS, FreeBSD, OpenBSD or Cygwin. It does this by decoding the instructions itself and translating Linux system calls to the host. Hot code is JIT-compiled to native functions on x86_64 and aarch64.

The README pitches it as a smaller, more portable alternative to qemu-x86_64: about 221kb against a 4mb binary, and running on any POSIX system rather than only Linux. Decoding uses a trimmed-down version of Intel's Xed disassembler. Guest memory is virtualized through a four-level page table with a small TLB, or through a faster linear mapping.

The companion program, blinkenlights, is the reason to stop by. It is a terminal UI debugger that draws memory panels as IBM Code Page 437 glyphs, and the panels change as you single-step the assembly. You can also scroll the mouse wheel over the disassembly to run execution backward. In the README's words: "Unlike GDB, Blinkenlights focuses on visualizing program execution."

The larger idea is that a CPU is just a program you can read. Because the whole emulator is small, you can follow how instructions, memory and syscalls fit together, and then watch a real binary do it.

## Install

```
brew install blink
# The README builds from source (needs a C11 compiler and a modern GNU Make). The TUI needs a UTF-8 VT100/xterm-style terminal such as kitty, GNOME Terminal or Terminal.app.
```

## Try this

```
blink -v
```
Prints the version and build configuration, confirming the install works.

```
blinkenlights third_party/cosmo/tinyhello.elf
```
Opens the bundled hello-world binary in the debugger TUI so you can step through it and watch memory change. The file ships in the source repository.

```
blink third_party/cosmo/tinyhello.elf
```
Runs the same hello-world binary headless under the emulator, with no debugger.

## What's unique

Most emulators are big and hide what they do. Blink is a few hundred kilobytes, runs on many hosts, and ships a debugger built around watching execution, with reverse stepping.

## Caveats

Not every Linux program works: many address families and Linux-only syscalls return EINVAL, x87 long double is only 64-bit, and the README gives no maintenance dates.

## Links

- [blink on GitHub](https://github.com/jart/blink)
- [Blinkenlights project page](https://justine.lol/blinkenlights)
- [Getting Started with Cosmopolitan Libc (blog)](https://jeskin.net/blog/getting-started-with-cosmopolitan-libc/)
- [blink-isystem (musl headers for Blink builds)](https://github.com/jart/blink-isystem)
