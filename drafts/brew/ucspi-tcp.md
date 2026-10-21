---
name: ucspi-tcp
title: ucspi-tcp
source: brew
category: fundamentals
commitment: quick
tags: [djb, inetd, network, quick, tcp, unix]
homepage: https://cr.yp.to/ucspi-tcp.html
scout_score: 6
status: draft
---

# ucspi-tcp

**TLDR;** D. J. Bernstein's tcpserver and tcpclient turn any program that reads stdin and writes stdout into a TCP server or client, no socket code needed.

ucspi-tcp is a set of small Unix tools for building TCP client-server applications. `tcpserver` listens on a host and port. For each incoming connection it forks a program you name, with descriptor 0 reading from the network and descriptor 1 writing to it. Details about the connection arrive as environment variables: local and remote host names, IP addresses and ports. `tcpclient` does the mirror image, making an outgoing connection and running a program wired to it the same way.

The package exists as a replacement for inetd. The homepage states it plainly: "inetd is unreliable under high loads." It also says inetd has no effective resource management and a listen() backlog that is typically only 5 or 10. In response, tcpserver has a concurrency limit (default 40, set with `-c`) that defers new connections instead of running the machine out of processes and memory.

The idea underneath is that a network service can be an ordinary program. It does not link a networking library or implement a plugin interface. It reads input, writes output, and looks at its environment. Access control follows the same spirit. `tcprules` compiles allow and deny rules into a cdb hash file, so lookups stay fast with thousands of rules, and the rules can be recompiled while the server runs.

The bundled extras are small sample clients built on tcpclient (`who@`, `date@`, `finger@`, `http@`, `tcpcat`, `mconnect`), plus `recordio`, which logs what a server's input and output looked like. Together they make a compact way to see what a TCP conversation is made of.

## Install

```
brew install ucspi-tcp
# Unix only. Building from source instead: unpack ucspi-tcp-0.88, run make, then as root run make setup check (installs under /usr/local).
```

## Try this

```
tcpserver --help
```
Prints usage for tcpserver, whose form is tcpserver opts host port prog. It is a quick look at the options before you wire up a first service.

```
tcpserver -c n
```
Caps simultaneous connections at n. New connections wait while n copies of your program are running. The default is 40.

```
tcpclient --help
```
Prints usage for tcpclient, the outgoing-connection counterpart that runs a program attached to the socket.

## What's unique

Connection metadata reaches an ordinary program through environment variables, and access rules compile into a cdb hash that can be swapped while the server runs. It is a small, Unix-style alternative to inetd, xinetd, netcat and netpipes.

## Caveats

The pages carry no visible release date and the latest package named is 0.88, so treat it as old, finished software. The docs are terse and assume Unix background.

## Links

- [Homepage](https://cr.yp.to/ucspi-tcp.html)
- [Install page](https://cr.yp.to/ucspi-tcp/install.html)
- [tcpserver man-style page](https://cr.yp.to/ucspi-tcp/tcpserver.html)
