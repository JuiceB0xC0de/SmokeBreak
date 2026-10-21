---
name: ejabberd
title: ejabberd
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, chat, erlang, mqtt, protocol, server, xmpp]
homepage: https://www.ejabberd.im
scout_score: 5
status: draft
---

# ejabberd

**TLDR;** An Erlang server that speaks XMPP, MQTT and SIP from one config file, so you can run your own chat infrastructure and see how it works.

ejabberd is an open-source realtime messaging server written in Erlang/OTP by ProcessOne. It accepts client connections (XMPP on port 5222, server-to-server on 5269, MQTT on 1883 in the homepage's sample config) and handles chat, group rooms, pub/sub, presence, message archives and push. Storage can be SQL, Redis or LDAP. It is a server you run, not a chat client.

Behaviour lives in a single `ejabberd.yml` file that lists listeners and modules, such as `mod_mam` for archives, `mod_muc` for group chat, `mod_pubsub` and `mod_push`. You administer a running node with `ejabberdctl`, a REST API or a web admin. Reading the config and the command list is a good way to see what a chat protocol is made of.

The idea underneath is twofold. XMPP is an open, federated messaging standard, so anyone can run a server that talks to other servers. And Erlang's 'let-it-crash' model, built around lightweight processes, supervision and clustering, is the reason servers like this are designed the way they are. The homepage frames the project as messaging for organisations that would rather run their own than hand it to someone else.

## Install

```
brew install ejabberd
# If you face nodedown problems, add your machine name to /private/etc/hosts after 'localhost'.
# Pulls in erlang and elixir as dependencies. A real deployment also needs DNS and TLS certificates; the first-run walkthrough is in the docs at https://docs.ejabberd.im
```

## Try this

```
ejabberdctl help
```
Lists the administration commands the server exposes, a quick map of what it can do.

```
man ejabberd.yml
```
Opens the manual page for the configuration file, where listeners and modules are defined.

```
ejabberdctl --help
```
Prints usage for the control script that starts, stops and administers a node.

## What's unique

One server speaks XMPP, MQTT and SIP (with STUN/TURN for WebRTC) over shared auth and storage, which is unusual next to single-protocol chat servers. Clustering and hot code upgrades come from the Erlang runtime rather than being add-ons.

## Caveats

It is a server product, not a toy: running it well takes protocol and Erlang-ops knowledge, and much of the homepage's scale and customer claims are unverified vendor marketing.

## Links

- [Homepage](https://www.ejabberd.im)
- [Documentation](https://docs.ejabberd.im)
- [GitHub repository](https://github.com/processone/ejabberd)
