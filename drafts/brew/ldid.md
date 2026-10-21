---
name: ldid
title: ldid
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, code-signing, entitlements, ios, mach-o, macos, reverse-engineering]
homepage: https://cydia.saurik.com/info/ldid/
scout_score: 8
status: draft
---

# ldid

**TLDR;** A small tool that signs Mach-O binaries and dumps their entitlements, showing how Apple's code signing works at the level of raw signature blocks.

ldid edits the code signature block inside Mach-O binaries, the executable format used on macOS and iOS. The homepage describes three modes: `-S` signs a binary from scratch and allocates its entitlements, `-s` updates the hashes on an existing signed binary, and `-e` dumps the entitlements.

Every signed Apple binary carries a blob that says what it is allowed to do. Entitlements are those permissions, and the signature block holds them alongside hashes of the code. Normally you only meet this through Apple's own tooling. ldid works on the block directly, so you can read it, rewrite it, and see what changes.

The homepage is a Cydia page, which suggests the original tool came out of the iOS jailbreak world, though the brief does not confirm that. The package installed by Homebrew appears to follow the ProcursusTeam fork, whose README lists changes: loading keys through PKCS#11, PKCS#12 keys with passwords, OpenSSL 3 support, and an `-arch arch_type` flag so you do not have to type the raw CPU type.

The project's own description is short: "This program lets you manipulate the signature block in a Mach-O binary." That smallness is the appeal. One tool, three flags, and a clear view of a mechanism most developers never look at.

## Install

```
brew install ldid
```

## Try this

```
ldid --help
```
Prints the tool's usage text so you can see which options your build supports.

```
ldid -e <binary>
```
Dumps the entitlements embedded in the given Mach-O binary.

```
ldid -S <binary>
```
Signs the binary from scratch and allocates its entitlements. Try it on a copy, not the original.

## What's unique

It works directly on the raw signature block in a few flags, so the whole sign, re-hash and inspect workflow fits in one short paragraph.

## Caveats

The documentation I could read is thin: the homepage lists three flags and the fork README is a changelog, so anything beyond `-S`, `-s`, `-e` and `-arch` needs `--help` or the source.

## Links

- [Homepage (Cydia)](https://cydia.saurik.com/info/ldid/)
- [ProcursusTeam fork (GitHub)](https://github.com/ProcursusTeam/ldid)
- [Original source repository](https://git.saurik.com/ldid.git)
