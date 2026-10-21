---
name: ipapatch
title: ipapatch
source: brew
category: take-things-apart
commitment: quick
tags: [go, ios, ipa, mach-o, quick, reverse-engineering]
homepage: https://github.com/asdfzxcvbn/ipapatch
scout_score: 5
status: draft
---

# ipapatch

**TLDR;** A single Go binary that injects a dylib load command into the Mach-O binaries inside an iOS IPA, and into its plugins, with no external tools.

ipapatch takes an iOS app package (an IPA, which is a zip archive) and writes a patched copy. By default it injects zxPluginsInject, a rewrite of an earlier patch by Chocolate Fluffy. The README says the patch fixes problems with the share sheet, widgets, VPNs, and more. A `--dylib` flag swaps in a different dylib, and `--plugins-only` restricts the patching to plugin binaries and leaves the main executable alone.

The interesting part is how it patches. It adds a dylib load command directly to the Mach-O binary, using blacktop's ipsw and go-macho libraries, instead of calling out to an external injector. A Mach-O header contains a list of load commands that tell the loader which libraries to pull in. Adding one more entry to that list is how code gets into an app that never asked for it.

Since v2.0.0 it also handles the archive itself instead of shelling out to `zip`. The author describes dropping that dependency as a deliberate test of whether anything breaks. `--zip` remains as a fallback. The README's own claim is that it is "fully cross-compatible with macOS, linux, and iOS".

It is a small, readable project for seeing how app binaries are modified. Because it is plain Go over a documented format, you can follow the whole path from IPA to patched binary.

## Install

```
brew install ipapatch
# prebuilt binaries are also on the GitHub releases page. No runtime needed. You need an IPA file to patch.
```

## Try this

```
ipapatch --help
```
Prints the usage text and the list of flags.

```
ipapatch --input app.ipa --output app-patched.ipa
```
Injects the default zxPluginsInject dylib into the app's binaries and writes a new IPA.

```
ipapatch --input app.ipa --plugins-only --inplace
```
Patches only the plugin binaries and overwrites the input file with the result.

## What's unique

Load command injection is done natively in Go, so one binary with no external tools runs on macOS, Linux, and iOS.

## Caveats

The README does not cover installing or signing the patched IPA, which is left to you, and Windows is untested.

## Links

- [GitHub homepage and README](https://github.com/asdfzxcvbn/ipapatch)
- [Latest release binaries](https://github.com/asdfzxcvbn/ipapatch/releases/latest)
- [zxPluginsInject (default embedded dylib)](https://github.com/asdfzxcvbn/zxPluginsInject)
