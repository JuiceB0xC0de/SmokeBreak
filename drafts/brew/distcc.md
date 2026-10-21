---
name: distcc
title: distcc
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, ancient, build, c, compiler, distributed, network, protocol]
homepage: https://github.com/distcc/distcc/
scout_score: 5
status: draft
---

# distcc

**TLDR;** distcc spreads C and C++ compile jobs across machines on your network by shipping preprocessed source to volunteer servers and getting object files back.

distcc is a front-end for your existing compiler. You run a normal build, usually `make -j` with `CC=distcc`, and each compile job is sent over the network to a machine running the `distccd` daemon. The client runs the preprocessor locally and sends the full preprocessed source. The server runs gcc or clang and returns the object file. distcc is not a compiler itself.

The design choice is the interesting part. The README contrasts distcc with other distributed build systems that need a shared filesystem, synchronized clocks, or identical libraries and headers on every machine. Because distcc ships preprocessed source, none of that is needed: any machine with a compiler can join. In the project's words, "Shipping files across the network takes time, but few cycles on the client machine."

There is also a pump mode, added in distcc 3.0, which moves preprocessing onto the servers too, so the client does no preprocessing at all. The cost is that client and server must have matching system headers. The stated goals are that results always match a local compile, that it is simple to install and use, and that it is often two or more times faster.

The idea underneath is a small, old example of farming out work over a simple protocol with very few assumptions about the machines involved. It is worth reading even if you never build anything large with it.

## Install

```
brew install distcc
# Needs a C/C++ compiler (gcc or clang) on each server machine. Upstream route on other machines: ./configure && make && sudo make install
# No accounts or special hardware. Depends on python@3.15 via brew.
```

## Try this

```
distccd --daemon
```
Starts the distcc server on a machine. The docs say to add --allow options to restrict who can connect.

```
export DISTCC_POTENTIAL_HOSTS='localhost red green blue'
```
Tells the client which servers it may send jobs to. The host names here are examples from the docs.

```
cd ~/work/myproject; pump make -j8 CC=distcc
```
Runs a parallel build through the pump wrapper, with compile jobs sent out to the listed servers.

## What's unique

It needs no shared filesystem, synchronized clocks, or matching libraries, because it sends preprocessed source over the wire. Pump mode goes further and offloads preprocessing as well.

## Caveats

The docs are from the early 2000s and the README shows no recent activity, so treat it as quiet rather than actively maintained; gcc is the main focus, clang is supported, and pump mode needs matching system headers on client and server.

## Links

- [GitHub repository (homepage)](https://github.com/distcc/distcc/)
- [Documentation site](https://distcc.github.io/)
- [Stack Overflow tag](http://stackoverflow.com/questions/tagged/distcc)
