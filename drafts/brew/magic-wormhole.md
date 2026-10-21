---
name: magic-wormhole
title: magic-wormhole
source: brew
category: fundamentals
commitment: quick
tags: [cli, cryptography, network, pake, protocol, quick]
homepage: https://magic-wormhole.readthedocs.io/en/latest/
scout_score: 5
status: draft
---

# magic-wormhole

**TLDR;** Send a file between two computers by reading a short code aloud, with end-to-end encryption and no accounts or shared server.

Magic Wormhole is a Python library and a command-line tool, `wormhole`, for moving files, directories, short text, or other network streams from one machine to another. The sender runs a command that prints a short code such as 7-crossover-clockwork. The receiver types that code into a second command, confirms, and the data arrives. The code is single-use and does not need to be memorized.

The docs frame it as a tool for when the humans can talk to each other but the computers cannot. They contrast it with USB sticks, scp/ssh (which needs prior accounts), email, and Dropbox links. Passwords and SSH keys are named as the main use case. The name comes from the image of two wizards speaking the same phrase to open a connection between them.

The idea underneath is a password-authenticated key exchange. Both peers run SPAKE2, treating the short, low-entropy code as the password, and derive a strong shared key from it. Each code works only once, so a man-in-the-middle gets a single guess, and failed guesses show up as errors on the other side. In the project's words: "Each code is one-time use only, so attackers (e.g. a malicious Mailbox server) get only a single guess when attempting to subvert a connection."

The plumbing is modest. A mailbox server, a WebSocket relay, carries the first messages so nobody needs an IP address. The peers then swap network hints and try a direct connection. If that fails, a Transit Relay glues the two TCP connections together. All traffic is encrypted with keys derived from the PAKE secret, so the relays never see the contents.

## Install

```
brew install magic-wormhole
# No account or server setup needed: a public mailbox server and transit relay are built in.
# Both peers need the tool installed, and they must use the same mailbox server (--relay-url overrides the default).
```

## Try this

```
wormhole send README.md
```
Sends a file and prints a wormhole code for the receiver to type.

```
wormhole receive
```
Prompts for the code, then asks for confirmation before writing the file.

```
wormhole send --text TEXT
```
Sends a short string of text instead of a file.

## What's unique

It needs no accounts, keys, or shared server, only a short phrase two people can say to each other. It also works as a PAKE building block for other applications.

## Caveats

Both peers must be online at the same time, within about an hour of each other, with no built-in timeouts, and the public mailbox and relay are best-effort and could be withdrawn if abused.

## Links

- [Documentation homepage](https://magic-wormhole.readthedocs.io/en/latest/)
- [Welcome page with the Example and install details](https://magic-wormhole.readthedocs.io/en/latest/welcome.html)
- [Source repository](https://github.com/magic-wormhole/magic-wormhole)
