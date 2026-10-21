---
name: jack
title: JACK
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, daemon, midi, real-time, routing]
homepage: https://jackaudio.org/
scout_score: 6
status: draft
---

# JACK

**TLDR;** A real-time audio server that lets any program's sound output feed another program's input, treating audio and MIDI as one patchable graph.

JACK (JACK Audio Connection Kit) is a sound server API with a pair of daemon implementations. Programs connect to it as clients, and the server moves audio and MIDI between them with low latency. The homepage opens with a question: "Have you ever wanted to take the audio output of one piece of software and send it to another?" That is the whole pitch. One program's output can feed another program's input, or several, and the result can be recorded back in the first program.

Underneath is a processing graph. The server drives it, and each client runs once per audio cycle. The JACK2 README (jackdmp, a C++ implementation aimed at multiprocessor machines) describes a data-flow activation model. Clients that don't depend on each other in the graph can run at the same time. The graph is accessed without locks, so connections can change while audio keeps playing.

The server can run in synchronous mode, waiting for every client each cycle. In asynchronous mode it reuses the previous cycle's output for any client that misses its deadline. A late client then gives a partial result rather than a dropout for everyone.

The idea it opens up is modular audio: small programs that each do one thing with sound, wired together like a patch bay. For developers, JACK offers a cross-platform API for device sharing and routing between applications, which the homepage calls easy to learn and use.

## Install

```
brew install jack
```

## Try this

```
jackd --help
```
Prints the server's options, including how to choose a driver and set up the audio device it will run on.

## What's unique

JACK treats audio and MIDI as one real-time routing graph that any program can join. With JACK2, a late client degrades gracefully instead of stalling the whole chain.

## Caveats

The pages read give no usage examples, no release dates, and no word on which JACK implementation the Homebrew formula installs, and the README's Travis CI badge points to a legacy service.

## Links

- [JACK homepage](https://jackaudio.org/)
- [JACK2 source repository (GitHub)](https://github.com/jackaudio/jack2)
- [JACK wiki](https://github.com/jackaudio/jackaudio.github.com/wiki)
