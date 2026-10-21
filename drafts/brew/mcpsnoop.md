---
name: mcpsnoop
title: mcpsnoop
source: brew
category: fundamentals
commitment: quick
tags: [debugging, json-rpc, mcp, protocol, proxy, quick, tui]
homepage: https://github.com/kerlenton/mcpsnoop
scout_score: 6
status: draft
---

# mcpsnoop

**TLDR;** A transparent proxy and terminal UI that shows every JSON-RPC message passing between an AI client and its MCP server, like Wireshark for MCP.

Model Context Protocol (MCP) is how AI clients such as Cursor, Claude Code and Claude Desktop talk to tool servers. Under the hood it is JSON-RPC frames going back and forth, usually over a process's stdin and stdout. Normally nobody sees them. mcpsnoop sits in that path and copies each frame without changing either side.

You put `mcpsnoop --` in front of the server command your client launches. That shim forwards bytes verbatim and sends a copy of every frame to a hub. Running `mcpsnoop` with no arguments opens the live TUI, which finds running shims through a well-known socket and backfills past sessions from disk, so neither side has to start first. For Streamable HTTP servers, `mcpsnoop http` works as a reverse proxy and also records HTTP statuses such as 401, 403, 202 and 502, which carry no JSON-RPC message at all.

The README's argument for existing is that the official MCP Inspector connects as its own client. It therefore never sees what your real client actually sends: calls the model never made, wrong arguments, or capability mismatches. mcpsnoop watches the real conversation instead.

Captures can be saved as session logs and exported as json, html, text, har or OpenTelemetry spans. They can also be checked in CI by replaying a recorded session against each new build of a server, with no model involved. It is a small door into how an emerging protocol behaves on the wire.

## Install

```
brew install mcpsnoop
# also: npx mcpsnoop, npm i -g mcpsnoop, or go install github.com/kerlenton/mcpsnoop/cmd/mcpsnoop@latest
# To watch a real client, edit its MCP config so the command is mcpsnoop with args ['--', <original command>], then restart the client.
```

## Try this

```
mcpsnoop demo
```
Plays a scripted session so you can see the TUI working with no setup.

```
mcpsnoop
```
Opens the live TUI, which finds running shims on its own and backfills past sessions from disk.

```
mcpsnoop wrap my-server
```
Routes one Claude Desktop server through mcpsnoop by editing only that server's entry in its config; `mcpsnoop unwrap my-server` undoes it.

## What's unique

It sits in the real data path between your actual client and server rather than acting as a client itself. It can also replay a recorded session in CI without calling a model, and export traffic as OpenTelemetry spans.

## Caveats

It runs the server command you wrap, so only wrap trusted servers, and captures can contain prompts, credentials and tool results, so scrub them before sharing.

## Links

- [Homepage (GitHub repo and README)](https://github.com/kerlenton/mcpsnoop)
- [Releases](https://github.com/kerlenton/mcpsnoop/releases)
- [Checking sessions in CI (docs/CI.md)](https://github.com/kerlenton/mcpsnoop/blob/main/docs/CI.md)
- [OpenTelemetry and Prometheus (docs/OPENTELEMETRY.md)](https://github.com/kerlenton/mcpsnoop/blob/main/docs/OPENTELEMETRY.md)
