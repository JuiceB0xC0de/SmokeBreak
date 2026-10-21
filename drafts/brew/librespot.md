---
name: librespot
title: librespot
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, audio, library, network, protocol, rust, spotify]
homepage: https://github.com/librespot-org/librespot
scout_score: 5
status: draft
---

# librespot

**TLDR;** An open-source Spotify Connect client in Rust that turns any computer into a headless speaker your Spotify app can see and play to.

librespot is a client library for Spotify, written in Rust. It can act as a Spotify Connect receiver: run the bundled program, and a new device appears in the Spotify app on your phone. Pick it, and the audio plays through whatever machine is running librespot. Playback goes through Rodio by default, with ALSA, GStreamer, PortAudio, PulseAudio, JACK, SDL, Pipe and Subprocess available as other backends.

The README presents it as an alternative to the official closed-source libspotify, which it describes as now deprecated, and says it will also offer extra features the official library does not. The current organisation exists because the original project by plietar is no longer actively maintained, so this fork was set up to keep it maintained and upgraded.

The interesting part is that it is a library first. Other projects embed it, including Spotifyd, ncspot, Snapcast and raspotify. The README does not explain the internals, but it points to a docs folder with brief protocol documentation and says the best way to learn how it works is to read the code. That makes it a way into how a commercial streaming service's device protocol is put together.

A cache directory, if you set one, holds an authentication blob. The README recommends permissions of 700 on it.

## Install

```
brew install librespot
# Requires a Spotify Premium account. Free accounts are not supported and the README says that will not change.
# The README's own route is `cargo install librespot`; on Linux, building from source needs ALSA headers (libasound2-dev on Debian/Ubuntu, alsa-lib-devel on Fedora).
```

## Try this

```
librespot --name DEVICENAME
```
Starts the minimal headless Spotify Connect receiver; a device with that name shows up in your Spotify app.

```
librespot -n "Librespot Speaker" -b 160
```
Creates a speaker called Librespot Speaker serving 160 kbps audio.

```
librespot -n "Librespot" -b 320 -c ./cache --enable-volume-normalisation --initial-volume 75 --device-type avr
```
Runs at 320 kbps with a cache folder and volume normalisation, starts at volume 75, and appears in the app as an Audio/Video Receiver.

## What's unique

It is a reusable library rather than just a player, so a whole family of other Spotify tools are built on it. Its README also lists an unusually long set of audio backends.

## Caveats

It needs Spotify Premium, and the README's disclaimer says connecting to Spotify's API this way is probably forbidden by Spotify, so use is at your own risk.

## Links

- [GitHub repository (homepage)](https://github.com/librespot-org/librespot)
- [crates.io package](https://crates.io/crates/librespot)
- [Options wiki page (runtime flags)](https://github.com/librespot-org/librespot/wiki/Options)
