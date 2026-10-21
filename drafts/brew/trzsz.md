---
name: trzsz
title: trzsz
source: brew
category: fundamentals
commitment: quick
tags: [file-transfer, protocol, quick, ssh, terminal, tmux]
homepage: https://trzsz.github.io
scout_score: 5
status: draft
---

# trzsz

**TLDR;** trz and tsz move files through your existing SSH terminal session, like rz/sz, but they work inside tmux, where the old tools do not.

trzsz is a pair of commands, `trz` to upload and `tsz` to download, that run on the remote machine inside an ordinary terminal session. There is no second scp or sftp connection to set up. The local terminal or wrapper catches the transfer and shows a progress bar with file name, size, speed and time remaining.

The author built it for chains like laptop -> hostA -> hostB -> docker -> tmux, where scp and sftp are awkward. lrzsz handles this sort of hop, but not under tmux. The README quotes it plainly: "tmux is not going to support rz / sz ( 906, 1439 ), so trzsz ( trz / tsz ) was developed."

The idea underneath is old: file transfer carried in-band, over the same byte stream as your keystrokes, which is what the rz/sz family does. The brief does not describe trzsz's wire protocol, so read the README before assuming details. What it does show is the practical layer. The local end has to cooperate, so you use tssh, `trzsz ssh`, iTerm2 through `trzsz-iterm2`, tabby, electerm, ttyd, or a web terminal via trzsz.js.

It also supports directories (`-d`), resuming from a breakpoint when you overwrite an existing file (`-y`), binary mode, control-character escaping, and tunable chunk size and timeout.

## Install

```
brew install trzsz
# This installs trz, tsz and trzsz-iterm2. The remote machine needs trzsz too (Go version recommended; pip, npm or brew also work).
# The local side needs a supported terminal or wrapper such as tssh, iTerm2 with trzsz-iterm2, or `trzsz ssh`. No account needed.
```

## Try this

```
trzsz ssh x.x.x.x
```
Logs in through the native trzsz wrapper, so trz and tsz work without a special terminal. Replace x.x.x.x with your host.

```
trz -d
```
Run on the remote side, it uploads files and directories from your local machine into the remote current directory.

```
tsz -y xxx
```
Downloads xxx from the remote machine, overwriting an existing local copy and resuming from the breakpoint if the file is partly there.

## What's unique

It fixes a specific gap: moving files in-band under tmux, which tmux has declined to support. The README says it works in normal tmux mode and with iTerm2's tmux -CC integration.

## Caveats

Plain ssh in an unsupported terminal will not work, since the local end must be trzsz-aware, and the brief could not confirm release recency.

## Links

- [Homepage](https://trzsz.github.io)
- [GitHub repository and README](https://github.com/trzsz/trzsz)
- [Go version install guide](https://trzsz.github.io/go)
- [iTerm2 trzsz integration](https://trzsz.github.io/iterm2)
