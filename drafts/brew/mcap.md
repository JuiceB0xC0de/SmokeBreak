---
name: mcap
title: mcap
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binary, file-format, logging, robotics, ros]
homepage: https://mcap.dev
scout_score: 5
status: draft
---

# mcap

**TLDR;** A command-line tool for MCAP, the self-describing container format that robots use to record timestamped sensor and message streams into one file.

MCAP (pronounced "em-cap") is an open source container file format for multimodal log data. It holds many channels of pre-serialized, timestamped messages in a single file. The messages can be Protobuf, DDS (CDR), ROS, JSON or anything else, because the format does not care how they were encoded. The `mcap` CLI is the tool for looking inside these files: it can inspect, merge and split them.

The idea underneath is that a log file should outlive the code that wrote it. Schemas are stored inside the file next to the data, so a reader years later can still make sense of the messages even after the codebase has changed. Serialization stays the user's problem; the container only handles framing, channels, timing and bookkeeping.

Files are row-oriented and append-only. The homepage says this minimizes disk I/O and reduces corruption risk on unclean shutdowns, which matters when a robot loses power mid-recording. Optional features include an index for fast seeking, chunk-based compression with LZ4 or Zstandard, and CRC checksums.

The format is written up in a public spec, and the repo includes a Kaitai Struct definition, so it is a readable example of how to design a binary log format. The homepage says MCAP is the default log format in ROS 2. It comes from the Foxglove project, and libraries exist for Python, TypeScript, Rust, C++, Go and Swift.

## Install

```
brew install mcap
# Or download the CLI from https://github.com/foxglove/mcap/releases?q=cli
# No hardware or account needed. You will need an .mcap file to inspect; the CLI guide covers where to get one.
```

## Try this

```
mcap --help
```
Lists the available subcommands, including those for inspecting, merging and splitting MCAP files.

## What's unique

The file carries its own schemas and leaves serialization to you, so one container can hold Protobuf, ROS, JSON and other messages and still be readable later.

## Caveats

It is a file format and libraries rather than an interactive app, so the CLI is only worth trying if you have an MCAP file to open, and the brief could not confirm recent release activity.

## Links

- [Homepage](https://mcap.dev)
- [File format specification](https://mcap.dev/spec)
- [CLI guide](https://mcap.dev/guides/cli)
- [Motivation paper (evaluation.pdf)](https://mcap.dev/files/evaluation.pdf)
