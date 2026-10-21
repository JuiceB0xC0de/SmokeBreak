---
name: luaradio
title: LuaRadio
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, dsp, flow-graph, lua, needs-hardware, sdr]
homepage: https://luaradio.io/
scout_score: 7
status: draft
---

# LuaRadio

**TLDR;** A tiny software-defined radio framework where you wire up receivers as plain Lua scripts: source, filters, demodulator, audio out, then run().

LuaRadio is a flow graph signal processing framework for software-defined radio. A flow graph is a chain of blocks, each doing one job: read samples from an RTL-SDR, tune to a frequency, filter, demodulate FM, play audio. In LuaRadio you write that chain as an ordinary Lua script, connect the blocks with `CompositeBlock():connect(...)`, and call `:run()`.

The README pitches it for rapid prototyping of software radios, modulation and demodulation utilities, and signal processing experiments. It can also be embedded in existing radio applications as a user-scriptable processing engine. The whole thing, LuaJIT included, is under 750 KB.

Blocks are written in pure Lua, but LuaJIT's FFI lets them wrap native libraries such as VOLK and liquid-dsp for speed and for talking to SDR hardware. That is the idea worth stealing: a radio receiver is just a small readable graph of stages, and you can reshape it by editing a few lines. It also ships built-in command-line receivers such as `rx_wbfm` and `rx_ax25` if you would rather listen than build.

The README says it runs well on a Raspberry Pi 3, which makes it a plausible base for a small dedicated radio box.

## Install

```
brew install luaradio
# Running the FM example needs an RTL-SDR dongle and PulseAudio for the audio sink. The brew formula pulls in luajit, fftw and liquid-dsp.
```

## Try this

```
luaradio --platform
```
Prints platform info: LuaJIT version, CPU, and whether fftw3f, volk and liquid features are available.

```
luaradio examples/rtlsdr_wbfm_mono.lua 91.1e6
```
Runs the wideband FM example script against an RTL-SDR dongle tuned to 91.1 MHz. Run it from a clone of the repo.

```
luaradio --help
```
Lists the command-line options for the executable.

## What's unique

The whole signal chain is ordinary Lua, in a binary small enough to embed, with the FFI reaching native DSP libraries only where speed matters.

## Caveats

Primarily a Linux tool, with macOS described as experimental for real-time and audio output; project activity looked quiet, with the homepage copyright reading 2016-2021.

## Links

- [Homepage](https://luaradio.io/)
- [Reference Manual](https://luaradio.io/docs/reference-manual.html)
- [GitHub repository](https://github.com/vsergeev/luaradio)
