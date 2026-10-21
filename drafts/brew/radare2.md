---
name: radare2
title: radare2
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binary-analysis, debugger, disassembler, reverse-engineering, tui]
homepage: https://radare.org
scout_score: 8
status: draft
---

# radare2

**TLDR;** A command-line reverse engineering framework that disassembles, patches, debugs and scripts binaries, firmware and live processes from a terse shell.

radare2 (r2) opens a file, raw memory, or a running process, local or behind a remote gdb/windbg server, and gives you a shell for taking it apart. Short commands do the work: `aaa` analyses the program, `afl` lists functions, `pdf` prints the disassembly of one function, `agf` draws its control-flow graph in ASCII. You can also edit bytes and write the changes back, so it patches as well as reads.

It began, in the README's words, as "a simple command-line hexadecimal editor focused on forensics", and r2 is "a complete rewrite of radare". That history shows. The tool still thinks in offsets, bytes and blocks, and everything is a command you can type, script and repeat.

The Homebrew package installs about twenty executables, and most are small single-purpose tools that share the same libraries. `rabin2` reads file headers and symbols, `rasm2` assembles and disassembles, `rahash2` hashes, `radiff2` diffs binaries, `rafind2` searches, and `rax2` converts between number bases. They are useful on their own before you ever open the full shell.

The larger idea is that reverse engineering is a conversation with a binary, and a scriptable one. r2 can be driven by an embedded JavaScript interpreter or through r2pipe from other languages. Plugins add CPU architectures, file formats and features, and `r2pm` installs third-party ones such as the r2ghidra decompiler, r2frida and the iaito Qt GUI.

## Install

```
brew install radare2
# the README recommends building from git instead:
# git clone https://github.com/radareorg/radare2 && radare2/sys/install.sh
# plugins are optional and installed separately with r2pm
```

## Try this

```
r2 /bin/ls
```
Opens the ls binary read-only in the r2 shell, ready for poking.

```
aaa
```
Typed inside the r2 shell, analyses the whole program; afl then lists the functions it found.

```
pdf; agf
```
Typed inside the r2 shell after seeking to a function (for example s sym.main), prints its disassembly and then an ASCII-art graph of its control flow.

## What's unique

It is a whole toolkit built around one terse, scriptable command language, and its plugins cover many CPUs, including exotic and retro ones. It can also mount several filesystems in userland.

## Caveats

The command language is cryptic and takes a while to learn, and each plugin can carry a different licence than the LGPLv3 core (check with r2 -Lj).

## Links

- [Homepage](https://radare.org)
- [Official radare2 book (usage docs)](https://book.rada.re)
- [GitHub repository and README](https://github.com/radareorg/radare2)
- [r2con talks on YouTube](https://www.youtube.com/c/r2con)
