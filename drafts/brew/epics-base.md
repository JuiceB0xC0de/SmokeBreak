---
name: epics-base
title: EPICS Base
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, control-systems, network, physics, protocol]
homepage: https://epics-controls.org/
scout_score: 5
status: draft
---

# EPICS Base

**TLDR;** The control-system toolkit behind particle accelerators and telescopes, which runs as a soft IOC on your laptop so you can poke at it with no hardware.

EPICS (Experimental Physics and Industrial Control System) is a set of software tools for building distributed control systems that operate devices such as particle accelerators, large experiments and major telescopes. EPICS Base is the core of that toolkit. The homepage describes systems that can span tens or hundreds of networked computers, run from a central room or remotely.

The central piece is the IOC, the Input/Output Controller. An IOC serves named records over a network protocol called Channel Access, and clients read, write or subscribe to those names. The Homebrew formula installs both sides: server programs like `softioc`, and client tools like `caget`, `caput` and `camonitor`. A soft IOC is the same server running on an ordinary computer with no instruments attached, which makes it a way to see the model without a lab.

It exists so that labs do not have to build control infrastructure from scratch. Many networked computers need to communicate and give feedback, and EPICS supplies that layer. EPICS 7 adds a structured data system and a newer protocol, pvAccess, served by the `pv*` tools (`pvget`, `pvput`, `pvmonitor`, `pvlist`). The homepage says it enables applications that need higher abstraction.

The door here is the idea of a control system as named values on a network, with every device, sensor and setpoint addressable the same way. The README does not explain the record and database model in detail, so expect to lean on the documentation after the first example.

## Install

```
brew install epics-base
# Add to your shell configuration:
export EPICS_BASE=$HOMEBREW_PREFIX/opt/epics-base/libexec
export EPICS_HOST_ARCH=$($HOMEBREW_PREFIX/opt/epics-base/bin/EpicsHostArch.pl)
```

## Try this

```
softioc --help
```
Shows the options of the soft IOC server, which serves records over Channel Access without any hardware.

```
caget --help
```
Shows how to read the value of a named record from a running IOC.

```
pvget --help
```
Shows the pvAccess client, the EPICS 7 counterpart for fetching structured data.

## What's unique

It is control-system software with a long record at scientific facilities, and it runs as a software IOC on an ordinary machine. You can try the server side without a lab.

## Caveats

The tools are aimed at large distributed systems, so a small test works but the full feature set is heavy, and the README's own example builds from source rather than via Homebrew.

## Links

- [Official website](https://epics-controls.org/)
- [Documentation](https://docs.epics-controls.org/en/latest/)
- [Repository](https://github.com/epics-base/epics-base)
