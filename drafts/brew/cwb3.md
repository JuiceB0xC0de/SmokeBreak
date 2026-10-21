---
name: cwb3
title: CWB (IMS Open Corpus Workbench)
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, corpus, linguistics, query-language, text-analysis]
homepage: https://cwb.sourceforge.io/
scout_score: 6
status: draft
---

# CWB (IMS Open Corpus Workbench)

**TLDR;** Index and query text corpora of up to two billion words with linguistic annotations, using CQP, a dedicated corpus query language and engine.

The IMS Open Corpus Workbench, usually called CWB, is a set of open-source tools for managing and querying large text corpora that carry linguistic annotations. The homepage puts the size limit at about 2 billion words. Its central piece is CQP, which the project calls "the flexible and efficient query processor" at its core.

The package installs a family of cwb-* utilities alongside cqp, cqpcl and cqpserver. From their names, they appear to encode text into an indexed form, decode it back, describe a corpus, and scan it. The brew metadata names a default registry directory, `$HOMEBREW_PREFIX/share/cwb/registry`, which suggests each corpus is described by a registry file kept there. That detail comes from the package metadata, not from the documentation.

The idea underneath is corpus linguistics. Instead of grepping raw text, you search over words that have been tagged with extra layers such as lemma or part of speech, and you ask questions about those layers. A purpose-built query language and index let that work on corpora far too large for ad hoc scripts. It is a door into how linguists study language at scale.

The homepage says version 3.5 is the current stable release and that 3.0 is of historical interest only. The brief does not cover the documentation, so the encoding workflow and query syntax are not described here.

## Install

```
brew install cwb3
# Default registry directory: $HOMEBREW_PREFIX/share/cwb/registry
# You need an annotated corpus to query; the package does not appear to bundle one.
```

## Try this

```
cqp --help
```
Prints the command-line options of the CQP query processor.

```
cwb-encode --help
```
Shows how the encoder is invoked, the tool that turns annotated text into an indexed corpus.

```
cwb-describe-corpus --help
```
Shows the options for inspecting a corpus that is already encoded.

## What's unique

It is a purpose-built corpus index plus the CQP query language, aimed at annotated text at the billion-word scale rather than general-purpose search.

## Caveats

The brief draws only on the homepage, which says some pages may be out of date, shows no release date, and sends bug reports to a tracker that needs a login; you also need your own annotated corpus to do anything real.

## Links

- [CWB homepage](https://cwb.sourceforge.io/)
- [SourceForge project page (downloads, bug tracker)](https://sourceforge.net/projects/cwb/)
