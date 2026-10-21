---
name: geph4
title: geph4
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, censorship, network, protocol, proxy, tunnel]
homepage: https://geph.io/
scout_score: 5
status: draft
---

# geph4

**TLDR;** A command-line client for Geph, a censorship-circumvention tunnel that rotates bridge routes and opens local SOCKS5 and HTTP proxies.

geph4-client connects to a Geph exit server and exposes the tunnel as local proxies on 127.0.0.1, SOCKS5 on port 9909 and HTTP on 9910 by default. On Linux it can also route the whole system through a TUN device, and on Windows it uses WinDivert. There are a few other subcommands, `sync`, `binder_proxy` and `debugpack`, which are mostly used by the GUI or for exporting debug logs.

The README calls Geph "a modular Internet censorship circumvention system designed specifically to deal with national filtering." The homepage frames it as a VPN built from the ground up to resist ISP-level censorship, instead of one that plays cat-and-mouse with censors.

The interesting idea is the transport. `connect` builds a tunnel that keeps a sosistab2 Multiplex session alive over several routes at once, some direct and some through bridges, and switches to the best one that works. Where exits are blocked outright, as in China, only bridge routes are used. Blocked bridges get swapped out as the client rotates through them.

The `sync` step fetches subscription and exit information through domain fronting. It then checks the exit list against a public record on the Mel blockchain, so a compromised central server cannot quietly hand the client bad exits. Reading how those pieces fit together is a good way into how national filtering works and how tunnels are built to survive it.

## Install

```
brew install geph4
# Alternative from the README: install Rust, then run `cargo install geph4-client`
# VPN mode needs root. Connecting needs credentials; the README uses public demo accounts.
```

## Try this

```
geph4-client -h
```
Lists the subcommands and flags.

```
geph4-client connect --exit-server 2.mtl.ca.ngexits.geph.io auth-password --username public5 --password public5
```
Connects through a named exit server with the README's public demo account and opens local SOCKS5 and HTTP proxies on ports 9909 and 9910.

```
geph4-client debugpack --export-to /your/preferred/path/
```
Exports Geph's debug logs as an SQLite database to the directory you give.

## What's unique

It keeps a multiplex of routes and rotates bridges instead of relying on one fixed server. It also checks its exit list against a public blockchain record.

## Caveats

This is the older client and the brief could not confirm it is still maintained. VPN mode needs root and is not supported on macOS, and the README examples hard-code an exit server and public demo credentials.

## Links

- [Geph homepage](https://geph.io/)
- [geph4 repository (README source)](https://github.com/geph-official/geph4)
- [sosistab2 (transport library)](https://github.com/geph-official/sosistab2)
