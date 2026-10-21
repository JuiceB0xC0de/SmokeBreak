---
name: austin
title: Austin
source: brew
category: take-things-apart
commitment: quick
tags: [cpython, flamegraph, profiler, python, quick, tui]
homepage: https://github.com/P403n1x87/austin
scout_score: 5
status: draft
---

# Austin

**TLDR;** Austin reads a running Python process's memory from outside and samples every thread's call stack, with no changes to the code being watched.

Austin is a frame stack sampler for CPython, written in pure C. It finds the interpreter's data structures in the target process's memory and reads out the running threads and the stack of frames each one is executing. It does this at a regular interval, 100 microseconds by default. The target can be launched under Austin or attached to by PID, including child processes.

It is deliberately just a sampler. Austin writes raw stacks in a compact binary format called MOJO and leaves aggregation to other tools. The README says this is what lets it sample faster than profilers that aggregate while running. Its output can be converted to collapsed stacks for FlameGraph, to Speedscope JSON, or to pprof. There is also a VS Code extension and a separate top-like terminal UI.

The idea underneath is that a running interpreter is just memory laid out in a known shape, and you can read it from outside. The README puts it as 'Hence, one can use Austin to easily make powerful statistical profilers that have minimal impact on the target application and that don't require any instrumentation.' It is a small way into how CPython represents threads and frames, and into statistical profiling in general.

A `-w` mode prints the current stacks of all threads in a running process, which is a quick way to ask a live program what it is doing right now.

## Install

```
brew install austin
# Attaching to other processes needs sudo on macOS, and root or CAP_SYS_PTRACE on Linux.
```

## Try this

```
austin -o profile.mojo python myscript.py
```
Launches your script under Austin and writes the sampled stacks to profile.mojo.

```
sudo austin -w `pgrep -f my-running-python-app`
```
Prints the current stacks of all threads in a running Python process to the terminal.

```
austin --help
```
Lists the available options.

## What's unique

It is only a sampler: no instrumentation and no aggregation at run time, just raw stacks in a binary format that other tools turn into flame graphs and profiles. It can also attach to a live process, including children and sub-interpreters.

## Caveats

Attaching needs root or CAP_SYS_PTRACE on Linux and sudo on macOS, which fails for SIP-protected Python builds such as the system Python and python.org installers; output is binary, so write it to a file.

## Links

- [Austin GitHub repository and README](https://github.com/P403n1x87/austin)
- [MOJO binary format (project wiki)](https://github.com/P403n1x87/austin/wiki/The-MOJO-file-format)
- [Austin TUI](https://github.com/P403n1x87/austin-tui)
- [Austin VS Code extension](https://marketplace.visualstudio.com/items?itemName=p403n1x87.austin-vscode)
