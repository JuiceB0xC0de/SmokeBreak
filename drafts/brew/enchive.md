---
name: enchive
title: Enchive
source: brew
category: take-things-apart
commitment: quick
tags: [archival, c, crypto, curve25519, encryption, quick]
homepage: https://github.com/skeeto/enchive
scout_score: 6
status: draft
---

# Enchive

**TLDR;** A tiny dependency-free C tool that encrypts files to yourself, producing archives indistinguishable from random bytes, with keys you can derive from a passphrase.

Enchive encrypts files for long-term archival, to yourself. You run `keygen` once to make a keypair, then `archive` encrypts any file to the public key and `extract` decrypts it with the secret key and passphrase. With no filenames it reads standard input and writes standard output, so it slots into pipes.

The design is small enough to read in an evening. For each file it generates a fresh ephemeral Curve25519 keypair and does a Diffie-Hellman exchange against your master public key. The hashed shared secret keys ChaCha8. The output is an 8-byte IV, the 32-byte ephemeral public key, the ciphertext, and an HMAC-SHA256 of the plaintext. The README uses the per-file ephemeral key to justify the short IV.

There is no magic number or header. In the README's words, encrypted files have "no distinguishing marks whatsoever", so they look like random data. The idea underneath is public-key encryption used as a backup tool: you can archive on a machine that never holds the secret key, and decrypt only where it lives.

Keys can also be derived from a passphrase with a memory-hard, scrypt-like function, 512MB by default, so the key can live in your head rather than in a file. The README presents it as a focused alternative to GnuPG or encrypted filesystems, and notes GnuPG cannot derive a key pair from a passphrase.

## Install

```
brew install enchive
```

## Try this

```
enchive keygen
```
Generates enchive.pub and enchive.sec in ~/.config/enchive, prompting for a passphrase to protect the secret key.

```
enchive archive sensitive.zip
```
Encrypts the file to sensitive.zip.enchive and leaves the original in place. The output looks like random data.

```
enchive extract sensitive.zip.enchive
```
Prompts for your passphrase and reproduces the original file.

## What's unique

The output has no header or magic number, and the key pair can be derived from a memorable passphrase using a memory-hard function. All of it is one small C program with no dependencies.

## Caveats

The README gives no version, dates or changelog, so maintenance status is unclear; it does no error recovery, and passphrase-derived keys are only as strong as the passphrase.

## Links

- [Enchive on GitHub](https://github.com/skeeto/enchive)
- [Manual page enchive(1)](http://nullprogram.com/enchive/)
