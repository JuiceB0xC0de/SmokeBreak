---
name: libusbmuxd
title: libusbmuxd
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, ios, needs-hardware, protocol, tunneling, usb]
homepage: https://www.libimobiledevice.org/
scout_score: 5
status: draft
---

# libusbmuxd

**TLDR;** A client library and two tools, iproxy and inetcat, that tunnel TCP connections to an iPhone over USB, using the usbmux protocol Apple's own software uses.

When an iPhone is plugged into a computer, programs do not talk to USB directly. A daemon called usbmuxd owns the USB link and multiplexes many TCP-style connections over it. Applications connect to a local socket the daemon serves and ask for a port on the device. libusbmuxd is the client library for that socket.

Two command-line tools ship with it. `iproxy` binds local TCP ports and forwards them to ports on the device, so an ordinary local client can reach a service running on the phone. `inetcat` is a netcat-like tool: it opens a TCP port on the device and exposes it on stdin and stdout, which makes it usable as an SSH ProxyCommand with no port forward at all.

The daemon ships with iTunes on Windows and Mac OS X. The libimobiledevice project reimplemented it as open source for Linux and for people who do not want iTunes. The library is mostly used by other libimobiledevice tools to reach services on iOS devices.

The odd part is the transport idea. A phone on a cable behaves like a host on a tiny private network, reached through a socket. Point the client at a different socket and the same tools work against a phone plugged into another machine.

## Install

```
brew install libusbmuxd
On Linux, the usbmuxd daemon must be installed on the system. macOS has its own copy. Windows needs Apple's Apple Mobile Device Support package (part of iTunes). You need an iOS device plugged in over USB to do anything useful.
```

## Try this

```
iproxy --help
```
Shows iproxy's usage and options.

```
iproxy 2222:22
```
Forwards local port 2222 to port 22 on the first USB-connected device, so ssh to localhost port 2222 reaches its sshd. Only works on jailbroken devices with sshd installed.

```
inetcat --help
```
Shows inetcat's usage and options.

## What's unique

One environment variable, USBMUXD_SOCKET_ADDRESS, points the client at a usbmuxd socket on another machine, so tools on one host can reach a phone plugged into a different one. inetcat also turns an SSH ProxyCommand into a direct route to a device port.

## Caveats

This is plumbing: it does nothing visible without a usbmuxd daemon and a device, and the SSH example only applies to jailbroken devices; Windows support is limited.

## Links

- [libimobiledevice homepage](https://www.libimobiledevice.org/)
- [libusbmuxd repository (README)](https://github.com/libimobiledevice/libusbmuxd)
- [libusbmuxd issue tracker](https://github.com/libimobiledevice/libusbmuxd/issues)
