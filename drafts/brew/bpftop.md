---
name: bpftop
title: bpftop
source: brew
category: take-things-apart
commitment: quick
tags: [ebpf, kernel, linux, monitoring, quick, tui]
homepage: https://github.com/jfernandez/bpftop
scout_score: 6
status: draft
---

# bpftop

**TLDR;** A top-style live table of the eBPF programs running inside your Linux kernel, with per-program runtime, event rate and CPU estimates.

bpftop lists every eBPF program currently loaded on a Linux machine, refreshed every second. Each row shows the program's ID, type and name, its average runtime, events per second and an estimated CPU percentage. Press Enter on a row and it opens time-series graphs for that program. It also shows which processes hold a reference to each program.

eBPF lets small programs run inside the kernel, attached to network hooks, tracepoints, security checks and more. Tools like tracers, load balancers and firewalls load them constantly, and normally you never see them. bpftop is a way to look at what is attached to your kernel right now and which of it is expensive.

The mechanism is the interesting part. The kernel keeps eBPF runtime statistics switched off by default because collecting them costs something. bpftop turns them on with the BPF_ENABLE_STATS syscall command and samples once a second. When it exits, it closes the file descriptor that command returned, and the kernel stops counting. In the README's words: "This tool minimizes overhead by enabling performance statistics only while it is active."

The project was formerly maintained by Netflix and is now an independent project maintained by Jose Fernandez. It is written in Rust.

## Install

```
curl -fsSL https://bpftop.sh/install | sh
# or: sudo dnf install bpftop / sudo pacman -S bpftop / nix profile install nixpkgs#bpftop
# Linux only, needs root to run. The binary links to libz and libelf at runtime.
```

## Try this

```
sudo bpftop
```
Opens the live table of loaded eBPF programs with a 1-second refresh. Press Enter on a row for graphs.

```
sudo bpftop -d 2
```
Same view, refreshing every 2 seconds (the delay accepts 1 to 3600).

```
journalctl _COMM=bpftop
```
Shows bpftop's own logs from the systemd journal.

## What's unique

It pays the cost of eBPF statistics only while it is open, then switches them off on exit. It also shows which processes reference each program, so you can see what is attached to the kernel.

## Caveats

Linux only, requires root, and full detail needs kernel 5.8 or later; it shows an empty table unless something has loaded eBPF programs, and the brew formula installs no executables listed here, so Linux install paths from the README are the safer route.

## Links

- [GitHub repository and README](https://github.com/jfernandez/bpftop)
- [Netflix announcement blog post](https://netflixtechblog.com/announcing-bpftop-streamlining-ebpf-performance-optimization-6a727c1ae2e5)
- [LWN.net article](https://lwn.net/Articles/963767/)
- [Fedora package](https://src.fedoraproject.org/rpms/bpftop)
