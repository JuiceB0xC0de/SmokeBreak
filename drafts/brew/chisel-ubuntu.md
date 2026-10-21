---
name: chisel-ubuntu
title: Chisel
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, containers, debian, go, packaging, ubuntu]
homepage: https://github.com/canonical/chisel
scout_score: 6
status: draft
---

# Chisel

**TLDR;** Chisel carves Ubuntu's Debian packages into small slices, so you can build a root filesystem with only the files you need.

Chisel is a Go command-line tool from Canonical. You name an Ubuntu release and a list of slices, such as `libgcc-s1_libs` or `libssl3_libs`. It fetches the matching packages from the Ubuntu archive and extracts only those slices into a target directory. What you get is a trimmed filesystem tree, meant as the base for a smaller container image.

The idea underneath is that a package is too coarse a unit. Package A may ship files that nobody depending on it ever uses. In the README's words, "Slices are basically subsets of the Debian packages, with their own content and set of dependencies to other internal and external slices." Chisel treats a package as a block of stone to carve rather than something you install whole.

Slice definitions are YAML files kept in a separate repository, chisel-releases, with one file per package per release. Each slice lists paths and can name dependencies on other slices. Paths can also be made, copied, symlinked or generated as text. Starlark mutation scripts can reproduce what a maintainer script would have done. Packages are fetched with GPG signature checking. Reading those definitions is a good way to see how a package's files are really divided up.

## Install

```
go install github.com/canonical/chisel/cmd/chisel@latest
# The README gives only this install route and does not mention brew. It needs a Go toolchain and network access to the Ubuntu archives.
```

## Try this

```
chisel help --all
```
Prints a short description of every command.

```
chisel cut --release ubuntu-22.04 --root myrootfs/ libgcc-s1_libs libssl3_libs
```
Fetches those slices from the Ubuntu 22.04 archives and installs only them into myrootfs/, which you can then inspect.

```
chisel help cut
```
Shows the details of the cut command, including how to point --release at a local directory of slice definitions.

## What's unique

Slice definitions live in a separate data repository and can include Starlark scripts that stand in for maintainer scripts. That makes packages cuttable at the file level.

## Caveats

Ubuntu only, with no support yet for non-Ubuntu or multiple repositories, file ownership is not preserved, and the brief could not confirm recent project activity.

## Links

- [GitHub repository (homepage, README)](https://github.com/canonical/chisel)
- [Chisel documentation](https://ubuntu.com/chisel/docs/latest/)
- [chisel-releases (slice definitions database)](https://github.com/canonical/chisel-releases)
