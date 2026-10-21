---
name: powerman
title: powerman
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, datacenter, needs-hardware, network, pdu, power]
homepage: https://github.com/chaos/powerman
scout_score: 5
status: draft
---

# powerman

**TLDR;** Remote, parallel control of switched power distribution units, driven by expect-style scripts that teach it new hardware. A look at how clusters get power-cycled.

powerman turns a rack of switched power distribution units (PDUs) into something with names you can address. You give it devices and actions such as on, off or cycle. It sends them to the hardware in parallel over telnet, raw sockets or serial lines, or through coprocess plugins for other protocols.

It began as cluster work at Lawrence Livermore National Laboratory in 2002. The README says it was designed for "remote power control of Linux systems in a data center or cluster environment". It also says it has been used in embedded management appliances, home automation and high availability service management.

The idea underneath is the physical layer of operations. When a machine hangs hard, someone has to cut its power, and that someone is usually a script talking to a box with a telnet prompt. powerman hides the differences between those boxes. Each device is described in an expect-like scripting language, so new hardware can be supported without changing the core. The README says the coprocess interface has reached SNMP, IPMI, Insteon and Redfish.

The executables list suggests a `powermand` daemon with client tools such as `powerman` and `pm`, plus helpers like `httppower`, `plmpower` and `redfishpower`. The README does not say how they fit together, so check the docs before assuming.

## Install

```
brew install powerman
# Real use needs a switched PDU or another power-control device reachable over network or serial. Without one you can only read the help output.
```

## Try this

```
powerman --help
```
Prints the client's options, the quickest way to see what actions and targeting it offers.

```
powermand --help
```
Shows the daemon's options, which hints at how devices are configured and served.

```
redfishpower --help
```
Shows the helper that handles Redfish, one of the protocols powerman reaches through coprocesses.

## What's unique

Telnet, serial, SNMP, IPMI, Insteon and Redfish devices all sit behind one naming and parallel-execution layer. New devices are added by writing expect-like scripts rather than changing the core.

## Caveats

Useful only with real power-control hardware, and the README gives no first-run guide, commands or maintenance status.

## Links

- [GitHub repository (homepage)](https://github.com/chaos/powerman)
