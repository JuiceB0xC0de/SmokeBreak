---
name: ssdeep
title: ssdeep
source: brew
category: take-things-apart
commitment: quick
tags: [forensics, hashing, malware, quick, similarity]
homepage: https://ssdeep-project.github.io/ssdeep/
scout_score: 7
status: draft
---

# ssdeep

**TLDR;** A hashing tool that scores how similar two files are instead of just whether they match, widely used in malware triage and forensics.

ssdeep computes context triggered piecewise hashes (CTPH), also called fuzzy hashes. You give it files and it prints a hash string for each. Those strings can be compared to estimate how alike the original inputs are. A companion library, libfuzzy, exposes the same idea to other programs.

Ordinary cryptographic hashes are built so that changing one byte changes the whole result. That is right for integrity checks and useless for asking whether two files are nearly the same. ssdeep takes the opposite approach. In the homepage's words, "CTPH can match inputs that have homologies": runs of identical bytes in the same order, even when the bytes between them differ in content and length.

The trick is in the name. The file is split into pieces, and the split points are set by the content itself rather than by fixed offsets. An insertion or edit in one place disturbs only nearby pieces, and the rest still line up. The full mechanism is in the Digital Investigation paper "Identifying almost identical files using context triggered piecewise hashing", which the homepage links.

That makes it a door into malware analysis and forensics, where you often want to know whether a new sample is a variant of one you have already seen. The homepage notes that ssdeep hashes appear in the Basic Properties section of VirusTotal.

## Install

```
brew install ssdeep
```

## Try this

```
ssdeep --help
```
Prints the list of options, including how to hash files and how to compare them against each other.

## What's unique

It is the long-standing reference fuzzy hash. The project says that despite newer alternatives it stays a primary choice because it is fast, which it claims is about twice as fast as TLSH.

## Caveats

The latest release listed is 2.14.1 from 2017, so it is quiet rather than actively developed, and the speed claims against TLSH are the project's own.

## Links

- [ssdeep project homepage](https://ssdeep-project.github.io/ssdeep/)
