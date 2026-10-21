---
name: nacl
title: NaCl
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, c, crypto, library, public-key, signatures]
homepage: https://nacl.cr.yp.to/
scout_score: 6
status: draft
---

# NaCl

**TLDR;** A C crypto library by Daniel Bernstein and colleagues that fixes the algorithms for you, so you just say "sign this message" or "box this message".

NaCl (pronounced "salt") is a C and C++ library for network communication, encryption, decryption and signatures. You pass in messages and keys as byte strings and get back ciphertext, authentication tags, signatures or hashes as byte strings. It covers public-key authenticated encryption, scalar multiplication and signatures, secret-key encryption and authentication, one-time authentication, hashing and constant-time string comparison.

The idea underneath is that most crypto failures come from choices the programmer should never have had to make. Typical libraries ask you to pick primitives, modes and padding, then glue them together. NaCl ships a preselected set of modern primitives. One crypto_box call does the key handling, encryption and authentication that would otherwise be a multi-step RSA, AES and SHA-256 pipeline. In the project's words, it "allows, and encourages, the programmer to simply say 'sign this message.'"

It also takes an unusual approach to speed. The build compiles every implementation of each function with every compiler option it finds, times them on the machine doing the build, and keeps the fastest. New CPUs get good code without anyone writing detection logic. The code avoids secret-dependent branches and array indices, which is how it resists timing and cache attacks.

Reading its API and its features page is a compact way to see how a modern, opinionated crypto interface is put together. Many later libraries borrowed its design.

## Install

```
brew install nacl
# The Homebrew formula installs no executables, only the library (it depends on libcpucycles).
# The project's own route is to build from source: download a tarball, unpack it, and run ./do. It writes libraries and headers to build/<hostname>.
```

## Try this

```
wget https://hyperelliptic.org/nacl/nacl-20110221.tar.bz2
```
Downloads the 2011 release tarball used in the project's installation instructions.

```
bunzip2 < nacl-20110221.tar.bz2 | tar -xf - && cd nacl-20110221
```
Unpacks the source and enters the directory.

```
./do
```
Compiles NaCl for every ABI and compiler it detects, benchmarks the implementations, and writes the fastest libraries and headers into build/<hostname>.

## What's unique

It builds every implementation of each function, times them on your machine and keeps the fastest. Its one-call crypto_box API also fixes the primitives and wire format instead of asking you to choose.

## Caveats

The pages are old (homepage stamped 2016, features page 2011), system-wide install is listed as a TO DO, there is no shipped Python binding, and C callers must check error codes themselves.

## Links

- [NaCl homepage](https://nacl.cr.yp.to/)
- [Installation page](https://nacl.cr.yp.to/install.html)
- [Features page](https://nacl.cr.yp.to/features.html)
