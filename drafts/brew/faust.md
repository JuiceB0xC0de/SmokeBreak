---
name: faust
title: Faust
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, compiler, dsp, language, plugins, synthesis]
homepage: https://faust.grame.fr
scout_score: 8
status: draft
---

# Faust

**TLDR;** A functional language for sound: write a synth or effect once, then compile it to plugins, apps, web audio, and objects for Max, Pure Data and SuperCollider.

Faust (Functional Audio Stream) is a functional programming language for real-time signal processing and synthesis. You write a DSP specification, and the compiler translates it into sample-level code in C++, C, Rust, WebAssembly, LLVM IR and other targets. The project describes itself as "fully compiled".

The long list of `faust2...` executables is the second half of the system. Each one is a wrapper script that pairs the generated code with an architecture file, which supplies the audio driver, the user interface, or the plugin format. That is how one source file becomes a JACK app with a Qt interface, a VST or LV2 plugin, a Pure Data external, a SuperCollider UGen, or a mobile app. There are many of these scripts, and most people will only ever use a few.

The idea underneath is that audio processing can be described as composed signal flows instead of loops over buffers. Because the program is a specification rather than a hand-written implementation, the same description can be retargeted to hardware and hosts that have nothing in common. GRAME in Lyon has developed it since 2002.

The master branch can also emit LLVM IR and run it through a JIT, which lets libfaust be embedded in other C++ programs and used by tools such as FaustLive. A browser Playground and Web IDE run the compiler with no install at all, so you can try a program before you commit to the toolchain.

## Install

```
brew install faust
# Each faust2... script needs its own dependencies. For example, faust2jaqt needs JACK and Qt installed separately.
# No install needed to try it first: https://faustplayground.grame.fr/
```

## Try this

```
faust --help
```
Lists the compiler's options, including the choice of output language.

```
faust2jaqt yourCode.dsp
```
Compiles a Faust file into a JACK application with a Qt interface (needs JACK and Qt).

```
faust2
```
Type this in a terminal and press Tab to list every faust2... target tool.

## What's unique

One functional DSP source compiles to an unusually wide range of targets: plugin formats, computer music environments, embedded boards, mobile and web. The compiler also runs in the browser.

## Caveats

Each faust2... target has its own dependencies and some will not build out of the box, and the Rust port (faust-rs) is flagged by the project as exploratory and not production-ready.

## Links

- [Faust homepage](https://faust.grame.fr)
- [GitHub repository (README)](https://github.com/grame-cncm/faust)
- [Faust Playground (compile in the browser)](https://faustplayground.grame.fr/)
