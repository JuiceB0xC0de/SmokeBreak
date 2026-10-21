---
name: freeipmi
title: FreeIPMI
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, bmc, ipmi, needs-hardware, network, protocol, servers]
homepage: https://www.gnu.org/software/freeipmi/
scout_score: 7
status: draft
---

# FreeIPMI

**TLDR;** GNU command-line tools for talking to a server's baseboard management controller: read sensors, event logs, power state, and serial console, locally or over the network.

FreeIPMI is a set of command-line tools and C libraries for IPMI v1.5 and 2.0, the management interface built into most server hardware. A baseboard management controller (BMC) is a small computer on the motherboard that stays alive when the host is off. FreeIPMI sends it requests and gets back sensor values, event records, hardware inventory, and configuration results.

It works in two ways. In-band, it talks to the BMC from the host OS through drivers. Out-of-band, it talks over the network using IPMI's LAN protocols, so a machine can be queried or power-cycled without any OS running. The homepage names the features most people want: "sensor monitoring, system event monitoring, power control, and serial-over-LAN (SOL)."

The toolset is split into many small programs, each with one job: `bmc-info`, `ipmi-sensors`, `ipmi-sel`, `ipmi-power`, `ipmiconsole`, `ipmi-dcmi`. There are also daemons such as `ipmiseld`, `ipmidetectd` and `bmc-watchdog`, and the project mentions support for large HPC and cluster environments. For programmers, matching libraries wrap sensor monitoring, SOL consoles and node detection, and a low-level libfreeipmi sits beneath them.

The interesting idea is the hidden second computer: a management plane that runs separately from the operating system and answers to a different protocol.

## Install

```
brew install freeipmi
# Useful output needs a BMC: either local access through a BMC driver on a server, or network access to one with LAN credentials.
```

## Try this

```
ipmi-sensors --help
```
Lists the options for reading temperature, voltage and fan sensors from a BMC.

```
bmc-info --help
```
Shows how to query a BMC for its identity and capabilities, locally or remotely.

```
ipmi-power --help
```
Shows the options for checking or changing a machine's power state through its BMC.

## What's unique

It covers in-band and out-of-band IPMI in one GNU toolset, with focused single-purpose tools, daemons for cluster nodes, and C libraries for building your own.

## Caveats

Without a server BMC or network access to one, there is little to see, and the homepage does not list supported platforms or build requirements.

## Links

- [FreeIPMI homepage](https://www.gnu.org/software/freeipmi/)
