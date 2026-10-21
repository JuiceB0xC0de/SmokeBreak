---
name: stm32flash
title: stm32flash
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, bootloader, firmware, microcontroller, needs-hardware, serial, stm32]
homepage: https://sourceforge.net/projects/stm32flash/
scout_score: 5
status: draft
---

# stm32flash

**TLDR;** A small command-line tool that programs STM32 microcontrollers through the chip's built-in serial bootloader, using only a USB-serial adapter and no debug probe.

stm32flash writes firmware to STM32 ARM microcontrollers by talking to the bootloader ST programs into the chip at the factory. You point it at a serial device such as `/dev/ttyS0`, or an I2C device, and it sends the initial handshake. After that it issues bootloader commands to identify the chip, erase, write, read back and verify flash. It accepts Intel HEX or raw binary and detects which one it has been given.

The idea underneath is that a bare microcontroller is not a sealed box. Before any of your code runs, a ROM bootloader is waiting to be spoken to over a plain serial line. Once you see that, flashing stops being a vendor IDE feature and becomes a short conversation of bytes. It also works in reverse: you can read flash out to a file or to stdout, or jump to an address and start running.

Entering bootloader mode usually means holding the chip's boot pins in a certain state during reset. The `-i` option lets stm32flash do that for you by driving GPIO pins, or RTS and DTR lines on the serial adapter, in a sequence you describe. How well that works depends on how your board is wired.

The project was originally written by Geoffrey McRae and has been maintained by Tormod Volden since 2012. One SourceForge reviewer said ST's own STCubeProgrammer gave them trouble and stm32flash worked out of the box.

## Install

```
brew install stm32flash
# Hardware needed: an STM32 board plus a USB-serial adapter (or a UART/I2C connection) wired to the chip's bootloader pins.
```

## Try this

```
stm32flash /dev/ttyS0
```
Connects to the chip's bootloader on that serial port and prints device information.

```
stm32flash -r filename /dev/ttyS0
```
Reads the chip's flash contents into a file.

```
stm32flash -w filename -v -g 0x0 /dev/ttyS0
```
Writes a firmware file to flash, verifies it, then starts execution at address 0x0.

## What's unique

It uses the chip's own ROM bootloader over a plain serial line, so no ST-LINK or debug probe is needed. It is a small scriptable binary that can toggle boot and reset pins through GPIO or RTS/DTR.

## Caveats

It needs real hardware and correct wiring, entering bootloader mode is board dependent, and some USB-serial adapters are fiddly (the wiki has a Hints page for this).

## Links

- [SourceForge project homepage](https://sourceforge.net/projects/stm32flash/)
- [Wiki home (README text)](https://sourceforge.net/p/stm32flash/wiki/Home/)
- [GitLab mirror](https://gitlab.com/stm32flash/stm32flash)
- [Bug tracker](https://sourceforge.net/p/stm32flash/tickets/)
