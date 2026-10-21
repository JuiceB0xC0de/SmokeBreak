---
name: ad
title: ad
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [acme, afternoon, editor, modal-editing, plan9, rust, tui]
homepage: https://github.com/sminez/ad
scout_score: 5
status: draft
---

# ad

**TLDR;** A Rust text editor that pairs vi and kakoune style modal editing with Plan 9 Acme's idea that text on screen can be executed.

ad (pronounced A.D.) is a terminal text editor written in Rust. Its editing model comes from vi and kakoune: modes, selections, motions. Its approach to extending itself comes from Plan 9's Acme, where you run external programs from inside the editor instead of writing plugins in an embedded language. The README puts it as text being something you can execute as well as edit.

The command language is the interesting part. ad implements the core of the sam editor's language, structural regular expressions, and has since split that out into its own crate called structex. Structural regexes describe edits as a pipeline over regions of text, which is a different way of thinking about search and replace. The editor also carries its own character-stream regex engine, a gap buffer, tree-sitter highlighting with a regex fallback, and a minimal LSP client.

The other half of the Acme idea is the outside door. ad exposes its state through a virtual filesystem (fsys, built on its own 9p implementation), so external programs can drive the editor through a simple protocol. The stated aim is "a comfortable editing environment to work in that supports direct interaction with external tools and programs from the outside rather than pulling everything in."

The author is explicit that this is a playground. It is not trying to replace vim, kakoune or emacs, just to be a small editor that can be hacked on.

## Install

```
The Homebrew formula is listed, but the README says packaging with default config files is not in place and recommends building from source with a Rust toolchain: `git clone git@github.com:sminez/ad.git && cd ad && cargo install --path .` Then optionally run `cargo xtask setup-dotfiles`, after reading what it does in xtask/src/setup.rs, since it writes config files.
```

## Try this

```
ad --help
```
Lists the command line options of the editor.

```
cargo xtask setup-dotfiles
```
Run from the cloned repo, it sets up default config files. The README asks you to review its actions first.

```
:help
```
Typed inside ad, not the shell, it opens the built-in help, which is the main user documentation.

## What's unique

Instead of a plugin language, ad makes text executable in the Acme style and uses a self-implemented sam-style structural regex language for commands, all built largely from scratch on purpose.

## Caveats

The README says ad is a playground, not recommended as a primary editor, with little documentation beyond :help, likely bugs and crashes, and keybindings that may change.

## Links

- [ad homepage (GitHub repo and README)](https://github.com/sminez/ad)
- [Video tour of ad (YouTube, may be out of date)](https://www.youtube.com/watch?v=jb2pAi5hLUg)
- [structex: the extracted sam-style structural regex engine](https://github.com/sminez/structex)
