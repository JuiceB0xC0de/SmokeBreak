---
name: xwpe
title: xwpe
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, borland, editor, ide, lsp, retro, tui]
homepage: https://codeberg.org/mendezr/xwpe
scout_score: 6
status: draft
---

# xwpe

**TLDR;** A Borland-style terminal IDE from 1993, revived in 2026, with function-key menus, mouse support, and a modern LSP and DAP client bolted on.

xwpe is a programming editor and IDE for UNIX terminals and X11, modelled on the Borland C and Pascal environments. It has syntax highlighting, project management, menus driven by function keys, mouse support and Emacs-style cursor keys. F9 builds and lets you step through compiler errors, and Ctrl-G R starts a debugger. It can drive compilers and debuggers for 12 languages from inside the editor.

The project is old and was revived. Fred Kruse wrote the original in 1993, Dennis Payne continued it from 1997 to 2006, and according to the README it then went untested for nearly 20 years. In 2026 Juan Manuel Mendez Rey took it up again. The stated aim is a discoverable Borland-style interface with no per-project config and no heavy GUI runtime, which works over SSH or on a plain console.

The new part is that it speaks LSP and DAP, the same protocols VS Code and Neovim use. Behind an Alt-Q prefix it offers hover, go-to-definition, references, rename and diagnostics for C/C++, Python, Go, Rust and Scala. It also does source-level debugging for Go and Rust. Existing servers such as clangd, Metals and Delve plug in.

Underneath is a C program that draws its own interface: ncurses in the terminal (the wpe binary), and Cairo, Pango and Xft in graphical mode (xwpe), on native Wayland or X11. The idea worth poking at is how much of a modern editing workflow a 1990s menu-and-function-key design can hold once the language servers do the heavy lifting.

## Install

```
brew install xwpe
# installs the terminal binaries we and wpe. Compilers, language servers and debuggers are set up separately (see docs/ide-setup.md in the repo).
```

## Try this

```
wpe file.c
```
Opens a file in the ncurses terminal editor, where F9 builds and the menus are reachable with keys or mouse.

```
info xwpe
```
Opens the 13-chapter Texinfo manual.

```
man xwpe
```
Shows the man page for the command-line options.

## What's unique

It keeps the menus and zero-config feel of a DOS-era Borland IDE, yet the terminal build speaks LSP and DAP. It also has a native Wayland backend and a binary of a few megabytes.

## Caveats

The README says the LSP client is newer and still maturing, and rename only applies to the current file.

## Links

- [Codeberg repository (homepage)](https://codeberg.org/mendezr/xwpe)
- [Historical archive](https://codeberg.org/mendezr/xwpe-archives)
- [Dennis Payne continuation (1.5.x) site](https://www.identicalsoftware.com/xwpe/)
