---
name: slirp4netns
title: slirp4netns
source: brew
category: fundamentals
commitment: quick
tags: [containers, linux, namespaces, nat, network, quick, rootless]
homepage: https://github.com/rootless-containers/slirp4netns
scout_score: 5
status: draft
---

# slirp4netns

**TLDR;** Gives an unprivileged Linux network namespace a working internet connection with no root, using a TCP/IP stack that runs entirely in user space.

Since Linux 3.8, an ordinary user can create network and user namespaces. The README points out the catch: those namespaces were not very useful, because linking one to the host with a veth pair needs root. So the namespace sat there with no internet.

slirp4netns fills the gap. You run it on the host, give it the PID of a process inside the namespace and the name of a TAP device, and it attaches that device to libslirp, a TCP/IP stack in user space. The namespace gets a tap0 interface (the README example shows 10.0.2.100/24), a built-in nameserver at 10.0.2.3, and outbound access through the host. It runs as a separate process next to the namespace, not as a library.

The idea underneath is old. Slirp emulates a network in ordinary program code: it takes packets from one side and re-makes them as normal sockets on the other, a bit like NAT done by an application instead of the kernel. That is why no privileges are needed. The README says this one is tuned to avoid copying packets across namespaces, and it cites a 2018 iperf3 benchmark in which it beat vde_plug and VPNKit.

It is also plumbing that real tools depend on. The brief names rootless Podman, Buildah, RootlessKit and k3s as users. Running the quick start by hand shows what they do for you: make a namespace, wire it up, and point DNS at the right place.

## Install

```
brew install slirp4netns
# Linux only: it depends on Linux network namespaces. No account or hardware needed.
# If unshare fails on Debian, Arch or old CentOS 7, you may need: user.max_user_namespaces=28633 and, where present, kernel.unprivileged_userns_clone=1, then sudo sysctl --system
```

## Try this

```
unshare --user --map-root-user --net --mount
```
Terminal 1: creates user, network and mount namespaces as a normal user. This is the first step of the quick start, and the namespace has no network yet.

```
slirp4netns --configure --mtu=65520 --disable-host-loopback $(cat /tmp/pid) tap0
```
Terminal 2: attaches a tap0 device to the namespace whose PID you saved in /tmp/pid, backed by the user-space stack.

```
curl https://example.com
```
Run inside the namespace, after pointing resolv.conf at the nameserver 10.0.2.3, to confirm outbound access works without root.

## What's unique

It makes an otherwise cut-off unprivileged namespace reach the internet with no root and no veth pairs. It is the networking backend behind rootless Podman, Buildah, RootlessKit and k3s.

## Caveats

Linux only, and unshare may need sysctl or kernel changes on some distros; the README's iperf3 benchmark dates from 2018.

## Links

- [GitHub repository and README](https://github.com/rootless-containers/slirp4netns)
- [Manual (slirp4netns.1.md)](https://github.com/rootless-containers/slirp4netns/blob/master/slirp4netns.1.md)
- [Releases (static binaries)](https://github.com/rootless-containers/slirp4netns/releases)
- [libslirp](https://gitlab.freedesktop.org/slirp/libslirp)
