---
name: sshuttle
title: sshuttle
source: brew
category: fundamentals
commitment: quick
tags: [network, proxy, quick, ssh, tcp, vpn]
homepage: https://github.com/sshuttle/sshuttle
scout_score: 6
status: draft
---

# sshuttle

**TLDR;** Tunnels whole subnets over a plain SSH connection, so you reach a remote network by its real addresses without a VPN or admin rights.

sshuttle is a command-line proxy that sends your network traffic through an SSH connection. You give it a remote SSH host and the subnets you want to reach, and it forwards every port on those networks, not only the ones you named in advance. Programs on your machine see the remote hosts' real IP addresses, not a pile of localhost port mappings.

The README aims it at a specific situation: you can SSH into a remote network, there is no usable VPN, you may lack admin rights there, and OpenSSH port forwarding is too slow or fiddly for many hosts. It also points out that OpenSSH's PermitTunnel is off by default and carries TCP over TCP, which performs badly.

The idea underneath is the interesting part. The how-it-works page says sshuttle is "not exactly a VPN, and not exactly port forwarding." It tracks every connection: it reassembles the TCP stream locally, multiplexes it statefully over one SSH session, and splits it back into packets at the far end. In the project's words, "It's just data-over-TCP, which is safe." Reading that page is a short way into how transparent proxying and TCP behaviour work.

## Install

```
brew install sshuttle

Needs a host you can reach over SSH. I did not verify the client privileges or remote-side requirements, so check the Requirements page in the docs before the first run.
```

## Try this

```
sshuttle --help
```
Lists the options, including how to name the remote host and the subnets to route through it.

## What's unique

It keeps per-connection state instead of tunnelling raw packets, which avoids TCP-over-TCP. The README also says it knows of no other program that fits this combination of client OS, ssh-only access, no remote admin rights and no VPN.

## Caveats

Windows support is marked experimental, and I could not confirm recent release dates, though the project appears maintained.

## Links

- [Homepage (GitHub README)](https://github.com/sshuttle/sshuttle)
- [Documentation (stable)](https://sshuttle.readthedocs.io/en/stable/)
- [How it works](https://sshuttle.readthedocs.io/en/stable/how-it-works.html)
- [Installation](https://sshuttle.readthedocs.io/en/stable/installation.html)
