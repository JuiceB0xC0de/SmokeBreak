---
name: vamp-plugin-sdk
title: Vamp Plugin SDK
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, c++, dsp, library, music-information-retrieval]
homepage: https://www.vamp-plugins.org/
scout_score: 6
status: draft
---

# Vamp Plugin SDK

**TLDR;** A plugin format for audio analysis: plugins listen to a file and return pitch curves, onset times and spectra instead of sound.

Vamp is an API and C/C++ SDK for audio analysis plugins. A host application loads a plugin and feeds it sampled audio. The plugin produces no audio back. It returns descriptive data such as note onset times, spectrograms, or curves like power and fundamental frequency. In the project's words, "a Vamp plugin does not generate audio output, but some sort of symbolic information instead".

It was built at the Centre for Digital Music at Queen Mary, University of London, for developers and DSP researchers. The idea is that feature extraction code should be written once and run in any host that speaks the format. Sonic Visualiser and Audacity can both load Vamp plugins.

Under the hood a plugin is a dynamic library exposing a plain C entry point, `vampGetPluginDescriptor`. A C++ layer sits on top, and a small hosting library handles plugin discovery, channel mixdown, block buffering and frequency-domain conversion. The SDK includes example plugins (ZeroCrossing, SpectralCentroid, PowerSpectrum, AmplitudeFollower, PercussionOnsetDetector, FixedTempoEstimator) and a skeleton for writing your own.

The Homebrew package installs two tools: `vamp-simple-host`, which runs a plugin over a whole audio file, and `vamp-rdf-template-generator`, aimed at linked-data use. Together they are a way into music information retrieval: turning a recording into structured data you can compute with.

## Install

```
brew install vamp-plugin-sdk
# Needs no account or hardware. You will need audio files and Vamp plugins to run it on. The SDK's example plugins are built from source with CMake (-DVAMPSDK_BUILD_EXAMPLE_PLUGINS=ON), and I did not check whether the Homebrew package ships them.
```

## Try this

```
vamp-simple-host --help
```
Prints usage and how to list available plugins and run one over an audio file.

```
vamp-rdf-template-generator --help
```
Shows the options for generating RDF description templates for a plugin.

```
cmake .. -DVAMPSDK_BUILD_EXAMPLE_PLUGINS=ON
```
From a build directory in the SDK source, configures a build that includes the example analysis plugins such as ZeroCrossing and SpectralCentroid.

## What's unique

Plugins return structured features rather than audio, so it works as a shared format for music analysis research. The plain C ABI keeps plugins portable across hosts.

## Caveats

It is aimed at C and C++ developers, and the simple host runs whole files with default parameters only; the README itself says it is not really simple.

## Links

- [Vamp homepage](https://www.vamp-plugins.org/)
- [SDK source and README (GitHub)](https://github.com/vamp-plugins/vamp-plugin-sdk)
- [Vamp plugin writing guide (PDF)](https://www.vamp-plugins.org/guide.pdf)
