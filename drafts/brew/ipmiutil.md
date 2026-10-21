---
name: ipmiutil
title: ipmiutil
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, bmc, ipmi, protocol, server-management]
homepage: https://ipmiutil.sourceforge.net/
scout_score: 6
status: draft
---

# ipmiutil

**TLDR;** A suite of 23 command-line tools for talking to the hidden management controller inside server hardware: sensors, event logs, power, and a remote serial console.

Many servers contain a second, small computer called a baseboard management controller. It runs whether or not the main machine is on, and it speaks IPMI, a standard protocol for out-of-band management. ipmiutil is a set of command-line tools that talk to it. Per the project, they read and set sensor values and thresholds, manage the System Event Log, open a serial-over-LAN console, and handle power control and related tasks.

The package installs 23 executables, each with a narrow job. Names like isensor, isel, isol, iuser, iwdt and ihealth cover sensors, event log, serial console, users, watchdog timer and a health check. ipmiutil itself is the main entry point. Output is plain text on the terminal.

The project calls itself "an easy to use set of IPMI server management utilities" and says it was formerly called panicsel. It also says that IPMI values it does not yet recognize are returned anyway, "rather than just 'na' or Unknown." It claims Linux can run driverless, which suits boot media and embedded environments, and that on Windows it uses native drivers.

The idea underneath is out-of-band management: a machine you can inspect, reset or watch from a console even when its operating system is hung or absent. The tools are a way in to that layer. Be aware that you need a machine with an IPMI controller to see anything real.

## Install

```
brew install ipmiutil
Needs a machine with an IPMI-capable management controller (typically server hardware), or network access to one, for most commands to return anything useful.
```

## Try this

```
ipmiutil --help
```
Prints the list of IPMI functions the main tool offers and its options.

```
isensor --help
```
Shows how to read sensor values and thresholds from the management controller.

```
isel --help
```
Shows how to view or manage the System Event Log.

## What's unique

It splits IPMI work into many small single-purpose tools, and the project says it runs natively on Windows and driverless on Linux. Both are the project's own claims.

## Caveats

Without IPMI hardware most commands have nothing to talk to, and I could not read a README, so the commands here are limited to --help.

## Links

- [Homepage](https://ipmiutil.sourceforge.net/)
- [SourceForge project page](https://sourceforge.net/projects/ipmiutil/)
