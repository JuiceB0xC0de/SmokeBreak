---
name: ipsw
title: ipsw
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, apple, firmware, ios, macos, needs-hardware, reverse-engineering]
homepage: https://blacktop.github.io/ipsw
scout_score: 7
status: draft
---

# ipsw

**TLDR;** A single command-line tool for downloading, unpacking and picking apart Apple firmware: dyld caches, kernelcaches, Mach-O binaries and more.

ipsw is a toolkit for researching iOS and macOS internals. It downloads IPSW and OTA firmware files, Xcode, macOS installers and kernel debug kits, then opens them up. Each area is a subcommand group: `download` and `extract` for firmware, `dyld` for shared caches, `macho` for binaries, `kernel` for kernelcaches, and `idev` for a connected device. Output is terminal text, with `--json` on commands that support it.

The README calls it an "iOS/macOS Research Swiss Army Knife". The homepage says it was built to be easy to install and use from an intuitive CLI, and credits Jonathan Levin's tools and iOS internals documentation as an influence.

The idea underneath is that Apple's operating systems ship as big, layered images, and most of what you think of as the system lives inside them. On modern Apple systems, system libraries are merged into a dyld shared cache. The README notes that you can use the cache directly for Objective-C analysis, because extracted dylibs can still reference metadata stored elsewhere in the cache. So the tool can dump class headers straight from the cache rather than from extracted files. Diffing two firmware builds shows what Apple changed between releases.

It can also disassemble a symbol, search a directory of binaries for a given import, and extract a single kernel extension by bundle ID. Optional LLM decompilation sends disassembly to a provider you configure when you pass `--dec`. An optional `ipswd` daemon exposes a REST API.

## Install

```
brew install ipsw
# the maintainer's tap includes the extras build:
brew install blacktop/tap/ipsw
# Linux: sudo snap install ipsw
# Windows: scoop bucket add blacktop https://github.com/blacktop/scoop-bucket.git, then scoop install blacktop/ipsw
# Most commands need a firmware file or binary to work on; the idev commands need a connected iOS device.
```

## Try this

```
ipsw download ipsw --device iPhone16,1 --latest
```
Downloads the latest IPSW for an iPhone 15 Pro.

```
ipsw extract --kernel /path/to/firmware.ipsw
```
Pulls the kernelcache out of a local IPSW.

```
ipsw class-dump /path/to/dyld_shared_cache_arm64e SpringBoardServices --headers -o headers
```
Writes Objective-C headers for SpringBoardServices from the cache into a headers directory.

## What's unique

It puts firmware download, diffing, dyld cache class-dumping, KEXT extraction and device access into one binary. It also ships an agent skill so tools like Claude Code can drive it in plain language.

## Caveats

Some commands depend on the host OS or build variant, Homebrew core and the maintainer's tap differ in extras, and building from source needs Go 1.26+ and CGO.

## Links

- [Homepage and docs](https://blacktop.github.io/ipsw)
- [Installation guide](https://blacktop.github.io/ipsw/docs/getting-started/installation)
- [Agent skill (ipsw-skill)](https://github.com/blacktop/ipsw-skill)
