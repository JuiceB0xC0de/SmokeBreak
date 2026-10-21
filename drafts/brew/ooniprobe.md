---
name: ooniprobe
title: ooniprobe
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, censorship, measurement, network, open-data]
homepage: https://ooni.org/
scout_score: 6
status: draft
---

# ooniprobe

**TLDR;** A command-line client that tests what your own internet connection blocks or interferes with, and contributes the results to a public censorship dataset running since 2012.

ooniprobe runs network measurement tests from wherever you are. It checks whether websites and apps are reachable, and it measures the speed and performance of your connection. Each run produces measurements that are sent to the Open Observatory of Network Interference (OONI), which publishes them as an open dataset covering more than 200 countries.

The project describes itself as "a non-profit free software project that aims to empower decentralized efforts in documenting Internet censorship around the world." The idea is that censorship is hard to prove from the outside. Many people each measure their own connection, and the combined data shows what is blocked, where, and when.

Under the hood, the README describes a measurement engine written in Go, a test helper server called oohelperd, and an experimental client called miniooni. The CLI also links a Rust library used for user authentication. The brief did not cover the individual test mechanisms in detail, so the docs are the place to learn what each test does.

The CLI is one of several clients. The project also ships desktop, Android and iOS apps. Per the install page, once installed it runs tests automatically every day, so it can work as a quiet background sensor on your machine.

## Install

```
brew install ooniprobe
# the formula depends on tor, which brew installs for you
# optional: turn on the daily automatic run
ooniprobe autorun start
```

## Try this

```
ooniprobe --help
```
Lists the available subcommands and options for the client.

```
ooniprobe autorun start
```
Turns on the automatic daily test run after a Homebrew install.

## What's unique

It is a real, long-running measurement network where an ordinary person can see what is blocked on their own connection. The results feed an open dataset anyone can explore.

## Caveats

Measurements are published to a public dataset, so read the project's data policy before running tests, and note that the docs site was rate-limited when the brief was written, so test details are unverified.

## Links

- [OONI homepage](https://ooni.org/)
- [CLI install page](https://ooni.org/install/cli)
- [GitHub repo: ooni/probe-cli](https://github.com/ooni/probe-cli)
