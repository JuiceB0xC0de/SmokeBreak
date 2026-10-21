---
name: sysdig
title: sysdig
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, containers, linux, syscalls, tracing, troubleshooting]
homepage: https://sysdig.com/
scout_score: 5
status: draft
---

# sysdig

**TLDR;** Sysdig records Linux system calls and shows what every process and container is doing, like strace, tcpdump, htop and lsof in one tool.

Sysdig installs into the Linux kernel and captures system calls and other OS events from a machine. It ships two programs: `sysdig`, the general command-line tool, and `csysdig`, a curses-based interactive UI. The README's own summary: "Think about sysdig as strace + tcpdump + htop + iftop + lsof + ...awesome sauce."

The project starts from a complaint. Troubleshooting a machine usually means SSH-ing in and juggling many dated tools with inconsistent interfaces, and many of them break down inside containers. Sysdig aims to put them behind one interface and to inspect containers deeply without instrumenting them.

The idea underneath is the one tcpdump and Wireshark use for networks: capture first, analyse later. Sysdig can write activity to trace files that store rich system state, so you can replay a problem with full context after the fact. Almost everything a program does to the outside world passes through a system call, so a stream of them is a very honest record of what software is doing.

The homepage at sysdig.com is a commercial cloud security site for a paid product, not documentation. The open-source project lives on GitHub, and the wiki there is the real manual.

## Install

```
brew install sysdig
# The README itself documents a Docker image (docker.io/sysdig/sysdig, run with --privileged and host mounts) or deb/rpm packages from GitHub releases; the brew route is not covered there. It targets Linux and needs kernel-level access.
```

## Try this

```
sysdig
```
Launches the main tool, which captures and prints live system events from the machine.

```
csysdig
```
Opens the curses-based interactive UI for browsing processes, containers and activity.

```
sysdig --help
```
Lists the available options so you can see what capture and filter controls exist.

## What's unique

It treats system calls as something you can record to a file and analyse later, like a packet capture, and it claims deep container inspection without changing the containers.

## Caveats

The README is silent on kernel requirements and permissions beyond a privileged container, the homepage is a commercial product site, and I could not confirm recent project activity.

## Links

- [Homepage (commercial Sysdig product site)](https://sysdig.com/)
- [GitHub repository (open-source sysdig, README)](https://github.com/draios/sysdig)
- [Project wiki (full documentation)](https://github.com/draios/sysdig/wiki)
- [Video introduction to csysdig](https://www.youtube.com/watch?v=UJ4wVrbP-Q8)
