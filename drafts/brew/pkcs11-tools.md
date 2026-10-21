---
name: pkcs11-tools
title: pkcs11-tools
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cryptography, hsm, keys, needs-hardware-optional, pkcs11]
homepage: https://github.com/Mastercard/pkcs11-tools
scout_score: 5
status: draft
---

# pkcs11-tools

**TLDR;** Unix-style ls, cat, mv, rm and od for the keys inside hardware security modules and software tokens, so you can see what a PKCS#11 token holds.

pkcs11-tools is a set of small command-line programs for managing objects on anything that speaks PKCS#11, the standard C interface that hardware tokens, smart cards and HSMs expose. Its commands are modelled on Unix file tools: p11ls lists objects, p11cat prints a public key as PEM, p11od dumps every attribute in hex, p11mv renames, p11rm deletes. Other commands generate keys (p11keygen), build certificate signing requests (p11req), make self-signed certificates (p11mkcert), and import certificates, public keys or data.

Each command loads a PKCS#11 library, chosen with -l or the PKCS11LIB environment variable, then picks a slot and token with -s and -t. Objects are addressed by name, such as pubk/rsa or seck/aes-128. A PIN can be passed with -p or PKCS11PASSWORD. Bash and zsh completion queries the token live. Wrapper scripts named with_softhsm, with_yubico, with_nfast and so on find a vendor's library for you.

The idea underneath is that a key on an HSM is an object you can name and inspect but usually cannot read. Private keys stay inside the device, and you move them only by wrapping: encrypting one key under another. p11wrap writes a wrapped key to stdout in a documented file format, p11unwrap reads it back in, and p11rewrap does both steps in one go. You can do all of this without hardware, using SoftHSM, NSS or Kryoptic as a software token.

The tool comes from Eric Devolder at Mastercard. The README describes it as compatible with many implementations, including both IBM and Oracle JVMs.

## Install

```
brew install pkcs11-tools
# Needs a PKCS#11 library to talk to. SoftHSM is the easiest no-hardware option: brew install softhsm
# Depends on OpenSSL 3.x (the formula pulls in openssl@4).
```

## Try this

```
p11ls -l /usr/local/opt/softhsm/lib/softhsm/libsofthsm2.so -s 0
```
Lists the objects on the token in slot index 0 of SoftHSM, with attributes in long format.

```
p11keygen -k ec -q prime256v1 -i my-ec-key sign=true verify=true
```
Generates an elliptic-curve key pair on prime256v1 labelled my-ec-key, usable for signing and verifying.

```
p11od pubk/dh
```
Dumps every attribute of a public key object in hex, with attribute names shown.

## What's unique

Most PKCS#11 tooling is a thin wrapper around one vendor's library. This gives you a file-manager-style toolset that works across many tokens, with a documented wrapped-key format that lets you move a key from one token to another.

## Caveats

You need a PKCS#11 library to point it at (SoftHSM works), it requires OpenSSL 3.x, and the AWS CloudHSM support is disabled by default and has significant limits, including no p11mv, p11setattr or p11od.

## Links

- [GitHub repository and README](https://github.com/Mastercard/pkcs11-tools)
- [Manual](https://github.com/Mastercard/pkcs11-tools/blob/master/docs/MANUAL.md)
- [Change log](https://github.com/Mastercard/pkcs11-tools/blob/master/CHANGELOG.md)
