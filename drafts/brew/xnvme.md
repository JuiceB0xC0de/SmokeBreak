---
name: xnvme
title: xNVMe
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, c-library, io_uring, needs-hardware, nvme, storage, user-space]
homepage: https://xnvme.io/
scout_score: 5
status: draft
---

# xNVMe

**TLDR;** One C API and a set of command-line tools for talking to NVMe drives from user space, with the I/O backend picked at runtime.

xNVMe is a C library, libxnvme, plus tools built on it, for programming NVMe storage devices from user space on Linux, FreeBSD, macOS and Windows. The API covers DMA-capable memory allocation, synchronous and asynchronous command submission, and queries for device geometry and parameters. The tools (`xnvme`, `lblk`, `zoned`, `kvs`, `xdd`) are command-line front ends for the NVM, Zoned and key-value command sets.

The idea underneath is a plumbing problem. Each platform offers several ways to reach a drive: io_uring, io_uring_cmd, libaio or block IOCTLs on Linux, native drivers elsewhere, SPDK, or a user-space PCIe driver called uPCIe. The README puts the cost as n platforms times m I/O interfaces, and aims to "reduce your code-complexity from n * m ... to 1." The backend is chosen at runtime, so the same application code runs unmodified across them.

The README also describes `homi`, a daemon it calls "the software equivalent of SR-IOV", which lets several host processes and accelerator compute kernels run I/O directly against one NVMe controller. There is also a Fio IO engine for benchmarking, and a ublk server called `qublk` so kernel file systems can coexist with the user-space drivers.

This is a door into how storage I/O works below the file system: queues, command sets, zoned namespaces and what each kernel interface costs you.

## Install

```
brew install xnvme
# Using the tools needs access to a real NVMe device; the README does not describe the privileges required.
```

## Try this

```
xnvme --help
```
Lists the subcommands of the main tool for talking to NVMe devices.

```
zoned --help
```
Shows the tool for Zoned Namespace devices.

```
lblk --help
```
Shows the tool for logical block (NVM command set) operations.

## What's unique

One C API hides very different I/O paths (io_uring, libaio, SPDK, a user-space PCIe driver) and picks one at runtime. The homi daemon, which shares one controller among processes and accelerator kernels, is an unusual idea for a user-space library.

## Caveats

Real use needs NVMe hardware, and the README does not state supported hardware or kernel versions; the brief did not verify the first-run steps or any command examples.

## Links

- [Documentation homepage](https://xnvme.io/)
- [GitHub repository (README)](https://github.com/xnvme/xnvme)
- [Releases (v0.7.5 latest)](https://github.com/xnvme/xnvme/releases)
- [Python package on PyPI](https://pypi.org/project/xnvme)
