---
name: gnmic
title: gnmic
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, grpc, network, protocol, telemetry, yang]
homepage: https://gnmic.openconfig.net
scout_score: 5
status: draft
---

# gnmic

**TLDR;** A command-line client for gNMI, the gRPC protocol modern network gear uses to expose config and live telemetry, which can also act as a telemetry collector.

gnmic is a Go client for gNMI, a protocol from the OpenConfig project. Routers and switches that support it expose a gRPC endpoint. gnmic talks to that endpoint with four calls, each its own subcommand: `capabilities`, `get`, `set` and `subscribe` (`sub` for short).

The interesting one is subscribe. Instead of polling a device with SNMP, you ask for a path such as a port's statistics and the device streams updates back, for example every 10 seconds. The paths come from YANG models, the schemas that describe what a device can report or be configured with. Reading the output shows you how a vendor's internal state is laid out as a tree.

The same binary can run as a collector. It takes streams from many targets, passes them through event processors that filter, enrich and convert them, and writes the result to outputs such as Prometheus, InfluxDB, Kafka, NATS or ClickHouse. The project's pitch is "Streaming telemetry that works."

Prompt mode is a side door. Point it at a clone of the OpenConfig YANG models and the CLI suggests XPATH values as you type. The README calls this "voodoo magic", and it works as a way to browse a model without reading the schema files.

## Install

```
brew install gnmic
# You also need a device that exposes gNMI (a lab router or a vendor container image). The homepage examples assume user admin and --insecure, which turns TLS off.
```

## Try this

```
gnmic --help
```
Lists the subcommands and global flags, including the target, credential and TLS options.

```
gnmic -a 10.1.0.11:57400 -u admin -p admin --insecure capabilities
```
Asks the device which models, encodings and gNMI version it supports. Replace the address with your own lab device.

```
gnmic -a 10.1.0.11:57400 -u admin -p admin --insecure subscribe --path '/state/port[port-id=1/1/c1/1]/statistics' --sample-interval 10s
```
Streams port statistics from the device every 10 seconds. The path is from the homepage example and depends on the device.

## What's unique

It covers both ends in one binary: a one-off CLI for poking a single device, and a collector that fans streams out to many backends. Prompt mode adds YANG-aware path suggestions.

## Caveats

It needs a gNMI-capable device to be useful, the examples disable TLS and are lab-only, and Windows is supported only through WSL.

## Links

- [Homepage and documentation](https://gnmic.openconfig.net)
- [GitHub repository (openconfig/gnmic)](https://github.com/openconfig/gnmic)
- [Install options](https://gnmic.openconfig.net/install/)
- [Prompt mode (YANG path suggestions)](https://gnmic.openconfig.net/user_guide/prompt_suggestions/)
