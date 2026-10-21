---
name: btfs
title: btfs
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, bittorrent, filesystem, fuse, network, protocol]
homepage: https://github.com/johang/btfs
scout_score: 6
status: draft
---

# btfs

**TLDR;** Mounts a .torrent file or magnet link as a read-only directory, so ls, cat and video players can read files that download from the swarm as they are opened.

btfs is a FUSE filesystem. You give it a .torrent file or a magnet link and an empty directory, and the torrent's contents show up as ordinary files there. The README says the data is downloaded on demand as applications read it, so nothing needs to be fetched in full before you start looking around.

The idea underneath is that a filesystem is a very old, very general interface, and almost every program already speaks it. Put a network protocol behind that interface and unmodified tools can use it with no knowledge of the protocol. The README says ls, cat and cp work as expected, and that players such as vlc and mplayer work without changes. Because reads drive what gets fetched, a player can begin a video before the whole file has arrived.

The README does not describe the internals. The dependency list names libtorrent-rasterbar and curl, which suggests libtorrent handles the swarm side, but that is an inference. The mount is read-only. Installing the formula also gives you `btfsstat` and `btplay`, which the brief does not document.

It is a small tool with a clear premise, and a good way to see what happens when a download stops being a task and becomes a place.

## Install

```
brew install btfs
# macOS also needs macFUSE: brew install --cask macfuse
# Debian/Ubuntu: apt-get install btfs
# Needs a FUSE implementation (FUSE 3 on Linux) and an empty directory to mount onto.
```

## Try this

```
btfs video.torrent mnt
```
Mounts the torrent onto the existing empty directory mnt, and its files appear there as read-only entries.

```
vlc video.mp4
```
Run from inside mnt, this plays a file straight from the mounted torrent, fetching pieces as vlc reads them.

```
fusermount -u mnt
```
Unmounts the directory and shuts down the btfs mount.

## What's unique

It turns a torrent swarm into a plain directory that unmodified programs can open, rather than a download you manage in a client.

## Caveats

The README gives no version or date, so how actively it is maintained is unclear, and the mount is read-only and needs FUSE (macFUSE on macOS).

## Links

- [BTFS GitHub repository (homepage and README)](https://github.com/johang/btfs)
