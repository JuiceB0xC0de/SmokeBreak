---
name: dfu-programmer
title: dfu-programmer
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, atmel, dfu, firmware, microcontrollers, needs-hardware, usb]
homepage: https://github.com/dfu-programmer/dfu-programmer
scout_score: 7
status: draft
---

# dfu-programmer

**TLDR;** A command-line tool that flashes Atmel microcontrollers over USB using the DFU protocol, for chips that already carry a DFU bootloader.

dfu-programmer is the host side of a firmware update. You plug in an Atmel chip that is running a DFU-capable bootloader, and the tool talks to it over USB through libusb to load new firmware. The README lists supported families as 8051, AVR, AVR32 and XMEGA, with STM32F4 marked experimental.

It exists because, in the README's words, "the Atmel \"FLIP\" program for flashing devices does not support flashing via USB on Linux, and because standard DFU loaders do not work for Atmel's chips." It is built from Atmel's published specifications rather than from a generic DFU client.

The idea underneath is the bootloader. A chip that ships with a small piece of resident code can accept new programs over a plain USB cable, with no separate programmer hardware. Using this tool shows what a firmware update looks like from the host: the device announces itself as a DFU class device, the host erases and writes memory, and optionally validates it. Release notes mention a flash command with options such as --erase-first, --validate-first and --ignore-outside.

The README gives no flashing examples, so the program's own help output is the place to learn the command set.

## Install

```
brew install dfu-programmer
Requires libusb (installed as a dependency). To do anything useful you need an Atmel chip or board with a DFU bootloader, put into bootloader mode.
```

## Try this

```
dfu-programmer --help
```
Prints the supported targets and commands, which is the quickest way to see the command set the README leaves out.

## What's unique

It is a DFU client written specifically for Atmel's USB bootloaders, which generic DFU tools did not handle, and it covers several Atmel chip families in one program.

## Caveats

It needs real hardware with a DFU bootloader already installed, STM32F4 support is experimental, and the README gives no flashing examples.

## Links

- [GitHub repository (homepage)](https://github.com/dfu-programmer/dfu-programmer)
- [Project website](http://dfu-programmer.github.io)
- [Releases](https://github.com/dfu-programmer/dfu-programmer/releases)
