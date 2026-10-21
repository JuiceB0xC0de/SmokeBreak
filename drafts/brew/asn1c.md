---
name: asn1c
title: asn1c
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, asn1, c, compiler, protocol, serialization, x509]
homepage: https://lionet.info/asn1c/blog
scout_score: 5
status: draft
---

# asn1c

**TLDR;** A compiler that turns ASN.1 schemas, the grammar behind X.509 certificates and phone network signalling, into C code that reads and writes BER, DER, PER and XER.

ASN.1 is a schema language for describing structured data, and it sits under a lot of things nobody looks at. The README names X.509 certificates in HTTPS, control data between phones and the network, and car-to-car communication. asn1c takes ASN.1 module files and generates C source, described as C++ compatible, with one .c and .h pair per type by default. The generated code serializes native C structures into BER, DER, OER, PER or XER and parses them back.

The author's stated reason is a gap: the README says the ASN.1 family is large and complex, and that no open source compiler supports all of it. It calls asn1c "arguably the most evolved open source ASN.1 compiler."

The compiler works in three stages. It parses the schema into a syntax tree, fixes the tree by checking for semantic errors and rewriting it into canonical form, then compiles it to C. The -E, -F and -P options print the result after each stage, so you can see how the tool understood your schema before any C is written. The generated API pairs encoders and decoders by transfer syntax, for example der_encode() with ber_decode(), or uper_encode() with uper_decode().

The formula also installs enber, unber and crfc2asn1.pl. The README parts the brief covers do not describe them. The source tarball's examples directory includes crfc2asn1.pl, which extracts ASN.1 modules from RFC documents. That makes it a handy way to get real schemas to feed the compiler.

## Install

```
brew install asn1c
```

## Try this

```
asn1c -h
```
Lists the command-line options. The README also points to man asn1c.

```
asn1c -P ./examples/rfc3280-*.asn1
```
Compiles the X.509 PKI module from the source tarball's examples and prints the generated code to stdout instead of writing files. You need the examples directory from the source.

```
asn1c -EF <module-to-test.asn1>
```
Parses and semantically fixes a module and dumps the result, which shows how the compiler read your schema and whether a construct is supported.

## What's unique

The README includes a table mapping each encoding to the encode and decode functions that interoperate. The staged dump options let you inspect how the compiler understood your schema, which is unusual for a code generator.

## Caveats

Status is unclear: the author's blog said in 2010 that development was on hold, CER encoding and APER are listed as unsupported, and the README admits the full ASN.1 standard is not covered.

## Links

- [Homepage (ASN.1 Exposed blog)](https://lionet.info/asn1c/blog)
- [GitHub repository and README](https://github.com/vlm/asn1c)
- [Usage manual (PDF, linked from README)](https://github.com/vlm/asn1c/blob/master/doc/asn1c-usage.pdf)
