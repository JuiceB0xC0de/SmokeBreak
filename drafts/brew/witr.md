---
name: witr
title: witr
source: brew
category: take-things-apart
commitment: quick
tags: [cli, debugging, linux, macos, processes, quick, tui]
homepage: https://github.com/pranshuparmar/witr
scout_score: 5
status: draft
---

# witr

**TLDR;** witr answers "why is this running?" for a process, port, container or file by tracing it back through the chain of parents that started it.

witr takes a process name, PID, port, file path or container name and prints a short narrative of where it came from. The output is an ancestry chain such as systemd → pm2 → node, plus the thing that supervises it, the working directory, open sockets and any warnings. It can print plain text, a short or tree view, or JSON, and there is an interactive terminal dashboard.

The README's complaint is that ps, top, lsof, ss, systemctl and docker ps each show what is running, but you have to correlate their output yourself to work out why. witr tries to give that causality in one answer.

The idea underneath is in the project's own words: "witr treats everything as a process question." A port, a locked file and a container are each mapped to a PID, and then the parent chain is walked. It picks one primary source, such as a systemd unit, launchd job, container, pm2, cron, SSH session or tmux session. If the original parent has exited, the chain marks the break instead of guessing. That makes it a handy way to learn how process ancestry, supervisors and orphaned children actually work on your machine.

It reads /proc on Linux and uses ps, lsof and similar tools on macOS and FreeBSD. On Windows it calls Win32 APIs directly. Exit codes distinguish clean runs, warnings, not found, permission denied and cause unknown, so scripts can act on the result.

## Install

```
brew install witr
# Also available via an install script, MacPorts, apt on recent Debian/Ubuntu, AUR, winget, Scoop, npm, go install, Nix and others.
# Full visibility often needs sudo (Administrator terminal on Windows). Container lookups need the relevant runtime CLI (docker, podman, etc.) on PATH.
```

## Try this

```
witr node
```
Finds processes matching "node" and prints their ancestry chain, source, working directory, git repo and sockets.

```
witr --port 5000 --short
```
Shows only the ancestry chain for whatever is listening on port 5000, e.g. systemd → PM2 → python.

```
witr --file /var/lib/dpkg/lock
```
Explains which process is holding that file open and why it is running.

## What's unique

It turns every question about a port, file or container into a question about a PID, then explains the causal chain instead of listing state. It also ships a stable JSON contract and documented exit codes aimed at scripts and AI coding agents.

## Caveats

Source selection is described as best-effort, some details need sudo, and platform support varies: Windows lacks tmux/screen and schedule detection, and macOS SIP hides some process details even with sudo.

## Links

- [GitHub repository (homepage)](https://github.com/pranshuparmar/witr)
- [Browser tutorial and sandbox (simulated Linux box)](https://pranshuparmar.github.io/witr/)
- [Author's write-up: witr, why is this running?](https://medium.com/@pranshu.parmar/witr-why-is-this-running-a9a97cbedd18)
