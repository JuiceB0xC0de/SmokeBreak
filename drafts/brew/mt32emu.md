---
name: mt32emu
title: mt32emu (Munt)
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, emulation, library, midi, vintage-hardware]
homepage: https://github.com/munt/munt
scout_score: 7
status: draft
---

# mt32emu (Munt)

**TLDR;** A software emulation of the Roland MT-32 synthesiser modules, the sound module behind a generation of DOS game music, usable as a library or through a Qt app.

Munt is a monorepo built around mt32emu, a C/C++ library that approximates the Roland MT-32, CM-32L and LAPC-I synthesiser modules in software. Front ends feed it MIDI messages and it returns rendered audio. The main end-user program is mt32emu_qt, a Qt GUI that accepts MIDI from virtual or real ports or from Standard MIDI files, and can render those files to WAV or RAW. Other pieces include an SMF-to-WAV converter, a Windows MME driver, a Linux ALSA driver and a DOSBox patch.

The project exists so that developers can embed an MT-32 in a driver or application, and so that people can play MIDI through one on an ordinary computer. The README is upfront that the emulation is approximate. The Qt app also "Emulates the funny MT-32 LCD" and shows the synth's internal state in real time, so you can watch the little display and the parts react as notes arrive.

The idea underneath is that a synth of this kind is a set of sampled sounds plus a particular synthesis engine and a MIDI interface. Reproducing it in software means reproducing that behaviour closely enough to sound right, in real time. That makes the project a way into MIDI routing (CoreMIDI, ALSA sequencer, JACK MIDI, raw ports) and into how old hardware gets preserved in code.

Before you start: the READMEs I read do not say where the Roland control and PCM ROM images come from. mt32emu_qt has a GUI to manage ROMs, but expect to supply them yourself.

## Install

```
brew install mt32emu
# Homebrew installs the library (no executables). For the Qt app, build mt32emu_qt from the munt repo with CMake and Qt (4 to 6).
# You will also need to supply your own Roland ROM images.
```

## Try this

```
cmake -DCMAKE_BUILD_TYPE:STRING=Release .
```
Configures an in-tree build of mt32emu_qt with optimisations on; the README says they are off by default.

```
make
```
Compiles the app after the CMake configure step.

```
sudo modprobe snd_virmidi
```
On Linux, loads the kernel module that creates virtual raw MIDI ports (4 by default), bound to ALSA sequencer ports.

## What's unique

It emulates the MT-32's LCD and shows the synth's internal state live. It is also a library others can embed, with MIDI support across several systems including a JACK mode.

## Caveats

The brew formula installs only the library, with no executables; the GUI needs a separate source build, you must supply your own ROM images, and the README calls the emulation approximate.

## Links

- [Munt monorepo (homepage)](https://github.com/munt/munt)
- [mt32emu_qt README](https://github.com/munt/munt/tree/master/mt32emu_qt)
- [Roland MT-32 on Wikipedia](https://en.wikipedia.org/wiki/Roland_MT-32)
