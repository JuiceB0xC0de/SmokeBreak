---
name: ecl
title: ECL
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, common-lisp, compiler, embeddable, language, lisp]
homepage: https://ecl.common-lisp.dev
scout_score: 7
status: draft
---

# ECL

**TLDR;** A maintained Common Lisp implementation built to be embedded in other programs, with a REPL and a small config helper.

ECL is short for Embeddable Common-Lisp. The project's GitLab page calls it the "Embeddable Common-Lisp main repository" and lists the license as GNU LGPLv2.1. Brew installs two executables: `ecl`, the Lisp implementation itself, and `ecl-config`, which by its name reports configuration details for building against it.

The name points to the idea underneath it. Common Lisp is a large, old, standardized language, and an implementation meant to be embedded suggests a Lisp you can put inside another program instead of only running it on its own. The pages I could read do not spell out how that works, so treat the specifics as something to find out by poking at it.

The project is not new. Its release blog runs from 2005 to 2026, with recent releases 26.3.27 and 26.5.5. For a reader curious about Lisp, that makes it a long-running alternative to the better-known implementations, and a way into a language family with a very different feel from most modern tools.

## Install

```
brew install ecl
```

## Try this

```
ecl --help
```
Lists the command-line options for the ECL binary.

```
ecl-config --help
```
Shows what the configuration helper can report.

## What's unique

It is a Common Lisp that is named for, and aimed at, being embedded in other software. It also has a release history of roughly twenty years.

## Caveats

The README and manual were not reachable when this was written, so specific features, platform support and usage are unverified; the homepage is only a release blog.

## Links

- [Homepage (ECL blog and release news)](https://ecl.common-lisp.dev)
- [GitLab repository](https://gitlab.com/embeddable-common-lisp/ecl)
