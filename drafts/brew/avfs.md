---
name: avfs
title: AVFS
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, ancient, archives, filesystem, fuse]
homepage: https://avf.sourceforge.net/
scout_score: 6
status: draft
---

# AVFS

**TLDR;** A virtual file system that lets ordinary programs open archives and remote locations as if they were directories, with no recompiling and no kernel changes.

AVFS presents the inside of an archive as a directory tree. Point it at a tar, gzip, zip, bzip2, ar or rar file, or a floppy image, and the contents become reachable through normal file access. The homepage also lists remote handlers: ftp, http, webdav, rsh/rcp and ssh/scp sessions. More handlers come through Midnight Commander's external FS.

The homepage states the goal in one sentence: "AVFS is a system, which enables all programs to look inside archived or compressed files, or access remote files without recompiling the programs or changing the kernel." The point is that the programs stay as they are. You do not need an `unzip` step or a special archive-aware tool. Whatever you already use to read files gets the ability.

The homepage notes that the shared library supporting AVFS with LD_PRELOAD is LGPL-licensed. That suggests the trick is to intercept file calls in a preloaded library, but the page does not explain the mechanism, so treat that as an inference. The Homebrew formula also depends on libfuse, which hints at a FUSE mount as another route.

The idea underneath is that an archive is just a naming scheme for files, and the file system interface is a good place to hide that. The homepage lists Pavel Machek's podfuk as a similar project.

## Install

```
brew install avfs

The formula depends on bzip2, libfuse and xz. It installs no executables on the path, so there is no command to run straight after installing. Expect to read the AVFS documentation for how to mount or preload it.
```

## Try this

## What's unique

It aims to give existing, unmodified programs access to archive and remote contents, rather than offering its own commands for extracting or browsing.

## Caveats

The homepage gives no release date, version, platform list or install steps, the formula installs no executables, and the project's maintenance status is unknown.

## Links

- [AVFS homepage](https://avf.sourceforge.net/)
