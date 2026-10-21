---
name: vip
title: vip
source: brew
category: languages-and-oddities
commitment: quick
tags: [ancient, pipes, quick, shell, unix]
homepage: https://users.cs.duke.edu/~des/vip.html
scout_score: 5
status: draft
---

# vip

**TLDR;** A 1997 Bourne shell script that drops into the middle of a pipe so you can edit the stream by hand before it moves on.

vip is a small shell script, about 3 KB, that "provides for interactive editing in a pipeline." The homepage says it "can be used syntactically like a filter," so it goes between two commands in a pipe and takes whatever flows through it.

The idea underneath is a different way of building pipelines. Normally you write a pipeline, run it, look at the output, tweak a stage, and run it all again. vip puts a human in the middle of the stream. The author's 1997 ;login: article is titled "Toolman Edits Pipes -- Interactively!", and that title is about the only framing the homepage offers.

The homepage does not say what editor vip opens, what it emits, or what options it takes. The man page and article links did not load when checked, so the details are unverified. Treat it as a small, old artifact to read: a short shell script is easy to open and see how it works. It was written by Daniel E. Singer at Duke Computer Science, and the page was last updated 12/17/97.

## Install

```
brew install vip
```

## Try this

```
vip --help
```
Asks the script for usage. The homepage documents no options, so what this prints is unverified.

## What's unique

Most pipeline tools transform a stream automatically. vip is a filter that stops the stream so a person can edit it before it continues.

## Caveats

Documentation is thin, the man page and article were unreachable, and the page has not been updated since 1997, so behavior on current shells is unverified.

## Links

- [vip homepage (Daniel E. Singer, Duke CS)](https://users.cs.duke.edu/~des/vip.html)
