---
name: libpointing
title: libpointing
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, c++, hid, library, mouse, needs-hardware]
homepage: https://github.com/INRIA/libpointing
scout_score: 5
status: draft
---

# libpointing

**TLDR;** A C++ library that reads raw mouse events and replicates the pointer acceleration curves of Windows, macOS and Xorg, so you can compare them on the same input.

Libpointing gives a program direct access to HID pointing devices such as mice. Each event arrives as raw data: x and y displacement, button state and a timestamp. The operating system's own pointer acceleration can be bypassed, so you see what the hardware actually reported rather than what the OS made of it.

The second half of the library is about transfer functions, the curves that turn raw mouse counts into pixels moved on screen. Libpointing can replicate the ones used by Windows, OS X and Xorg, and it lets you write your own. The README describes the goal as replicating them "as faithfully as possible". It came out of a UIST'11 paper titled "No More Bricolage! Methods and tools to characterize, replicate and compare pointing transfer functions" (Casiez and Roussel).

In use, a program builds a PointingDevice and a DisplayDevice from URI-style strings such as "any:?debugLevel=1". It then creates a TransferFunction, for example "sigmoid:?debugLevel=2", that links them. A callback receives the timestamp, raw dx, dy and button bits for each event, and the function's applyi method turns them into pixel displacements. The main loop calls PointingDevice::idle(100) to pump events.

The larger idea is that the feel of a mouse is mostly a function nobody looks at. Once you can see raw counts and swap the curve, pointer acceleration becomes something you can measure and experiment with. Bindings exist for Java, Python and Node.js.

## Install

```
brew install libpointing
# Installs a library only, no executables. You write a C++ program and link with: -lpointing -L/usr/local/lib
# Needs a mouse or other HID pointing device to be useful.
```

## Try this

```
brew install libpointing
```
Installs the library and headers on macOS via Homebrew.

```
-lpointing -L/usr/local/lib
```
Linker flags to add when compiling your own C++ program against libpointing on macOS.

```
qmake && make
```
Builds everything from a source checkout on macOS or Linux, if you want the repository's own code to read.

## What's unique

It reproduces the real acceleration curves of Windows, OS X and Xorg, so you can run the system function and a replica side by side on identical input. Devices are chosen at run time through URIs, and hot-plugging is supported.

## Caveats

It is a library with no command-line tool, the README's only code sample is C++, and the activity level is unclear: the wiki Installation page was last edited in April 2020.

## Links

- [Homepage (GitHub repository)](https://github.com/INRIA/libpointing)
- [Wiki: Installation](https://github.com/INRIA/libpointing/wiki/Installation)
- [Paper: No More Bricolage! (UIST'11)](https://doi.org/10.1145/2047196.2047276)
