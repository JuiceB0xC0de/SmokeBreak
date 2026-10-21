---
name: guile-fibers
title: guile-fibers
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, concurrency, guile, library, lisp, scheme]
homepage: https://codeberg.org/guile/fibers
scout_score: 5
status: draft
---

# guile-fibers

**TLDR;** A Guile Scheme library for lightweight fibers that talk over synchronous channels, built on the ideas of Concurrent ML.

Fibers adds cheap, Go-like concurrency to Guile Scheme. You start a fiber with `spawn-fiber`, run the whole thing inside `run-fibers`, and let fibers exchange values over channels using `make-channel`, `put-message` and `get-message`. The README's example is a client and a server swapping messages over two channels and printing what they receive.

The README describes it as providing "Go-like concurrency for Guile Scheme, in the tradition of Concurrent ML." That second half is the interesting part. Concurrent ML is a design from the Standard ML world in which channels are synchronous and first-class, and communication is something you can compose. Go borrowed part of that lineage. Here it is applied in a Lisp with a long history of experimenting with control flow.

There is no executable to run. The library is the thing, and the output is whatever your own Scheme program prints. That makes it a small way to learn how channel-based concurrency feels without leaving a REPL. The brief could not read the manual's contents or the README's account of internals, so how the scheduler works is left for you to find in the source and docs.

## Install

```
brew install guile-fibers
# Needs Guile. Homebrew also pulls in libevent and bdw-gc.
# Upstream ships no release tarballs. To build from source you need git, Autoconf, Automake and Libtool, and Guile 3.0.x or 2.2.x.
```

## Try this

```
git clone https://codeberg.org/guile/fibers
```
Fetches the source, including the README with the client and server channel example.

```
./env guile
```
Run from inside the cloned repo, this starts Guile with Fibers available from the source tree, with no install step.

```
autoreconf -vfi
```
Generates the configure script in a checkout, the first step of the README's build from a tagged release.

## What's unique

It is Concurrent ML brought to Guile rather than a plain Go imitation, with synchronous, first-class channels. The README's example is short enough to paste into a session.

## Caveats

Upstream provides no release tarballs, supports only Guile 2.2 and 3.0, and its contribution policy rejects LLM-generated contributions.

## Links

- [Homepage (Codeberg)](https://codeberg.org/guile/fibers)
- [Releases](https://codeberg.org/guile/fibers/releases)
- [Manual](https://doc.guix.gnu.org/fibers/latest/en/html_node/)
