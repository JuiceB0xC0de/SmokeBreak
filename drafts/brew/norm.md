---
name: norm
title: NORM
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, c, library, multicast, network, protocol]
homepage: https://www.nrl.navy.mil/itd/ncs/products/norm
scout_score: 6
status: draft
---

# NORM

**TLDR;** A reliable multicast transport protocol from the US Naval Research Laboratory, where receivers ask for what they missed instead of acknowledging everything, with a C library and demo apps.

NORM stands for NACK-Oriented Reliable Multicast. It is a transport protocol from the US Naval Research Laboratory, and the repository is its source release. The build produces libnorm, a static C library with an API in `normApi.h`, along with a command-line demo called `norm`, a small `normTest` playground, and API examples such as `normDataSend` and `normDataRecv`.

The name carries the central idea. In a typical reliable transport, the receiver acknowledges data and the sender tracks every receiver. With multicast, one sender may face a very large group, and per-packet acknowledgments from all of them would not work well. A NACK-oriented design flips it: receivers speak up only when they notice something missing. The README does not walk through this reasoning, so the details of how NORM does it are something to find in the code and the bundled guides.

The README also mentions two NRL applications built on NORM. One is a GUI multicast chat that shares files and images, described as "Like IRC with no server needed." The other is a tunnel for real-time UDP streams such as RTP. A NORP proxy lives in a `norp` directory. The demo app is described as "useful for file transfers (and streaming on Unix)."

The brief does not cover first-run usage in detail, so expect to read the API guides in the repo (PDF and HTML) and the example sources to see how it behaves.

## Install

```
No `brew install` line is confirmed by the brief, though a Homebrew formula named norm exists and installs no executables. To build from source: `git clone --recurse-submodules https://github.com/USNavalResearchLaboratory/norm.git`, then build with `./waf configure` and `./waf`. The protolib dependency is a git submodule; if you cloned without it, run `git submodule update --init`. Docker is an alternative, since the repo includes a Dockerfile. No accounts or hardware are mentioned.
```

## Try this

```
git clone --recurse-submodules https://github.com/USNavalResearchLaboratory/norm.git
```
Fetches the NORM source along with the protolib submodule it needs to build.

```
docker run -it --rm --name norm-send <norm:image> normDataSend
```
Starts the data-send example in a container built from the repo's Dockerfile, with <norm:image> standing in for your built image.

```
docker run -it --rm --name norm-recv <norm:image> normDataRecv
```
Starts the matching receiver in a second terminal to pick up what normDataSend sends.

## What's unique

It is a reliable multicast transport with a real C API and working demos, built on receivers requesting repairs rather than senders collecting acknowledgments. The server-free multicast chat app is an unusual showcase.

## Caveats

Maintenance status is unclear from the brief (the Docker default tag is v1.5.9), the NRL homepage returned 403, the license is NRL's own paragraph rather than a standard one, and the README says more tutorial material is still to come.

## Links

- [NRL NORM homepage (returned 403 when checked)](https://www.nrl.navy.mil/itd/ncs/products/norm)
- [GitHub source repository](https://github.com/USNavalResearchLaboratory/norm)
- [GitHub Discussions](https://github.com/USNavalResearchLaboratory/norm/discussions)
- [NORP proxy website](https://www.nrl.navy.mil/itd/ncs/products/norp)
