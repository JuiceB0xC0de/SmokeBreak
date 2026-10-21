---
name: git-annex
title: git-annex
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, cli, distributed, git, haskell, storage]
homepage: https://git-annex.branchable.com/
scout_score: 6
status: draft
---

# git-annex

**TLDR;** git-annex lets git track huge files without storing their contents, and keeps a log of which drive holds which copy.

git-annex runs inside an ordinary git repository. When you add a file, it checksums the content, stores it under `.git/annex/objects`, and commits only a symlink to git. The repository stays small, and the large files live outside the history.

The central idea is location tracking. Each repository records which other repositories hold each file's content, so any clone can tell you where a file is, including which USB drive to plug in. There is no central server. Commands like `get`, `drop`, and `move` use that knowledge, and `drop` refuses to remove local content unless it can verify enough other copies exist. The `numcopies` setting sets how many copies count as safe.

Content can travel to other clones, ssh remotes, USB drives, or special remotes such as S3, optionally encrypted. The homepage describes it as built for 'git users who love the command line' and stresses that the repository format is plain git and files on disk, to keep it usable for the long term. It is written in Haskell, and the homepage also describes an optional assistant that works as a folder synchroniser.

## Install

```
brew install git-annex
# S3 and other special remotes need their own credentials, e.g. AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in the environment
# ssh remotes need full shell access or git-annex-shell on the remote host
```

## Try this

```
git init && git annex init "portable USB drive"
```
Turns a new git repository into an annex and gives it a description that other repositories will see.

```
git annex add .
```
Checksums the files in the current directory, moves their content into the annex, and stages symlinks for git.

```
git annex fsck
```
Verifies checksums and checks that the numcopies requirement is met; bad content is moved to .git/annex/bad/ instead of being deleted.

## What's unique

Every clone keeps a distributed record of where all copies of each file live, and refuses to drop content it cannot verify elsewhere. It does this using plain git and files on disk, with no central server.

## Caveats

The command set is large, special remotes and ssh setups need credentials or shell access, and the walkthrough page footer shows it was last edited in 2017, so parts of the docs may be dated.

## Links

- [git-annex homepage](https://git-annex.branchable.com/)
- [Walkthrough](https://git-annex.branchable.com/walkthrough/)
- [Install page](https://git-annex.branchable.com/install/)
