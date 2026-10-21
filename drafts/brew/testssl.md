---
name: testssl
title: testssl.sh
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, bash, network, protocol, ssl, starttls, tls]
homepage: https://testssl.sh/
scout_score: 5
status: draft
---

# testssl.sh

**TLDR;** A TLS scanner written in plain bash that probes a server's protocols, ciphers and known flaws one handshake at a time, on any port.

testssl.sh takes a host, a host:port or an HTTPS URL and asks the service what it will speak. It lists the supported protocol versions and cipher suites, then checks for known TLS flaws and misconfigurations. Output is colour-coded good or bad. It also reads HTTP security headers, tests MX records, and handles STARTTLS services such as SMTP, IMAP, POP3 and XMPP, so it is not limited to web servers.

Most checks run over raw bash sockets rather than through an OpenSSL binary. The homepage says this has been true of almost every check since version 2.9.5. That means the script builds and reads handshakes itself, and can test cipher suites the local OpenSSL was never compiled with. OpenSSL is still used for a few things such as verify, ocsp and pkey.

The idea underneath is that a TLS connection is a negotiation, and a server's answers to that negotiation can be read directly. Run it against a few hosts and you start to see what clients and servers offer each other, and why old protocol versions and cipher suites got retired. It is also private: in the project's words, "It's only you who sees the result, not a third party."

## Install

```
brew install testssl
# Needs only /bin/bash at runtime (bash >= 3.2, plus sed and awk). Homebrew pulls in openssl@4 as a dependency.
# Alternative: git clone --depth 1 https://github.com/testssl/testssl.sh.git --branch 3.3dev
```

## Try this

```
testssl.sh <hostname>
```
Runs the default full check: protocols, ciphers, flaws and more, with colour-coded results.

```
testssl.sh -x ECDH google.com
```
Tests only the ECDH ciphers the server offers, and also lists the ones it does not.

```
testssl.sh --mx google.com
```
Tests the domain's mail servers in priority order via STARTTLS on port 25, which needs outbound port 25 open.

## What's unique

It is a full TLS scanner in plain bash that does most handshake work over bash sockets, so it can test ciphers one by one, including ones the local OpenSSL lacks. It also covers STARTTLS across many protocols.

## Caveats

Version 3.2 gets no new features, the 3.3dev branch may change output and break scripts that parse it, and some core functions still depend on an OpenSSL binary.

## Links

- [Project homepage](https://testssl.sh/)
- [GitHub repository (README)](https://github.com/testssl/testssl.sh)
- [DeepWiki AI-generated docs](https://deepwiki.com/testssl/testssl.sh)
