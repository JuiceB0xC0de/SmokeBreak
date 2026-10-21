---
name: daemontools
title: daemontools
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, logging, old-school, process-supervision, services, unix]
homepage: https://cr.yp.to/daemontools.html
scout_score: 5
status: draft
---

# daemontools

**TLDR;** D. J. Bernstein's minimal service supervisor: a directory with a run script is a service, and it gets restarted whenever it dies.

daemontools is a collection of tools for managing UNIX services, according to its homepage. The central program, supervise, starts a service and restarts it if it dies. In the homepage's words, "all supervise needs is a directory with a run script that runs the service." There is no config format to learn. A service is a folder and a script.

The second main piece is multilog, which takes a service's error output and saves it to one or more logs. It can timestamp each line, include or exclude lines matching patterns for each log, and rotate logs to limit disk use. If the disk fills up, it "pauses and tries again, without losing any data." That is a deliberate choice, and it shows how the suite thinks about failure.

The package also ships svscan, svscanboot, svc, svstat, svok, tai64n, tai64nlocal, setuidgid, envuidgid, envdir, softlimit, setlock, fghack, pgrphack and readproctitle. The homepage lists these by name, and this entry does not describe them further. Several of the names suggest small single-purpose tools meant to be chained together, which is a Unix idea worth studying.

The underlying idea is process supervision: a long-running parent that owns a service, watches it, and restarts it, instead of a service that daemonizes itself and hopes. Reading daemontools is a short way into that model, and into the design style behind it.

## Install

```
brew install daemontools
# Homebrew keeps services in $HOMEBREW_PREFIX/etc/service/
# The homepage has 'How to install' and 'How to start' sections; check them before first run.
```

## Try this

```
supervise --help
```
Runs the supervisor with no valid service directory, so expect a usage message rather than documentation. The homepage is the real manual.

```
svstat --help
```
Shows how to query the state of a supervised service directory.

```
multilog --help
```
Shows the usage line for the logger that timestamps, filters and rotates a service's output.

## What's unique

A service is just a directory with a run script, and there is no config format at all. The logger's rule of pausing on a full disk instead of dropping data is a specific, stated design decision.

## Caveats

The brief came only from the homepage, which shows no version or release date, so project status and the exact install and first-run steps are unverified.

## Links

- [daemontools homepage (D. J. Bernstein)](https://cr.yp.to/daemontools.html)
