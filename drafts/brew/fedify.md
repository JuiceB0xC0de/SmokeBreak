---
name: fedify
title: fedify
source: brew
category: fundamentals
commitment: afternoon
tags: [activitypub, afternoon, debugging, fediverse, json-ld, network, protocol]
homepage: https://fedify.dev/cli
scout_score: 5
status: draft
---

# fedify

**TLDR;** A command-line tool that fetches and prints raw ActivityPub objects, and gives you a throwaway public inbox to watch what a federated server sends.

fedify is the CLI that ships with the Fedify framework, which is for building ActivityPub servers. ActivityPub is the protocol behind Mastodon and much of the fediverse. The tool is meant for Fedify developers, but its README says it works with any ActivityPub-enabled server.

The everyday command is `fedify lookup`. Give it an object URL or an actor handle like `@user@example.com`, and it resolves the handle, fetches the object over HTTP, parses the JSON-LD and prints it. You can read it as a formatted dump, as compacted or expanded JSON-LD, or as raw JSON. With `--traverse` it walks a collection such as an outbox and prints the objects inside rather than the collection itself.

Some objects refuse anonymous requests. For those, `--authorized-fetch` generates a one-time key pair, starts a temporary server to publish the public key, and signs the request. It tries RFC 9421 HTTP signatures first and falls back to the older draft-cavage style. It also resolves FEP-ef61 portable objects (`ap://` URIs with DIDs).

`fedify inbox` goes the other way. It starts an ephemeral server with a one-time actor, exposes it on a short-lived public HTTPS name, and logs every activity that arrives. Point a server at it and you see what that server sends. The docs note: "Although the given URIs and handle are short-lived, they are anyway publicly dereferenceable until the server is terminated." There is also `fedify init`, which scaffolds a new Fedify project.

## Install

```
brew install fedify
# also: npm install -g @fedify/cli (Node is a dependency of the brew formula)
# authorized fetch and inbox need a temporary public tunnel (fedify.com.es, serveo.net or pinggy.io are named in the docs)
```

## Try this

```
fedify lookup @fedify-example@fedify-blog.deno.dev
```
Resolves the handle and prints the actor's ActivityPub object.

```
fedify lookup --traverse https://fosstodon.org/users/hongminhee/outbox
```
Walks the outbox and prints the posts inside it rather than the collection wrapper.

```
fedify inbox
```
Starts a temporary public ActivityPub inbox and logs incoming activities until you press ^C.

## What's unique

fedify inbox gives you a disposable public actor and inbox for watching a server's outgoing traffic. Authorized fetch tries both signature schemes and resolves FEP-ef61 portable objects, which most ActivityPub tooling does not do.

## Caveats

Authorized fetch and inbox expose a temporary server to the public internet through a tunnel service, and the brief could not read the full inbox, relay or nodeinfo docs.

## Links

- [Homepage (CLI docs)](https://fedify.dev/cli)
- [Markdown version of the CLI docs](https://fedify.dev/cli.md)
- [GitHub repository](https://github.com/fedify-dev/fedify)
- [GitHub releases](https://github.com/fedify-dev/fedify/releases)
