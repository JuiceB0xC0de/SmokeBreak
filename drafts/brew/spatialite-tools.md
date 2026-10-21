---
name: spatialite-tools
title: spatialite-tools
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, gis, maps, openstreetmap, shapefile, sql, sqlite]
homepage: https://www.gaia-gis.it/fossil/spatialite-tools/index
scout_score: 5
status: draft
---

# spatialite-tools

**TLDR;** A bundle of about twenty command-line tools that turn SQLite into a GIS workbench: shapefiles, OpenStreetMap, GPS photos and routing networks, all in one database file.

spatialite-tools is the command-line companion to SpatiaLite, a spatial extension for SQLite. The main tool, `spatialite`, is described as "a complete CLI front-end, more or less equivalent to the well known sqlite3 front-end, but fully supporting SpatiaLite". You get the familiar SQLite shell, with geometry types and spatial functions available.

The other executables are small single-purpose converters and checkers. They import and export Shapefiles and DBF files, check shapefiles for anomalies, load EXIF/GPS metadata from JPEG pictures, import GML and DXF files, build routing networks, process OpenStreetMap data, and handle XML. The XML tools were funded by the Tuscany Region's Territorial and Environmental Information System.

The idea underneath is that a spatial database does not have to be a server. A whole map dataset can live in one SQLite file that you copy around, query with SQL, and feed from the shell. If GIS has seemed like heavy desktop software, this is a way in that looks like a pipeline of small Unix tools.

## Install

```
brew install spatialite-tools
```

## Try this

```
spatialite --help
```
Lists the options of the SpatiaLite-aware SQLite shell.

```
spatialite_tool --help
```
Shows the options of the general import and export tool for shapefiles, DBF and similar formats.

```
exif_loader --help
```
Shows how to load EXIF and GPS metadata from JPEG pictures into a database.

## What's unique

It is a whole suite of small converters around one idea, SQL for maps in a single SQLite file, and its shell is a drop-in replacement for sqlite3.

## Caveats

The homepage has no usage examples or build notes, and the last release listed is 5.1.0a from August 2023, so expect to learn it from --help and the SpatiaLite docs.

## Links

- [spatialite-tools homepage](https://www.gaia-gis.it/fossil/spatialite-tools/index)
