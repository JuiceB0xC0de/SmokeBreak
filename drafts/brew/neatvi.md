---
name: neatvi
title: neatvi
source: brew
category: languages-and-oddities
commitment: quick
tags: [bidi, c, editor, quick, tui, utf-8, vi]
homepage: https://repo.or.cz/neatvi.git
scout_score: 5
status: draft
---

# neatvi

**TLDR;** A small vi/ex clone written in C, built to edit text that mixes right-to-left scripts like Farsi or Arabic with left-to-right text.

Neatvi is a modal editor with an ex command line, in the vi tradition. You pass it files on the command line, edit them in the terminal, and write them back. Its stated purpose is editing bidirectional UTF-8 text: files where right-to-left scripts such as Farsi or Arabic sit alongside left-to-right text.

The author, Ali Gholami Rudi, announced it in 2015: "I am writing Neatvi, a vi/ex editor for editing bidirectional utf-8 files." Most vi clones assume text runs left to right. Here the changelog shows the bidi focus, with commits on right-to-left handling such as adding a Persian letter to the CR2L table in conf.h.

The idea underneath is that a terminal editor has to decide how to order characters on screen, move the cursor through mixed-direction lines, and keep that consistent with what is stored in the file. A small codebase that takes this on directly is a good way to see how much a plain-text assumption hides.

It has also grown beyond that: tag commands (:tag, :tnext, :tprev, :pop), a gf command that opens the file under the cursor, extended registers, ex command history, and an LSP client for finding references and jumping to definitions. The author's news page suggests a trick: run git ls-files >ls, open ls in the editor, and use gf as a file explorer.

## Install

```
brew install neatvi
```

## Try this

```
neatvi --help
```
Prints whatever usage the binary offers; the repo README is one line, so this is a reasonable first look.

```
git ls-files >ls
```
Writes the repository's file list into a file named ls, the first step of the author's file-explorer workflow.

```
vi ls
```
Opens that list in the editor (the author's page writes vi; run it with neatvi). With gf, you can open the file whose path is under the cursor.

## What's unique

Most vi clones treat text as left-to-right. Neatvi exists specifically for bidirectional UTF-8 editing, and its commit history shows that focus.

## Caveats

The README is a single line and the author's neatvi page returns 404, so there is no easy usage or key-binding documentation to find online; expect to rely on vi knowledge.

## Links

- [Repository (homepage, git summary and README)](https://repo.or.cz/neatvi.git)
- [Author's project page (LITCAVE, news and Neatvi notes)](https://dev.rudi.ir/)
