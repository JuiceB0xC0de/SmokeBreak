---
name: launch_socket_server
title: launch_socket_server
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, go, launchd, macos, network, sockets]
homepage: https://github.com/mistydemeo/launch_socket_server
scout_score: 5
status: draft
---

# launch_socket_server

**TLDR;** A small macOS proxy that lets launchd bind a privileged port like 80 and hand connections to a server running as an ordinary user.

launch_socket_server solves one old Unix problem: ports under 1024 are privileged, but you do not want your web server or other daemon running as root just to listen on one. On macOS, launchd can open the socket itself. This program sits between launchd and your server, takes the socket launchd hands over, and forwards each incoming connection to your unprivileged program.

The forwarding goes over a Unix domain socket by default. The proxy creates the socket path and passes it to your program in the `LAUNCH_PROGRAM_SOCKET_PATH` environment variable. Your server unlinks any existing file at that path, binds to it, and stays in the foreground. A TCP address such as `127.0.0.1:8000` works too, via `LAUNCH_PROGRAM_TCP_ADDRESS`.

The idea underneath is socket activation. The system, not your program, owns the listening socket and passes it along through the `launch_activate_socket` API (OS X 10.9 and later). Separating who opens a port from who serves it is a pattern worth knowing, and this is a small, readable example of it. The README calls the project an MIT-licensed fork maintained by Misty De Méo, from an original by Sam Stephenson in 2014.

Setup is a launchd plist in `/Library/LaunchDaemons`. Its `Sockets` key names the port, and its `ProgramArguments` begin with the path to launch_socket_server. You can also use `-` in place of a server path to run it as a pure proxy with no child program.

## Install

```
brew install launch_socket_server
# macOS only. The upstream README describes building from source instead: brew install go, then make, then make install (to /usr/local, or set PREFIX).
# You also need a launch daemon plist in /Library/LaunchDaemons, loaded with sudo.
```

## Try this

```
sudo launchctl load -Fw /Library/LaunchDaemons/com.example.myserver.plist
```
Registers and starts your launch daemon, so launchd opens the privileged port and launch_socket_server proxies to your program.

```
sudo launchctl unload -Fw /Library/LaunchDaemons/com.example.myserver.plist
```
Unloads the daemon and releases the port.

## What's unique

It relies on launchd's own socket activation, so the privileged bind happens in the system and your program never runs as root. It can also act as a plain proxy to a TCP address with no child program.

## Caveats

macOS only, needs OS X 10.9 or later, and the brief could not confirm recent maintenance; your server must stay in the foreground and unlink its socket before binding.

## Links

- [Homepage / README (GitHub)](https://github.com/mistydemeo/launch_socket_server)
- [launchd(8) man page (Apple)](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man8/launchd.8.html)
- [login_wrapper helper in the repo](https://github.com/mistydemeo/launch_socket_server/blob/master/libexec/launch_socket_server/login_wrapper)
