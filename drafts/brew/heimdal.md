---
name: heimdal
title: Heimdal
source: brew
category: fundamentals
commitment: days-off
tags: [authentication, days-off, gssapi, kerberos, network, pki, protocol]
homepage: https://github.com/heimdal/heimdal
scout_score: 5
status: draft
---

# Heimdal

**TLDR;** A free Kerberos 5 implementation whose bundled tools let you look at tickets, keytabs and credential caches, the machinery behind single sign-on.

Heimdal is an implementation of Kerberos 5, the network protocol in which a trusted server issues tickets so users and services can prove who they are without sending passwords around. The README describes it as an implementation of "ASN.1/DER, PKIX, and Kerberos", and the GitHub topics add gssapi, krb5-kdc and pki-library.

The brew formula installs a large set of command-line tools. The familiar ones are `kinit` (get a ticket), `klist` (list what you hold), `kdestroy`, `kpasswd`, `kadmin` and `ktutil`. Less obvious ones include `kgetcred`, `kswitch`, `hxtool`, `gsstool`, `string2key`, `otp` and `kf`. The README does not explain what these take in or produce, and says only that "There are man pages for most of the commands."

The README gives no stated motivation. What the brief does establish is that Heimdal is one of the two main free Kerberos 5 implementations, the alternative to MIT Kerberos. Reading its tools side by side is a way to see how tickets, keytabs and the credential cache fit together, which is a door into how authentication works on many corporate and university networks.

## Install

```
brew install heimdal
# Real use needs a Kerberos realm and a KDC to talk to. The brief found no first-run setup steps.
```

## Try this

```
kinit --help
```
Prints the options for requesting a ticket-granting ticket, the first step of Kerberos login.

```
klist --help
```
Shows how to list the tickets in a credential cache.

```
krb5-config --help
```
Shows the build and link information the installed Kerberos library reports to programs.

## What's unique

It is an independent second implementation of Kerberos 5, not MIT's, and it ships a wide set of small tools, including ones like `string2key` and `otp`, that expose individual pieces of the protocol.

## Caveats

The README is thin and defers to a wiki, the brief could not confirm recent activity, and doing anything real requires a Kerberos realm and KDC to talk to.

## Links

- [GitHub repository (homepage)](https://github.com/heimdal/heimdal)
- [Project site](https://heimdal.software/heimdal/)
- [Building and installing wiki](https://github.com/heimdal/heimdal/wiki/Building-and-installing)
- [Issue tracker](https://www.heimdal.software/heimdal/issues)
