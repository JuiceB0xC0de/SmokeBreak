---
name: gocryptfs
title: gocryptfs
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, cryptography, encryption, filesystem, fuse, go]
homepage: https://nuetzlich.net/gocryptfs/
scout_score: 5
status: draft
---

# gocryptfs

**TLDR;** An encrypted overlay filesystem that shows a folder of encrypted files as plain ones, and makes file-by-file encryption easy to look inside.

gocryptfs is a FUSE filesystem written in Go. You point it at a directory of ciphertext and a mountpoint, give it a password, and the mountpoint shows ordinary files. Underneath, each plaintext file is stored as exactly one encrypted file on disk. That ciphertext directory can sit on a USB stick or in a synced folder such as Dropbox.

The idea underneath is file-based encryption, as opposed to whole-disk encryption. Because files stay separate, a sync tool like rsync only has to move the files that changed, and the encrypted store grows with the disk instead of needing a fixed-size container. The project was inspired by EncFS and aims to fix its security problems while keeping good performance.

The design treats names and contents separately. Contents are encrypted in 4kB blocks with AES-GCM (or XChaCha20-Poly1305 if chosen at init), costing a small header per file and 32 bytes of overhead per block. File names use EME wide-block encryption with a per-directory IV, and the password goes through scrypt. Look at the ciphertext directory while it is mounted and you can see what an encrypted file tree looks like.

There is also a reverse mode. It takes an existing plaintext directory and presents an encrypted view of it, using deterministic AES-SIV, which suits backups. The full scheme is written up in a separate security design document on the project site.

## Install

```
brew install gocryptfs
Mounting needs FUSE working on your system (libfuse is a listed dependency). Linux is the native platform. No account or hardware is required.
```

## Try this

```
mkdir cipher plain
```
Creates an empty directory for the ciphertext and a mountpoint for the plaintext view.

```
gocryptfs -init cipher
```
Initialises an encrypted filesystem in cipher, asks for a password and prints the master key.

```
gocryptfs cipher plain
```
Mounts the encrypted directory at plain. Files you create there show up in cipher with scrambled names and contents.

## What's unique

It encrypts names and contents as separate layers and ships a reverse mode that exposes an encrypted view of a plain directory. Independent tools such as gocryptfs-inspect, cppcryptfs and DroidFS can also read the format.

## Caveats

Linux is the native platform, macOS support is described as beta-quality, and the project says to back up important data and keep the printed master key somewhere safe.

## Links

- [Homepage](https://nuetzlich.net/gocryptfs/)
- [GitHub repository](https://github.com/rfjakob/gocryptfs)
- [Security design document](https://nuetzlich.net/gocryptfs/security/)
