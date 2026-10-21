---
name: baresip
title: baresip
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, audio, network, protocol, sip, tui, voip]
homepage: https://github.com/baresip/baresip
scout_score: 5
status: draft
---

# baresip

**TLDR;** A small, modular SIP softphone in C that lets you watch a VoIP call get set up, negotiated and carried, all from a terminal.

Baresip is a SIP user agent: a softphone without the phone. It registers an account with a SIP server, places and receives calls, and carries audio and video over RTP. It is a C library of protocol modules plus a thin front end, and the README lists a console, a menu UI, an embedded HTTP server and a TCP/UDP control console among its interfaces.

The project describes itself as a "Minimalistic and modular VoIP client", with a focus on RFC compliance, robustness, low footprint and portable C99/C11 code. The core stack is SIP for signaling, SDP for describing media, RTP/RTCP for carrying it, and STUN/TURN/ICE for getting through NAT.

That split is the door into something larger. A phone call on the internet is two conversations: one that says who is calling whom and what formats each side can handle, and another that moves the actual sound. Baresip keeps those layers visible. Codecs (g711, opus), audio drivers (alsa, pulse, coreaudio, pipewire), NAT traversal, and encryption (srtp, dtls_srtp, gzrtp) are each a separate plug-in module. The build only compiles the ones you ask for, and only when their dependencies are installed.

Config files are generated in `$HOME/.baresip` on first run, so you can read them to see what the client assumes by default. You will need a SIP account or server to place a real call.

## Install

```
brew install baresip
# You need a SIP account (from a provider or your own server) to place real calls.
# Config files are generated in $HOME/.baresip on first run.
```

## Try this

```
baresip --help
```
Lists the command-line options, a quick view of what the client can be told to do.

```
baresip
```
Starts the client; on first run it generates its config files in $HOME/.baresip, which you can open and read.

## What's unique

The feature surface is unusually broad for a small C project: video, conferencing, TLS/SRTP/ZRTP/DTLS-SRTP, ICE/TURN, even MQTT and a JSON TCP control interface, all as optional modules.

## Caveats

It needs a SIP account to do anything interesting, and the README gives no version or release date, so the config wiki is the real starting point.

## Links

- [GitHub repository and README](https://github.com/baresip/baresip)
- [Configuration wiki](https://github.com/baresip/baresip/wiki/Configuration)
- [Configuration examples](https://github.com/baresip/baresip/tree/master/docs/examples)
- [Mailing list](https://groups.google.com/g/baresip)
