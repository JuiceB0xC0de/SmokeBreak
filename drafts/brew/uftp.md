---
name: uftp
title: UFTP
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, encryption, multicast, network, protocol, udp]
homepage: https://uftp-multicast.sourceforge.net/
scout_score: 6
status: draft
---

# UFTP

**TLDR;** Sends one encrypted file stream over UDP multicast to many receivers at once, repairing losses with selective retransmits. A door into one-to-many delivery.

UFTP is a family of programs for sending files to many receivers simultaneously. The server (`uftp`) reads files and sends them at a rate you set. Each receiver (`uftpd`) catches the same multicast stream and reassembles the file. Because UDP does not guarantee order, every block is numbered. In the project's words: "Because UDP does not guarantee that packets will arrive in order, each block is numbered so the client can properly reassemble the file."

Reliability comes from negative acknowledgments. Receivers stay quiet when things go well and report only the blocks they missed, at section or end-of-file boundaries. The server then retransmits just those blocks. A session runs in three phases: announce and register, file transfer, then completion and confirmation. Keys are negotiated with a TLS-based scheme extended so that many receivers share one group key.

The homepage says it was built for satellite links with two-way communication, where propagation delay makes TCP-based transfer highly inefficient. Sending once and repairing only the gaps avoids paying a round trip per window for every receiver.

The optional proxy (`uftpproxyd`) handles networks where multicast does not reach. It supports NAT traversal and multicast tunneling, and aggregates receiver responses on the way back. `uftp_keymgt` manages keys.

## Install

```
brew install uftp
# depends on openssl@4, which brew pulls in
```

## Try this

```
uftp --help
```
Lists the sender's options, including the send rate and multicast settings.

```
uftpd --help
```
Shows the receiver daemon's options.

```
uftp_keymgt --help
```
Shows the key management utility's options.

## What's unique

Encrypted multicast delivery with NAK-based selective repeat and a shared TLS-derived group key is uncommon. Proxies let receivers behind NAT or without multicast routing take part.

## Caveats

Real multicast needs network support that many home and cloud networks lack, and the homepage's release dates are inconsistent, so maintenance status is unclear.

## Links

- [UFTP homepage](https://uftp-multicast.sourceforge.net/)
