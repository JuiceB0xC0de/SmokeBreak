---
name: cmix
title: cmix
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, compression, machine-learning, math, prediction]
homepage: https://www.byronknoll.com/cmix.html
scout_score: 6
status: draft
---

# cmix

**TLDR;** A lossless compressor that mixes about 2,000 predictive models and an LSTM to squeeze files smaller than almost anything, at the cost of hours of CPU and tens of gigabytes of RAM.

cmix takes one file in and writes one compressed file out. Decompression runs the same process in reverse, so it takes as long to unpack as to pack. Before compressing, it detects the kind of data (executable, English text, image) and transforms it into a more predictable form. English text gets a dictionary-based word replacement, for example.

The compression itself is prediction. cmix codes the data one bit at a time. In v21, about 2,077 independent models each guess the probability that the next bit is 1. A context mixer, a small layered network of weights, combines those guesses. A secondary estimation stage refines the result, and an arithmetic coder turns the final probability into bits. The better the prediction, the fewer bits it takes to store what actually happened.

That is the idea underneath: compression and prediction are the same problem. The README lists a byte-level LSTM mixer, trained with backpropagation through time and Adam, as a component unique to cmix. The author started the project in December 2013 and says most of the ideas came from Matt Mahoney's book Data Compression Explained.

The README states the goal plainly: "aimed at optimizing compression ratio at the cost of high CPU/memory usage." It means that. It is a tool for seeing how far prediction can be pushed, not for backing up your laptop.

## Install

```
brew install cmix
# Needs a lot of memory: the README recommends at least 32GB of RAM.
# Source builds use make; the README suggests -O3 for builds that must match across machines.
```

## Try this

```
cmix --help
```
Prints the built-in usage, since the README does not show the basic compress and decompress syntax.

```
tar
```
Not a cmix command, but cmix handles only single files, so bundle a directory into one tar archive first, then give cmix the archive.

```
./enwik9-preproc c path_to_enwik9
```
Runs the helper tool from the README's enwik9 steps, preprocessing the benchmark file into .ready4cmix before compression.

## What's unique

Most compressors of this kind mix a few dozen models. cmix mixes about 2,077, adds an LSTM mixer the author calls unique to it, and feeds a PPM model's predictions into that LSTM.

## Caveats

Extremely slow and memory-hungry: the author's benchmarks report about 18 hours and 19 to 31 GB of memory for a 100 MB file, and the same time again to decompress.

## Links

- [Homepage (Byron Knoll)](https://www.byronknoll.com/cmix.html)
- [GitHub repository](https://github.com/byronknoll/cmix)
- [precomp (optional preprocessing)](https://github.com/schnaader/precomp-cpp)
