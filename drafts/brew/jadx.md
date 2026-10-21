---
name: jadx
title: jadx
source: brew
category: take-things-apart
commitment: quick
tags: [android, decompiler, gui, java, quick, reverse-engineering]
homepage: https://github.com/skylot/jadx
scout_score: 6
status: draft
---

# jadx

**TLDR;** jadx turns Android APKs and Dex files back into readable Java source, with a command-line tool and a GUI for browsing the result.

jadx takes a compiled Android app and writes out Java source plus decoded resources. It accepts .apk, .dex, .aab, .xapk, .apkm, .apks and .zip files, and also plain Java .jar, .class and .aar files and .smali files. Binary resources are decoded too, so AndroidManifest.xml comes out readable rather than packed inside resources.arsc.

The idea underneath is that an app you install is not a sealed box. Android apps ship as Dalvik bytecode, and that bytecode keeps enough structure to be turned back into something that looks like the original code. Reading that output is a good way to see how a real app is put together: which permissions it asks for, how screens are wired, what it does at startup.

The command-line tool writes a directory of sources. The jadx-gui front end adds syntax highlighting, jump to declaration, find usages and full-text search, which makes a large app navigable. A deobfuscator is included for apps whose names have been scrambled, and jadx-gui has a smali debugger, with setup described on a wiki page.

The decompiler is honest about its limits. The README says that "in most cases jadx can't decompile 100% of the code, so errors will occur." Expect some methods to come out broken or as commented-out fallback code.

## Install

```
brew install jadx
# needs 64-bit Java 11 or later at runtime; the Homebrew formula depends on openjdk
```

## Try this

```
jadx --help
```
Lists every option, including the deobfuscation and renaming flags.

```
jadx -d out app.apk
```
Decompiles the APK and writes Java sources and decoded resources into the directory out. The brief shows this form with classes.dex; an .apk is an accepted input too.

```
jadx --log-level ERROR app.apk
```
Decompiles the APK and prints only error-level log output, which quiets the noise on big apps.

## What's unique

One tool covers APKs, app bundles, split packages, plain Java classes and smali, and also decodes binary resources. It ships both a command-line tool and a GUI with search, usage lookup and a smali debugger.

## Caveats

It cannot decompile everything; the README warns that errors will occur in most cases, and points to a troubleshooting wiki.

## Links

- [GitHub repository and README (homepage)](https://github.com/skylot/jadx)
- [jadx-gui features overview](https://github.com/skylot/jadx/wiki/jadx-gui-features-overview)
- [Troubleshooting Q&A wiki](https://github.com/skylot/jadx/wiki/Troubleshooting-Q&A)
