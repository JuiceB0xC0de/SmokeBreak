---
name: bubblewrap
title: bubblewrap
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, containers, linux, namespaces, sandboxing]
homepage: https://github.com/containers/bubblewrap
scout_score: 7
status: draft
---

# bubblewrap

**TLDR;** A small Linux tool that builds a container-like sandbox from kernel namespaces without root, so you can see how Flatpak-style isolation is assembled.

Bubblewrap (`bwrap`) runs a command inside a sandbox you describe on the command line. It starts by creating a new, empty mount namespace whose root is a tmpfs, invisible to the host and cleaned up when the last process exits. Your options then build the world inside it: which host directories to bind in, whether read-only, what goes in /proc and /dev, and which namespaces to unshare.

It exists because tools like docker and systemd-nspawn are built for administrators, and the README argues they are not safe to hand to unprivileged users, since access can be turned into a root shell on the host. Bubblewrap uses unprivileged user namespaces instead of setuid, and sets PR_SET_NO_NEW_PRIVS so setuid binaries cannot escalate. Flatpak is one of the tools that builds on it.

The idea underneath is that a container is not a special object. It is a process with a rearranged view of the filesystem, PIDs, network and users. Because bubblewrap is a low-level building block, not a finished sandbox, you assemble that view yourself, one flag at a time. In the README's words: "bubblewrap is not a complete, ready-made sandbox with a specific security policy." That makes it a good way to learn what isolation actually consists of.

## Install

```
brew install bubblewrap
# Linux only. The kernel must support unprivileged user namespaces; the setuid mode has been removed.
```

## Try this

```
bwrap --help
```
Lists the mount, namespace and environment options you combine to describe a sandbox.

```
bwrap \
    --ro-bind /usr /usr \
    --symlink usr/lib64 /lib64 \
    --proc /proc \
    --dev /dev \
    --unshare-pid \
    --new-session \
    bash
```
Starts a bash shell in a sandbox that reuses the host's /usr read-only, with its own /proc, /dev and PID namespace. The README calls this example incomplete and illustrative only.

## What's unique

It gets container-style isolation without setuid or root, and stays small so the security-relevant code is easy to audit. Unlike Firejail, it has no desktop-specific features; those are left to the calling application.

## Caveats

Linux only, and the protection level depends entirely on the arguments you pass, so a careless setup gives weak isolation; anything mounted in, like a D-Bus socket, can be an escape route.

## Links

- [Bubblewrap GitHub repository (README)](https://github.com/containers/bubblewrap)
- [Flatpak](https://www.flatpak.org)
- [xdg-dbus-proxy](https://github.com/flatpak/xdg-dbus-proxy)
