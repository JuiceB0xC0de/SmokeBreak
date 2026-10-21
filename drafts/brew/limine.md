---
name: limine
title: Limine
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, bios, bootloader, osdev, secure-boot, uefi]
homepage: https://github.com/Limine-Bootloader/Limine
scout_score: 5
status: draft
---

# Limine

**TLDR;** A bootloader for x86, ARM and RISC-V machines, and a readable way into what happens between power-on and the first line of a kernel.

Limine is the program that runs when a machine powers on and loads an operating system kernel. You write a limine.conf, put its boot files where the firmware looks for them, and it starts Linux, a Multiboot 1 or 2 kernel, or a kernel that speaks the Limine boot protocol. It can also chainload other loaders. It targets IA-32, x86-64, aarch64, riscv64 and loongarch64.

The installation paths show how firmware finds code. On UEFI, the BOOT*.EFI files are copied into /EFI/BOOT on a FAT system partition. On BIOS, the host tool `limine bios-install` writes boot code into an MBR disk or a GPT BIOS boot partition. Limine can also be packed into a hybrid ISO that boots either way, or served over PXE. USAGE.md documents all of these in one place.

The README calls Limine the reference implementation of the Limine boot protocol, which is the handoff contract between bootloader and kernel. That makes it a practical starting point if you want to write a hobby kernel: the protocol spec is a separate document, and a bootloader implements the other side.

The security material is the unusual part. Secure Boot enforcement is opt-in and works by enrolling a hash of the config file. Measured Boot extends TPM PCRs 8 and 9 with the loaded artifacts, and the docs give the exact byte strings to hash so an outside verifier can recompute the values.

## Install

```
brew install limine
# Homebrew installs only the host tool, `limine`. Actually booting anything needs a disk image or a spare machine/VM, plus a limine.conf (format in CONFIG.md). Building a hybrid ISO also needs xorriso.
```

## Try this

```
limine --help
```
Lists the host tool's subcommands, so you can see what installation work it does.

```
limine bios-install image.iso
```
Writes BIOS boot code into a hybrid ISO that was built beforehand with xorriso.

```
b3sum --length 128 limine.conf
```
Produces the 128-byte BLAKE3 hash used to enroll the config for Secure Boot.

## What's unique

One document covers BIOS, UEFI, hybrid ISO and PXE installs. The Measured Boot scheme is specified down to the exact bytes hashed for each TPM PCR extend.

## Caveats

Filesystem support is limited to FAT12/16/32 and ISO9660, and with Secure Boot enabled any config hash mismatch panics and halts the machine with no return to the menu.

## Links

- [Homepage / GitHub repository](https://github.com/Limine-Bootloader/Limine)
- [USAGE.md (install and deployment guide)](https://github.com/Limine-Bootloader/Limine/blob/trunk/USAGE.md)
- [INSTALL.md (build and install)](https://github.com/Limine-Bootloader/Limine/blob/trunk/INSTALL.md)
- [Limine boot protocol spec (PROTOCOL.md)](https://github.com/Limine-Bootloader/limine-protocol/blob/trunk/PROTOCOL.md)
