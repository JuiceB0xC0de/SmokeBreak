---
name: apktool
title: apktool
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, android, apk, java, reverse-engineering, smali]
homepage: https://apktool.org
scout_score: 5
status: draft
---

# apktool

**TLDR;** Takes a compiled Android app apart into readable resources and smali code, then rebuilds your edited folder back into a working APK.

Apktool is a command-line tool for reverse engineering closed, binary Android apps. Give it an APK and it writes out a project-style folder: the manifest and resources decoded to nearly their original form, and the app's code disassembled into smali, a human-readable assembly for Android's Dalvik bytecode. Files it does not recognise are copied across as they are.

The interesting part is the round trip. After decoding, you can edit a string, swap an image, or change a smali instruction, then run the build command. It reassembles the smali into classes.dex, rebuilds the resources, and packages a new APK. The README gives localizing an app or adding features as examples of why someone would want this. The project says it can also help you step through smali code while debugging.

That makes it a door into how Android apps are put together. An APK is a zip of compiled code, binary-encoded XML and assets, and seeing it laid out as plain files shows what the build tools normally hide. There is also an analyze option: adding -m to a decode skips the rebuild step and just unpacks resources and manifest for inspection.

The README says Apktool is not intended for piracy or other non-legal uses, and closes with a plea: "Just try to be fair with the authors of an app, that you use and probably like."

## Install

```
brew install apktool
# pulls in openjdk as a dependency; you need an APK file of your own to try it on
```

## Try this

```
apktool d test.apk
```
Decodes test.apk into a folder named test holding the manifest, decoded resources and smali code.

```
apktool b test
```
Rebuilds the decoded folder test into a new APK.

```
apktool --help
```
Lists the available commands and options.

## What's unique

Unlike a plain decompiler that only lets you read, it aims to round-trip: decode, change resources or smali, and rebuild a working APK from the same project-style folder.

## Caveats

Decoding is "nearly original" rather than exact, so rebuilt output may differ from the source, and the project asks that it not be used for piracy.

## Links

- [Project homepage](https://apktool.org)
- [Documentation](https://apktool.org/wiki/the-basics/intro)
- [Source (GitHub)](https://github.com/iBotPeaches/Apktool)
- [Downloads mirror](https://connortumbleson.com/apktool)
