---
name: git-bug
title: git-bug
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, bug-tracker, git, go, offline-first, tui]
homepage: https://github.com/git-bug/git-bug
scout_score: 6
status: draft
---

# git-bug

**TLDR;** A bug tracker that lives inside your git repository as git objects, syncs through normal remotes, and works fully offline.

git-bug stores issues and identities as git objects in the repository itself. No server, no database, and no files added to your working tree. You create an identity, add bugs from the command line, and share them with `git bug push` and `git bug pull` against the same remotes you already use for code.

The idea underneath is that git is already a distributed, content-addressed store with built-in replication, and it can hold more than source files. The README says the on-disk format is a DAG of entities, specified in a separate spec repository. Each bug is a history of operations rather than a mutable row, which is how it can merge between clones without a central service.

The pitch is practical as well as odd. The README says it prevents vendor lock-in: 'your usual service is down or went bad? You already have a full backup.' Bridges import and export bugs with GitHub, GitLab, Jira and Launchpad, so the local copy can mirror a hosted tracker. You can browse bugs in a terminal UI (`git bug termui`) or a web UI served from the same Go binary by a local HTTP server, backed by a GraphQL API.

## Install

```
brew install git-bug
# Bridges need an account login and an access token for the target service. The README points to INSTALLATION.md for building from source.
```

## Try this

```
git bug user create
```
Creates your identity, which the README lists as the first step.

```
git bug add
```
Opens your editor to write a title and message, then stores a new bug in the repo.

```
git bug ls "status:open sort:edit"
```
Lists open bugs sorted by last edit using the query language.

## What's unique

Most trackers keep issues on a server. This one keeps them as git objects in your repo, and bridges let the same local data sync with GitHub, GitLab, Jira or Launchpad.

## Caveats

The README calls the web UI workflow 'WIP', bridge support varies by tracker, and I could not confirm the latest release date from the README.

## Links

- [Homepage / GitHub repo](https://github.com/git-bug/git-bug)
- [Installation guide](https://github.com/git-bug/git-bug/blob/trunk/INSTALLATION.md)
- [Feature matrix](https://github.com/git-bug/git-bug/blob/trunk/doc/feature-matrix.md)
- [On-disk format spec](https://github.com/git-bug/spec)
