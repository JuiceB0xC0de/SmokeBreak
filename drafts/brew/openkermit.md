---
name: openkermit
title: Open Kermit
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, file-transfer, protocol, retro, scripting, serial, tui]
homepage: https://www.openkermit.org/
scout_score: 6
status: draft
---

# Open Kermit

**TLDR;** C-Kermit, a serial and network communications package from 1981 with a built-in scripting language, file transfer protocol, and expect-style automation, still under active development.

Open Kermit is the current home of C-Kermit, a text-mode communications package. It bundles several things: an implementation of the Kermit file transfer protocol, a network client and server, a serial port interface, a BBS client, and a portable scripting language. The scripting language is described as "similar in concept to the shell, but with built-in screen-scraping automation like expect and built-in file transfer."

Kermit started at Columbia University in 1981. The homepage says Open Kermit is the third project to carry it forward, after the original Columbia effort and the Kermit Project. It was set up after one of Kermit's founders retired following 44 years. The earlier project sites are kept online as a historical snapshot, so the history can be browsed.

The idea underneath is that file transfer and terminal automation were once one problem, solved over unreliable serial lines between very different machines. Kermit is a protocol built for that world, and the same tool still talks to modern networks. The homepage claims it runs on hundreds of platforms, from 1970s computers and 1990s pocket calculators to current desktop and mobile systems. That claim is the project's own.

The Homebrew formula installs three executables: kermit, ckermit.ini, and kermit-sshsub. The homepage text does not describe inputs, outputs, or usage in detail, so the docs are the place to go after the first run.

## Install

```
brew install openkermit
```

## Try this

```
kermit --help
```
Prints the command-line usage summary for the kermit executable, a first look at what the program accepts.

## What's unique

It combines a file transfer protocol, serial and network terminal, and an expect-style scripting language in one package, with a lineage that runs unbroken from 1981.

## Caveats

The brief covers only the homepage, so usage examples, release dates, and the downloads page are unchecked.

## Links

- [Open Kermit homepage](https://www.openkermit.org/)
