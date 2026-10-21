---
name: rvvm
title: RVVM
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, emulator, jit, operating-systems, risc-v, virtual-machine]
homepage: https://github.com/LekKit/RVVM
scout_score: 6
status: draft
---

# RVVM

**TLDR;** A RISC-V emulator with a tracing JIT that boots real operating systems like Linux, Haiku and the BSDs in a window, from one small binary.

RVVM emulates a RISC-V computer. You hand it a firmware image (the README's example uses OpenSBI plus U-Boot as `fw_payload.bin`), optionally a disk image, and some settings for memory, cores and display. It then boots the guest in a window with a framebuffer, a UART terminal, and keyboard and mouse input. The README says guests already include Linux, Haiku, FreeBSD and OpenBSD.

The project describes itself as emphasizing "performance, security, lean code and portability". The CPU runs through a tracing JIT with x86_64, ARM64 and RISC-V backends, which the README claims is faster than QEMU TCG. The README also lists an interpreter for RV64IMAFDC, and a `librvvm` library that the `rvvm` binary builds on. That library is MPL 2.0 and meant for embedding and writing new devices, while the front end is GPL 3.0.

The idea underneath is that an instruction set is just a contract, and an emulator is a small program that honors it. RISC-V is open and compact, so it is a good place to watch a foreign architecture boot: firmware hands off to a bootloader, which hands off to a kernel, all running on a machine that does not physically exist. There is also a work-in-progress userland mode for running single RISC-V programs on a different host architecture, with no guest OS.

## Install

```
brew install rvvm
# Needs sdl2-compat (pulled in by brew). To boot anything you must supply your own RISC-V firmware image (e.g. OpenSBI + U-Boot) and a guest disk image; the project wiki lists recommended ones.
```

## Try this

```
rvvm -h
```
Prints the help text listing the options for memory, cores, display, disks and networking.

```
rvvm fw_payload.bin -i drive.img -m 2G -smp 2 -res 1280x720 -portfwd tcp/127.0.0.1:2022=22
```
Boots a two-core, 2 GiB guest from firmware and a disk image in a 1280x720 window, forwarding host port 2022 to the guest's SSH port.

## What's unique

It aims to be a lean, portable RISC-V emulator whose tracing JIT the authors say beats QEMU TCG, and it ships an embeddable library for writing new devices.

## Caveats

Userland emulation and shadow pagetable acceleration are marked WIP, sound, USB XHCI and virtio devices are on the TODO list, and you must find your own firmware and guest images.

## Links

- [Homepage / GitHub repository](https://github.com/LekKit/RVVM)
- [Wiki (features, building, running)](https://github.com/LekKit/RVVM/wiki)
- [WASM demo](https://lekkit.github.io/test/index.html)
- [Nightly build artifacts](https://nightly.link/LekKit/RVVM/workflows/build/staging)
