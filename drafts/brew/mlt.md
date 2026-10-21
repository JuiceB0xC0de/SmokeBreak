---
name: mlt
title: MLT
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, audio, cli, ffmpeg, video, xml]
homepage: https://www.mltframework.org/
scout_score: 5
status: draft
---

# MLT

**TLDR;** The multitrack video engine behind Shotcut, Kdenlive and Flowblade, with a melt command that plays and renders compositions described in XML.

MLT is an open source multimedia framework for authoring, managing and running multitrack audio and video compositions. Its homepage says it was "designed and developed for television broadcasting." Media clips, XML composition files and filter or transition plug-ins go in, and rendered or played audio and video come out.

Most people meet it indirectly. Shotcut, Kdenlive and Flowblade are all built on it. The Homebrew formula installs `melt`, the command-line player and renderer that sits on the same engine, so you can use it without any editor in front of it.

The idea underneath is that a timeline does not have to live in a GUI. MLT describes a composition in a declarative XML format, so a project is a file that tools can read, generate, diff and render. The release notes mention producers, consumers, filters, transitions and tractors, which is the vocabulary of that model. Filters come from a wide plug-in ecosystem, including frei0r, LADSPA, LV2, VST2, OpenFX, Movit and libplacebo.

The README is a build and install reference and sends you to the docs for usage, so the front door is a bit bare. The homepage suggests that "the easiest way to try out and learn MLT is by downloading Shotcut." Using melt directly is the way to see the engine without the editor around it.

## Install

```
brew install mlt
# installs the melt and melt-7 executables; the formula pulls in ffmpeg, opencv, Qt and many other libraries, so expect a large download
```

## Try this

```
melt --help
```
Prints melt's usage, which is the quickest way to see what the player and renderer accept.

```
melt video.mp4
```
Plays a video file of your choosing through melt's player. On Linux the README sets SDL_AUDIODRIVER=alsa in front of this when the default audio driver is a dummy.

## What's unique

It is the shared engine under several desktop video editors, and it exposes that engine as a command-line tool and an XML composition format. Most video tools only give you the GUI.

## Caveats

The README covers building and installing rather than usage, so you will be reading the docs; the sox filter is deprecated, and some features depend on optional libraries.

## Links

- [MLT homepage](https://www.mltframework.org/)
- [Documentation](https://www.mltframework.org/docs/)
- [Install guide](https://mltframework.org/docs/install/)
- [GitHub repository](https://github.com/mltframework/mlt)
