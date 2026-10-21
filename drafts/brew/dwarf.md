---
name: dwarf
title: dwarf
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binary, elf, hex-editor, mach-o, pe, reverse-engineering]
homepage: https://github.com/elboza/dwarf-ng/
scout_score: 5
status: draft
---

# dwarf

**TLDR;** A gdb-flavoured hex editor that understands ELF, PE and Mach-O headers as editable variables, so you can patch binaries at the structure level.

dwarf-ng is a command-line object file tool and hex editor. You open a file and get a shell-like prompt whose commands follow a gdb-like syntax: a letter for the operation, an optional `?` for help, then arguments such as an address or block size. It handles raw files, ELF (32 and 64-bit), PE (PE32 and PE+), and Mach-O.

The interesting part is that headers are exposed as variables. For ELF you get `$elf`, `$ph[0..n]` and `$sh[0..n]`; Mach-O has `$mac` and `$lc`; PE has `$pe` and `$sect`. You can print them, assign to them, use them in expressions, and write bytes at the offset a header field points to. The README says you can also create new file headers, inject headers and code or data, and use the tool as a compiler back-end.

The README describes it as "a little and powerful object file manipulation tool and hex editor" "in the spirit of _gdb_". The idea underneath is that an executable is just a structured byte array. Once you can address its section headers by name, you see how loaders and linkers read the file, and how little stands between a binary and your edits.

Despite the name, the README does not describe parsing DWARF debug information. The name appears to be the tool's own identity, not a debug-format reader.

## Install

```
brew install dwarf
# Config is optional: /etc/dwarfrc and ~/.dwarfrc (e.g. work_on_tmpcopy, verbose, colors). No accounts or hardware needed.
```

## Try this

```
dwarf -h
```
Prints the usage banner, including the version and the list of command-line options.

```
o myfile
```
Run inside the dwarf prompt: opens a file and probes its type, loading the ELF, PE or Mach-O structures.

```
x 0x100
```
Run inside the prompt: hexdumps the open file starting at offset 0x100.

## What's unique

It is a gdb-style hex editor that understands several executable formats at once and exposes their headers as variables you can assign, resize and rebuild.

## Caveats

The help banner reads dwarf-ng-0.4.0 with copyright through 2017, and the README gives no release dates, so maintenance status is unclear; only raw, ELF, PE and Mach-O are supported.

## Links

- [dwarf-ng GitHub repository](https://github.com/elboza/dwarf-ng/)
- [dwarf man page](https://github.com/elboza/dwarf-ng/blob/master/doc/xdwarf.man.html)
