---
name: apkid
title: APKiD
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, android, python, reverse-engineering, yara]
homepage: https://github.com/rednaga/APKiD
scout_score: 7
status: draft
---

# APKiD

**TLDR;** PEiD for Android: point it at an APK and it reports which compilers, packers and obfuscators were used to build and wrap the app.

APKiD takes an APK, a DEX file, or a directory and scans the contents with YARA rules. For each classes.dex it reports what it recognizes, such as the compiler (the README's example prints `|-> compiler : dx`), packers, obfuscators, and other traits. Output is plain text, JSON with `-j`, or files in a directory with `-o`.

The README describes it as "PEiD for Android", after the Windows tool that identified packers and compilers in PE executables. The author's stated uses are spotting pirated and malicious apps and fingerprinting AppShielding and mobile RASP SDKs.

The idea underneath is that an app is rarely shipped as it was compiled. Build tools leave marks, and protection tools leave their own. Matching those marks with signature rules shows how an app was wrapped before you open a disassembler. It also shows which protections you are about to run into.

The rule set is meant to grow. The README invites issues for unrecognized files and asks for ideas beyond packers, including anti-disassembler and anti-VM tricks. That makes the rules a small catalogue of how apps defend themselves.

## Install

```
brew install apkid
# Needs an Android APK or DEX file to scan. No account or hardware. Also available via `pip install apkid`.
```

## Try this

```
apkid --help
```
Prints the usage text: scan depth, timeout, recursion, typing mode, and JSON output options.

```
apkid path/to/example.apk
```
Scans the APK and prints the compilers, packers and obfuscators it recognizes for each classes.dex.

```
apkid -j path/to/example.apk
```
Prints the same findings as JSON, which is easier to feed into scripts.

## What's unique

It is modelled directly on PEiD and driven by YARA rules anyone can extend, so it works as a catalogue of how Android apps get wrapped, not only a compiler detector.

## Caveats

Detection is only as good as the rule set, so unknown packers go unrecognized until someone submits a sample, and the project's current maintenance status is unclear from the README.

## Links

- [GitHub repository](https://github.com/rednaga/APKiD)
- [PyPI package](https://pypi.org/project/apkid/)
- [Detecting Pirated and Malicious Android Apps with APKiD](http://rednaga.io/2016/07/31/detecting_pirated_and_malicious_android_apps_with_apkid/)
- [APKiD: Fast Identification of Mobile RASP SDKs (BlackHat USA Arsenal 2023 slides)](https://github.com/enovella/cve-bio-enovella/blob/master/slides/bheu23-enovella-APKID.pdf)
