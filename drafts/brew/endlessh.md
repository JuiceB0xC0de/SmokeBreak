---
name: endlessh
title: endlessh
source: brew
category: fundamentals
commitment: quick
tags: [network, protocol, quick, security, ssh, tarpit]
homepage: https://github.com/skeeto/endlessh
scout_score: 8
status: draft
---

# endlessh

**TLDR;** An SSH tarpit that listens on a port and drips an endless, random banner to anything that connects, leaving bots stuck for hours.

Endlessh listens on a TCP port (2222 by default) and, for each client that connects, sends one random banner line every few seconds. It never finishes. A client that follows the protocol politely keeps waiting. The README says it "keeps SSH clients locked up for hours or even days at a time."

The trick sits in the earliest part of an SSH connection. Before any key exchange or encryption, the server may send lines of text ahead of its version string, and the client is expected to read them. Endlessh stays in that phase indefinitely, so it needs no crypto libraries. It is a single-threaded C program that uses poll() to hold many clients at once. Line length is randomized up to a configurable maximum, and the delay between lines is set in milliseconds.

The intended use is to move your real SSH server to another port and put endlessh on the one scanners hit. The author's stated aim is to let script kiddies get stuck in the tarpit instead of bothering a real server. It is also a small, readable example of how much a protocol's own patience can be used against a client. The author has a blog post going into the idea.

The config file reads much like OpenSSH config, and SIGHUP reloads it without a restart.

## Install

```
brew install endlessh

The default port is 2222, so you can try it without touching your real SSH server. To use it as a real tarpit, you would first move sshd off port 22.
```

## Try this

```
endlessh --help
```
Prints the available options, such as port, delay, maximum line length and config file.

```
endlessh -v >endlessh.log 2>endlessh.err
```
Runs the tarpit with verbose logging on the default port, writing activity to endlessh.log and errors to endlessh.err.

## What's unique

It needs no cryptography and no threads. It wins by stalling clients in the banner stage with a poll() loop.

## Caveats

Logging is off unless you pass -v, and the README does not explain how to move your real SSH server off port 22, nor does it give any information on release dates or upkeep.

## Links

- [Endlessh GitHub repository](https://github.com/skeeto/endlessh)
- [Author's blog post on the tarpit](https://nullprogram.com/blog/2019/03/22/)
