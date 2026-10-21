---
name: netcode
title: netcode
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, c, crypto, gamedev, library, network, protocol, udp]
homepage: https://github.com/mas-bandwidth/netcode
scout_score: 5
status: draft
---

# netcode

**TLDR;** A small C library that adds secure, token-authenticated connections on top of UDP, built for multiplayer games and a clear look at connection design.

netcode is a C library that gives UDP something it lacks: a connection. Real-time games use UDP because TCP's head-of-line blocking holds back newer packets while older dropped ones are resent. But UDP has no notion of who is connected, so every game ends up building that layer itself, which the author calls "a lot of work!"

The design puts trust in a backend. A web service, such as a matchmaker, issues each authorized client a connect token. The server is created with a shared 32 byte private key and a maximum token lifetime, and it accepts only clients holding a valid token. It refuses tokens that could have been issued before it started. Connected clients take one of a fixed number of slots, and when the slots are full new clients are denied quickly.

Once connected, client and server exchange unreliable, unordered packets that are encrypted and signed with libsodium. The library stops there on purpose. In the author's words, it lets you "quickly get to exchanging unreliable unordered packets and get busy building the rest of your game network protocol."

The idea underneath is worth the visit: how to do a handshake, authorization and replay protection with little machinery, and keep access control out of the game server. There is a written standard (netcode 1.02) and ports in C#, Go, Rust, Unity, UE4 and TypeScript, so you can compare the same protocol across languages.

## Install

```
brew install netcode
# Installs the C library only, with libsodium as a dependency. No executables are installed. The README gives no build steps, so you read client.c and server.c and link against it from your own C code. A real game also needs a backend that issues connect tokens.
```

## Try this

```
netcode_default_server_config( &server_config );
```
Fills a server config struct with defaults, ready for you to override fields.

```
struct netcode_server_t * server = netcode_server_create( server_address, &server_config, time );
```
Creates a server bound to an address such as "127.0.0.1:40000", and returns NULL on failure.

```
netcode_server_start( server, 16 );
```
Starts the server with 16 client slots.

## What's unique

Authorization lives in a web backend that issues connect tokens, not in the game server, so matchmaking and access control stay outside it. It is a small protocol with a written standard and many ports.

## Caveats

It is a library with no command-line tool, the README gives no platform or build instructions and no visible version or release dates, and you need your own token-issuing backend to use it for real.

## Links

- [Project homepage (GitHub)](https://github.com/mas-bandwidth/netcode)
- [netcode 1.02 standard](https://github.com/mas-bandwidth/netcode/blob/main/STANDARD.md)
- [IMPLEMENTERS.md](https://github.com/mas-bandwidth/netcode/blob/main/IMPLEMENTERS.md)
