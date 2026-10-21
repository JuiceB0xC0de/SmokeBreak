---
name: vde
title: vde
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, ethernet, network, simulation, switch, tunnels, virtualization]
homepage: https://github.com/virtualsquare/vde-2
scout_score: 7
status: draft
---

# vde

**TLDR;** A software Ethernet switch you can plug processes, VMs and ssh tunnels into, so you can build and rewire a virtual LAN from the shell.

VDE, Virtual Distributed Ethernet, is a software Ethernet switch plus virtual cables. The `vde_switch` daemon listens on a UNIX control socket (default `/tmp/vde.ctl`) and forwards Ethernet frames between whatever is plugged into it. It can also run as a hub with `-hub`. The README puts the effect plainly: "All units connected to the VDE see each other as they were on a real ethernet."

The cable is the interesting part. `vde_plug` attaches a process's stdin and stdout to a switch, and a VDE cable is two plugs joined by a pipe. Shells have no way to wire two commands to each other in both directions, so VDE ships `dpipe`, a double pipe that feeds each command's stdout into the other's stdin. Swap one plug for `ssh remote_machine vde_plug` and the cable now runs across the network to a switch on another machine.

VDE was based on uml-router and was aimed at User-Mode Linux setups. The goal is to join many virtual machines and real hosts into one Ethernet-like network, even across several physical computers. A host tap interface can be bridged onto a switch, so the real machine joins the virtual LAN too.

There is also a mobility feature. Several cables can share a group number, so you can add a new path, drop the old one, and move a live network from eth0 to ppp0 without breaking the connections running over it. Along the way you learn how switches learn MACs, what a hub does differently, and why loops are dangerous.

## Install

```
brew install vde
# A tap-backed switch needs root. Remote cables need ssh or netcat on both ends. Host addressing needs ifconfig or iproute2.
```

## Try this

```
vde_switch /tmp/my.ctl
```
Starts a second switch on a custom control socket, without root.

```
dpipe vde_plug = vde_plug /tmp/my.ctl
```
Joins the default switch and the /tmp/my.ctl switch into one local cable.

```
dpipe vde_plug /tmp/my.ctl = ssh remote_machine vde_plug
```
Joins your local switch to a switch on a remote machine, with ssh carrying the cable.

## What's unique

The cable is just stdin and stdout, so any pipe, including ssh, can be an Ethernet cable. The bundled `dpipe` exists because shells cannot do two-way pipes.

## Caveats

The README's copyright lines stop at 2011 and it shows no recent activity. It says spanning tree is not implemented, so a loop in your topology can corrupt forwarding tables and saturate the network.

## Links

- [VDE 2 repository and README](https://github.com/virtualsquare/vde-2)
