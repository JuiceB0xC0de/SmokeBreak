---
name: irrtoolset
title: IRRToolSet
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, bgp, network, protocol, routing, rpsl]
homepage: https://github.com/irrtoolset/irrtoolset
scout_score: 6
status: draft
---

# IRRToolSet

**TLDR;** Command-line tools for reading and analysing internet routing policies written in RPSL, the language networks use to publish who routes what in the Internet Routing Registries.

IRRToolSet works with routing policies stored in Internet Routing Registries (IRRs). These are public databases where network operators publish their routing intentions as text in the Routing Policy Specification Language (RPSL). The toolset installs three executables: `peval`, `rpslcheck` and `rtconfig`.

According to the README, the tools cover automated router configuration, routing policy analysis, and ongoing maintenance of routing information. The goal was to make routing information more convenient and useful for network engineers. The README does not describe what each executable takes in or puts out, so the `--help` output is the place to start.

The interesting part is the idea underneath. Routing between networks is a web of agreements, and RPSL is a way of writing those agreements down in a form a machine can read. Once policy is data, you can check it and generate router configuration from it. That is a door into how the internet's routing registries work.

The project is old and says so: "IRRToolSet has a long history and several parties hold copyright to various parts of IRRToolSet." It is also no longer actively maintained, which makes it more of a historical artefact than a daily driver.

## Install

```
brew install irrtoolset
# Building from source instead needs a GNU C++ compiler, libreadline, automake, autoconf, libtool, bison and flex.
```

## Try this

```
peval --help
```
Prints the usage text for peval, one of the three tools, so you can see what it expects.

```
rpslcheck --help
```
Shows the options for rpslcheck.

```
rtconfig --help
```
Shows the options for rtconfig, the tool for router configuration.

## What's unique

It is a tool built directly around RPSL and the IRR system, with a long history in network operations. The README itself sends you to BGPQ4 for everyday use.

## Caveats

The README states it is not actively maintained and recommends BGPQ4 as the maintained alternative; the code also carries a mix of licences and copyright holders.

## Links

- [Project homepage (GitHub)](https://github.com/irrtoolset/irrtoolset)
- [BGPQ4, the maintained alternative named in the README](https://github.com/bgp/bgpq4)
- [Mailing list subscription page](https://lists.isc.org/mailman/listinfo/irrtoolset)
