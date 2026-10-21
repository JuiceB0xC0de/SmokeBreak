---
name: i2pd
title: i2pd
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, anonymity, daemon, network, overlay-network, protocol]
homepage: https://i2pd.website/
scout_score: 6
status: draft
---

# i2pd

**TLDR;** A C++ router that joins I2P, an anonymous overlay network where websites and services live inside the network and hide their users' real IP addresses.

i2pd is the I2P Daemon, a C++ implementation of an I2P client. Running it makes your machine a node in I2P, which the README calls "a universal anonymous network layer." Participants do not reveal their real IP addresses, and all communication over the network is end-to-end encrypted.

The README lists the uses: anonymous peer-to-peer applications such as filesharing and cryptocurrencies, and anonymous client-server applications such as websites, instant messengers and chat servers. It also advertises a rich set of APIs for people building secure applications on top. The homepage frames the goal as a network "free from censorship" and "free from privacy violations."

The idea underneath is an overlay network: a second layer of addressing and routing that runs on top of the ordinary internet and keeps its own traffic inside it. Running a router is the practical way to learn how that works. The README does not describe the routing internals. The specifications at geti2p.net/spec and the docs at i2pd.readthedocs.io are the places to dig.

The project stresses a small footprint and simple dependencies, so it can run headless on a small machine. The homepage pitch is that leaving a node up around the clock helps the network. Configuration lives in a config file, and the repository ships an example at contrib/i2pd.conf.

## Install

```
brew install i2pd
# Configuration is via a config file; an example is at contrib/i2pd.conf in the repo. The run guide is in the user-guide docs.
```

## Try this

```
i2pd --help
```
Prints the daemon's command-line options, a starting point before you read the example config file.

## What's unique

It is a complete I2P router in C++ with a small footprint and few dependencies, so it runs headless on many platforms, including as a Docker image or Snap, instead of requiring a heavier runtime.

## Caveats

The fetched pages give no first-run steps or release dates, so expect to read the docs and the example config before the router does anything useful.

## Links

- [Homepage](https://i2pd.website/)
- [Documentation (readthedocs)](https://i2pd.readthedocs.io/en/latest/)
- [GitHub repository](https://github.com/PurpleI2P/i2pd)
- [Example config file](https://github.com/PurpleI2P/i2pd/blob/openssl/contrib/i2pd.conf)
