---
name: xdotool
title: xdotool
source: brew
category: take-things-apart
commitment: quick
tags: [automation, cli, input, quick, windows, x11]
homepage: https://www.semicomplete.com/projects/xdotool/
scout_score: 5
status: draft
---

# xdotool

**TLDR;** Type, click, and rearrange windows on an X11 desktop from the shell, by sending synthetic input through the X server.

xdotool is a command-line tool for X11 desktops that simulates keyboard and mouse input and manages windows. You can search for windows by name or class, then focus, move, resize, or hide them, or send them keystrokes. On window managers that support it, it can also switch desktops and move windows between them.

The homepage gives no formal rationale, but the idea is plain: a desktop is something you can script from the shell without writing an Xlib program. It generates input through X11's XTEST extension and other Xlib functions, and window searches and changes go through the same X interface.

The interesting part is chaining. A search returns window IDs, and the next command in the line can act on them. The page's example is `xdotool search "Mozilla Firefox" windowactivate --sync key --clearmodifiers ctrl+l`, which finds Firefox, focuses it, and presses Ctrl+L to reach the URL bar. Behind it sits a larger idea: the X server treats a synthetic keypress much like a real one, which is why one small tool can drive almost any graphical program.

## Install

```
brew install xdotool
# macOS: XTEST must be enabled in the X11 server (XQuartz):
defaults write org.x.X11 enable_test_extensions -boolean true
# Needs a running X11 session. On Debian/Ubuntu: apt-get install xdotool
```

## Try this

```
xdotool --help
```
Prints the list of commands the tool understands.

```
xdotool search "Mozilla Firefox" windowactivate --sync key --clearmodifiers ctrl+l
```
Finds a Firefox window, focuses it, and sends Ctrl+L to jump to the URL bar.

```
xdotool search --onlyvisible --classname "gnome-terminal" windowsize %@ 500 500
```
Resizes every visible gnome-terminal window to 500 by 500 pixels.

## What's unique

It chains find, focus, resize, and keystroke steps on one shell line, so desktop automation needs no code beyond that line.

## Caveats

It targets X11 and the page does not mention Wayland; the homepage is dated 2015, I couldn't confirm recent activity, and on macOS XTEST must be enabled by hand.

## Links

- [xdotool homepage (Jordan Sissel's project page)](https://www.semicomplete.com/projects/xdotool/)
