---
name: srtp
title: libSRTP
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, crypto, library, network, protocol, rtp, voip]
homepage: https://github.com/cisco/libsrtp
scout_score: 5
status: draft
---

# libSRTP

**TLDR;** Cisco's reference C library for SRTP, the encryption layer under WebRTC and VoIP calls, with a small demo that sends words over an encrypted stream.

libSRTP implements the Secure Real-time Transport Protocol from RFC 3711. You give it plain RTP or RTCP packets and a policy: which stream (SSRC), which crypto profile, and a master key and salt. `srtp_protect()` returns encrypted, authenticated SRTP packets. `srtp_unprotect()` takes them back and returns verified RTP. The API is small and opaque, declared in `include/srtp.h`.

It was written by David McGrew at Cisco, and the README frames it as a reference implementation meant to promote the use, understanding and interoperability of Secure RTP. It also covers the Universal Security Transform and AES-GCM from RFC 7714. The crypto backend is pluggable: an internal AES and SHA-1 by default, or OpenSSL or NSS if you configure them in.

The idea underneath is how real-time media gets protected packet by packet. A session holds a stream context per sending source. The packet's sequence number supplies the low 16 bits of the packet index, and replay protection sits in the crypto engine. Reading the library shows how encrypted calls work without a TCP-style connection.

The Homebrew formula installs the library. The `rtpw` demo lives in the source tree's `test/` directory, so you build from source to run it. It sends dictionary words from a sender to a receiver over SRTP.

## Install

```
brew install srtp
# Installs the library only (no executables). To run the rtpw demo, build from source: https://github.com/cisco/libsrtp (needs a C toolchain)
```

## Try this

```
./configure --enable-openssl && make
```
Run in a source checkout, this builds libsrtp with the OpenSSL backend, which adds AES-192 and AES-GCM.

```
meson test -C builddir
```
After meson setup and compile, this runs the test suite of the Meson build.

```
test/rtpw -s -k $k -e 128 -a 0.0.0.0 9999
```
Sends dictionary words over SRTP with a hex master key, AES-128 encryption and authentication. Run the same with -r for the receiver.

## What's unique

It is the reference implementation of SRTP, the encryption layer under many WebRTC and VoIP stacks. The policy-driven API and the rtpw demo make the protection model easy to see.

## Caveats

It is a library with no executables; the demo needs a source build, parts of the README are dated (copyright 2001-2017), and the README warns the library can be misused in ways that leave security inadequate.

## Links

- [GitHub repository (homepage)](https://github.com/cisco/libsrtp)
- [Releases](https://github.com/cisco/libsrtp/releases)
- [RFC 3711 (SRTP)](https://tools.ietf.org/html/rfc3711)
