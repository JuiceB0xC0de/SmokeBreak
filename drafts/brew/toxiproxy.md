---
name: toxiproxy
title: Toxiproxy
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, chaos-testing, go, latency, network, proxy, tcp]
homepage: https://github.com/shopify/toxiproxy
scout_score: 5
status: draft
---

# Toxiproxy

**TLDR;** A TCP proxy that lets you slow, drop, cut and reset connections to Redis, MySQL or anything else, on demand, from a CLI or an HTTP API.

Toxiproxy sits between your application and a service it depends on. You create a proxy with a name, a listen address and an upstream address, then point the app at the listen address. Traffic flows through untouched until you add a toxic: latency with jitter, a bandwidth cap, packet loss, a connection reset, or taking the whole proxy down.

Shopify built it to prove with tests that an application has no single points of failure, and has used it in all development and test environments since October 2014. The README says existing tools lacked the dynamic API needed for integration and unit testing, and that Linux tools like `nc` "are not cross-platform and require root, which makes them problematic in test, development and CI environments."

The idea underneath is that a network failure is just a transformation on a byte stream, and you can make it a switch you flip. Each toxic sits on the upstream or downstream side of a connection and alters the data. A toxicity setting applies it to only a fraction of connections, so you can see how your code behaves when some requests are slow and others are fine. That is closer to how real networks fail than a clean outage.

The server exposes an HTTP API on port 8474, and the CLI is a thin client for it. Client libraries in many languages, with Ruby the original, let test code turn faults on and off.

## Install

```
brew tap shopify/shopify
brew install toxiproxy
# Docker alternative: docker run --rm -it ghcr.io/shopify/toxiproxy
# Start the server with toxiproxy-server; the CLI talks to it over HTTP on port 8474.
```

## Try this

```
toxiproxy-cli create -l localhost:26379 -u localhost:6379 shopify_test_redis_master
```
Creates a proxy listening on port 26379 that forwards to a Redis on port 6379.

```
toxiproxy-cli toxic add -t latency -a latency=1000 shopify_test_redis_master
```
Adds a 1000 ms downstream delay, so anything connecting through the proxy gets slow responses.

```
toxiproxy-cli list
```
Shows each proxy with its listen address, upstream, enabled state and active toxics.

## What's unique

It is built to be driven from test code. Faults can be switched on and off through an API, and the Ruby client can scope a fault to a single block.

## Caveats

The HTTP API is unauthenticated by default and can create proxies to arbitrary upstreams, so never expose it to an untrusted network; set TOXIPROXY_AUTH_TOKEN to require a bearer token.

## Links

- [Toxiproxy GitHub repository](https://github.com/shopify/toxiproxy)
- [Shopify blog post on resilient Rails applications](https://shopify.engineering/building-and-testing-resilient-ruby-on-rails-applications)
- [Releases (binaries and packages)](https://github.com/Shopify/toxiproxy/releases)
