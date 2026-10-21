---
name: mapscii
title: mapscii
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [braille, maps, nodejs, openstreetmap, quick, tui, visual]
homepage: https://github.com/rastapasta/mapscii
scout_score: 6
status: draft
---

# mapscii

**TLDR;** Draws a pannable, zoomable world map in your terminal using Braille characters, and you can try it over telnet with nothing installed.

MapSCII is a Node.js renderer that takes OpenStreetMap-derived vector tiles and turns them into text. Each Braille character carries a 2x4 grid of dots, so a terminal cell becomes a small canvas for drawing coastlines, roads and borders. Plain ASCII and block-character modes are also available. It runs in xterm-compatible terminals and is steered with arrow keys, the a and z keys to zoom, or mouse drag and scroll.

The tiles can come from the bundled OSM2VectorTiles-based server, from any vector tile server you point it at, or from local VectorTile and MBTiles files. The README says styling can follow the Mapbox Style spec, and that it can show points of interest around a location.

The idea underneath is the pipeline from geography to glyphs. Protobuf tiles are decoded, polygons are triangulated, lines are simplified and rasterised with Bresenham, and the result is quantised to xterm-256 colours. Each step is a small, well-known algorithm from cartography or graphics. Reading the dependency list (vector-tile, earcut, rbush, simplify-js, bresenham) is a tidy tour of how a web map works, done without a browser.

The README gives no motivation beyond its tagline, "The Whole World In Your Console". It is also "100% pure JavaScript!"

## Install

```
brew install mapscii
# needs Node (installed as a brew dependency); no account or API key. Mouse control needs a terminal that supports mouse events.
```

## Try this

```
telnet mapscii.me
```
Connects to the public hosted instance, so you see the Braille world map without installing anything.

```
mapscii
```
Starts the interactive map locally; pan with arrow keys, zoom with a and z, or drag and scroll with the mouse.

```
npx mapscii
```
Runs it straight through npm without a global install.

## What's unique

It turns a whole-world vector map into Braille glyphs in an ordinary terminal, and it is reachable over telnet with no client-side install.

## Caveats

The README lists open TODOs: it is not yet optimised for large areas, tile downloading shares the main thread, and no release date or last commit is visible, so its maintenance status is unclear.

## Links

- [GitHub repository (homepage)](https://github.com/rastapasta/mapscii)
- [Asciinema demo recording](https://asciinema.org/a/117813?autoplay=1)
- [Public demo via telnet](telnet://mapscii.me)
- [OSM2VectorTiles (bundled tile source)](https://github.com/osm2vectortiles)
