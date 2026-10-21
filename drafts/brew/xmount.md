---
name: xmount
title: xmount
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, disk-images, forensics, fuse, virtualization]
homepage: https://www.sits.lu/xmount
scout_score: 5
status: draft
---

# xmount

**TLDR;** Presents a forensic or virtual disk image as a different image format through a FUSE mount, so you can boot or inspect it without converting a copy.

Xmount takes a disk image in one format and exposes it as a file in another, on the fly. Inputs include Raw/DD, Expert Witness (EWF), AFFv3, VirtualBox VDI and QEMU QCOW2. Outputs include Raw/DD, Apple DMG, Microsoft VHD, VirtualBox VDI and VMware VMDK. It does this by mounting a FUSE virtual file system, so no full converted copy is written to disk.

Writes are supported too. Changes go to a separate cache file, and the original acquired image stays untouched. The stated use is booting acquired hard disk images in QEMU, KVM, VirtualBox, VMware or similar, which matters when the image is evidence and must not change.

On top of the same input handling sit morphing functions: Combine merges several input images into one output, Raid reconstructs RAID0 sets, and Unallocated extracts unallocated sectors from FAT or HFS filesystems. These make it a way into how disk images and their containers are laid out, and how a disk can be a layered, virtual thing.

The homepage gives no command lines or walkthrough, so expect to read the man page or the help output once it is installed.

## Install

```
brew install xmount
# needs a working FUSE setup to mount the virtual file system
```

## Try this

## What's unique

Few small tools read forensic containers like EWF and AFFv3 and also give writable, copy-on-write access to the result, with RAID reconstruction and image combining built in.

## Caveats

The homepage shows no version or release date, so maintenance status is unclear, and Homebrew lists no executables to run. Forensic containers are input-only, RAID support is RAID0 only, and unallocated extraction handles only FAT and HFS.

## Links

- [Xmount homepage (SITS Sarl)](https://www.sits.lu/xmount)
