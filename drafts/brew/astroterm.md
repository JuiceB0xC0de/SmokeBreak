---
name: astroterm
title: astroterm
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [astronomy, quick, simulation, terminal, visual]
homepage: https://github.com/da-luce/astroterm
scout_score: 6
status: draft
---

# astroterm

**TLDR;** A planetarium in your terminal that draws real star, planet and moon positions for any place and date, and can spin the sky forward in time.

astroterm is a star map written in C. You give it a latitude and longitude, or a city name, plus a date and time in UTC (or let it use the system clock). It then draws the sky for that place and moment in ASCII, with optional Unicode, braille and colour. It can also animate the sky at a speed you choose.

The README pitches it as a way to look at the sky without a telescope: "no telescope required!" Because the date is a free parameter, it works for past and future skies too. The README's own example is the morning of the Apollo 11 launch, seen from Kennedy Space Center, checked against Stellarium.

The positions come from published astronomy methods rather than a lookup of pictures. The README credits Meeus-style solar position work, Paul Schlyter's planetary method, JPL approximate planetary positions, and Greg Miller's RA/Dec to Alt/Az conversion. Stars come from the Yale Bright Star Catalog, constellation figures from Stellarium's sky culture, and city coordinates from GeoNames.

The idea underneath is coordinate transforms: catalogue positions fixed on the celestial sphere, converted to what one observer sees at one instant. Once you have watched the sky wheel by at high speed, the move from sky maps to ephemerides and celestial mechanics is a short one.

## Install

```
brew install astroterm
# Unicode on Linux: the README says to set LC_ALL and LC_CTYPE to en_US.UTF-8 and configure the locales package.
```

## Try this

```
astroterm --color --constellations --speed 10000 --fps 64 --city Singapore
```
Runs the README's "spinning globe" view: a coloured sky with constellation figures, sped up 10,000 times, over Singapore.

```
astroterm --latitude 28.573469 --longitude -80.651070 --datetime 1969-7-16T8:00:00
```
Shows the sky over Kennedy Space Center on the morning of the Apollo 11 launch.

```
astroterm --city Orlando --datetime 1969-7-16T8:00:00 -m
```
Draws a similar Apollo-morning sky from the nearest major city and displays metadata.

## What's unique

It renders real ephemeris positions inside a terminal, so you can jump to any historical date and check the result against Stellarium. Constellation figures are drawn as braille stick figures, with an optional azimuthal grid.

## Caveats

Only x86_64 Linux prebuilt binaries are offered for now (arm64 is listed as "to come"), and Unicode or braille output depends on your terminal's locale and font.

## Links

- [Project homepage (GitHub)](https://github.com/da-luce/astroterm)
- [Releases](https://github.com/da-luce/astroterm/releases)
- [Homebrew formula](https://formulae.brew.sh/formula/astroterm)
- [Stellarium web comparison for Apollo 11 example](https://stellarium-web.org/skysource/UpsPeg?fov=185.00&date=1969-07-19T09:00:00Z&lat=28.47&lng=-80.56&elev=0)
