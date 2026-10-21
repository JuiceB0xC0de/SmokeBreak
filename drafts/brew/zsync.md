---
name: zsync
title: zsync
source: brew
category: fundamentals
commitment: quick
tags: [delta-transfer, http, network, protocol, quick, rsync]
homepage: https://zsync.moria.org.uk/
scout_score: 5
status: draft
---

# zsync

**TLDR;** Downloads a new version of a file over plain HTTP by fetching only the parts that changed from your old copy, with rsync's algorithm run on the client.

zsync is a file transfer program. You give it a small `.zsync` file and an older copy of the file you want. It works out which blocks you already have, then downloads only the missing ones from an ordinary web server.

The idea is to move the rsync algorithm to the client. Normally rsync makes the server compute checksums for every request, which is expensive when thousands of people download the same file. With zsync, the distributor runs `zsyncmake` once to produce a static `.zsync` file of precalculated checksums plus a simple text header. The client reads that and does the comparison itself. In the author's words, it "requires no special server software" and "imposes no extra load on the server."

The metadata file is plain and editable. It can point to a relative URL on the same server, or to one or more absolute URLs, so a third party could host a `.zsync` file that points back at the original site. The stated target is one big file on a server, such as an ISO image, going out to many downloaders who already hold a previous version.

The project dates from 2004 and never reached v1.0. The author does little active development now, but still reviews bug reports and pull requests.

## Install

```
brew install zsync
```

## Try this

```
zsync --help
```
Lists the client's options for fetching a file from a .zsync URL while reusing a local older copy.

```
zsyncmake --help
```
Shows the options for the distributor-side tool that builds a .zsync file from a file you already have.

## What's unique

The server does no rsync work at all. The checksums sit in a static file, so any plain HTTP server or shared hosting account can offer delta downloads.

## Caveats

It only helps when someone has already generated a .zsync file for the target, it never reached v1.0, directory transfer is not planned, and the 0.7 and 0.8 rewrites are less mature than 0.6.x.

## Links

- [zsync homepage](https://zsync.moria.org.uk/)
- [Download index (source tarballs)](https://zsync.moria.org.uk/download)
