---
name: afflib
title: AFFLIB
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, disk-images, file-formats, forensics, library]
homepage: https://github.com/sshock/AFFLIBv3
scout_score: 6
status: draft
---

# AFFLIB

**TLDR;** A C library and toolkit for the Advanced Forensic Format, an open disk-image container that carries its own metadata, signatures and encryption.

AFFLIB reads and writes the Advanced Forensic Format (AFF), a file format for storing a disk image together with its metadata. The command-line tools convert images between raw/dd, split raw, AFF, AFD (a directory of AFF files) and AFM (an AFF file that annotates a raw file). They also compare images, copy them with verification, print info and statistics, and emit XML metadata.

The interesting part is what the container holds besides the bytes. AFF can carry digital signatures and a chain-of-custody segment, so an image can describe where it came from and show that it has not changed. It also supports encryption that is applied and removed on the fly while the image is processed. The README says: "AFF allows for forensic disk images to stored encrypted and decrypted on-the-fly for processing." The stated aim is that privacy-sensitive images can be stored or shared, even over the Internet.

There is also a diskprint feature, which produces an XML fingerprint of a disk image without hashing the whole disk. Tools such as affuse, affcat and affinfo let you look inside a container, which makes this a practical way to see how an evidence format is laid out and how it differs from a plain dd file.

This is AFFv3, which the README says is in maintenance mode while AFFv4 is developed. The README says AFFv4 will be based on ZIP64 instead of the purpose-built container. AFF itself is described as "an open format unencumbered by copyright or patent protection."

## Install

```
brew install afflib
```

## Try this

```
affinfo --help
```
Shows usage for the tool that prints information about an AFF file.

```
affconvert --help
```
Shows how to convert images between raw and AFF formats.

```
fls -o 63 -i afflib foo.vmdk
```
Uses Sleuth Kit's fls (a separate install) with the afflib image type to list files in an image, with a partition offset of 63. This example comes from the README.

## What's unique

Forensic containers usually come from closed vendors. This one is open, with signatures, encryption and a chain-of-custody record built into the file.

## Caveats

AFFv3 is in maintenance mode while AFFv4 is developed, and the README gives no build instructions or recent activity dates.

## Links

- [Homepage (sshock fork)](https://github.com/sshock/AFFLIBv3)
- [Download source (simsong/AFFLIBv3, linked from README)](https://github.com/simsong/AFFLIBv3)
