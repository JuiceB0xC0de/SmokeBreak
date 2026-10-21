---
name: badkeys
title: badkeys
source: brew
category: take-things-apart
commitment: quick
tags: [crypto, keys, math, quick, security, ssh, tls]
homepage: https://badkeys.info
scout_score: 6
status: draft
---

# badkeys

**TLDR;** Checks public keys, certificates and live SSH or TLS hosts against known cryptographic weaknesses, from the Debian OpenSSL bug to ROCA to leaked vendor keys.

badkeys takes public keys in several formats: PEM PKCS #1 and PKCS #8 keys, X.509 certificates, certificate signing requests and SSH public keys. It detects the format itself and checks each key against a list of known flaws. It can also connect to hosts and check the keys they present. A web version at badkeys.info does the same with pasted keys.

The checks go beyond a mathematical sanity test. They include the Debian OpenSSL bug, common prime factors shared between keys, ROCA, Fermat factorization, Wiener's small private exponent attack, and several vendor-specific flaws. It also flags discouraged choices such as DSA keys and unusual RSA exponents or key sizes. The homepage's success stories point at real finds: printer firmware RSA keys, and certificates using ROCA-vulnerable keys or OpenSSL test keys.

The idea underneath is that a key can look perfectly valid and still be broken, because of how it was generated or because someone already has its private half. Two RSA keys that share a prime can be factored by anyone holding both. A key in a public blocklist is compromised no matter how good its math is. badkeys is a way to see how keys go wrong in practice.

By default it prints nothing for a clean key, and only reports vulnerable ones. The exit code is a bitmask: 4 means a vulnerable key was found, 2 means some input could not be scanned.

## Install

```
brew install badkeys
badkeys --update-bl

The blocklist data has to be downloaded with --update-bl before the first scan. SSH scanning needs the paramiko Python package as an extra dependency. The README's own route is pip3 install badkeys, ideally in a virtual environment.
```

## Try this

```
badkeys --update-bl
```
Downloads the blocklist data that the checks need before the first scan.

```
badkeys test.crt my.key
```
Scans a certificate and a key file, detecting each format automatically. It prints nothing if both are clean.

```
badkeys -ts example.org
```
Connects to the host, scans the keys it presents over TLS and SSH, and reports any that are vulnerable.

## What's unique

Most key checkers only test the key's mathematics. badkeys also includes a community-maintained blocklist of compromised private keys, and its web page has a 'Fill with test data' button that loads sample keys for each weakness.

## Caveats

The README says the Python API is in beta and may change regularly, and TLS scanning cannot see multiple certificates on one host, such as ECDSA and RSA together.

## Links

- [badkeys.info (web version)](https://badkeys.info)
- [GitHub repository](https://github.com/badkeys/badkeys)
- [PyPI package](https://pypi.org/project/badkeys/)
