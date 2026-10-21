---
name: net-snmp
title: Net-SNMP
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, monitoring, network, protocol, snmp]
homepage: http://www.net-snmp.org/
scout_score: 7
status: draft
---

# Net-SNMP

**TLDR;** The reference toolkit for SNMP, the protocol routers, printers and UPSs use to report their state: query devices, receive traps, or run your own agent.

Net-SNMP is a suite of command-line tools, a trap receiver daemon, an extensible agent daemon, a Tk/Perl MIB browser, and C and Perl libraries. It implements SNMP v1, v2c and v3 over IPv4 and IPv6. The request tools such as `snmpget`, `snmpwalk` and `snmpset` talk to a device and read or change its management data. Other tools translate between numeric OIDs and their textual MIB names.

SNMP is, in the homepage's words, "a widely used protocol for monitoring the health and welfare of network equipment (eg. routers), computer equipment and even devices like UPSs." It runs quietly on a huge amount of hardware, and most people never see it. This suite is a way to look at what those devices are willing to say about themselves.

The package covers both ends of the conversation. `snmptrapd` receives notifications and can log them to syslog or a text file, forward them elsewhere, or hand them to an external program. `snmpd` is an agent that answers queries, so your own machine can become something SNMP can ask questions of. It can be extended with loadable modules, external scripts, SMUX or AgentX.

The idea underneath is the MIB: a shared, tree-shaped naming scheme where every measurable thing on a device has a numeric address. Learning to walk that tree is learning how network monitoring systems see the world.

## Install

```
brew install net-snmp
# The MIB browser (tkmib) needs Tk and Perl. Querying a device needs one that speaks SNMP, or you can run snmpd locally.
```

## Try this

```
snmpget --help
```
Shows the options for fetching a single value from an SNMP device, the simplest request the suite makes.

```
snmpwalk --help
```
Shows how to walk a device's whole tree of management data, the usual way to see what it exposes.

```
snmptranslate --help
```
Shows how to convert between numeric OIDs and readable MIB names, a good first look at the naming tree.

## What's unique

It is both halves of SNMP in one package: the polling tools, the trap receiver and an agent you can extend with scripts or modules. It also supports both the older SMUX and newer AgentX extension protocols.

## Caveats

The homepage warns that functionality varies by operating system, and the MIB browser needs Tk and Perl.

## Links

- [Net-SNMP homepage](http://www.net-snmp.org/)
