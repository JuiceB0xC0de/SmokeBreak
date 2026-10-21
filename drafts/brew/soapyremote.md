---
name: soapyremote
title: SoapyRemote
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, needs-hardware, network, sdr, streaming, udp]
homepage: https://github.com/pothosware/SoapyRemote/wiki
scout_score: 6
status: draft
---

# SoapyRemote

**TLDR;** Turns any SoapySDR-supported radio into a network device, so software on one machine can tune and stream from an SDR plugged into another.

SoapyRemote has two halves. SoapySDRServer runs on the machine with the radio attached. A client plugin on another machine registers with SoapySDR, finds the server, and presents the remote radio as an ordinary local device. SoapySDRUtil and any application built on the SoapySDR API can then use it without changes.

The wiki pitches it this way: "The remote support feature can turn any SDR into a network peripheral." Its listed uses include sharing one device across several processes or hosts, adapting an IPv4-only SDR to an IPv6 network, and helping with embedded-device development.

The interesting part is the transport. Discovery, creation and configuration run over a simple RPC protocol on TCP. Sample streams use a separate windowed-datagram protocol over UDP, with flow-control messages so the sender never sends more than the receiver's socket buffers can hold. TCP streaming is available as an option. Radio samples are a continuous, high-rate stream, so this is a small look at what it takes to move them across a network without dropping them.

Stream behaviour is tuned with per-stream keys such as remote:format (for example CS16 or CS8 on the wire), remote:scale and remote:prot. The wiki explains the reasoning behind each, which makes it a readable primer on the bandwidth versus fidelity trade-offs.

## Install

```
brew install soapyremote
# Needs SoapySDR (installed as a dependency) and an SDR that SoapySDR supports.
# SoapyRemote must be installed on both the machine with the hardware and the client machine.
# On Ubuntu, avahi-daemon and libavahi-client-dev are recommended for discovery.
```

## Try this

```
SoapySDRServer --bind
```
Run on the machine with the radio. Starts the server with default binding so clients can discover and open the device.

```
SoapySDRUtil --find="remote=myServer"
```
Run on the client. Lists the devices on a named server instead of relying on auto-discovery.

```
SoapySDRServer --bind="0.0.0.0:1234"
```
Starts the server on a custom address and port.

## What's unique

The server is a transparent transport for the whole SoapySDR API, so existing SDR applications can use a remote radio with only extra device arguments. The wiki also documents the stream protocol and its tuning knobs.

## Caveats

Needs an SDR to be useful, and good performance on Linux takes tuning (larger socket buffers, possibly jumbo frames, thread priority); the wiki was last edited in 2019 and recent activity is unconfirmed.

## Links

- [Wiki (homepage)](https://github.com/pothosware/SoapyRemote/wiki)
- [Repository](https://github.com/pothosware/SoapyRemote)
- [SoapySDR wiki (dependency)](https://github.com/pothosware/SoapySDR/wiki)
- [Pothos SDR downloads (prebuilt installers)](https://github.com/pothosware/PothosCore/wiki/Downloads)
