---
name: decompose
title: decompose
source: brew
category: take-things-apart
commitment: quick
tags: [docker, graphviz, network, quick, reverse-engineering, visualization]
homepage: https://github.com/s0rg/decompose
scout_score: 6
status: draft
---

# decompose

**TLDR;** Reads the live network connections of running Docker containers and draws the architecture, so you can see how an undocumented stack fits together.

decompose asks the Docker daemon what is running, then looks at what each container is actually talking to. From that it builds a graph of who listens on which ports and who connects to whom. The default output is a JSON stream. It can also write graphviz dot, structurizr DSL, PlantUML, compose YAML, a pseudographical tree, CSV, or plain statistics such as node, connection and listen-port counts.

The author built it for a specific problem: a large dockerized legacy system with more than 470 containers, "without any schemes and having a bare minimum of documentation". Tools that rebuild a picture from compose files only see what the configuration claims. decompose observes the running system instead, so it can find connections the configuration never mentions.

On Linux as root it uses nsenter to look inside each container's network namespace, which works even for scratch-based images with no tools in them. Without root, or on other systems, it runs netstat inside each container, and a container without netstat shows no connections. All output formats are sorted, so you can commit them to version control and diff how a stack changes over time.

The idea underneath is that a running system is its own documentation. You can recover architecture from behaviour. Saved JSON streams can be loaded and merged, so several snapshots can build up a fuller picture.

## Install

```
brew install decompose
# needs a running Docker daemon; settings come from DOCKER_HOST and related environment variables
# on Linux, run with sudo for the nsenter strategy and unix-socket matching
```

## Try this

```
decompose -format dot | dot -Tsvg > redis-cluster.svg
```
Pipes the connection graph through graphviz (installed separately) and renders an SVG of your running stack.

```
sudo decompose > nodes-1.json
```
Saves the full JSON stream of the running environment to a file, using the nsenter strategy as root.

```
decompose -cluster auto:0.6 -format sdsl > workspace.dsl
```
Groups services automatically by port-set similarity and writes a structurizr DSL workspace.

## What's unique

It reconstructs architecture from observed connections inside live containers rather than from compose files. Its sorted output also makes the result diffable in version control.

## Caveats

Only established and listening connections are listed, so short-lived ones are missed, and containers without netstat show nothing unless you run as root on Linux; the brief could not confirm recent maintenance.

## Links

- [GitHub repository (homepage)](https://github.com/s0rg/decompose)
- [Releases (binaries, deb, rpm)](https://github.com/s0rg/decompose/releases)
- [Docker Hub image](https://hub.docker.com/r/s0rg/decompose)
