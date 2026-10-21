---
name: ipmitool
title: ipmitool
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, bmc, hardware, ipmi, network, protocol, servers]
homepage: https://codeberg.org/IPMITool/ipmitool
scout_score: 5
status: draft
---

# ipmitool

**TLDR;** A command-line client for the BMC, the tiny second computer inside most servers that can power-cycle the machine and read its sensors even when the OS is down.

Most servers contain a second, smaller computer called the baseboard management controller, or BMC. It runs on standby power, has its own network path, and answers to a protocol called IPMI. ipmitool is a plain command-line client for it. It reads sensors, prints the System Event Log and FRU inventory, changes LAN settings, and controls chassis power. It reaches the BMC through the Linux OpenIPMI driver at /dev/ipmi0, or over the network using RMCP/RMCP+ packets on UDP port 623.

It began with Duncan Laurie at Sun Microsystems, with remote power control as the first goal. It grew into a general tool for administrators who like scriptable command-line utilities, and for people debugging or building their own BMC firmware. The README is clear about its limits: "ipmitool was not written to provide large-scale (aka Enterprise) management application functionality."

The idea underneath is that IPMI is just requests made of a network function, a command number and a payload. `ipmitool raw 6 4` sends command 4 in netfn 6, the self-test, and the BMC replies with bytes. `ipmitool mc selftest` is the same call with a readable answer. The README goes further than most into IPMB bridging, where requests hop through other controllers by address and channel, and it says plainly where that breaks.

The package also ships ipmievd, a daemon that listens for BMC events and writes them to syslog.

## Install

```
brew install ipmitool
# Needs real IPMI hardware (a BMC) to do anything useful.
# For the local interface on Linux: kernel modules ipmi_msghandler, ipmi_devintf and ipmi_si, plus /dev/ipmi0.
# LAN access (lanplus) needs OpenSSL, which brew pulls in.
```

## Try this

```
ipmitool --help
```
Lists the interfaces and top-level command groups such as chassis, mc, sensor, sel and fru.

```
ipmitool -I open shell
```
Opens an interactive ipmitool> prompt over the local OpenIPMI driver, where you can type commands like chassis status one at a time.

```
ipmitool raw 6 4
```
Sends the raw self-test command to the BMC. The README shows the reply as 55 00, which `ipmitool mc selftest` renders as 'Selftest: passed'.

## What's unique

It exposes IPMI at both levels: friendly subcommands and raw netfn/command bytes. Its README documents IPMB bridging with real addresses and admits where it fails.

## Caveats

You need actual IPMI hardware for anything useful. Serial is unsupported, CI only builds on Ubuntu and Fedora, and enabling IPMI-over-LAN can be risky on buggy BMCs or shared NICs.

## Links

- [IPMItool homepage (Codeberg)](https://codeberg.org/IPMITool/ipmitool)
- [IPMItool manpage (ipmitool.1.in)](https://codeberg.org/IPMITool/ipmitool/src/branch/master/doc/ipmitool.1.in)
- [Intelligent Platform Management Interface specification (Intel)](https://www.intel.com/content/www/us/en/servers/ipmi/ipmi-home.html)
