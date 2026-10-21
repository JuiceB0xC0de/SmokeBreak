---
name: precomp
title: precomp
source: brew
category: take-things-apart
commitment: quick
tags: [compression, deflate, file-formats, lossless, quick]
homepage: http://schnaader.info/precomp.php
scout_score: 6
status: draft
---

# precomp

**TLDR;** Precomp opens up zip, PDF, PNG and similar files, undoes the compression inside them, and stores the raw data so it can be compressed again, smaller.

Precomp is a command-line precompressor written in C++. Give it a file that is already compressed, such as a PDF, PNG, ZIP, GIF, JPG, MP3 or bZip2 file, and it hunts for zLib/Deflate, bZip2, GIF, JPG or MP3 streams inside. It decompresses each one it finds. The result is normally a .pcf file, compressed with LZMA2, that is smaller than what a general-purpose compressor manages on the original.

The trick is a round-trip check. In the README's words, "Precomp tries to decompress the streams, and if they can be decompressed and 're-'compressed so that they are bit-to-bit-identical with the original stream, the decompressed stream can be used instead of the compressed one." Streams that fail the check are left alone, so the original can always be restored exactly. For Deflate it uses preflate to build reconstruction information. For JPG and MP3 it relies on packJPG/brunsli and packMP3.

The idea underneath is that compressed data looks like noise to a compressor, so compressing it twice gains almost nothing. If you can undo the first compression reversibly, the second compressor finally sees the real structure. There is also a `-cn` mode that writes the decompressed data plus reconstruction data without compressing it, so you can hand it to a stronger compressor of your choice.

It is also a quiet way to see how many compressed streams are tucked inside everyday file formats. A zip, a PDF and a PNG all turn out to be containers for Deflate data.

## Install

```
brew install precomp
```

## Try this

```
precomp --help
```
Lists the options, including the modes for compression, restoring and output naming.

```
precomp silesia.zip
```
Precompresses the zip into silesia.pcf. In the README's example, 7-Zip at Ultra leaves it at 67,405,052 bytes (99.7%), while Precomp gets it to 47,122,779 bytes (69.7%).

```
precomp -r -osilesia.zip_ silesia.pcf
```
Restores the original from the .pcf into silesia.zip_. Follow with `diff -s silesia.zip silesia.zip_` to confirm the two files are identical.

## What's unique

It does lossless recompression of data that is already compressed, which general compressors cannot do. It only accepts a stream after checking that it can be rebuilt bit for bit.

## Caveats

The official homepage returned 404 when checked, and the brief could not confirm whether the project is still maintained; the README's copyright range ends in 2021.

## Links

- [Homepage (returned 404 when checked)](http://schnaader.info/precomp.php)
- [GitHub repository](https://github.com/schnaader/precomp-cpp)
- [GitHub releases (binaries)](https://github.com/schnaader/precomp-cpp/releases)
- [Issue list](https://github.com/schnaader/precomp-cpp/issues)
