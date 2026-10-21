---
name: mergiraf
title: Mergiraf
source: brew
category: take-things-apart
commitment: quick
tags: [developer-tools, git, merge, parsing, quick, rust, syntax-trees]
homepage: https://mergiraf.org
scout_score: 5
status: draft
---

# Mergiraf

**TLDR;** A Git merge driver that parses code into syntax trees, so it can resolve conflicts that line-by-line merging gives up on.

Git merges by comparing lines of text. When two branches touch nearby lines, it stops and writes conflict markers, even if the changes are unrelated as far as the code is concerned. Mergiraf replaces that step with one that understands structure. It takes the base, left and right versions of a file, parses them with a language-specific grammar, and resolves conflicts using syntax-aware heuristics.

It works in stages. First it runs a normal line-based merge, and if that is conflict-free it returns the result immediately. Otherwise it parses the files and tries to reconcile both sides at the tree level. If a file cannot be parsed, it falls back to line-based merging. Where it judges a resolution suspicious, it leaves conflict markers behind. The project's own phrasing of that stance is "Don't sweep conflicts under the rug".

The underlying idea is that source code is a tree that happens to be stored as lines, and tools that respect the tree can answer questions that line diffs cannot. Mergiraf plugs into Git's own merge, rebase, cherry-pick and revert, so there is no separate step. You can also run it by hand on a conflicted file, or use it as a merge tool with Jujutsu. Its `review` command shows the work it did on a merge it resolved, which makes it a way to see how a tree-based merge reasons.

Languages are added declaratively. The homepage calls that the nonviolent option: "It's a nonviolent animal, so it prefers that over imperatives."

## Install

```
brew install mergiraf
# Then configure Git. The usage docs require diff3 conflict style for every workflow:
git config --global merge.conflictStyle diff3
git config --global merge.mergiraf.driver 'mergiraf merge --git %O %A %B -s %S -x %X -y %Y -p %P -l %L'
# Add this line to your global gitattributes file (narrower patterns like *.py also work):
# * merge=mergiraf
# The docs recommend Git v2.44.0 or newer.
```

## Try this

```
mergiraf languages --gitattributes
```
Prints the supported file extensions in gitattributes format, ready to paste into your config.

```
mergiraf solve config.yml
```
Runs Mergiraf by hand on a file left conflicted after a git merge stopped.

```
mergiraf review geolocation.cpp_o0i2JL8B
```
Shows the work Mergiraf did on a merge it resolved, using the merge id printed in Git's output.

## What's unique

It works on real syntax trees yet is built to prefer leaving conflict markers over guessing. It hooks into Git's normal merge, rebase, cherry-pick and revert flow.

## Caveats

Each language needs its own parser, so unsupported or unparseable files fall back to line-based merging, and zdiff3 conflict style breaks base reconstruction and should not be used.

## Links

- [Homepage](https://mergiraf.org)
- [Codeberg repository](https://codeberg.org/mergiraf/mergiraf)
- [Usage docs](https://mergiraf.org/usage.html)
- [Installation docs](https://mergiraf.org/installation.html)
