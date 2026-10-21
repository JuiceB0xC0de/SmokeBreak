---
name: linecast
title: linecast
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [astronomy, maps, python, quick, tides, visual, weather]
homepage: https://github.com/ashuttl/linecast
scout_score: 5
status: draft
---

# linecast

**TLDR;** Seven live terminal apps that draw weather, tides, sun, moon, sky, radar and maps as line art from free public data, with no API keys.

linecast is a single command with seven subcommands: weather, sunshine, moon, sky, tides, radar, and maps. Each fetches free public data for a location and draws it as a full-screen terminal view. `--print` gives a static frame instead. Several apps also offer `--json` for raw data and `--oneline` for a status bar. No accounts or API keys are needed.

The README frames it as "The Old Farmer's Almanac meets Minitel" and cites a 1990s Minitel weather screen as prior art. The idea is to show this kind of information as drawn charts rather than text tables. The brief describes a weather year laid out the way Tufte drew New York's, a sky view that can lie back until the horizon becomes a circle with the whole sky inside it, and a tide view that splits the tide into sun and moon components.

There is a cultural layer too. It has built-in sky cultures (22, per the README) and traditional calendars and hours, including Hawaiian, Chinese, Hebrew, and Islamic. Colors come from your terminal theme, and the mouse works. Where real radar is not openly published, a precipitation model fills in.

The sun, moon, tide and sky apps are a way into how these cycles relate. The tide breakdown in particular shows the pull of both bodies on the water.

## Install

```
brew install linecast
# no install: uvx linecast weather
# needs Python 3.10 or newer; on Windows use Windows Terminal
```

## Try this

```
uvx linecast weather
```
Runs the weather app without installing anything, using a location guessed from your IP address.

```
linecast maps --view now
```
Opens a full-terminal rotating globe with live daylight and clouds.

```
linecast tides --month
```
Opens the tides app directly on the month view.

## What's unique

It treats astronomical and weather data as drawn charts rather than tables, adopts your terminal theme, and includes traditional calendars and sky cultures.

## Caveats

Activity status is unknown from the README; a location guessed from IP can be far off over a VPN or SSH, and real radar covers only North America, Europe, and parts of Asia.

## Links

- [GitHub repository (homepage)](https://github.com/ashuttl/linecast)
- [Gallery of app states](https://github.com/ashuttl/linecast/blob/main/docs/gallery.md)
- [Configuration docs](https://github.com/ashuttl/linecast/blob/main/docs/configuration.md)
- [PyPI package](https://pypi.org/project/linecast/)
