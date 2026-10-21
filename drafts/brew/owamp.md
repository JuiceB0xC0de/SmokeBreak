---
name: owamp
title: owamp
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, latency, measurement, network, protocol]
homepage: https://www.internet2.edu/products-services/performance-analytics/performance-tools/
scout_score: 6
status: draft
---

# owamp

**TLDR;** Measures network latency and packet loss in each direction separately between two hosts, instead of blending them into one round-trip number like ping.

OWAMP is an implementation of the One-Way Active Measurement Protocol. Ping reports a round trip, which hides the fact that the path out and the path back are often different routes with different problems. OWAMP measures each direction on its own, so a slow or lossy leg shows up on the side where it actually happens.

The package installs seven executables: owampd, owfetch, owping, owstats, owtvec, owup, and powstream. The names suggest a daemon (owampd), a client (owping), and tools for fetching and summarising results (owfetch, owstats, powstream), but the brief could not confirm what each one takes in or emits, so check the `--help` output before assuming.

It comes out of the Internet2 performance tools, which the project describes as "Performance monitoring tools to help network engineers quickly identify service problems across national and international networks." The repo describes itself as "A tool for performing one-way or two-way active measurements." The idea underneath is that one-way timing is a different problem from round-trip timing, and a good door into how network measurement works.

## Install

```
brew install owamp
# pulls in the i2util dependency. Meaningful measurements need a second host running the daemon (owampd); setup and platform support were not confirmed.
```

## Try this

```
owping --help
```
Lists the options for the one-way ping client.

```
owampd --help
```
Shows how to run the measurement daemon that a remote owping would talk to.

```
powstream --help
```
Shows the options for the tool that appears to run continuous measurements.

## What's unique

It measures each direction of a path separately, so a one-way latency or loss figure is not mixed with the return path.

## Caveats

The brief could not retrieve the README, so usage, build requirements, clock-sync needs, and last release date are unverified, and the homepage is a generic Internet2 page.

## Links

- [Internet2 Performance Tools (homepage)](https://www.internet2.edu/products-services/performance-analytics/performance-tools/)
- [GitHub repository](https://github.com/perfsonar/owamp)
