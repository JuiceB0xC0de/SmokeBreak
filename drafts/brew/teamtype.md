---
name: teamtype
title: Teamtype
source: brew
category: fundamentals
commitment: quick
tags: [collaboration, crdt, editors, local-first, peer-to-peer, quick]
homepage: https://teamtype.github.io/teamtype/
scout_score: 6
status: draft
---

# Teamtype

**TLDR;** Teamtype lets two people edit the same local text files in real time, peer to peer, from whichever editor each prefers, with no server or account.

Teamtype is a small daemon, `teamtype`, that syncs plain text files between machines. One person runs `teamtype share` in a directory and gets a short join code. The other runs `teamtype join` with that code in their own directory. From then on, edits flow both ways, and each side sees the other's cursor and selection. It works on whole directories, not just one file.

The files stay as ordinary files on disk, so you keep full access to them offline. This is the local-first idea: the network is a way to reconcile copies, not the place the document lives. The README credits Automerge, Iroh, and Magic Wormhole as the underlying pieces. Connections between peers are encrypted and need no server.

Editors do not need to know any of that. They talk to the local daemon over a simple JSON-RPC protocol, and a plugin only has to implement that. There are plugins for Neovim and VS Code/Codium, plus community ones for JetBrains, TeXstudio and others. The README pitches it as "the missing real-time complement to Git and other version control systems", aimed at pair programming, brainstorming and note-taking.

The project says it is not a company and has nothing to sell. It was funded by NLnet NGI0 Core in 2024 and the Prototype Fund in 2025. It was previously called Ethersync, so older talks and posts use that name.

## Install

```
brew install teamtype
# You also need an editor plugin: teamtype-nvim for Neovim, or the 'Teamtype' extension for VS Code/Codium.
# Make sure teamtype is on PATH when the editor launches. No account needed. Windows is supported only through WSL.
```

## Try this

```
teamtype share
```
Run in the directory you want to share. Prints a join code such as 5-hamburger-endorse and reports when a peer connects.

```
teamtype join 5-hamburger-endorse
```
Run in a separate directory, even on the same machine, with the code from the sharer. Stores the peer's address in .teamtype/config and connects.

```
teamtype --help
```
Lists the available subcommands and options.

## What's unique

It is peer to peer and editor-agnostic at once: no server, no account, and any editor with a plugin can join the same session.

## Caveats

The maintainers work on it in their free time and the README admits open bugs; joining overwrites any existing .teamtype/config in that directory, and Windows works only via WSL.

## Links

- [Teamtype Documentation (homepage)](https://teamtype.github.io/teamtype/)
- [GitHub repository and README](https://github.com/teamtype/teamtype)
- [FOSDEM 2025 talk (10 min)](https://fosdem.org/2025/schedule/event/fosdem-2025-4890-ethersync-real-time-collaboration-in-your-text-editor-/)
- [Editor plugin development guide](https://teamtype.github.io/teamtype/editor-plugin-dev-guide.html)
