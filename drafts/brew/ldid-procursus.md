---
name: ldid-procursus
title: ldid-procursus
source: brew
category: take-things-apart
commitment: quick
tags: [code-signing, ios, mach-o, macos, quick, reverse-engineering]
homepage: https://github.com/ProcursusTeam/ldid
scout_score: 7
status: draft
---

# ldid-procursus

**TLDR;** A command-line tool that signs Mach-O binaries with a real key or a fake signature, a direct way to see how iOS and macOS code signing works.

ldid puts signatures into Mach-O binaries, the executable format used by macOS and iOS. It can sign with a real key, or it can fake-sign, which attaches a signature without any trusted certificate chain behind it. The Procursus fork installs two executables, `ldid` and `ldid2`.

The README for this fork is a list of changes from Saurik's original ldid, not a usage guide, and it states no motivation. The listed changes include manpages in English, Traditional Chinese, and Simplified Chinese, OpenSSL 3 support, p12 keys with passwords, key loading through PKCS#11, a `-arch arch_type` flag so you do not have to type the raw CPU type, and clearer errors.

The idea underneath is that a signature on an Apple binary is a separate, inspectable piece of data that the system checks. A tool that can write one with or without a trusted chain lets you poke at what is enforced and what is not. Fake signing is the interesting part: it shows how much of the check is about a signature being present and well-formed versus who issued it.

Because the README shows no full invocations, the manpages and source are the place to learn the real workflow.

## Install

```
brew install ldid-procursus
# Depends on libplist and openssl@3, which brew installs. Real signing needs a key (a p12 file, or a PKCS#11 token); the README does not say how to set this up.
```

## Try this

```
ldid --help
```
Prints the tool's usage so you can see which signing and inspection options this build offers.

```
ldid2 --help
```
Shows the usage for the second installed executable, so you can compare it with ldid.

```
man ldid
```
Opens the manpage this fork added, the best written reference since the README has no examples.

## What's unique

It can fake-sign Mach-O binaries, which makes code signing enforcement something you can experiment with directly. This fork adds PKCS#11 key loading and manpages in three language variants.

## Caveats

The README has no usage examples or install steps, and the upstream source was unreachable when checked, so confirm behaviour from the manpages or source; project status is unclear.

## Links

- [GitHub repository (ProcursusTeam/ldid)](https://github.com/ProcursusTeam/ldid)
- [Upstream ldid git (Saurik), unreachable during this read](https://git.saurik.com/ldid.git)
