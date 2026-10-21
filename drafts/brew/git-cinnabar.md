---
name: git-cinnabar
title: git-cinnabar
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, git, mercurial, protocol, remote-helper, version-control]
homepage: https://github.com/glandium/git-cinnabar
scout_score: 6
status: draft
---

# git-cinnabar

**TLDR;** A git remote helper that clones and pushes to Mercurial repositories, translating between the two object models without a local Mercurial clone underneath.

git-cinnabar lets git talk to Mercurial. You run `git clone hg::<url>` where you would normally give a git URL, and the Mercurial repository arrives as ordinary git history. The target can be a local path or an http, https or ssh address. After that you use git as usual.

Underneath, it converts Mercurial changesets into git commits and keeps metadata that maps SHA-1s in both directions. Two commands expose that mapping: `git cinnabar hg2git` prints the git commit for a changeset, and `git cinnabar git2hg` does the reverse. The README sets it apart from other helpers: "Contrary to other such helpers ... it doesn't use a local mercurial clone under the hood." It speaks to the remote directly instead.

It exists mainly to make Mozilla's large Mercurial repositories, mozilla-central and its relatives, usable from git, including workflows like the try server. The idea underneath is that git and Mercurial are two different ways of naming and storing the same history, and a faithful translator has to decide what identity means in each. Hashes cannot match, so the tool carries a durable map between them.

## Install

```
brew install git-cinnabar
# depends on mercurial, which brew installs for you. If another git-remote-hg is already on PATH, make sure the git-cinnabar directory comes first.
```

## Try this

```
git clone hg::<mercurial repo>
```
Clones a Mercurial repository (local path, http, https or ssh) into a normal git repository.

```
git cinnabar hg2git <changeset>
```
Prints the git commit that corresponds to a Mercurial changeset. Abbreviated SHA-1s work if unambiguous.

```
git cinnabar git2hg <commit>
```
Prints the Mercurial changeset that corresponds to a git commit.

## What's unique

It talks to the Mercurial remote directly and keeps its own bidirectional SHA-1 map, rather than wrapping a hidden local Mercurial clone. Its hg:// URLs even put the transport in the port field, such as hg://host:ssh/path, so they survive the msys shell.

## Caveats

The README calls it "still in early infancy" with metadata that "might get corrupted"; push is limited to non-merge commits by default, and obsolescence markers, phases and namespaces are unsupported.

## Links

- [GitHub repository and README](https://github.com/glandium/git-cinnabar)
- [Wiki: Mozilla git workflow for Gecko development](https://github.com/glandium/git-cinnabar/wiki/Mozilla:-A-git-workflow-for-Gecko-development)
