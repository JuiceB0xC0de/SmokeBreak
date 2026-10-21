---
name: gource
title: Gource
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [generative, git, quick, visual, visualisation]
homepage: https://gource.io/
scout_score: 6
status: draft
---

# Gource

**TLDR;** Gource replays a repository's commit history as an animated tree, with contributors drifting around it as they change files.

Gource reads the history of a version-controlled project and plays it back as a moving picture. The root directory sits at the centre, directories become branches, and files become leaves. Contributors appear at the moment they made a change and work on the part of the tree they touched. In the homepage's words: "Developers can be seen working on the tree at the times they contributed to the project."

It reads Git, Mercurial, Bazaar and SVN history directly. For CVS it can parse logs produced by third-party tools. Run plain `gource` inside a repository and it replays that repository's log in a window. The homepage also notes that the video output can be piped to ffmpeg, so a replay can become a file.

The idea underneath is that a commit log is a record of how people moved through a codebase over time, and a list hides that. Seen as a tree, you can watch a project grow, see which areas attract many hands, and notice when a quiet corner suddenly wakes up. The changelog mentions options such as `--start-date`, `--stop-date` and `--file-idle-time` for narrowing the date range and controlling how long files stay on screen.

The author also takes paid work for bespoke visualisation, and donations support the open-source project. The homepage points to Logstalgia, a related tool that does something similar for web-server logs.

## Install

```
brew install gource
# Needs a graphical desktop with OpenGL. No accounts or services needed.
```

## Try this

```
gource
```
Run inside a Git, Mercurial, Bazaar or SVN working directory, it opens a window and replays that repository's history as an animated tree.

```
gource --help
```
Lists the available options for date ranges, output and display.

## What's unique

Most version-control tools show history as text. Gource shows it as a growing tree with people moving around it, and it works from several version-control systems.

## Caveats

Maintained but slow-moving (latest release 0.56, March 2026), and Wayland support is described as experimental.

## Links

- [Gource homepage](https://gource.io/)
