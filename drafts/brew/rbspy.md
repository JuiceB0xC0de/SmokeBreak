---
name: rbspy
title: rbspy
source: brew
category: take-things-apart
commitment: quick
tags: [flamegraph, profiler, quick, ruby, rust]
homepage: https://rbspy.github.io/
scout_score: 6
status: draft
---

# rbspy

**TLDR;** A sampling profiler that attaches to a running Ruby process by PID and shows which functions eat the time, with no restart or code changes.

rbspy is a CPU profiler for Ruby, written in Rust. Point it at the PID of a Ruby process that is already running, or have it launch a script, and it periodically samples the call stack. It prints a live summary of the top functions, and it can save the raw samples to disk and turn them into a flamegraph.

The README frames the problem plainly: "Have a running Ruby program that you want to profile without restarting it?" Most profilers need to be loaded into the program or wrapped around it. rbspy works from outside, so the target program does not need to know it is being watched.

The idea underneath is sampling versus instrumentation. Instead of hooking every function call, a sampling profiler takes snapshots at intervals and counts where the program was. The README says this keeps overhead low and makes it "safe to run in production". The raw data is kept so it can be analysed in several ways later, not only viewed live.

It is a small, concrete way to see how a profiler can look inside another process, and a door into flamegraphs and stack sampling generally.

## Install

```
brew install rbspy
# Linux: download a release from the GitHub releases page and move the binary to /usr/local/bin (musl builds are statically linked; gnu builds need GNU libc)
# or, with Rust 1.56+: cargo install rbspy --locked
```

## Try this

```
rbspy record --pid $PID
```
Attaches to an already-running Ruby process and starts profiling it.

```
rbspy record -- bundle exec ruby my-script.rb
```
Launches the script under the profiler and reports where it spent its time.

```
rbspy --help
```
Lists the subcommands and options.

## What's unique

It attaches to a Ruby process that is already running, so you can profile a live workload without restarting it or touching its code. It also keeps raw data for later analysis plus a flamegraph.

## Caveats

The brief could not confirm recent activity, the README does not say what permissions attaching to a PID needs, and the Rust crate API is explicitly unstable.

## Links

- [rbspy homepage](https://rbspy.github.io/)
- [GitHub repository and README](https://github.com/rbspy/rbspy)
- [Installing rbspy (docs)](https://rbspy.github.io/installing.html)
- [crates.io package](https://crates.io/crates/rbspy)
