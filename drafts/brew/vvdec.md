---
name: vvdec
title: vvdec
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, codec, h266, library, video, vvc, wasm]
homepage: https://www.hhi.fraunhofer.de/en/departments/vca/technologies-and-solutions/h266-vvc.html
scout_score: 5
status: draft
---

# vvdec

**TLDR;** Fraunhofer's open-source H.266/VVC video decoder: feed it a raw next-generation bitstream and get plain YUV frames back, with a library underneath.

vvdec is Fraunhofer HHI's software decoder for H.266/VVC (Versatile Video Coding), the successor to H.265/HEVC. It is a C library with a small command-line app, vvdecapp, that reads a raw VVC bitstream and writes decoded frames as raw YUV or YUV4MPEG2 (y4m). It can also write to stdout, so it fits into a pipe. The project says it supports all features of the VVC Main10 profile.

The homepage presents it as a reference-quality, open-source decoder for a standard that claims about 50% bit-rate reduction over HEVC at the same subjective quality. The README gives no other motivation. A paired encoder, VVenC, is listed alongside it, and the README shows decoded output piped straight into that encoder's app.

The interesting part is how a codec looks from the inside. The library API is small: you hand it one NAL unit at a time through vvdec_decode(). It answers VVDEC_TRY_AGAIN until it has a full picture, then VVDEC_OK with a frame, and vvdec_flush() drains what is left. Decoding runs on a thread pool sized by --threads. The authors cite an ICIP 2020 paper on the live-decoder design, and they say it can decode 4Kp60 in real time. It also builds to WebAssembly for the browser.

The door here is the structure of modern video: bitstreams, NAL units, access units, and frames reconstructed from them. You need a VVC file to try it on, since the README does not point to a ready-made sample.

## Install

```
brew install vvdec
You also need a raw VVC bitstream (.266 or similar) to decode. To build from source instead, you need CMake; the WebAssembly build needs the Emscripten SDK.
```

## Try this

```
vvdecapp --help
```
Prints the full list of decoder options, including threading.

```
vvdecapp -b str.266 -o raw_yuv.y4m
```
Decodes a raw VVC file into a YUV4MPEG2 file, chosen by the .y4m extension.

```
vvdecapp -b str.266 --y4m -o - | vvencapp -i - -o newstr.266 --y4m
```
Streams decoded frames into the separate VVenC encoder app to re-encode them. vvencapp is not part of this project.

## What's unique

It is an open decoder for a very new codec that aims at live 4K60 decoding on the CPU, and it compiles to WebAssembly so it can run in a browser.

## Caveats

Full support is claimed only for the Main10 profile, some platforms are marked untested or not working, and the wiki labels the standalone vvdecapp app as deprecated in favour of the library.

## Links

- [Homepage (Fraunhofer HHI H.266/VVC page)](https://www.hhi.fraunhofer.de/en/departments/vca/technologies-and-solutions/h266-vvc.html)
- [GitHub repository (README)](https://github.com/fraunhoferhhi/vvdec)
- [Wiki: How to use VVdeC](https://github.com/fraunhoferhhi/vvdec/wiki/How-to-use-VVdeC)
- [ICIP 2020 paper: Towards A Live Software Decoder Implementation For The Upcoming VVC Codec](https://doi.org/10.1109/ICIP40778.2020.9191199)
