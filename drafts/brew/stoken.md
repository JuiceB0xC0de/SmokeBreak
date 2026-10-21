---
name: stoken
title: stoken
source: brew
category: fundamentals
commitment: quick
tags: [needs-token, protocol, quick, securid, two-factor]
homepage: https://github.com/stoken-dev/stoken
scout_score: 5
status: draft
---

# stoken

**TLDR;** An open-source reimplementation of the RSA SecurID software token that turns a seed into the six-digit login codes, from the command line.

stoken generates tokencodes compatible with RSA SecurID 128-bit (AES) tokens. You import a token once, either as a raw seed string or from an sdtid XML file, and each later run derives the current one-time code from that seed. `--next` shows the code after it. The project also ships a GTK+ GUI, `stoken-gui`, and a shared library, `libstoken`, that other programs can call.

The README presents it as a Linux and UNIX alternative to the proprietary RSA software token. It names blind and other disabled users as people it helps get past hurdles in login systems. It also says plainly that it is a hobbyist project, not affiliated with or endorsed by RSA Security.

The idea underneath is that a hardware-flavoured, proprietary-looking second factor is a shared secret plus the clock, and a small program can do the same job. Reading how the import, the optional password on the seed, and the optional PIN fit together shows what a token actually holds. Because libstoken exists, tools like OpenConnect can link against it and send the generated code as the password, so the token stops being a separate app.

## Install

```
brew install stoken
# You also need a token to import: a seed string or an .sdtid file from your own account.
```

## Try this

```
stoken import --file mytoken.sdtid
```
Imports a token from an sdtid XML file and prompts for an optional password to encrypt the seed on disk.

```
stoken tokencode
```
Prints the current tokencode, asking for a PIN if the token requires one.

```
stoken tokencode --next
```
Shows the next code in the sequence.

## What's unique

It reimplements a proprietary two-factor token scheme as a small open tool, and it also exposes a library so programs like OpenConnect can generate codes themselves.

## Caveats

You need a real token seed to do anything, the Windows build is labelled experimental, caching a PIN in ~/.stokenrc is explicitly less secure, and I could not confirm how recently it has been maintained.

## Links

- [Project homepage (GitHub README)](https://github.com/stoken-dev/stoken)
