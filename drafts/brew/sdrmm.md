---
name: sdrmm
title: SDR-- (sdrmm)
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, decoders, needs-hardware, network, sdr, server]
homepage: https://github.com/Newspicel/sdrminusminus
scout_score: 5
status: draft
---

# SDR-- (sdrmm)

**TLDR;** A patch-cable style software-defined radio app that runs on your desktop or on a server beside the antenna, with a browser as the front panel.

SDR-- is an application for listening to, decoding, and recording radio signals. You plug in a radio, with an RTL-SDR dongle as the README's first example, and build a signal chain out of nodes on a canvas. A Device node produces raw IQ samples, a channel node such as WFM turns them into audio, and a Speaker node plays it. You connect them with wires in the Patch view.

The idea underneath is that a software-defined radio is just a stream of samples passing through stages. Here every stage is a visible box. Wiring Device iq to WFM iq, then WFM audio to the Speaker, shows the whole path from antenna to sound. Nodes you use often can be pinned to a simpler Rack view with the p key.

The architecture is the other draw. In the README's words: "Run the desktop app with a local SDR, or place the server near your antenna and connect through a browser. Both use the same receiver engine and interface." The radio can sit in a window, an attic, or a shed while you tune from elsewhere. Automation is exposed through REST, WebSocket, and MCP APIs, and a phone remote is offered.

The decoder catalogue is broad: aircraft, ships, pagers, digital voice, weather satellites, DAB, DVB, and more. Outputs include audio, decoded messages, maps, recordings, and network IQ.

## Install

```
brew install sdrmm
# this is the server formula; the desktop app is a separate cask: brew install sdrmm-app
# needs an SDR such as an RTL-SDR dongle (Airspy, AntSDR, FUNcube Dongle, Aaronia and KrakenRF are also listed); the formula pulls in ffmpeg
```

## Try this

```
sdrmm --help
```
Lists the server's options, a starting point before you open the browser interface.

```
brew install sdrmm-app
```
Installs the desktop app via the Homebrew cask, for use with a locally attached SDR.

```
docker pull ghcr.io/newspicel/sdrmm:nightly
```
Pulls the nightly container image, a build of main replaced every night, if you would rather run the server in Docker.

## What's unique

It pairs a visual patch-and-rack signal graph with a very wide decoder catalogue in one app. The same engine runs locally or remotely behind a browser, with REST, WebSocket, and MCP automation, which is unusual for a radio tool.

## Caveats

You need real SDR hardware to get anything out of it, v2.3.0 flags breaking REST API changes, and the repo and brew naming is split between SDR--, sdrminusminus, and sdrmm.

## Links

- [Homepage / GitHub repo](https://github.com/Newspicel/sdrminusminus)
- [Documentation](https://sdrmm.com/docs/)
- [GitHub releases](https://github.com/Newspicel/sdrmm/releases)
