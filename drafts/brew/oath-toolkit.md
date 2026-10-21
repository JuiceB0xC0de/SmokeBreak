---
name: oath-toolkit
title: OATH Toolkit
source: brew
category: fundamentals
commitment: quick
tags: [authentication, cli, hotp, otp, protocol, quick, totp]
homepage: https://oath-toolkit.codeberg.page/
scout_score: 5
status: draft
---

# OATH Toolkit

**TLDR;** Command-line tools for generating and checking the HOTP and TOTP one-time codes behind everyday two-factor logins, so you can compute them yourself.

OATH Toolkit is a set of C libraries, command-line tools and a PAM module for building one-time password authentication systems. It implements HOTP (RFC 4226), the counter-based algorithm, and TOTP (RFC 6238), the time-based variant that most authenticator apps use. It also handles PSKC (RFC 6030), a standard container format for shipping secret keys around.

Two executables come with it. `oathtool` generates and validates one-time passwords. `pskctool` works with PSKC key containers. The homepage does not spell out exactly what each tool takes in and puts out, so check the man pages after installing.

The idea underneath is small enough to hold in your head. A shared secret and a counter, or the current time, go into a keyed hash, and a short number comes out. Your phone and the server each do this separately and compare results. Running the algorithm from a terminal turns a six-digit code that looks like magic into something you can reproduce. The PAM module shows how the same check plugs into a Unix login.

The project describes itself plainly: "OATH Toolkit provide components to build one-time password authentication systems." It is free software, with the libraries under LGPLv2+ and the tools under GPLv3+.

## Install

```
brew install oath-toolkit
```

## Try this

```
oathtool --help
```
Lists the options for generating and validating one-time passwords, including the choice between HOTP and TOTP modes.

```
pskctool --help
```
Shows what the PSKC key container tool can do.

## What's unique

It covers the whole stack in one package: the HOTP and TOTP algorithms, the PSKC key-container format, a command-line generator, and a PAM module for logins.

## Caveats

The homepage lists two security advisories (CVE-2026-109117 for 2.0.1 to 2.6.14, CVE-2024-47191 for 2.6.7 to 2.6.11), so make sure you have 2.6.15 or later, and it offers no usage examples.

## Links

- [OATH Toolkit homepage](https://oath-toolkit.codeberg.page/)
