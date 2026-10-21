---
name: wayland
title: Wayland
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, compositor, display, protocol, x11]
homepage: https://wayland.freedesktop.org
scout_score: 5
status: draft
---

# Wayland

**TLDR;** The protocol that replaces X11 for talking to a display server, with wayland-scanner turning its XML protocol definitions into C code.

Wayland is a protocol and architecture for putting graphics on a screen. Applications are clients, and a display server called a compositor draws their windows and passes along keyboard and mouse input. The homepage describes it as a language rather than a program: "Wayland is the language (protocol) that applications can use to talk to a display server in order to make themselves visible and get input from the user (a person)."

The idea underneath is that the protocol is the shared contract. Unlike X11, there is no single canonical server. In the project's words, "every graphical environment brings with it one of many compositor implementations." Window management and much of the user experience tend to live in the compositor instead of in swappable parts.

The protocols themselves are written in XML. The core library, libwayland, turns those definitions into a C API that only encodes and decodes messages between compositor and clients. It does not implement Wayland. The page says Wayland can also run nested inside another X11 or Wayland session, and that some web browsers use it for internal communication between their own parts.

The one executable this formula installs is wayland-scanner. The brief does not describe it, so treat it as the tool that works with those XML definitions, and read its help output to see what it offers.

## Install

```
brew install wayland
```

## Try this

```
wayland-scanner --help
```
Prints the scanner's usage, a first look at the tool that works with Wayland's XML protocol definitions.

## What's unique

It is a protocol with no reference server: every desktop brings its own compositor, and the XML definitions are the thing everyone agrees on.

## Caveats

The formula is a library and protocol toolkit, not an application, so there is little to run directly; the real behaviour lives in compositors, and the brief could not confirm project recency.

## Links

- [Wayland homepage](https://wayland.freedesktop.org)
