---
name: ios-webkit-debug-proxy
title: ios-webkit-debug-proxy
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, debugging, ios, needs-hardware, protocol, usb, websocket]
homepage: https://github.com/google/ios-webkit-debug-proxy
scout_score: 6
status: draft
---

# ios-webkit-debug-proxy

**TLDR;** Bridges the debugging protocol iOS exposes over USB to websockets, so you can inspect Safari tabs on a real iPhone from a desktop.

ios_webkit_debug_proxy (iwdp) listens to the debugging traffic an iOS device exposes over USB, through the usbmuxd daemon, and re-serves it as websockets and JSON. The README describes the goal as "allowing developers to send commands to MobileSafari and UIWebViews on real and simulated iOS devices."

The port scheme is simple. A device list appears at localhost:9221. Each attached device gets its own port starting at 9222, assigned first-come-first-serve and kept across unplug and replug until the proxy restarts. Each port serves JSON endpoints listing that device's open tabs, plus websocket URLs a DevTools-style frontend can connect to. That makes it easy to script as well as to use by hand.

The idea underneath is that a phone's browser inspector is just a protocol on a wire, and a bridge can translate it. The catch is that the protocols have drifted. The README says there are "major discrepancies between Chrome Remote Debugging Protocol and Webkit Inspector Protocol," so newer Chrome DevTools cannot talk to Safari directly. You need an older or Safari-extracted inspector frontend, or the README's alternative route through Firefox DevTools via mozilla/valence.

The proxy is a bridge, not a debugger. It gives you the plumbing between USB, usbmuxd and websockets, and leaves the choice of frontend to you.

## Install

```
brew install ios-webkit-debug-proxy
# Needs an iOS device over USB (or the iOS Simulator, started before the proxy).
# On the device: Settings > Safari > Advanced > Web Inspector = ON, and keep a Safari tab open.
# Windows: scoop install ios-webkit-debug-proxy (extras bucket, plus iTunes). Linux needs several libraries built from source.
```

## Try this

```
idevice_id -l
```
Lists attached devices that usbmuxd can see, a check before starting the proxy. It comes from libimobiledevice's utilities.

```
ios_webkit_debug_proxy
```
Starts the proxy with default settings. Open localhost:9221 for the device list, then follow a device's port from 9222 to see its tabs.

```
ios_webkit_debug_proxy -f chrome-devtools://devtools/bundled/inspector.html
```
Serves a specific DevTools frontend page. Links on localhost:9222 are blocked with this frontend, so paste the URL into the address bar.

## What's unique

It is a bridge, not a debugger: it turns a phone's USB inspector channel into plain websocket and JSON endpoints that any compatible frontend can use. Its one-port-per-device mapping stays stable across reconnects.

## Caveats

Needs an iOS device or the Simulator, and parts of the docs look dated: the default frontend URL pins a Chrome DevTools build from around 2013 to 2015, and newer Chrome DevTools does not work with Safari.

## Links

- [GitHub repository and README](https://github.com/google/ios-webkit-debug-proxy)
- [Design document](https://github.com/google/ios-webkit-debug-proxy/blob/master/design.md)
- [Example clients](https://github.com/google/ios-webkit-debug-proxy/blob/master/examples/README.md)
