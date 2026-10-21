---
name: gzrt
title: gzrt
source: brew
category: take-things-apart
commitment: quick
tags: [compression, file-formats, forensics, gzip, quick, recovery]
homepage: https://www.urbanophile.com/arenn/coding/gzrt/gzrt.html
scout_score: 6
status: draft
---

# gzrt

**TLDR;** gzrecover skips past the damaged bytes in a corrupted .gz file and saves whatever it can still read, where gunzip gives up at the first error.

gzrecover is the one program in the gzip Recovery Toolkit. It reads a damaged gzip archive, from a file or from standard input, and skips over bad data. What it manages to read goes into a new file with a `.recovered` suffix (any `.gz` is stripped), or to standard output with `-p`. Run with `-v`, it reports where it found bad bytes.

The author wrote it after a backup restore failed. Bad sectors had corrupted the archive, and gzip stopped about 10% of the way through. In the README's words, "gzip craps out 10% of the way through your archive." Most of the backup was lost, and gzrecover is the attempt to get the rest back. The README does not describe the internal algorithm. A scout note says it scans deflate streams, but that is not confirmed by the README.

The idea underneath is that a compressed file is a chain of dependent pieces, so one flipped bit can wreck everything after it for a normal decompressor. A tool that tolerates the damage and keeps going shows how those formats fail and how much is still recoverable.

For tarballs there is a two-step chain. Run gzrecover first, then hand the `.recovered` file to GNU cpio, because GNU tar rejects format errors that cpio tolerates.

The output is not guaranteed to be good. The README says plainly that "Everything should be manually verified."

## Install

```
brew install gzrt
# installs the gzrecover executable
# for recovered tarballs, GNU cpio 2.6 or higher is also needed
```

## Try this

```
gzrecover my-corrupted-backup.tar.gz
```
Scans the damaged archive and writes whatever it can read to my-corrupted-backup.tar.recovered next to the input.

```
cpio -F my-corrupted-backup.tar.recovered -i -v
```
Extracts files from the recovered tar stream with GNU cpio, which tolerates format errors that GNU tar rejects.

```
cpio --version
```
Checks that GNU cpio is installed and at version 2.6 or higher, which the tarball workflow needs.

## What's unique

Instead of giving up at the first error like gunzip, it skips past the damage and keeps whatever it can read. It pairs with cpio for tarballs, which gives a practical recovery chain for broken backups.

## Caveats

The latest release is 0.8 from 2013, and the author warns the output is likely to include some bad data, so everything must be checked by hand; it also gets slower the more corrupt the file is.

## Links

- [gzrt homepage (author's page)](https://www.urbanophile.com/arenn/coding/gzrt/gzrt.html)
