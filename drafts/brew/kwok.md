---
name: kwok
title: kwok
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, control-plane, kubernetes, scale, simulation]
homepage: https://kwok.sigs.k8s.io
scout_score: 6
status: draft
---

# kwok

**TLDR;** Builds Kubernetes clusters full of fake nodes and pods, so you can watch a control plane cope with thousands of machines on a laptop.

KWOK stands for Kubernetes WithOut Kubelet. It ships two executables. `kwok` simulates the lifecycle of fake nodes, pods, and other API resources. `kwokctl` creates and manages whole clusters whose nodes are simulated by kwok. The result is a real Kubernetes API that kubectl, helm, and other standard clients can talk to, except the nodes report status and the pods never run anything.

The idea underneath is that a control plane does not care whether a node is real. It only sees objects and status updates. The homepage contrasts KWOK with kubemark, which is "a kubelet that does not actually run a container" and so still behaves like a kubelet and needs a lot of memory at scale. KWOK simulates only the node's behavior, which keeps memory use very low. The project pitches this as a way to see how the API server and controllers behave with thousands of nodes and tens of thousands of pods.

It also positions itself against kind. Where kind runs real Kubernetes in Docker, kwokctl can stand in when you do not need pods to actually run. Cluster creation works through a chosen runtime: binary, docker, podman, nerdctl, lima, finch, or kind-based variants. The README does not describe the internals beyond that, so the mechanism is worth reading about in the docs.

## Install

```
brew install kwok
# kwokctl needs a runtime. The binary runtime is recommended and works on linux, darwin and windows. Docker or Podman also work on some platforms.
```

## Try this

```
kwokctl --help
```
Lists the subcommands for creating and managing simulated clusters.

```
kwok --help
```
Shows the options for the process that simulates node and pod lifecycles.

## What's unique

It fakes only the node's behavior instead of running a kubelet, so the control plane sees realistic nodes at a memory cost far below kubemark's.

## Caveats

Simulated pods are not real, so curling a pod's IP returns nothing. Runtime support is uneven across platforms, and the performance figures are the project's own claims with no methodology given.

## Links

- [KWOK homepage](https://kwok.sigs.k8s.io)
- [GitHub repository (kubernetes-sigs/kwok)](https://github.com/kubernetes-sigs/kwok)
- [Manage simulated nodes and pods (docs)](https://kwok.sigs.k8s.io/docs/user/kwok-manage-nodes-and-pods/)
- [All-in-one pre-built image (docs)](https://kwok.sigs.k8s.io/docs/user/all-in-one-image/)
- [Contributor guide (docs)](https://kwok.sigs.k8s.io/docs/contributing/getting-started)
