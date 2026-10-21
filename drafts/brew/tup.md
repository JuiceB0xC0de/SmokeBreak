---
name: tup
title: tup
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, build-system, dependency-graph, fuse, make-alternative]
homepage: https://gittup.org/tup/
scout_score: 5
status: draft
---

# tup

**TLDR;** A file-based build system whose dependency arrows point up instead of down, so rebuilds after a small edit stay fast even on large projects.

Tup is a build system by Mike Shal for Linux, macOS and Windows. Per its homepage, it takes a list of changed files and a directed acyclic graph of dependencies, then runs only the commands needed to bring dependent files up to date. You run `tup` from anywhere in the tree, with no need to cd into a subdirectory first.

The pitch is a faster edit/compile/test loop than make and its relatives. The homepage says tup's dependency arrows point up rather than down, and credits that with its speed. The details are in a paper it links, 'Build System Rules and Algorithms'. It also says tup cleans up old files automatically, handles renames, and warns you when a build description is not parallel-safe. The author's line: 'Your version control lets you rename a file. Does your build system?'

The idea underneath is worth a look: instead of a build tool that rescans everything to find what is stale, it starts from what changed and works outward. That is a different way to think about what a build is. The macOS install notes, which depend on FUSE, hint that tup watches how files are accessed while commands run, though the homepage never says so outright.

The homepage is informal and jokey, and the speed claims come with no benchmarks shown.

## Install

```
brew install tup
# Needs libfuse as a dependency. On macOS, tup needs a FUSE implementation (FUSE-T or macFUSE); see the caveats.
```

## Try this

```
man ./tup.1
```
Opens the man page shipped in the source tree, the quickest way to see how tup describes itself.

```
tup
```
Run from anywhere inside a tup-managed tree, it updates whatever is out of date. No subdirectory needed.

```
git clone git://github.com/gittup/tup.git
```
Fetches the source; run ./bootstrap.sh inside it to build tup from the git tree.

## What's unique

Dependency arrows point up rather than down, which the author ties to its speed. It also claims to handle file renames and to flag builds that are not parallel-safe.

## Caveats

On macOS tup needs a FUSE implementation, and the recommended FUSE-T route involves a manual patched-libfuse build, while macFUSE needs a kernel extension enabled.

## Links

- [Homepage](https://gittup.org/tup/)
- [GitHub repository](https://github.com/gittup/tup)
- [Build System Rules and Algorithms (PDF), linked from the homepage](https://gittup.org/tup/build_system_rules_and_algorithms.pdf)
