---
name: acpica
title: ACPICA
source: brew
category: take-things-apart
commitment: afternoon
tags: [acpi, afternoon, bytecode, disassembler, firmware, reverse-engineering]
homepage: https://github.com/acpica/acpica
scout_score: 6
status: draft
---

# ACPICA

**TLDR;** Intel's reference ACPI toolkit: dump your machine's firmware tables, disassemble the AML bytecode inside, and run it in a simulator.

ACPI is how firmware tells an operating system what the machine is. Instead of the BIOS managing power itself, it hands the OS a set of tables. Some of those tables contain AML, ACPI Machine Language, which the project describes as "a binary pseudo-code format, which the operating system's ACPI AML interpreter parses to discover the machine's properties." Every PC has this bytecode sitting in its firmware.

ACPICA is the reference implementation of the interpreter side. Its kernel-side parts include an AML interpreter, a table manager, a namespace manager, a resource manager and event support. The project says almost every operating system except Windows uses it to enable ACPI. All OS-specific code is isolated in a small translation layer, so the same code runs inside kernels and in user-space tools.

The user-space tools are what make it a door for a curious person. acpidump writes the system's ACPI tables out as ASCII, and acpixtract does the reverse. iASL compiles ASL source to AML and disassembles AML back to source. AcpiExec is a simulator that runs firmware bytecode without the target hardware. AcpiHelp is a lookup aid. The brew formula also installs acpibin, acpiexamples and acpisrc, which the brief does not describe.

The site also documents a 'slack mode' that tolerates AML control methods that forget an explicit return, a bug it says Windows masks. It is a small sign of how much real-world firmware is sloppy.

## Install

```
brew install acpica
```

## Try this

```
iasl --help
```
Lists the options of the ASL compiler and AML disassembler.

```
acpidump --help
```
Shows how to dump the machine's ACPI tables as ASCII; reading real tables may need elevated privileges or a supported OS.

```
acpihelp --help
```
Shows how to look up ASL and AML terms from the command line.

## What's unique

It is the same interpreter code that real kernels use, packaged with a compiler, disassembler and simulator, so you can read and run firmware bytecode yourself.

## Caveats

The brief found no README or usage examples, and the site says nothing about macOS, so dumping tables on a Mac may not work and the tools may be most useful on saved table files.

## Links

- [GitHub repository](https://github.com/acpica/acpica)
- [ACPICA project site](https://www.acpica.org)
