---
name: jbigkit
title: jbigkit
source: brew
category: take-things-apart
commitment: quick
tags: [c-library, compression, fax, image-formats, jbig, netpbm, quick]
homepage: https://www.cl.cam.ac.uk/~mgk25/jbigkit/
scout_score: 5
status: draft
---

# jbigkit

**TLDR;** Converters and a C library for JBIG1, the fax-era lossless bilevel image standard that encodes pictures as a coarse layer followed by refinements.

JBIG-KIT is a C implementation of JBIG1 (ITU-T T.82), a lossless compression standard for bi-level images such as scanned documents. It ships as a portable library plus four small converters that behave like netpbm tools: `pbmtojbg` turns a PBM or PGM bitmap into JBIG data, and `jbgtopbm` turns it back. The `85` variants use the separate low-memory implementation of the T.85 profile.

The interesting part is how JBIG1 works. It uses arithmetic coding driven by the neighbourhood of already-seen pixels, and it can store an image progressively: a low-resolution layer first, then resolution-enhancement layers on top. A viewer can show a coarse picture while the rest arrives, much like a GIF loading in an old browser. The author says it beats G4 fax compression on typical scanned documents by roughly 1.1 to 1.5 times.

The library is built to decode incomplete and growing streams and to handle several streams at once, with no global or static variables. The `jbig85.c` variant can stream an image of initially unknown height while buffering only a few lines, which is why it suits fax machines and printer firmware. The standard is widely used there, and in document management systems. Markus Kuhn's homepage presents it as a reference implementation you can embed.

Some Linux distributions ship libtiff linked against it, so it may already be on your machine without you knowing.

## Install

```
brew install jbigkit
```

## Try this

```
pbmtojbg --help
```
Prints the encoder's options, including how the progressive resolution layers are controlled.

```
jbgtopbm --help
```
Prints the decoder's usage for turning a JBIG file back into a PBM or PGM bitmap.

```
pbmtojbg85 --help
```
Shows the low-memory T.85 encoder's options, the variant meant for embedded and fax work.

## What's unique

It is the reference-style implementation of a fax-era standard, built around progressive, streaming decoding of partial data. The same code is a library, a pair of netpbm-style tools, and a low-memory embedded variant.

## Caveats

The licence is GPL, so linking it into a combined work brings the whole work under the GPL (a commercial licence is available), and the full-memory `jbig.c` variant needs the whole uncompressed image in memory.

## Links

- [JBIG-KIT homepage (Markus Kuhn)](https://www.cl.cam.ac.uk/~mgk25/jbigkit/)
- [Source tarball jbigkit-2.2.tar.gz](https://www.cl.cam.ac.uk/~mgk25/jbigkit/download/jbigkit-2.2.tar.gz)
- [Git repository](https://www.cl.cam.ac.uk/~mgk25/git/jbigkit)
