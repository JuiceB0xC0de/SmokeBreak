---
name: micropython
title: MicroPython
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, embedded, language, microcontroller, needs-hardware, python]
homepage: https://www.micropython.org/
scout_score: 6
status: draft
---

# MicroPython

**TLDR;** A real Python 3 interpreter small enough for microcontrollers, with a REPL that runs on about 16k of RAM and talks to pins, buses and timers.

MicroPython is an implementation of Python 3 written in C99 with no external dependencies. It has an interactive prompt, closures, generators, exceptions and arbitrary-precision integers, and it fits in roughly 256k of code space and 16k of RAM. On a board, it can run and import scripts from an on-device filesystem.

The interesting part is the `machine` module and its siblings. They expose GPIO, timers, ADC, DAC, PWM, SPI, I2C, CAN, Bluetooth and USB as ordinary Python objects. The project's stated aim is a "bare-metal feeling: one should feel like they have complete control over the system, with very little between the programmer and the physical world."

The design leans on a split between source and bytecode. The `mpy-cross` tool precompiles scripts to `.mpy` files, which can be loaded from the filesystem or frozen into the firmware so they take no RAM. Each target (ESP32, RP2040/RP2350, STM32, nRF, SAMD, plus Unix and Windows) is a separate port that supplies the hardware-specific code.

The Homebrew formula gives you the Unix build and the cross-compiler. That is a small, odd Python you can run on your laptop to see what a stripped-down interpreter looks like, and a first step toward flashing a board.

## Install

```
brew install micropython
# Installs the `micropython` executable and the `mpy-cross` cross-compiler.
# The Unix build runs on your laptop. To touch real hardware you need a supported board (ESP32, RP2040, STM32, pyboard and others) and its firmware port.
```

## Try this

```
micropython --help
```
Lists the options of the Unix build of the interpreter. Run it with no arguments to get the REPL.

```
mpy-cross --help
```
Shows the options of the cross-compiler that turns .py scripts into precompiled .mpy bytecode.

## What's unique

It is a full Python interpreter, not a dialect or a macro layer, squeezed into a few kilobytes of RAM and given direct access to hardware peripherals. The project lists over twenty ports across three support tiers.

## Caveats

It implements only a subset of Python 3 (Python 3.4 syntax plus some later features), hardware modules differ by port, and the interesting part needs a physical board.

## Links

- [Homepage](https://www.micropython.org/)
- [Online documentation](https://docs.micropython.org/)
- [GitHub repository](https://github.com/micropython/micropython)
- [MicroPython store (pyboard)](https://store.micropython.org/pyb-features)
