---
name: afl++
title: AFL++
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, fuzzing, instrumentation, reverse-engineering, security]
homepage: https://aflplus.plus/
scout_score: 6
status: draft
---

# AFL++

**TLDR;** A coverage-guided fuzzer that mutates seed inputs, watches which code paths they reach, and keeps the ones that find new ones, until something crashes.

AFL++ is a fuzzing framework. You compile a target program with its compiler wrappers (`afl-cc`, `afl-c++`) so the binary reports which code paths each input exercises. Then `afl-fuzz` takes a directory of seed inputs, mutates them, and keeps any mutation that reaches new code. Crashes and hangs are saved under `crashes/` and `hangs/` in the output directory, and a status screen updates while it runs.

The idea underneath is that the program itself is the feedback signal. Random bytes rarely get past the first input check. Keeping inputs that reach new coverage lets the fuzzer gradually learn the shape of a file format or protocol without being told. The package also ships helpers: `afl-cmin` and `afl-tmin` shrink a corpus and individual inputs, `afl-showmap` prints coverage maps, and `afl-plot` draws graphs. There are binary-only modes (QEMU, Unicorn, QBDI) for targets you cannot recompile.

AFL++ is a community fork of American Fuzzy Lop by Michal 'lcamtuf' Zalewski. The homepage says it was created to merge the best features developed for the AFL family that were never merged into AFL, which has not been updated since November 2017. The README calls it "a superior fork to Google's AFL - more speed, more and better mutations, more and better instrumentation, custom module support, etc."

## Install

```
brew install afl++
# The README's first suggested route is Docker instead: docker pull aflplusplus/aflplusplus
# You also need a target whose source you can rebuild with afl-cc, plus some seed input files.
```

## Try this

```
afl-fuzz --help
```
Prints the fuzzer's usage and options, a quick look at what can be tuned.

```
CC=/path/to/afl-cc CXX=/path/to/afl-c++ ./configure --disable-shared && make clean all
```
Rebuilds a target project with AFL++'s compiler wrappers so it is instrumented.

```
./afl-fuzz -i seeds_dir -o output_dir -- /path/to/tested/program [...program's cmdline...]
```
Starts fuzzing a program that reads stdin, with the live status screen and results in output_dir.

## What's unique

It merges years of AFL improvements that never made it upstream into one maintained project, with several instrumentation modes including binary-only ones. Its license is also unusual: a per-file split, plus a commercial option paid as a donation to a good cause.

## Caveats

The dev branch is described as 'bleeding edge', and afl-fuzz is AGPL-3.0, so commercial use needs compliance or the EUR 20,000 donation license; the README also urges reading docs/fuzzing_in_depth.md before starting.

## Links

- [Homepage](https://aflplus.plus/)
- [GitHub repository](https://github.com/AFLplusplus/AFLplusplus)
- [Papers page](https://aflplus.plus/papers/)
