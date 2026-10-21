---
name: ladspa-sdk
title: LADSPA SDK
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, ancient, audio, c, linux-audio, plugins]
homepage: https://www.ladspa.org
scout_score: 5
status: draft
---

# LADSPA SDK

**TLDR;** The reference kit for LADSPA, a deliberately tiny 2000-era audio plugin standard, with three small command-line hosts and example plugins you can run.

LADSPA, the Linux Audio Developer's Simple Plugin API, is a standard for audio effects and processors. A developer compiles an effect such as a reverb into a shared library, and any LADSPA-aware host can load it. The homepage lists Ardour, Audacity, LMMS, Rosegarden, Csound and Pd among the hosts. The whole API lives in a single C header file.

The SDK adds terse documentation, ten example plugins, and three trivial command-line hosts: listplugins, analyseplugin and applyplugin. They let you see plugins without opening a full audio workstation. Hosts find plugin libraries by searching the colon-separated directories in the LADSPA_PATH environment variable, or the locations your distribution manages.

The interesting part is how much the design leaves out. The API handles only 32-bit floating point audio, on purpose, and it imposes no architecture on the host, which decides how to wire plugins together. The homepage says it aims to be "a good compromise between functionality, intuition and compatibility but is simple. The "S" in "LADSPA" is meant seriously." It was proposed on the Linux Audio Developer mailing list, and version 1 was finalised on 2 April 2000.

That makes it a short, readable case study in plugin API design. You can read the header in one sitting, then see why a standard this small still sits under a large ecosystem of Linux audio plugins.

## Install

```
brew install ladspa-sdk
# Depends on libsndfile. Plugins themselves are separate libraries; if a host cannot find them, set LADSPA_PATH to a colon-separated list of directories.
```

## Try this

```
listplugins
```
Lists the LADSPA plugins found on your system. It only finds them if LADSPA_PATH points at the directories holding plugin libraries.

```
analyseplugin --help
```
Shows usage for the small host that inspects a plugin library. The homepage names it but gives no usage, so check the help output.

```
applyplugin --help
```
Shows usage for the host that runs a plugin over an audio file. The homepage shows no command line for it.

## What's unique

It is a plugin standard whose authors deliberately kept it small, with float-only audio and no imposed host architecture. The whole API fits in one C header.

## Caveats

The homepage gives no release date or version beyond 1.1, the SDK is mostly developer material, and the brief could not confirm how it behaves on modern systems or what the three hosts print.

## Links

- [LADSPA homepage](https://www.ladspa.org)
- [linux-sound.org LADSPA page (other resources)](http://linux-sound.org/ladspa.html)
- [Steve Harris plugin collection](http://plugin.org.uk/)
