---
name: lziprecover
title: lziprecover
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, compression, data-recovery, error-correction, file-formats, lzip]
homepage: https://www.nongnu.org/lzip/lziprecover.html
scout_score: 5
status: draft
---

# lziprecover

**TLDR;** Repairs damaged lzip archives by using the format's built-in redundancy, and can rebuild one good file from several broken copies.

Lziprecover decompresses and tests files in the lzip (.lz) format, and tries to recover data from damaged ones. It can repair a flipped byte, merge several damaged copies into one good file, cut damaged members out of multimember files, and append a recovery record to a tar.lz archive. It also makes FEC files, which can protect any kind of file, not only lzip ones, and are offered as an alternative to par2.

The idea underneath is that a compressed stream can reveal where it broke. In lzip's LZMA stream, a match distance larger than the dictionary size is a forbidden symbol. When a bit flips, the decoder tends to hit one of these soon after, which narrows down where the damage is. The CRC and stored sizes then confirm whether a candidate repair is right. The author argues this is why automatic repair is practical for lzip, and writes: "It would be difficult to write an automatic recovery tool like lziprecover for the gzip format. And, as far as I know, it has never been written."

There are several modes. Byte-repair fixes up to one single-byte error per member. Merge mode rebuilds a correct file from the good parts of several damaged copies, which is why the author says compressed copies can be more useful redundancy than uncompressed ones. Reproduce mode regenerates a zeroed sector from a reference file, using the same lzip version that made the original. FEC data uses Galois fields GF(2^8) or GF(2^16).

The author frames it modestly: "Lziprecover is not a replacement for regular backups, but a last line of defense for the case where the backups are also damaged."

## Install

```
brew install lziprecover
# Reproduce mode also needs an lzip executable, of the same version that created the file.
```

## Try this

```
lziprecover --help
```
Lists the modes and options: repair, merge, reproduce, split, and FEC.

```
lziprecover -cd foo.tar.lz | tar -xf -
```
Decompresses a tar.lz archive to standard output and pipes it into tar to extract it.

```
lziprecover -cd --ignore-errors file.lz > file
```
Last-resort extraction: writes whatever is recoverable from a badly damaged file, possibly with garbage at the end of damaged members.

## What's unique

Most compressors fail completely on corruption. This one uses the lzip format's own structure to locate and fix errors, and can merge several damaged copies into one intact file.

## Caveats

Byte-repair handles only one single-byte error per member, it cannot help with total device failure, and the author says it is not a replacement for backups.

## Links

- [Lziprecover homepage](https://www.nongnu.org/lzip/lziprecover.html)
- [Online manual](https://www.nongnu.org/lzip/manual/lziprecover_manual.html)
- [Release downloads](http://download.savannah.nongnu.org/releases/lzip/lziprecover/)
