---
name: mpremote
title: mpremote
source: brew
category: radio-and-hardware
commitment: quick
tags: [micropython, needs-hardware, python, quick, repl, serial]
homepage: https://docs.micropython.org/en/latest/reference/mpremote.html
scout_score: 5
status: draft
---

# mpremote

**TLDR;** A command-line tool that opens a Python prompt on a MicroPython board over USB serial, and copies files, runs scripts, and mounts folders.

mpremote talks to a MicroPython board over its serial connection. Run with no arguments, it finds the first USB serial device and opens the REPL, which is the board's live Python prompt and program output. Beyond that it takes subcommands to copy, list, edit and delete files on the device, run or evaluate code, install packages with mip, build ROMFS images, and reset the board.

The docs describe it as an integrated set of utilities to remotely interact with, manage the filesystem on, and automate a MicroPython device. It pulls the serial terminal, file transfer and reset steps, which developers otherwise handle with separate tools, into one command. Commands chain with a `+`, so one line can copy a file and then drop you into the REPL.

Two ideas make it more than a serial terminal. `run` sends a local script to the device and executes it from RAM, so nothing is written to the board's filesystem. `mount` installs a filesystem driver on the device that uses the serial link as a side channel, and your host directory appears on the board at /remote. You edit code on your computer and the microcontroller sees it as its own files.

That is a small, concrete way into a bigger idea: a tiny computer with no screen or keyboard that you drive entirely through one cable and a protocol layered on top.

## Install

```
brew install mpremote
# Needs a MicroPython board reachable over a serial port. Auto-detection only finds USB serial ports.
# Alternatives: pip install --user mpremote, or pipx install mpremote
```

## Try this

```
mpremote
```
Connects to the first USB serial device and opens the REPL.

```
mpremote exec "import micropython; micropython.mem_info()"
```
Runs that Python on the device and prints its memory report.

```
mpremote mount .
```
Mounts the current local directory on the device as /remote and opens a REPL with it as the working directory.

## What's unique

The mount command exposes a host folder to the board as its filesystem over the existing serial link, so you can iterate without copying files. The cp command borrows scp's colon convention for remote paths.

## Caveats

Needs a MicroPython board to be useful, and the docs warn there is no supported way to undelete files removed with `mpremote rm -r :`.

## Links

- [mpremote documentation (MicroPython latest docs)](https://docs.micropython.org/en/latest/reference/mpremote.html)
