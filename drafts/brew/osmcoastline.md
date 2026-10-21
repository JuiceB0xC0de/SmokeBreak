---
name: osmcoastline
title: osmcoastline
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, geospatial, gis, maps, openstreetmap, spatialite]
homepage: https://osmcode.org/osmcoastline/
scout_score: 5
status: draft
---

# osmcoastline

**TLDR;** Turns the coastline ways in an OpenStreetMap planet file into closed land and water polygons, including a special case for Antarctica.

OpenStreetMap stores the world's coastline as thousands of separate ways tagged natural=coastline. A map renderer cannot draw a filled sea or continent from loose line segments. osmcoastline reads a planet file in PBF or XML, joins those ways into rings, and builds land polygons with holes for water. It then derives water polygons as the inverse of the land. The default output is a SpatiaLite database, and GDAL can convert it to other formats such as shapefiles.

The README describes five steps: filter the coastline ways and their nodes, assemble rings (closing gaps smaller than --close-distance), build land polygons, split large polygons with --max-points and --bbox-overlap, and create the water polygons. Each step writes problems into error_points and error_lines tables. The tool separates warnings (fixed or small geometry problems) from errors (larger ones). If errors remain, the README says you "probably do not want to use the generated data but fix the OSM data first." So the tool doubles as a quality check on a crowd-sourced map of the planet's edge.

The idea underneath is that a coastline is a topology problem. Lines must close into rings, rings must nest correctly, and the data has to be a valid polygon set. Antarctica is the odd one: its coastline is the only one allowed to stay open. The tool finds the open ends near 180° and joins them into a polygon that runs to the South Pole, or to the 85.0511° line in Web Mercator.

The companion tool osmcoastline_filter can cut a planet file to under 1% of its size, keeping only what coastlines need, so repeated runs are cheap.

## Install

```
brew install osmcoastline

You need an OSM planet file as input. The README warns that the full planet is very large. Dependencies (GDAL, GEOS, SpatiaLite, LZ4) come via brew.
```

## Try this

```
osmcoastline --help
```
Lists all command-line options, including --srs, --close-distance and --max-points.

```
osmcoastline_filter -o OUTFILE.osm.pbf INFILE.osm.pbf
```
Cuts a planet file down to the nodes and ways needed for coastlines, under 1% of the original size.

```
osmcoastline -o coastline.db planet.osm.pbf
```
Builds a SpatiaLite database with land polygons, water polygons and error tables.

## What's unique

It handles the planet's coastline as a whole, including the Antarctica special case, and reports data errors instead of silently papering over them.

## Caveats

It generally does not work on regional extracts, because unclosed coastlines cannot be assembled. The full planet file is huge, and output geometry is not simplified.

## Links

- [Homepage](https://osmcode.org/osmcoastline/)
- [GitHub repository and README](https://github.com/osmcode/osmcoastline)
- [GitHub releases](https://github.com/osmcode/osmcoastline/releases)
