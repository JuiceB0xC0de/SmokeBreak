---
name: zfp
title: zfp
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, compression, floating-point, hpc, library, science]
homepage: https://zfp.llnl.gov
scout_score: 6
status: draft
---

# zfp

**TLDR;** A compressor for grids of floating-point numbers that lets you read and write single elements without unpacking the whole array.

zfp is a library, with Python and Fortran bindings, for compressing multidimensional arrays of floats and integers. It also ships a small command-line tool, `zfp`, for compressing whole arrays to and from disk. It targets 2D, 3D, and 4D data with spatial correlation: fields from physics simulations, natural images, regularly sampled terrain. Output can be lossy with an error bound, or bit-for-bit lossless.

The idea underneath it is that the array is cut into small blocks, and each block is compressed on its own. A general-purpose compressor generally has to decode a stream from the start to reach one value. With independent blocks, zfp can decode just the block holding the element you want. That makes it usable as the in-memory storage of a running simulation, not only as a file format.

The homepage figure shows compression ratios ranging from 10:1 to 250:1, depending on how much error you accept. That tradeoff between accuracy and size is the door into a larger area: lossy compression for scientific data, where the question is how much precision your analysis actually needs. The README does not explain the mechanism in detail; it points to the algorithm page in the online docs, and it describes the work as loosely based on Peter Lindstrom's 2014 fixed-rate paper.

## Install

```
brew install zfp
```

## Try this

```
zfp --help
```
Prints the command-line options for compressing and decompressing arrays, including the modes for lossy and lossless output.

## What's unique

Most compressors treat data as a stream. zfp treats it as an array you can index, so individual values can be read and written while the data stays compressed.

## Caveats

Compression is lossy by default, it works best on 2D to 4D data (the README calls 1D use "generally discouraged"), and the `zfp` command-line tool is the least interesting part, since the library is the main product.

## Links

- [Homepage (LLNL)](https://zfp.llnl.gov)
- [Full documentation (Read the Docs)](https://zfp.readthedocs.io)
- [GitHub repository](https://github.com/LLNL/zfp)
- [Installation docs](https://zfp.readthedocs.io/en/latest/installation.html)
