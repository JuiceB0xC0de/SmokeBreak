---
name: dbus
title: D-Bus
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, daemon, desktop, ipc, protocol]
homepage: https://wiki.freedesktop.org/www/Software/dbus
scout_score: 5
status: draft
---

# D-Bus

**TLDR;** The message bus that lets desktop programs on one machine talk to each other, with tools to watch and poke it from a shell.

D-Bus is a message bus. A daemon, `dbus-daemon`, runs in the background, and applications connect to it to send each other messages. There are normally two instances: a system bus for things like new hardware or printer queue changes, and a per-login session bus for ordinary application-to-application talk. Two applications can also skip the daemon and talk directly over a one-to-one connection.

The homepage describes it as "a simple way for applications to talk to one another." It also takes on process lifecycle. Because the bus knows which names are claimed, it can make a single-instance application or daemon simple and reliable to write, and it can launch a service on demand when something first calls it.

The idea underneath is that a desktop is a crowd of cooperating processes, and they need a shared directory and a shared way to call each other. Once you see the bus, a lot of Linux desktop behaviour starts to make sense. The reference implementation is small: libdbus has no required dependencies, and the daemon needs only the expat XML parser. The installed tools, such as `dbus-monitor` and `dbus-send`, let you observe and send messages yourself.

On macOS via Homebrew, the session bus is easy to start. The system bus is a manual, root-level setup.

## Install

```
brew install dbus
# start the session bus now and at login:
brew services start dbus
# optional system bus (needs root, manual on macOS):
sudo cp -f $(brew --prefix dbus)/org.freedesktop.dbus-system.plist /Library/LaunchDaemons
sudo launchctl bootstrap system /Library/LaunchDaemons/org.freedesktop.dbus-system.plist
```

## Try this

```
dbus-monitor --help
```
Shows the options for the tool that watches messages passing over a bus.

```
dbus-send --help
```
Shows how to craft and send a message to a service on the bus.

```
dbus-daemon --help
```
Shows how the bus daemon itself is configured and started.

## What's unique

It is the reference implementation of the bus most Linux desktops are built on, and it also handles single-instance enforcement and on-demand service launch. The reference daemon needs only expat.

## Caveats

The low-level libdbus is not meant for application authors, the wiki points to higher-level bindings, and on macOS the system bus needs sudo and launchctl by hand.

## Links

- [Homepage (D-Bus wiki)](https://wiki.freedesktop.org/www/Software/dbus)
- [Reference implementation source (GitLab)](https://gitlab.freedesktop.org/dbus/dbus)
