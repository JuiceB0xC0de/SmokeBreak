---
name: dumbpipe
title: dumbpipe
source: brew
category: fundamentals
commitment: quick
tags: [nat-traversal, network, pipes, protocol, quic, quick]
homepage: https://dumbpipe.dev
scout_score: 6
status: draft
---

# dumbpipe

**TLDR;** A netcat-style tool that pipes stdin and stdout between two machines anywhere, addressed by a long key instead of an IP address.

Dumbpipe connects two machines directly and moves bytes between them, like a Unix pipe that crosses the network. Run `dumbpipe listen` on one machine and it prints a ticket, a long node identifier. On the other machine, run `dumbpipe connect <ticket>` with something on stdin, and the bytes come out on the listener's stdout. There are also TCP and Unix-socket variants that forward a local port or socket across the same connection.

The idea underneath is addressing by identity. Instead of an IP address, the peer is a 256-bit endpoint ID, so it can move between networks and still be found. The tool is a thin wrapper around the iroh Rust crate, which makes QUIC connections over what it calls a magic socket. It tries NAT hole punching first. When a direct path is impossible, it falls back to a mesh of relay nodes that carry UDP traffic over HTTP. The homepage estimates this fallback applies to 10-20% of connections. Connections are encrypted with TLS and can multiplex streams.

The README shows how far a plain pipe stretches: streaming a camera feed from ffmpeg into ffplay, sharing a terminal session, forwarding a dev server port, or exposing a Zellij session's Unix socket. It also lets you set a custom ALPN string to talk to other iroh protocols. The project's stance is that anything more, such as pubsub or sync, makes the pipe no longer dumb: "You decide how to feel about that."

## Install

```
brew install dumbpipe
# alternatives: cargo install dumbpipe, or curl -sL https://www.dumbpipe.dev/install.sh | sh
# you need two machines (or two terminals) to see it work
```

## Try this

```
dumbpipe listen
```
Generates a secret key on first run, then prints a ticket and a ready-to-copy `dumbpipe connect` line for the other machine.

```
echo "hello" | dumbpipe connect <ticket>
```
Sends the text to the listener using the ticket, and it appears on the listener's stdout.

```
dumbpipe connect-tcp --addr 0.0.0.0:3001 <ticket>
```
Listens on local port 3001 and forwards connections through the pipe to the service exposed by the remote listener.

## What's unique

Peers are addressed by key rather than IP, with NAT traversal and relay fallback built in, so a netcat-like workflow works between machines on different networks with no accounts or config.

## Caveats

The default relay network has capped bandwidth, and the README calls the project an example of what iroh can do; I found no release or last-commit date.

## Links

- [Homepage](https://dumbpipe.dev)
- [GitHub repository and README](https://github.com/n0-computer/dumbpipe)
- [iroh on crates.io (the underlying library)](https://crates.io/crates/iroh)
