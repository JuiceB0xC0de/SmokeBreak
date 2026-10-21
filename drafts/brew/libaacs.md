---
name: libaacs
title: libaacs
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, blu-ray, crypto, drm, library, reverse-engineering]
homepage: https://www.videolan.org/developers/libaacs.html
scout_score: 5
status: draft
---

# libaacs

**TLDR;** An open-source library implementing the AACS copy protection scheme used on Blu-ray discs, published as a research project for understanding how DRM and its crypto fit together.

libaacs implements the Advanced Access Content System (AACS) specification, the content protection scheme used on Blu-ray discs. Its homepage describes it as a research project that provides, in the project's words, "through an open-source library, a way to understand how the AACS works." The idea is that a protection scheme you can read as code is one you can study.

The project is not a decryption tool. The homepage says it offers no keys or certificates that could be used to decode encrypted copyrighted material, and it carries a legal disclaimer saying it does not infringe DRM rights or copyright. On its own, the library cannot unlock a disc. What it gives you is the structure of the system in readable form.

All cryptographic functions go through libgcrypt, the library's main dependency. The homepage does not explain the internals of the AACS implementation, so the code itself is where the learning is. The project also calls itself "a fun project to hack on, because it is DRM and crypto-related", which is an honest pitch: key hierarchies, licensing, and revocation are an unusual puzzle to read through.

Homebrew installs one executable, aacs_info. The homepage does not describe it, so what it takes as input and prints is not confirmed here. Start with its help output.

## Install

```
brew install libaacs
# depends on libgcrypt and libgpg-error, which brew pulls in
# Source alternative: git clone https://code.videolan.org/videolan/libaacs.git (build steps not confirmed)
```

## Try this

```
aacs_info --help
```
Prints the usage text for the one executable the formula installs, which is the quickest way to learn what it expects.

```
git clone https://code.videolan.org/videolan/libaacs.git
```
Fetches the library source from VideoLAN's GitLab so you can read how AACS is put together.

## What's unique

Most libraries in this space exist to play or rip media. This one presents itself as research and education, ships no keys or certificates, and treats the DRM as something to study.

## Caveats

It cannot decrypt discs by itself since it includes no keys, and what aacs_info does is undocumented on the homepage; maintenance status is unclear, with 0.12.0 named as the latest release but no dates found.

## Links

- [libaacs homepage](https://www.videolan.org/developers/libaacs.html)
- [Source repository (code.videolan.org)](https://code.videolan.org/videolan/libaacs)
