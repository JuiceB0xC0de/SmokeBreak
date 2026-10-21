---
name: libewf
title: libewf
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, disk-images, file-formats, forensics, library]
homepage: https://github.com/libyal/libewf
scout_score: 5
status: draft
---

# libewf

**TLDR;** An open library and set of tools for reading, writing and verifying Expert Witness forensic disk images, the container format behind EnCase evidence files.

libewf is a C library for the Expert Witness Compression Format (EWF), the container used to store forensic disk images. It reads SMART .s01, EnCase .E01 and .Ex01 images, and reads (but does not write) logical evidence files, .L01 and .Lx01. The command-line tools are thin front ends to the library, each named after its job.

The tools cover the life of an evidence image. `ewfacquire` and `ewfacquirestream` take data from a device, file or stdin and write EWF files. `ewfinfo` prints the metadata, `ewfverify` checks the stored data, and `ewfexport` converts to split RAW or another EWF version. `ewfmount` exposes an image through FUSE, so it looks like a raw disk. `ewfrecover` is described as a "special variant of ewfexport to create a new set of EWF files from a corrupt set."

The idea underneath is that a disk image is not just a copy of bytes. An evidence container wraps the data with compression, hashes, case metadata and error records, so a copy can be verified later. The README mentions empty-block compression, delta or shadow files for read/write access, and write resume. Running the tools on an image is a practical way into how forensic containers are laid out, and the library gives other software open access to a format otherwise tied to one proprietary toolchain.

## Install

```
brew install libewf
# ewfmount needs FUSE support; on macOS the wiki points to OSXFuse. No account or runtime is needed.
```

## Try this

```
ewfinfo --help
```
Lists the options for printing an image's stored metadata.

```
ewfverify --help
```
Shows how to check an image's stored data against its recorded checksums.

```
ewfacquire --help
```
Shows the options for imaging a device or file into EWF files.

## What's unique

It is an open implementation of a forensic container format that is otherwise tied to a proprietary toolchain, and it reads the newer Ex01 and logical L01 variants. The tools are small and single-purpose.

## Caveats

The project labels itself experimental: Ex01 bzip2 compression and encryption are unsupported, L01 files are read-only, and `ewfdebug` "does nothing at the moment."

## Links

- [GitHub repository (homepage)](https://github.com/libyal/libewf)
- [Project documentation (wiki Home)](https://github.com/libyal/libewf/wiki/Home)
- [Building from source (wiki)](https://github.com/libyal/libewf/wiki/Building)
- [Previous stable releases (legacy)](https://github.com/libyal/legacy/tree/master/libewf)
