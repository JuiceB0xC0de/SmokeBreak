---
name: kraftkit
title: KraftKit
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, containers, firecracker, go, qemu, unikernel, virtualization]
homepage: https://unikraft.org/docs/cli
scout_score: 5
status: draft
---

# KraftKit

**TLDR;** Build and boot unikernels, tiny single-purpose VMs that bundle an app with a minimal library OS, using a Docker-like workflow and the kraft command.

KraftKit ships as the `kraft` command. It takes an application, either a Dockerfile-based rootfs described by a Kraftfile or a pre-built image from the Unikraft catalog, and produces a unikernel image. It can run that image locally under QEMU, Xen or Firecracker, or push it as an OCI package. It also has local networking, volume and compose-style commands, and the README describes a Go SDK for building unikernels from code.

The idea underneath is the unikernel. A normal VM boots a general-purpose operating system and then runs your app on top. A unikernel compiles the app together with only the operating system pieces it needs, into one image that is the whole machine. Unikraft is the library OS that does this, and the README frames the result as lighter, faster, more secure and greener than containers and general-purpose VMs.

The workflow is deliberately familiar. Put a Kraftfile in a repo that points at an existing Dockerfile and a start command, then run `kraft run .`. kraft fetches the Unikraft components and libraries, configures and builds them for the target platform and architecture, and launches the result on a hypervisor. The local instance manager is described as daemonless.

The docs say the tool was modeled on popular package managers and build tools, so the unfamiliar part is the operating system model, not the commands. The docs recommend reading the concepts page first.

## Install

```
curl --proto '=https' --tlsv1.2 -sSf https://get.kraftkit.sh | sh
# or: brew install kraftkit
# Running unikernels needs a hypervisor: QEMU (4.2.0 to 9.2.1 per the compatibility table), Firecracker (1.4.1+), or Xen (4.19 or earlier). No account needed for local use.
```

## Try this

```
kraft -h
```
Prints the command tree, the version and the global flags.

```
kraft run unikraft.org/helloworld:latest
```
Pulls a pre-built Hello World unikernel from the catalog and boots it, which confirms the install works.

```
kraft run .
```
In a directory with a Kraftfile, builds the unikernel it describes and runs it.

## What's unique

Unikraft builds the library OS to match each app, and kraft wraps that in a Docker-like workflow. Existing Dockerfiles and Composefiles are reused, and a Go SDK and GitHub Action make it scriptable.

## Caveats

Unikernels are a different model from containers so existing Linux apps may need porting, Xen and Firecracker are Linux-only, and the homepage help output mixes in Unikraft Cloud commands that belong to a separate product.

## Links

- [Homepage: Unikraft CLI docs](https://unikraft.org/docs/cli)
- [GitHub repository (kraftkit)](https://github.com/unikraft/kraftkit)
- [Getting started guide](https://unikraft.org/docs/getting-started/)
- [App catalog](https://github.com/unikraft/catalog)
