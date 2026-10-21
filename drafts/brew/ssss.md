---
name: ssss
title: ssss
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [cryptography, math, quick, secret-sharing, unix]
homepage: http://point-at-infinity.org/ssss/
scout_score: 7
status: draft
---

# ssss

**TLDR;** Split a secret into n shares so any t of them rebuild it and fewer reveal nothing, using Shamir's 1979 scheme from the command line.

ssss is a small command-line implementation of Shamir's secret sharing. In split mode it asks for a secret at a prompt, takes a threshold t and a share count n, and prints n share strings, one per line, each prefixed with its share number. In combine mode you paste in any t of those lines and it prints the secret back.

The idea underneath is polynomial interpolation. The secret becomes a point on a random polynomial, and each share is another point on it. With t points you can recover the polynomial by Lagrange interpolation, and with fewer you cannot. The page puts it plainly: "in a (t,n) scheme one can prove that it makes no difference whether an attacker has t-1 valid shares at his disposal or none at all". That is a proof, not a hope about computational hardness.

B. Poettering wrote it in 2006 for practical uses such as spreading a password across several safe places or guarding a vault code. It links against GNU libgmp for the big-number arithmetic and reads randomness from /dev/random. The example prompt caps secrets at 128 ASCII characters. For anything larger, the author recommends encrypting the data with openssl or gpg and sharing only the key.

## Install

```
brew install ssss
# builds against gmp; needs /dev/random as an entropy source. The brew formula installs ssss-split (ssss-combine is the matching reconstruct command).
```

## Try this

```
ssss-split -t 3 -n 5
```
Prompts for a secret, then prints five shares, any three of which can reconstruct it.

```
ssss-combine -t 3
```
Prompts for three shares, one per line, then prints 'Resulting secret: ...'.

```
ssss-split --help
```
Lists the options for splitting.

## What's unique

It is a single-purpose Unix tool for the classic (t,n) threshold construction, and its homepage is frank about the scheme's limits, including the hybrid-encryption advice for larger secrets.

## Caveats

The project is quiet: the homepage was last modified in 2018, the latest tarball is 0.5, and the page says 0.5 may need a manual edit to compile; it is UNIX/Linux only.

## Links

- [ssss homepage (project page with docs and downloads)](http://point-at-infinity.org/ssss/)
