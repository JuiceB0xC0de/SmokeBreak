---
name: torf-cli
title: torf-cli
source: brew
category: take-things-apart
commitment: quick
tags: [bittorrent, cli, file-formats, protocol, python, quick, torrent]
homepage: https://github.com/rndusr/torf-cli
scout_score: 5
status: draft
---

# torf-cli

**TLDR;** A command-line tool that builds, inspects, edits and verifies .torrent files, so you can see exactly what is inside the metadata of a swarm file.

torf-cli reads and writes .torrent files and magnet URIs from the terminal. Point it at a directory and it builds a torrent, with trackers, a private flag and even a creation date of your choosing. Point it at an existing .torrent and it prints the name, info hash, size, trackers, piece layout, file list and magnet link. You can change a field such as the comment and write the result to a new file.

The README does not state a motivating problem. It presents the tool as a practical way to make, inspect and fix torrent files without a GUI client, with a configuration file for default options and profiles.

The interesting part is what a torrent file actually is: a small metadata dictionary, plus a list of hashes, one per piece of the content. Verification makes that concrete. Give torf a torrent and a path, and it compares the files against those hashes, then reports which files are wrong or which pieces are corrupt, down to a file that is one byte too large. When creating a torrent, it can also find an existing torrent with the same files and copy its piece hashes, so nothing has to be hashed again.

Output is meant for people, but `--json` and a raw metainfo dump (`-m`) make it easy to feed into jq or grep. That makes it a handy way to look at the bencoded structure underneath without writing a parser.

## Install

```
brew install torf-cli
# or, as the README recommends: pipx install torf-cli
# Needs Python; no account or hardware required.
```

## Try this

```
torf ./docs -t http://bar:123/announce -t http://baz:321/announce --private --date '2020-03-31 21:23:42'
```
Builds a private torrent from the ./docs directory with two trackers and a fixed creation date.

```
torf -i docs.torrent
```
Prints the torrent's name, info hash, size, trackers, piece layout, file list and magnet link.

```
torf -i docs.torrent -m
```
Dumps the raw metainfo dictionary as JSON, so you can see the structure the client reads.

## What's unique

Verification reports per-file errors and names the files covered by a corrupt piece. It can also reuse piece hashes from an existing torrent to skip rehashing.

## Caveats

The README gives no release dates and does not describe the configuration file format; editing writes a new file rather than changing the original in place.

## Links

- [GitHub repository (homepage)](https://github.com/rndusr/torf-cli)
- [Man page (HTML)](https://rndusr.github.io/torf-cli/torf.1.html)
- [PyPI package](https://pypi.org/project/torf-cli)
