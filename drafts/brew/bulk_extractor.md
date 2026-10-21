---
name: bulk_extractor
title: bulk_extractor
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c++, carving, disk-images, forensics]
homepage: https://github.com/simsong/bulk_extractor/wiki
scout_score: 7
status: draft
---

# bulk_extractor

**TLDR;** A forensics scanner that reads raw bytes, decodes anything that looks encoded or compressed, and pulls out emails, card numbers and images without parsing a file system.

bulk_extractor scans disk images, single files, or directories of files and writes out structured evidence: email addresses, credit card numbers, JPEGs, JSON snippets. It does not parse the file system at all. It treats the input as a stream of bytes and runs scanners over it. The README calls it a "get evidence" button for any kind of input.

The idea underneath is optimistic decoding. It probes every byte to see whether it starts a sequence that can be decompressed or decoded, such as Base64 or compressed data. Whatever it decodes is scanned again, recursively. That is how it finds a Base64-encoded JPEG or compressed JSON that a traditional carver, which looks for file headers, would walk straight past.

It was built for triage. With a large pile of data, you often cannot wait for a full file-system analysis, and the file system may be damaged or missing anyway. Results go into plain text files, and it also builds histograms of what it found, such as the most common email addresses or Google search terms. The README says these histograms have proven useful in investigative and law enforcement work. The cited reference is Garfinkel's 2013 paper, "Digital media triage with bulk data analysis and bulk_extractor".

Scanners are modules, and extra ones can be loaded as scan_*.so, .dylib or .dll plugins from directories given with -P or in BE_PATH. That makes it a reasonable place to read how a byte-stream pipeline is put together.

## Install

```
brew install bulk_extractor
# Alternative from source (the README's recommended route; needs a C++17 compiler): git clone https://github.com/simsong/bulk_extractor.git, then ./bootstrap.sh, ./configure, make, make check, make install
```

## Try this

```
bulk_extractor --help
```
Lists the options, including how to choose an output directory and enable or disable scanners.

```
bulk_extractor -S jpeg_carve_mode=2
```
Shows the -S syntax for setting a scanner parameter, here the JPEG carve mode (from the 2.1.1 release notes). Add an output directory and an input to run it for real; check --help for the exact arguments.

```
bulk_extractor64.exe -o output \\.\PhysicalDrive0
```
The README's Windows example: scans a raw physical disk and writes results to a separate output directory. Run it from an elevated prompt.

## What's unique

It decodes first and asks questions later: every byte is a possible start of encoded or compressed data, and the decoded result is rescanned. That finds things header-based carvers miss.

## Caveats

The README says the source tree is not the same as a tested release and recommends a tagged release for production use; native Windows builds are not supported, only an unsigned cross-compiled artifact.

## Links

- [Wiki homepage (now a navigation layer)](https://github.com/simsong/bulk_extractor/wiki)
- [Repository and README](https://github.com/simsong/bulk_extractor)
- [Published manuals and docs](https://simsong.github.io/bulk_extractor/)
- [Releases and source archives](https://github.com/simsong/bulk_extractor/releases)
