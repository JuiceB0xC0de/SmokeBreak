---
name: tile38
title: Tile38
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, database, geofence, geospatial, redis-protocol, server]
homepage: https://tile38.com/
scout_score: 5
status: draft
---

# Tile38

**TLDR;** A geolocation database where adding the word FENCE to a spatial query turns it into a live stream of enter and exit events.

Tile38 is an in-memory store for things that have a position. You put objects into named collections (points, bounding boxes, geohashes, GeoJSON) and ask questions with Nearby, Within and Intersects. A spatial index answers them. The server is `tile38-server` and the client is `tile38-cli`.

The interesting move is that a query and a monitor share one syntax. Add the `fence` keyword to a search and the connection stays open. The server then pushes a JSON message whenever an object enters, exits, crosses or stays inside the area. Fences can also be stored on the server, publishing to pub/sub channels with `setchan` or to webhooks with `sethook`, so the application code never has to poll positions and compare them.

The idea underneath is geofencing as a database feature rather than application logic. It also speaks Redis RESP natively, so the README notes that most Redis clients can talk to it. Results can also come back as JSON over HTTP and websockets, so `curl` is enough to drive it. That makes it a small, concrete way into spatial indexing, streaming queries and the Redis wire protocol all at once.

## Install

```
brew install tile38
# then start the server in one terminal:
tile38-server
# and connect from another:
tile38-cli
# no account needed; the CLI connects to localhost:9851 by default
```

## Try this

```
set fleet truck1 point 33.5123 -112.2693
```
Adds a lat/lon point named truck1 to a collection called fleet.

```
nearby fleet point 33.462 -112.268 6000
```
Searches fleet for objects within 6000 meters of a point; the README says this returns one truck.

```
nearby fleet fence detect enter,exit point 33.462 -112.268 6000
```
Turns the same search into a live geofence that holds the connection open and streams enter and exit events as trucks move.

## What's unique

A plain search becomes a live monitor by adding one keyword, with enter, exit, inside, outside and cross detection built in. It also speaks Redis RESP, so existing Redis clients work.

## Caveats

It is a server you run and configure more than a tool you browse, the README is only a quick start that points to tile38.com for the real docs, and recent project activity could not be confirmed.

## Links

- [Homepage](https://tile38.com/)
- [GitHub repository](https://github.com/tidwall/tile38)
- [Geofencing docs](https://tile38.com/topics/geofencing)
