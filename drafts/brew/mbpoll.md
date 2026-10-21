---
name: mbpoll
title: mbpoll
source: brew
category: radio-and-hardware
commitment: quick
tags: [industrial, modbus, needs-hardware, protocol, quick, serial]
homepage: https://epsilonrt.fr
scout_score: 6
status: draft
---

# mbpoll

**TLDR;** A command-line Modbus master that reads and writes registers on PLCs and sensors over serial or TCP, a way into the protocol factories run on.

mbpoll acts as a Modbus master from a shell. You give it a serial port or host name, a slave address, a table type and a start register. It sends the request and prints what comes back. With values after the device name it writes instead of reading. It covers discrete inputs, coils, input registers and holding registers, shown as decimal, hex, or 32-bit int and float.

Modbus is an old, simple request-and-reply protocol that sits inside a great deal of industrial equipment: meters, drives, PLCs, sensor boards. A device exposes numbered registers, and a master asks for them by address. Once you can poll one by hand, the protocol stops being mysterious. Its output format and option syntax are modelled on the proprietary modpoll tool, but the README says mbpoll is an independent GPL project with its own source.

By default it keeps polling at a set rate until Ctrl-C and prints frame statistics for each run. For RS-485 links, the RTS line can be used for direction control, optionally driven from a GPIO pin through piduino. That makes it a natural fit for a Raspberry Pi wired to a field device.

## Install

```
brew install mbpoll
# Needs a Modbus slave to talk to: a device on a serial adapter (RTU) or a host reachable over Ethernet (TCP). No account or licence key needed.
```

## Try this

```
mbpoll --help
```
Prints the option list, including the table type and format notation and the polling options.

```
mbpoll -a 33 -b 38400 -t 3 -r 1 -c 2 /dev/ttyUSB2
```
The README's example: reads input registers 1 and 2 from slave 33 over RTU at 38400 baud, polling repeatedly.

```
mbpoll -t4:int /dev/ttyUSB0 -- 123 -1568 8974 -12
```
Writes four values to holding registers as 32-bit ints. The -- keeps the negative numbers from being read as options.

## What's unique

One compact argument sets both table and format, such as -t 3:float, and address lists like -a 32,33,34,36:40 poll several slaves in one run. It also has RS-485 direction control through a GPIO pin.

## Caveats

You need a real or simulated Modbus device to see anything, RTU is serial-only, and the README says new feature work is going to a version 2 on libmodbuspp.

## Links

- [Homepage (author's blog, French)](https://epsilonrt.fr)
- [GitHub repository and README](https://github.com/epsilonrt/mbpoll)
- [Releases](https://github.com/epsilonrt/mbpoll/releases)
