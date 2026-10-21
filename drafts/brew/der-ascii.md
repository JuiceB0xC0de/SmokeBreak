---
name: der-ascii
title: der-ascii
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, asn1, ber, der, go, protocol, reverse-engineering, x509]
homepage: https://github.com/google/der-ascii
scout_score: 8
status: draft
---

# der-ascii

**TLDR;** Turns binary DER and BER into editable text and back again, so you can hand-craft ASN.1 structures, including deliberately broken ones, without counting bytes.

DER ASCII is a small text language for writing DER or BER encodings of ASN.1 structures. Two tools ship with it. `der2ascii` disassembles a binary file into text. `ascii2der` assembles text back into bytes. Curly-brace blocks get their length prefixes computed automatically, so you edit the content and the tool fixes the lengths.

The project's stated reason is test inputs: disassemble an existing structure, change it as text, reassemble it. In its own words, "This avoids having to manually fix up all the length prefixes. As a bonus, it acts as a human-readable view for DER structures." The language is also built to emit invalid encodings. Options such as `indefinite`, `long-form:N` and `adjust-length:N` let you write wrong or odd lengths on purpose.

The idea underneath is that ASN.1 is the binary format behind certificates and many other protocol structures, and most printers show a cleaned-up view of it. This one keeps every encoding variation, so the text round-trips to the same bytes. That makes it a way to see how tag-length-value encoding works, and to see what a parser does when the bytes lie.

The disassembler is a heuristic. It parses BER elements greedily, recurses into constructed bodies, decodes known types like INTEGER, OID, BOOLEAN, BIT STRING and BMPString, and falls back to hex literals when parsing fails. The spec notes that disassembly is not unique, so the same bytes can have more than one text form.

## Install

```
brew install der-ascii
# Upstream's own route, which needs a Go toolchain:
# go install github.com/google/der-ascii/cmd/...@latest
```

## Try this

```
der2ascii --help
```
Lists the options for turning a binary DER or BER file into DER ASCII text.

```
ascii2der --help
```
Lists the options for assembling DER ASCII text back into binary DER.

## What's unique

Most ASN.1 printers normalize what they show. This one is reversible by design and can deliberately encode broken input, such as wrong length prefixes or wrong constructed bits.

## Caveats

The README says der2ascii is a heuristic whose output, including formatting and OID recognition, may change between versions, and that this is not an official Google project; maintenance status was not checked.

## Links

- [GitHub repository (homepage)](https://github.com/google/der-ascii)
- [Language specification (language.txt)](https://github.com/google/der-ascii/blob/main/language.txt)
- [Samples directory](https://github.com/google/der-ascii/tree/main/samples)
