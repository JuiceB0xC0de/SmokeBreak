---
name: ns-3
title: ns-3
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, network, research, science, simulation, wifi]
homepage: https://www.nsnam.org/
scout_score: 6
status: draft
---

# ns-3

**TLDR;** A discrete-event network simulator used in research and teaching, where you model Wi-Fi, cellular and Internet protocols in software instead of on real hardware.

ns-3 is a discrete-event network simulator for Internet systems. Its homepage says it is "targeted primarily for research and educational use." It is free, open-source software under GPLv2, maintained by a worldwide community.

The idea underneath is the discrete-event simulation. Instead of running real packets over real wires, the simulator keeps a queue of timestamped events, such as a packet being sent, a frame arriving, or a timer firing. It jumps from one event to the next. That lets you model networks you could never build at home and run them far faster or slower than real time, with repeatable results.

The model library is large and still growing. According to the release notes, ns-3.49 adds 3GPP TR 38.901 inter-UE spatial consistency, large-bandwidth and large-antenna-array modeling, and an 8-11x speedup of the 3GPP channel model. It also adds a Flent application, Wi-Fi IBSS beaconing, and 6LoWPAN and Zigbee additions. The Wi-Fi and 3GPP channel models are the standouts in a long list of protocol models.

The release is distributed as a source archive of the mainline code. A companion ns-allinone bundle adds compatible contributed modules. The pages the brief draws on do not describe what a typical run takes in or produces, so expect to start from the project's documentation and tutorials.

## Install

```
brew install ns-3
# The formula depends on open-mpi. Upstream also distributes source archives (mainline, and an ns-allinone bundle with contributed modules) from nsnam.org.
```

## Try this

## What's unique

It is a real research-grade simulator with a broad, actively developed library of protocol models, from Wi-Fi to 3GPP cellular to Zigbee, that you can run on your own machine.

## Caveats

The brew formula installs no executables, and the pages I read gave no first-run steps, so expect to work from the upstream documentation; contributed-module docs are hosted outside nsnam.org.

## Links

- [ns-3 homepage](https://www.nsnam.org/)
- [ns-3.49 release page (changes, errata, docs, download)](https://www.nsnam.org/releases/latest/)
