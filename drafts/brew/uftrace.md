---
name: uftrace
title: uftrace
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, cpp, linux, profiling, rust, tracing, tui]
homepage: https://uftrace.github.io/slide/
scout_score: 6
status: draft
---

# uftrace

**TLDR;** uftrace records every function call a C, C++ or Rust program makes and prints it as an indented call tree with a duration on each line.

uftrace runs a program and hooks the entry and exit of each function, recording timestamps along with arguments and return values. The result is a nested, indented tree of calls, each with its duration. The same recording can be replayed, summarised into per-function statistics, graphed, or exported to Chrome trace viewer and flame graphs.

It was heavily inspired by the Linux kernel's ftrace function graph tracer, and carries that idea into user-space programs. Traditionally the program is built with `-pg` or `-finstrument-functions`, so the compiler inserts a small hook call into every function. Library calls are caught by hooking the PLT. Recordings land in a `uftrace.data` directory that the other subcommands read later.

The README also describes an experimental dynamic mode (`-P.`) that analyzes and patches function prologues at run time on x86_64 and AArch64, so no recompilation is needed. User functions, library calls, kernel functions, scheduler events and Python functions can all be shown on one timeline. It is a good way to see what a program does, rather than what its source says it does.

## Install

```
brew install uftrace
# Compiler-instrumented tracing needs your program built with gcc -pg or -finstrument-functions.
# Kernel tracing needs root and a kernel built with CONFIG_FUNCTION_GRAPH_TRACER=y.
```

## Try this

```
gcc -pg foobar.c && uftrace a.out
```
Builds a sample program with profiling hooks, then runs it live and prints the call tree with durations.

```
uftrace record a.out && uftrace replay
```
Saves the trace to uftrace.data, then prints the recorded calls as an indented tree.

```
uftrace report
```
Prints per-function statistics from the recording: total time, self time and call counts.

## What's unique

Most function tracers need the program recompiled. uftrace can also patch function prologues at run time (experimental), and it merges user, library, kernel and scheduler events into one timeline.

## Caveats

It cannot attach to an already running process yet, mainly supports x86_64 and AArch64 on Linux and Android, and its no-recompile mode is experimental.

## Links

- [Homepage (slide deck)](https://uftrace.github.io/slide/)
- [GitHub repository and README](https://github.com/namhyung/uftrace)
- [Tutorial (wiki)](https://github.com/namhyung/uftrace/wiki/Tutorial)
- [Lightning talk (video)](https://youtu.be/LNav5qvyK7I)
