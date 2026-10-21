---
name: libforensic1394
title: libforensic1394
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, dma, firewire, memory-forensics, needs-hardware, protocol, reverse-engineering]
homepage: https://freddie.witherden.org/tools/libforensic1394/
scout_score: 7
status: draft
---

# libforensic1394

**TLDR;** A C library with Python bindings that reads a running machine's physical memory over FireWire, using DMA, with nothing installed on the target.

libforensic1394 is a small library for live memory forensics over IEEE 1394, better known as FireWire. FireWire controllers can read and write another machine's physical memory directly (DMA), without the target's CPU or operating system taking part. The library wraps that capability in a simple C API, with Python bindings, so you can connect two machines with a cable and read memory from the running one.

The author describes it as a modern alternative to pythonraw1394, a Python wrapper around libraw1394. The main difference is native support for the newer "Juju" FireWire stack used by many GNU/Linux distributions. On Mac OS X it works through IOKit. The homepage says it improves on existing libraries by offering "a simple and clean interface to the the direct memory access functionality available over FireWire."

As the homepage gives it, the trick is that the library presents an SBP-2 unit directory to the remote device. SBP-2 is the protocol FireWire storage devices speak, so the target treats your machine as a disk and grants it memory access. A vectorised API takes advantage of the controllers' asynchronous capabilities. The author's own paper on the technique is the main source for the method.

The idea underneath is that a peripheral bus can be a path into memory, bypassing every protection the operating system provides. That is why it is useful for forensics, and why DMA attacks became a security topic. It is a way into hardware-level trust assumptions.

## Install

```
brew install libforensic1394
# Needs a FireWire (IEEE 1394) controller and a cable between two machines. The homepage does not state exact requirements. It lists a git repository and release 0.2 tarballs, built with CMake.
```

## Try this

## What's unique

It reads live physical memory through FireWire's DMA path, so the target needs no agent or software running on it. The API is small and clean for something so low-level.

## Caveats

The last release, 0.2, dates from 2010 and the page was last updated in 2015, so behaviour on current kernels is untested; it supports only GNU/Linux and Mac OS X, and you need FireWire hardware.

## Links

- [Homepage](https://freddie.witherden.org/tools/libforensic1394/)
