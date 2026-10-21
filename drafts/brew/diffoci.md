---
name: diffoci
title: diffoci
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, containers, diff, docker, oci, reproducible-builds]
homepage: https://github.com/reproducible-containers/diffoci
scout_score: 5
status: draft
---

# diffoci

**TLDR;** A diff tool for Docker and OCI container images that compares them layer by layer, built to check whether a rebuilt image matches the official one.

diffoci takes two image references and reports where they differ. References can be registry names like `alpine:3.18.2`, local Docker images via `docker://`, Podman images via `podman://`, or images in the containerd store. The output is a table of differing entries, each with a type, a name, and a digest or message for each input.

It exists to help with reproducible builds. You build an image from published source, then check whether your result matches the official binary image. In the README's words: "If the published source is trustable, this image binary can be trusted too."

The default strict mode compares everything, and the README admits it is "often too strict." The `--semantic` mode ignores timestamps, build history, file ordering inside tar layers, and image name annotations. What remains is the real difference. diffoci does not know the file formats inside layers, so a timestamp inside a nested tar such as Alpine's `scripts.tar` still shows up.

The README works through a case study: it diffs the official `golang:1.21-alpine3.18` image against a locally rebuilt copy and explains each leftover difference. Reading it shows how an image is really a stack of tar layers with whiteout entries and digests. With `--report-dir`, the conflicting files are written out so you can inspect them with `diff -ur` or diffoscope.

## Install

```
brew install diffoci
# No account needed for public images. Private registry images need ~/.docker/config.json from `docker login`. docker:// images need a running Docker, and platform filtering needs Docker v28+.
```

## Try this

```
diffoci diff --semantic alpine:3.18.2 alpine:3.18.3
```
Pulls two Alpine tags and prints a table of the files that differ between them, ignoring timestamp and ordering noise.

```
diffoci diff --semantic --report-dir=/tmp/diff alpine:3.18.2 alpine:3.18.3
```
Runs the same diff and also writes the conflicting files to /tmp/diff so you can compare them with diff -ur.

```
diffoci diff --platform=linux/amd64 IMAGE0 IMAGE1
```
Pins the comparison to one platform, which helps on non-Linux machines or with multi-platform images.

## What's unique

It compares images at the layer and tar-entry level, with a semantic mode that strips the noise reproducible-build work runs into. Its README doubles as a worked example of explaining every leftover difference.

## Caveats

Strict mode is usually too noisy, so you will want `--semantic`, and even that does not filter format-specific noise inside layer files like timestamps in Alpine's scripts.tar.

## Links

- [GitHub repository (homepage)](https://github.com/reproducible-containers/diffoci)
- [Releases and prebuilt binaries](https://github.com/reproducible-containers/diffoci/releases)
- [diffoscope (used in README for file-level diffs)](https://diffoscope.org/)
