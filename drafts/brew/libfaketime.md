---
name: libfaketime
title: libfaketime
source: brew
category: take-things-apart
commitment: quick
tags: [ld-preload, library, quick, simulation, testing, time]
homepage: https://github.com/wolfcw/libfaketime
scout_score: 6
status: draft
---

# libfaketime

**TLDR;** Makes one program believe it is a different date, without touching the real system clock. Useful for expired certificates, year-2038 tests, and reproducible builds.

libfaketime is a C shared library that intercepts the calls programs use to read the clock. It reports a fake date and time to the programs that load it, while the system clock stays as it was. In its own words: "This means you can modify the system time a program sees without having to change the time system-wide."

The fake time can be an absolute date, a start-at date, or a relative offset such as -15d. A relative offset is computed from real time, so the fake clock keeps ticking. An absolute date freezes the clock. The README advises, "Whenever possible, you should use relative offsets or 'start at' dates, and not use absolute dates." A frozen clock breaks programs that measure elapsed time. There are also modes for running the clock faster or slower, stepping a fixed amount on every call, and driving the time from a file that another process can touch to pause and resume it.

Underneath is dynamic linking. On Linux the library is loaded through LD_PRELOAD, on macOS through DYLD_INSERT_LIBRARIES, so its time functions replace the libc ones for that process. Once you see this, you start noticing how much software quietly trusts the clock: certificates, caches, timeouts, build timestamps. The README lists use cases such as deterministic builds, debugging expired SSL certificates, and testing year-2038 compliance.

The project also ships a faketime wrapper script that accepts natural phrases, interpreted by /bin/date, so you rarely need to set the environment variables by hand.

## Install

```
brew install libfaketime
# Linux or macOS only. The README documents manual LD_PRELOAD or DYLD_INSERT_LIBRARIES use; the faketime wrapper handles this for you.
```

## Try this

```
faketime '2018-12-24 08:15:42' /bin/date
```
Runs date with the clock set to an absolute moment in 2018. The real system time is untouched.

```
faketime 'last Friday 5 pm' /your/command/here
```
Runs your command with the clock set to a relative phrase, which /bin/date interprets. Swap in any command you like.

```
faketime --help
```
Prints the wrapper's usage and options.

## What's unique

It fakes time per process rather than system-wide, and can also run the clock at a chosen speed or step it a fixed amount per call, which gives programs a repeatable, deterministic clock.

## Caveats

Works on Linux and macOS only, cannot intercept statically linked or setuid programs, and runtimes such as Go, Python, and the JVM may bypass the preload or hang without extra settings.

## Links

- [GitHub repository and README](https://github.com/wolfcw/libfaketime)
- [Issues (CLOCK_MONOTONIC hangs and bug reports)](https://github.com/wolfcw/libfaketime/issues)
