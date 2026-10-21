---
name: keyd
title: keyd
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, daemon, evdev, keyboard, linux, remapping, uinput]
homepage: https://github.com/rvaiya/keyd
scout_score: 5
status: draft
---

# keyd

**TLDR;** A Linux daemon that remaps keys below the display server, bringing QMK-style layers and tap/hold keys to any keyboard with a short config file.

keyd reads raw key events from your physical keyboards through evdev, applies the mappings from a plain INI-style config, and writes the result to a virtual keyboard created through uinput. Because it sits below X and Wayland, the same config works in a text console, under X, or under Wayland.

The config is short. A line like `capslock = overload(control, esc)` makes Caps Lock act as Escape when tapped and Control when held. The same format covers layers, oneshot modifiers, per-keyboard sections selected by device ID, and Unicode output. Those features usually live in QMK-style keyboard firmware, and keyd moves them into the operating system.

The README's complaint is that "Linux lacks a good key remapping solution." The usual answer is to chain tools like xcape and xmodmap, which ties the result to X11. keyd replaces that chain with one daemon. The core is C in under 2000 lines, and the author aims for a sub-millisecond input loop.

The idea underneath is how a keypress becomes software on Linux. A device emits events, something grabs them, and something else re-emits them as a new device. Once you see that layer, remapping is only a matter of what you do in the middle. `keyd monitor` shows the key names and events as keyd sees them.

## Install

```
brew install keyd
# Linux only. The Homebrew formula's caveat says the default config goes in $HOMEBREW_PREFIX/etc/keyd/default.conf.
# The README itself documents no Homebrew route: it lists building from source (C compiler and kernel headers, then make && sudo make install) or a distro package.
# After a source or distro install: sudo systemctl enable --now keyd, with config in /etc/keyd/default.conf.
# Needs root and a systemd or similar service setup to run as a daemon.
```

## Try this

```
keyd monitor
```
Prints key names and events as keyd sees them, so you can find the names to use in the config. The README says to stop keyd first to see the raw input events.

```
sudo keyd reload
```
Reloads the config after you edit default.conf, for example after adding capslock = overload(control, esc) under [main].

```
sudo journalctl -eu keyd
```
Shows the service log, which is where config errors appear.

## What's unique

It brings layers, oneshot modifiers and tap/hold overloads, normally found in custom keyboard firmware, to the OS level. It does this in a small C daemon that does not depend on X11 or Wayland.

## Caveats

Linux only, and the README says nothing about Homebrew. A bad config can lock you out of your keyboard; the escape hatch is backspace+escape+enter, which terminates keyd. Application-specific remapping is marked experimental, and master may break between releases.

## Links

- [Homepage (GitHub repository)](https://github.com/rvaiya/keyd)
- [Man page (docs/keyd.scdoc)](https://raw.githubusercontent.com/rvaiya/keyd/refs/heads/master/docs/keyd.scdoc)
- [Changelog](https://github.com/rvaiya/keyd/blob/master/docs/CHANGELOG.md)
