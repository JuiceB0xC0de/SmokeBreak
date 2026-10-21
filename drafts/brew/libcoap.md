---
name: libcoap
title: libcoap
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, c, coap, iot, network, protocol, udp]
homepage: https://github.com/obgm/libcoap
scout_score: 6
status: draft
---

# libcoap

**TLDR;** A reference C implementation of CoAP, the tiny HTTP-like protocol that sensors and IoT gear speak, with a client and server you can run locally.

CoAP, the Constrained Application Protocol (RFC 7252), is built for devices with little computing power, memory, bandwidth, or packet size. It keeps the request and response shape of HTTP, with resources, methods and status codes, but runs over small UDP datagrams instead of TCP and text headers. libcoap is a C library that implements it. It needs only malloc() and BSD-style sockets, and it also supports Contiki-NG, ESP-IDF, LwIP and RIOT-OS.

The Homebrew formula installs the example programs from the repository: a CoAP client, a Resource Directory server and a general CoAP server. Each comes in a plain build and an `-openssl` build. The README says they exist "to demonstrate the use of this library", so you can start a server in one terminal and talk to it from a client in another, and see what a constrained-device protocol looks like on the wire.

The library goes well past the basics. It covers observe (RFC 7641), block-wise transfer (RFC 7959), OSCORE (RFC 8613), and CoAP over TCP, TLS and WebSockets (RFC 8323). It can use any of six TLS libraries for DTLS. CoAP is a good door into how IoT protocols trade features for size, and how security is retrofitted onto tiny devices.

## Install

```
brew install libcoap
```

## Try this

```
coap-server --help
```
Lists the options for the example CoAP server, since the README gives no usage notes.

```
coap-client --help
```
Shows how to choose a method, set a URI and send a request to a CoAP server.

```
coap-rd --help
```
Shows the options for the Resource Directory server, which lets devices register the resources they offer.

## What's unique

It is a reference-grade CoAP stack that covers many extensions (observe, block-wise transfer, OSCORE, CoAP over TCP and WebSockets) and runs from desktop POSIX down to embedded OSes.

## Caveats

The README does not document the executables' command-line usage, so you will rely on --help and libcoap.net, and features such as DTLS vary by platform.

## Links

- [Homepage (GitHub)](https://github.com/obgm/libcoap)
- [Documentation](https://libcoap.net)
- [Install guide](https://libcoap.net/install.html)
- [libcoap-minimal usage examples](https://github.com/obgm/libcoap-minimal)
