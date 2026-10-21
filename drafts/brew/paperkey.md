---
name: paperkey
title: paperkey
source: brew
category: take-things-apart
commitment: quick
tags: [backup, file-format, gpg, openpgp, quick]
homepage: https://www.jabberwocky.com/software/paperkey/
scout_score: 5
status: draft
---

# paperkey

**TLDR;** Strips an OpenPGP secret key down to its few hundred secret bytes so you can print it on paper and rebuild the full key later.

Paperkey reads an OpenPGP secret key, from GnuPG, PGP or similar, and throws away everything that is not secret. What remains is the secret key material plus a little packet structure. For a DSA and Elgamal key that was 1281 bytes whole, the author says the result is about 149 bytes. Output is base16 text by default, 78 columns wide, or raw bytes if you prefer. It includes a CRC so typos are caught.

The idea underneath is that a secret key file carries a complete copy of the public key, and public keys are easy to get from keyservers. Only the secret part needs archiving. To restore, you give paperkey the public key and the secret bytes you saved, and it rebuilds the secret key file. Any passphrase on the original key carries over unchanged.

The author's reasoning is that CD-Rs, tapes and drives often lose data within years, so paper is a last-resort backup. He is plain about the limits: "The goal with paper is not secure storage." and "paperkey doesn't do any crypto at all, but just saves and restores the original secret key, whether it is encrypted or not." In his words, "It's a lot easier to re-enter 149 bytes correctly."

It is also a small, readable way into the OpenPGP packet format: what a key file contains, which parts are secret, and which are just public data riding along.

## Install

```
brew install paperkey
You also need an OpenPGP tool such as GnuPG to export keys from. No account or other runtime is needed.
```

## Try this

```
paperkey --secret-key my-secret-key.gpg --output to-be-printed.txt
```
Extracts only the secret data from the key file into a text file meant for printing.

```
paperkey --pubring my-public-key.gpg --secrets my-key-text-file.txt --output my-secret-key.gpg
```
Restores the secret key by combining the public keyring with the saved secret text.

```
gpg --export-secret-key my-key | paperkey | lpr
```
Pipes an exported secret key through paperkey straight to the printer, since stdin is used when --secret-key is absent.

## What's unique

It shrinks a key to a few hundred bytes by noticing the public half is already available elsewhere. It is also upfront that it adds no crypto and that paper is not secure storage.

## Caveats

Restoring needs the matching public key and accurately re-entered text, a CRC error stops restore unless you pass --ignore-crc-error, and the homepage shows version 1.6 with copyright through 2018.

## Links

- [Paperkey homepage (David Shaw)](https://www.jabberwocky.com/software/paperkey/)
