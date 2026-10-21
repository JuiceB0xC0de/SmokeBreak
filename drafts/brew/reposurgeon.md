---
name: reposurgeon
title: reposurgeon
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cli, conversion, git, history, version-control]
homepage: http://www.catb.org/esr/reposurgeon/
scout_score: 7
status: draft
---

# reposurgeon

**TLDR;** A debugger-style tool that reads a repository's history, lets you rewrite it, and writes it back out, including into a different version-control system.

reposurgeon reads a repository's history into memory and lets you operate on it: edit old commit comments and metadata, remove or merge commits, delete files or whole subtrees from the past. It then writes the result out to another VCS or back to the same one. You drive it from an interactive prompt or from scripts.

The author's pitch is that it enables "risky operations that version-control systems don't want to let you do, such as editing past comments and metadata and removing commits." The man page describes a main use as helping a human produce higher-quality conversions between VCSes than fully automated converters manage. The homepage singles out scripted conversion from Subversion to any VCS with write support.

The idea underneath is git's fast-import stream. Instead of writing a reader and a writer for every pair of systems, reposurgeon parses and emits that stream, so anything with fast-export and fast-import tools can be handled. For systems without them, built-in extractor code replays history into an internal stream. Repositories read that way can be read but not modified. The stream format also gives the tool a common vocabulary of primitive operations.

The interface "resembles a symbolic debugger", and the package ships four helpers beside the main program: repocutter, repomapper, repotool and repobench.

## Install

```
brew install reposurgeon
# If a conversion needs a source VCS, its helper tools (for example fast-export equivalents) must be installed too. reposurgeon names any it is missing.
```

## Try this

```
reposurgeon --help
```
Prints usage for the main program so you can see the entry point before opening the prompt.

```
reposurgeon
```
Starts the interactive, debugger-like prompt where you read in a repository and issue editing commands.

```
repotool --help
```
Shows the helper that handles repository chores around a conversion.

## What's unique

It treats history as a specimen to be dissected, using a debugger-style prompt and git fast-import streams as a universal intermediate format. That lets one tool edit history across many VCSes.

## Caveats

Support is uneven: full read and write works for git, hg, bzr, brz, Fossil, darcs, RCS and SRC, while SCCS, CVS, svn and Software Heritage are read-only, and CVS conversions can need serious hand-hacking.

## Links

- [Homepage](http://www.catb.org/esr/reposurgeon/)
- [Manual page](http://www.catb.org/esr/reposurgeon/reposurgeon.html)
- [Repository Editing and Conversion With Reposurgeon](http://www.catb.org/esr/reposurgeon/repository-editing.html)
- [Source repository (GitLab)](https://gitlab.com/esr/reposurgeon)
