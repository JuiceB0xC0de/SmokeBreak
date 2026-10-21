---
name: ssh3
title: ssh3
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, go, http3, network, protocol, quic, ssh]
homepage: https://arxiv.org/abs/2312.08396
scout_score: 7
status: draft
---

# ssh3

**TLDR;** An experimental remote shell that runs the SSH Connection Protocol over HTTP/3 and QUIC, so a server can hide behind a secret URL and answer 404 to scanners.

SSH3 is a client (`ssh3`) and server (`ssh3-server`) written in Go. It gives you a remote terminal, like OpenSSH, but the secure channel is QUIC with TLS 1.3, and the connection is an HTTP/3 request. User authentication goes through HTTP Authorization. That covers passwords, public keys, an agent, and OpenID Connect logins through providers such as Google, GitHub or Microsoft Entra.

The authors say SSH dates from the late nineties and wanted to revisit it with modern transport. Their main claim is faster session establishment: 3 round trips instead of 5 to 7. The README is clear that this is about setup time, not throughput: "Faster for session establishment, not throughput !"

The idea underneath is that a shell session is just a set of semantics (channels, forwarding, exec) that can ride on any transport. Put them on HTTP/3 and you inherit things the web already has. The server can sit behind a secret URL path and return 404 to everything else. UDP port forwarding can use QUIC datagrams. Proxy jump uses that forwarding, so the middle host cannot decrypt end-to-end traffic. The README's own warning is to hide the path but never rely on it for access control.

The homepage is the arXiv paper, "Towards SSH3: how HTTP/3 improves secure shells". An Internet-Draft, draft-michel-remote-terminal-http3-00, describes the protocol. It is a good way to see how a protocol you use daily looks when rebuilt on a different layer.

## Install

```
brew install ssh3
# Needs a host to run ssh3-server on, plus an X.509 certificate and key (defaults ./cert.pem and ./priv.key).
# Self-signed (-generate-selfsigned-cert) or Let's Encrypt (-generate-public-cert) both work.
# Like OpenSSH, the server must run as root to log in other users.
```

## Try this

```
ssh3 --help
```
Lists the client's options, including key, password and config-based login.

```
ssh3-server -generate-public-cert my-domain.example.org -url-path /ssh3
```
Starts a public server on port 443 with a Let's Encrypt certificate, answering only on /ssh3.

```
ssh3 -privkey ~/.ssh/id_rsa username@my-server.example.org/my-secret-path
```
Connects with a private key, with the secret URL path appended to the host.

## What's unique

It keeps the SSH Connection Protocol but maps it onto HTTP/3, so the server can hide behind a secret URL and logins can go through an OpenID Connect provider. It also adds UDP port forwarding over QUIC datagrams, which OpenSSH lacks.

## Caveats

The README calls it an experimental proof of concept and says "Do not deploy the SSH3 server on your production servers for now"; it may be renamed, has no daemon, and lacks reverse port forwarding.

## Links

- [arXiv paper: Towards SSH3: how HTTP/3 improves secure shells (homepage)](https://arxiv.org/abs/2312.08396)
- [GitHub repository](https://github.com/francoismichel/ssh3)
- [Internet-Draft draft-michel-remote-terminal-http3-00](https://datatracker.ietf.org/doc/draft-michel-remote-terminal-http3/)
