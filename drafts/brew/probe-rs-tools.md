---
name: probe-rs-tools
title: probe-rs
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, debugging, embedded, jtag, needs-hardware, rust, swd]
homepage: https://probe.rs
scout_score: 6
status: draft
---

# probe-rs

**TLDR;** A Rust toolkit that flashes, runs and debugs microcontrollers through a hardware debug probe, streaming the chip's log output back to your terminal.

probe-rs connects to a debug probe (CMSIS-DAP, J-Link, ST-Link, FTDI, ESP32 USB JTAG, Blackmagic and others), attaches to a named chip, and talks to ARM, RISC-V and Xtensa cores over SWD or JTAG. From there it can flash an ELF, BIN or IHEX file, reset the target, and stream RTT and defmt output and panics back to your console. As a library it can also read and write target memory, halt, step and set breakpoints. It includes a Debug Adapter Protocol server so editors such as VS Code can use it.

The brew package installs three executables: probe-rs, cargo-flash and cargo-embed. The README says that for most projects probe-rs run is the one to use, and that cargo-embed is expected to be phased out. The README describes the project as "a modern, embedded debugging toolkit, written in Rust".

The usual setup is to put probe-rs run in .cargo/config.toml as the Cargo runner. After that, cargo run flashes the chip and shows its logs, so firmware on a board feels like running a native program.

Underneath is the idea that every chip has a small debug port, and a probe can use it to stop the processor, read its memory and rewrite its flash. Flash algorithms and target descriptions come from CMSIS-Packs. The README also describes a Linux mode, through a plugin crate, where a board's own GPIO or spidev pins act as the SWD probe, so no dedicated probe is needed.

## Install

```
brew install probe-rs-tools
# Needs a supported debug probe and a target board. Building from source needs Rust via rustup. The README recommends a precompiled release and points to https://probe.rs/docs/getting-started/installation.
```

## Try this

```
probe-rs --help
```
Lists the subcommands for working with probes and chips.

```
probe-rs run --chip nRF52840_xxAA
```
Flashes the firmware, resets the target and streams RTT/defmt output; the README uses this as a Cargo runner.

```
cargo run
```
With the runner set in .cargo/config.toml, flashes and runs the firmware on the chip.

## What's unique

Set as a Cargo runner, it makes cargo run flash the chip and show its logs in one step. Target support comes from CMSIS-Packs, and a Linux board's own pins can serve as the probe.

## Caveats

It needs a debug probe and a target board to do anything useful, and the Linux GPIO/SPI probe mode needs hand wiring and udev setup.

## Links

- [probe-rs homepage](https://probe.rs)
- [GitHub repository (README)](https://github.com/probe-rs/probe-rs)
- [Installation guide](https://probe.rs/docs/getting-started/installation)
- [VS Code debugger setup](https://probe.rs/docs/tools/debugger)
