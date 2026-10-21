---
name: dps8m
title: DPS8M
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [36-bit, afternoon, ancient, mainframe, multics, simulation]
homepage: https://dps8m.gitlab.io/
scout_score: 9
status: draft
---

# DPS8M

**TLDR;** A simulator of the 36-bit Honeywell/GE mainframes built to run Multics, so you can run software for hardware almost nobody has touched.

DPS8M simulates the 36-bit GE Large Systems / Honeywell / Bull 600/6000-series mainframes. Specifically it covers the Honeywell 6180, the Series-60 / Level-68, and the DPS-8/M. It runs on an ordinary host machine and emulates the hardware, so software written for those mainframes can run on it.

The reason this lineage matters is Multics. The homepage says these machines are "descended from the GE-645 and engineered to support the Multics operating system." The simulator exists to keep that family of machines runnable, long after the physical hardware went out of service.

The formula installs four executables: `dps8`, the simulator itself, plus `prt2pdf`, `punutil` and `tap2raw`. The names suggest helpers for printer output, punched cards and tape images, which fits the era. The brief did not include usage details for them, so treat that as a guess from the names.

The idea underneath is a machine with 36-bit words, from before the 8-bit byte became universal. Running it shows you a different architecture that you can actually use, not just read about. The homepage also mentions a hardware DPS-8/M and FNP project on FPGA, underway as of 2024.

## Install

```
brew install dps8m
```

## Try this

```
dps8 --help
```
Prints the simulator's command-line options, a first look at how it is driven.

## What's unique

A working emulator of a 36-bit Honeywell mainframe is rare, and this one targets the hardware family built for Multics.

## Caveats

The README just points to the project wiki and the brief found no build or first-run steps, so expect to read the wiki before anything boots.

## Links

- [DPS8M homepage](https://dps8m.gitlab.io/dps8m/)
- [GitLab repository](https://gitlab.com/dps8m/dps8m)
