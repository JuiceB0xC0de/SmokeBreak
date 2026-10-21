---
name: gmssl
title: GmSSL
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, crypto, sm2, sm3, sm4, standards, tls]
homepage: https://github.com/guanzhi/GmSSL
scout_score: 6
status: draft
---

# GmSSL

**TLDR;** A C crypto library and gmssl command-line tool implementing China's national cryptography standards (SM2, SM3, SM4, SM9, ZUC), a different crypto lineage from the usual AES and RSA.

GmSSL is an open-source cryptography toolkit written in C. It implements the Chinese national commercial cryptography algorithms, often called guomi or GM: SM2 for public-key work, SM3 for hashing, SM4 for block encryption, SM9 for identity-based crypto, and ZUC for stream encryption. It also covers X.509 certificates, CSRs, CRLs, PEM and PKCS #8 keys, SM2 digital envelopes, and some post-quantum signature schemes. You reach it through a `gmssl` command-line tool or the libgmssl C library.

It also speaks the protocols built on those algorithms: TLCP (GB/T 38636-2020), TLS 1.2, and TLS 1.3 with the RFC 8998 SM4-GCM-SM3 suite. The README says the project exists so that products can pass Chinese cryptographic product certification. It supports Chinese crypto hardware too, namely SDF PCI-E cards and servers and SKF USB keys. A SoftSDF sub-project provides a software stand-in for development.

The idea underneath is that cryptography is also standardised nationally, and the algorithms most Western developers know are one lineage among several. GmSSL lets you hash, sign and encrypt with the other one and compare how it is put together. Version 3 was rewritten from scratch. It can be configured to include only the national algorithms, avoids dynamic memory allocation, and is meant to run on bare-metal microcontrollers. Its TLS stack is a state machine that supports non-blocking mode.

## Install

```
brew install gmssl
```

## Try this

```
gmssl --help
```
Lists the subcommands the CLI offers, a starting map of the SM algorithms and certificate tools it exposes.

## What's unique

Few open-source libraries cover the whole Chinese national suite, including TLCP and the RFC 8998 TLS 1.3 suite, as a cross-platform package with a CLI. An OpenSSL compatibility layer lets Nginx 1.16 to 1.25 run on it.

## Caveats

The README is in Chinese and gives no CLI usage examples, so expect to explore with --help; GmSSL 3 is not API-compatible with OpenSSL, and recent activity could not be confirmed from the README.

## Links

- [GmSSL homepage (GitHub)](https://github.com/guanzhi/GmSSL)
- [SoftSDF (software SDF module)](https://github.com/GmSSL/SoftSDF)
- [OpenSSL-Compatibility-Layer](https://github.com/GmSSL/OpenSSL-Compatibility-Layer)
- [GmSSL-Python (ctypes binding)](https://github.com/GmSSL/GmSSL-Python)
