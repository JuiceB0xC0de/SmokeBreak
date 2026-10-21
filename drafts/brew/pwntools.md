---
name: pwntools
title: pwntools
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, ctf, exploitation, library, python, reverse-engineering]
homepage: https://github.com/Gallopsled/pwntools
scout_score: 6
status: draft
---

# pwntools

**TLDR;** A Python library and 19 command-line tools for writing exploits and poking at binaries, built for capture-the-flag competitions.

Pwntools is a CTF framework and exploit development library written in Python. A script starts with `from pwn import *`, sets a target context such as architecture and OS, opens a connection to a remote service with `remote()`, and sends it payloads. It can assemble and disassemble machine code, and its shellcraft module generates shellcode. `interactive()` hands the session over to you when the exploit lands.

The README says it is "designed for rapid prototyping and development, and intended to make exploit writing as simple as possible." The idea underneath is that exploit writing is mostly repetitive plumbing: talking to a socket, packing integers, building byte patterns, turning assembly into bytes. Pwntools turns that into a few lines of Python so the time goes into understanding the target.

The install also brings about 19 command-line tools that work without writing a script. Among them are `checksec` for a binary's protections, `cyclic` for de Bruijn patterns that locate overflow offsets, `asm` and `disasm`, `elfpatch`, `shellcraft`, `template`, and `hex`/`unhex`. Each is a small door into a piece of binary exploitation, such as how a crash maps to a buffer offset or what a hardened binary looks like.

## Install

```
brew install pwntools
# Upstream's documented route is pip: python3 -m pip install --upgrade pwntools
# Needs Python 3.10+ for 5.x. Assembling or disassembling foreign architectures needs extra system packages such as binutils. If pip-installed as a normal user, add ~/.local/bin to PATH. No account or hardware needed.
```

## Try this

```
pwn --help
```
Lists the subcommands of the main pwn tool, a quick map of what the toolkit covers.

```
checksec --help
```
Shows how to inspect an ELF binary for protections such as NX and stack canaries.

```
shellcraft --help
```
Shows how to generate shellcode for a chosen architecture and OS from the command line.

## What's unique

It reduces exploit scripting to a short Python idiom: connect, generate shellcode, drop into a shell. The bundled CLI tools cover much of the rest of the binary-exploitation toolbox in one install.

## Caveats

Official support centres on 64-bit Ubuntu LTS, other systems are described as "most functionality should work", and foreign-architecture assembly needs extra system packages.

## Links

- [Homepage (GitHub repo)](https://github.com/Gallopsled/pwntools)
- [Documentation](https://docs.pwntools.com/)
- [Installation docs](https://docs.pwntools.com/en/stable/install.html)
- [Tutorials](https://github.com/Gallopsled/pwntools-tutorial#readme)
