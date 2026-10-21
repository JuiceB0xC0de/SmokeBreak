---
name: landrun
title: landrun
source: brew
category: take-things-apart
commitment: quick
tags: [kernel, landlock, linux, quick, sandbox, security]
homepage: https://github.com/Zouuup/landrun
scout_score: 6
status: draft
---

# landrun

**TLDR;** Put landrun in front of any Linux command and the kernel itself restricts which files and network ports it can touch, with no root or containers.

Landrun is a small command-line wrapper around Landlock, a Linux security module that lets an unprivileged process restrict itself and its future children. You list what the command may read, write, or execute, and which TCP or UDP ports it may bind or connect to. Landrun builds that ruleset, applies it, and then runs your command. Anything outside the rules is denied by the kernel, and the command's output is otherwise unchanged.

The README's pitch is "No root. No containers. No SELinux/AppArmor configs." and it describes the tool as "Think firejail, but with kernel-level security and minimal overhead." It is written in Go on top of the go-landlock package.

The interesting part is the idea underneath. With no flags at all, `landrun ls` runs in a maximum-restriction jail, and you then add permissions one at a time until the program works. The denial errors teach you what a program actually touches: which libraries it loads, which config it reads, which ports it opens. The README suggests running under strace when the errors are unclear. Landrun also covers newer Landlock features such as UDP port control, IPC scoping, and pathname UNIX socket control, with a kernel-version table to match.

## Install

```
brew install landrun
# Needs Linux kernel 5.13+ with Landlock enabled. TCP rules need kernel 6.7+, UDP rules need 7.2+.
# Alternative: go install github.com/zouuup/landrun/cmd/landrun@latest (Go 1.24+)
```

## Try this

```
landrun ls
```
With no rules given, landrun applies maximum restrictions, so you see the command running in a jail where it can reach almost nothing.

```
landrun --rox /usr --connect-tcp 443 nc kernel.org 443
```
Runs nc with exec access to /usr and permission to connect only to TCP port 443.

```
landrun --rox /usr strace -f -e trace=all ls
```
Traces the sandboxed ls to show which accesses are being denied, the README's suggested debugging step.

## What's unique

It turns Landlock, a kernel feature most people never touch, into a one-line wrapper with path and port rules. There is no root, no container, and no policy language to learn.

## Caveats

Linux only, strict mode fails on kernels older than the requested Landlock ABI so most people will need --best-effort, and Go servers may escape TCP rules because of a Multipath TCP quirk.

## Links

- [Landrun GitHub repository](https://github.com/Zouuup/landrun)
- [Landlock project site](https://landlock.io)
- [go-landlock, the Go bindings used by landrun](https://github.com/landlock-lsm/go-landlock)
