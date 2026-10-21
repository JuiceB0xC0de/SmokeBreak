---
name: shmcat
title: shmcat
source: brew
category: take-things-apart
commitment: quick
tags: [c, debugging, ipc, quick, shared-memory, unix]
homepage: https://shmcat.sourceforge.net/
scout_score: 6
status: draft
---

# shmcat

**TLDR;** A small C tool that dumps System V and POSIX shared memory segments to your terminal, like cat for memory shared between processes.

shmcat prints the contents of shared memory segments. It handles both flavours Unix offers: System V segments, created with shmget and attached with shmat, and POSIX segments, created with shm_open. It can also dump plain files and text, so several kinds of objects can be dumped in one run.

The project page says it is "a simple tool that dumps shared memory segments (System V and POSIX), files and text. It might be useful when you have to debug programs that use shared memory." That is the whole pitch, and it is a fair one. Shared memory is how processes pass data without copying it through a pipe or socket, and it is hard to see from outside. Most debugging tools look at one process at a time. shmcat looks at the region between them.

The idea underneath is that inter-process memory is an object the kernel names and tracks, separate from any program. Once you know that, you can start asking which segments exist on your machine, who made them, and what is in them. The package also ships an optional utility that calculates System V IPC keys with the ftok(3) library function, which shows how two unrelated programs find the same segment.

## Install

```
brew install shmcat
# Platform support is listed as Linux and FreeBSD; the page says it 'probably' works on other un*x systems.
```

## Try this

```
shmcat --help
```
Prints the usage text, which is the surest way to see the options this version supports.

## What's unique

Few tools look directly at inter-process shared memory. This one covers both System V and POSIX segments, and also accepts files and text as inputs.

## Caveats

The homepage is only a SourceForge project listing with no examples or docs, and the page says nothing about recent kernels or container shared memory.

## Links

- [shmcat homepage (SourceForge)](https://shmcat.sourceforge.net/)
- [SourceForge project page](https://sourceforge.net/projects/shmcat/)
