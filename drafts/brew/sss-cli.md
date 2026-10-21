---
name: sss-cli
title: sss-cli
source: brew
category: deeper-rabbit-holes
commitment: quick
tags: [cryptography, math, quick, rust, secret-sharing]
homepage: https://github.com/dsprenkels/sss-cli
scout_score: 6
status: draft
---

# sss-cli

**TLDR;** Split a secret into shares with Shamir's scheme, then recover it from any threshold subset, with tamper detection built in.

sss-cli is two small commands: secret-share-split and secret-share-combine. You pipe a secret into the first with a share count (-n) and a threshold (-t), and it prints shares to stdout. Feed any t of those shares into the second and the original secret comes back. With fewer than t shares, you get nothing useful.

The idea underneath is Shamir's secret sharing. The secret is hidden in a polynomial, and each share is a point on it. Enough points pin the polynomial down and reveal the secret. Too few leave every possible secret equally likely. It is a short route into finite-field arithmetic and threshold cryptography.

The tool also deals with a weakness of the plain scheme. Basic Shamir gives confidentiality but not integrity, so someone could alter a share and the recovered secret would look valid but be wrong. The README says sss-cli wraps each share in an AEAD layer so tampering is detected. That is why the shares are much longer than the secret. The tool wraps the author's SSS library, and per the changelog the crypto comes from the RustCrypto crypto-secretbox crate.

## Install

```
brew install vitkabele/tap/sss-cli
# Not in homebrew-core; this uses a third-party tap.
# Alternative, needs Rust: cargo install --git https://github.com/dsprenkels/sss-cli --branch v0.1
```

## Try this

```
echo "Tyler Durden isn't real." | secret-share-split -n 4 -t 3 >shares.txt
```
Creates 4 shares of the secret, any 3 of which can recover it, and writes them to shares.txt.

```
head -n 3 shares.txt | secret-share-combine
```
Combines the first 3 shares and prints the original secret.

```
secret-share-split --help
```
Lists the options, since the README documents only -n and -t.

## What's unique

It adds an AEAD layer so tampered shares are detected, which most Shamir demos skip. The README is open about the size cost.

## Caveats

Maintenance status is unclear, the README is short and documents only -n and -t, and the Homebrew route depends on a third-party tap.

## Links

- [Homepage / repository](https://github.com/dsprenkels/sss-cli)
- [SSS library (underlying Shamir implementation)](https://github.com/dsprenkels/sss)
- [Homebrew tap with sss-cli formula](https://github.com/vitkabele/homebrew-tap)
