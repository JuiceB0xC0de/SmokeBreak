---
name: runit
title: runit
source: brew
category: fundamentals
commitment: quick
tags: [ancient, daemontools, init, quick, supervision, unix]
homepage: https://smarden.org/runit/
scout_score: 5
status: draft
---

# runit

**TLDR;** A tiny init and service supervisor from the daemontools lineage, showing how Unix boots and keeps daemons alive with a few shell scripts.

runit is an init scheme with service supervision, built as a small replacement for sysvinit and similar systems. It is a handful of programs: runit runs as process 1, runsvdir starts one runsv supervisor per entry in a service directory, and runsv keeps that service's run script alive. If the service dies, it is started again.

Boot is three stages, each a plain script. Stage 1 (/etc/runit/1) does one-time setup, with control of the console for an emergency shell. Stage 2 (/etc/runit/2) normally runs runsvdir, which should not return until halt or reboot, and is restarted if it crashes. Stage 3 (/etc/runit/3) runs on halt or reboot. The homepage states the goal: "runit is optimized for reliability and small size. The amount of code in process no 1 should be minimal."

The idea underneath is that a service is just a directory with a run script, and a supervisor is a small loop that restarts it. Logging goes through a log/ subdirectory piped to svlogd. Runlevels are handled with runsvdir and runsvchdir. Once that clicks, much of how Unix systems keep processes alive stops being mysterious.

The homepage is an old-school document that includes real process listings from 2002 Debian sarge servers. That is old, and fine for reading, because the model has barely changed.

## Install

```
brew install runit
# Homebrew does not install runit as an init replacement. The service directory is $HOMEBREW_PREFIX/var/service. Start a supervisor by hand with: runsvdir -P $HOMEBREW_PREFIX/var/service (may need root, depending on the services).
```

## Try this

```
runsvdir --help
```
Shows how the directory supervisor is invoked, the entry point for running services from a directory of run scripts.

```
sv --help
```
Shows the control command for starting, stopping and checking supervised services.

```
chpst --help
```
Shows the helper that runs a process with changed user, limits or environment.

## What's unique

It is init and supervisor in one small toolkit from the daemontools lineage, with a three-stage boot that is easy to read as shell scripts.

## Caveats

Not a drop-in init on macOS, the homepage shows no release date for 2.3.1, and its example output dates from 2002.

## Links

- [runit homepage](https://smarden.org/runit/)
- [How to install runit](https://smarden.org/runit/install.html)
