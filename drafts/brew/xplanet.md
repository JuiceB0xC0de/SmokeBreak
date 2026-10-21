---
name: xplanet
title: xplanet
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [astronomy, quick, science, visual, wallpaper]
homepage: https://xplanet.sourceforge.net/
scout_score: 5
status: draft
---

# xplanet

**TLDR;** Renders a shaded image of Earth, another planet, or the Moon as seen from any chosen place and date, then saves it or sets it as your wallpaper.

Xplanet draws a planet, moon, or the Sun from a chosen observer position and time. It can paint into an X window, write an image file (gif, jpg, png, ppm, tiff), or set the desktop background. Earth is the default target. You choose the date, the viewpoint, and whether you see a globe or a flat map in one of many projections: Mercator, Mollweide, Lambert, orthographic, azimuthal and others.

It was inspired by Xearth, which put an image of the Earth in the X root window. Xplanet goes further. The homepage says all the major planets and most satellites can be drawn. Positions come from a built-in model, or from JPL ephemeris and SPICE kernel files if you want precise ones. With the right data files you can center the view on a spacecraft such as Cassini or on Hubble, using NORAD IDs and TLE files.

The idea underneath is that a picture of the sky is a computation: put an observer somewhere, pick a time, and work out what is lit and what is in shadow. Changing the observer lets you see Earth from the Sun, or with the Moon 3 degrees to one side. With -wait or -num_times it re-renders on a timer, so the wallpaper follows real time.

## Install

```
brew install xplanet
Spacecraft and SPICE features need extra data files (JPL ephemeris, SPICE kernels, TLE files) and a build with those options. Map images are searched for in the current directory, then -searchdir, then ~/.xplanet on X11 or ~/Library/Xplanet on macOS.
```

## Try this

```
xplanet --help
```
Lists the large set of command-line options.

```
xplanet -output earth.png -geometry 800x800
```
Renders the Earth as it looks right now and saves it to a PNG instead of opening a window.

```
xplanet -target earth -separation moon:-3 -output moon.png
```
Renders Earth from a point where the Moon appears 3 degrees to its left.

## What's unique

It descends from Xearth but covers many bodies, many map projections, and real ephemeris and spacecraft-tracking input. The option set is big enough to make it a small astronomy visualizer, not just a wallpaper tool.

## Caveats

The documentation describes old platforms such as FreeBSD 5.1 and Sparc Solaris, no recent release date is visible, and the README warns that -pango appears to leak memory.

## Links

- [Xplanet homepage](https://xplanet.sourceforge.net/)
- [Option reference (the page served at /README)](https://xplanet.sourceforge.net/README)
