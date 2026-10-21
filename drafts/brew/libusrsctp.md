---
name: libusrsctp
title: libusrsctp
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, c, library, network, protocol, sctp, transport]
homepage: https://github.com/sctplab/usrsctp
scout_score: 6
status: draft
---

# libusrsctp

**TLDR;** A C library that runs SCTP, the message-oriented TCP alternative with multi-streaming and multihoming, entirely in userland, with a discard server and client to watch it move data.

libusrsctp implements SCTP (Stream Control Transmission Protocol) as a library, so an application can speak it without kernel support. The README lists FreeBSD, OpenBSD, Linux, Mac OS X and Windows. You call `usrsctp_init()`, open sockets with `usrsctp_socket()`, and move messages with `usrsctp_sendv()` and `usrsctp_recvv()`. The API is modelled on RFC 6458, the Sockets API Extensions for SCTP, and every call carries a `usrsctp_` prefix to keep it apart from the kernel versions.

SCTP is, in the README's words, "a message oriented, reliable transport protocol with direct support for multihoming that runs on top of IP or UDP." Where TCP gives you one byte stream, SCTP keeps message boundaries and can carry several independent streams in one association. A userland port lets programs use it on systems that do not ship it in the kernel.

The library can send SCTP directly over IP, which needs raw sockets and therefore root. It can also wrap SCTP packets in UDP datagrams. The Manual notes that some NAT boxes cannot pass SCTP, which is why the UDP mode exists, and it is also the easy way to experiment without privileges.

The formula installs no executables, so this is a library to build against. The source tree includes small example programs in `programs`, including a discard server and a client, and those are the quickest way to see the protocol working.

## Install

```
brew install libusrsctp
# Installs the library only, no executables. The example programs (discard_server, client) are built from the source repository: ./bootstrap, ./configure, make. Direct SCTP mode needs root; UDP encapsulation does not.
```

## Try this

```
./discard_server 11111 22222
```
Starts the discard server from the built source tree, using UDP encapsulation with local port 11111 and remote port 22222.

```
./client 127.0.0.1 9 0 22222 11111
```
Runs the client on the same machine and sends whatever you type on stdin to the discard server over SCTP wrapped in UDP.

```
cmake --build .
```
Builds the library and example programs after running cmake from a directory outside the source tree; the default is a DEBUG build with verbose output.

## What's unique

The kernel's SCTP tunables (buffer sizes, RTO timers, SACK frequency, congestion control module, CMT) are exposed as `usrsctp_sysctl_set_*` functions the application calls at runtime. It also ships a discard server and client, so you can watch SCTP move data end to end on one machine.

## Caveats

The Manual looks dated (test platforms include Ubuntu 11.10 and Mac OS X 10.7, many tunables are marked TBD), maintenance status is unconfirmed, usrsctp_sendv() supports only one destination address, and authinfo is not implemented.

## Links

- [GitHub repository (homepage)](https://github.com/sctplab/usrsctp)
- [Manual.md](https://github.com/sctplab/usrsctp/blob/master/Manual.md)
- [Example programs](https://github.com/sctplab/usrsctp/tree/master/programs)
