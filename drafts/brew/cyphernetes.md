---
name: cyphernetes
title: Cyphernetes
source: brew
category: languages-and-oddities
commitment: quick
tags: [graph, kubernetes, language, query-language, quick]
homepage: https://cyphernet.es
scout_score: 5
status: draft
---

# Cyphernetes

**TLDR;** A Cypher-style graph query language for Kubernetes: write MATCH and WHERE statements against cluster resources instead of chaining kubectl, xargs and bash.

Cyphernetes lets you query a Kubernetes cluster the way you would query a graph database. You write statements with MATCH, WHERE and DELETE, borrowed from Cypher, and it runs them against the objects in your cluster, Pods included. The homepage also describes a REPL, a web interface that draws the cluster as a graph, and a way to define reactive operators using query syntax.

The reason it exists, per the homepage, is that multi-step cluster work in kubectl tends to become a pipeline of shell pipes, xargs and inline bash. The homepage's own example deletes every non-running pod. In kubectl that takes a long `get | xargs bash -c` pipeline. In Cyphernetes it is one line: `MATCH (p:Pod) WHERE p.status.phase != "Running" DELETE p;`.

The idea underneath is that cluster state is already a graph. Deployments own ReplicaSets, which own Pods, and Services select Pods. If the relationships are first-class, one statement can span several resource types. The homepage says it discovers CRDs automatically and understands those relationships with no configuration. It does not explain the internals, so treat that as a claim to test.

## Install

```
brew install cyphernetes
# Needs access to a Kubernetes cluster (a kubeconfig) to run queries against.
```

## Try this

```
cyphernetes --help
```
Lists the available commands and options, a safe first look before pointing it at a cluster.

## What's unique

It reuses Cypher, a graph database query language, for Kubernetes, so relationships between resources are part of the query rather than something you stitch together in shell.

## Caveats

The homepage is marketing copy with no version or release date, and the GitHub README was not checked, so the REPL, web UI and operator claims are unverified; the homepage's example query is a destructive DELETE, so try it only on a throwaway cluster.

## Links

- [Homepage](https://cyphernet.es)
