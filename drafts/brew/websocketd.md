---
name: websocketd
title: websocketd
source: brew
category: fundamentals
commitment: quick
tags: [cgi, network, protocol, quick, unix, websocket]
homepage: http://websocketd.com
scout_score: 6
status: draft
---

# websocketd

**TLDR;** Turns any program that reads stdin and writes stdout into a WebSocket server, so a ten-line shell script can talk to a browser.

websocketd is a single binary that wraps an ordinary program and serves it over a WebSocket. When a browser connects, websocketd starts the program. Each incoming message becomes a line on its stdin, and each line the program prints to stdout goes back as a message. When the socket closes, the process is stopped.

The author's pitch is that no networking library, framework, or code change is needed. The homepage puts it this way: "It is CGI's idea, applied to WebSockets." Each connection gets its own process, just as classic CGI gave each request its own process. A counter script that runs in your shell runs unchanged behind a socket.

The door it opens is the protocol itself. WebSockets are usually hidden behind client and server libraries. Here you can watch the mapping directly: lines in, messages out, one process per connection. It also includes a static file server, a CGI server, and a built-in developer console that lets you inspect frames from a browser without writing any client code.

## Install

```
brew install websocketd
# No runtime or account needed. Single executable also available for Linux, macOS and Windows from websocketd.com/docs/start/install/
```

## Try this

```
websocketd --port=8080 ./count.sh
```
Serves your count.sh script as a WebSocket server on port 8080, starting a fresh copy of the script for each connection.

```
websocketd --devconsole
```
Starts the server with the built-in developer console, so you can open the root URL in a browser and inspect frames.

```
websocketd --help
```
Prints the command-line help listing all flags.

## What's unique

The program stays a plain stdin/stdout program with no WebSocket code, and the same script still runs in a shell. The built-in dev console lets you test it from a browser with no client code.

## Caveats

No release or last-commit date was visible, so how actively it is maintained is unconfirmed; also, teardown signals the whole process group, so scripts that deliberately spawn survivors need setsid.

## Links

- [Homepage](http://websocketd.com)
- [GitHub repository (README)](https://github.com/joewalnes/websocketd)
- [Documentation](https://websocketd.com/docs/)
- [Install page](https://websocketd.com/docs/start/install/)
