---
name: rura
title: rura
source: brew
category: take-things-apart
commitment: quick
tags: [debugging, pipelines, quick, shell, tui]
homepage: https://github.com/tlipinski/rura
scout_score: 6
status: draft
---

# rura

**TLDR;** A terminal scratchpad where you type a shell pipeline and watch its output update live, stage by stage, instead of editing and rerunning.

Rura is a terminal UI for building shell pipelines. You type something like `grep | sort | uniq` into an input line, and the output pane updates as you edit. Data can come from a file, from piped stdin, or from an initial command. You can run the whole pipeline or only part of it, inspect what a single stage produced, diff outputs between runs, and save commands as presets.

The README describes it as replacing the usual edit, up-arrow, rerun loop. Anyone who has built a long pipe by appending one `| awk ...` at a time and rerunning it knows that loop. Rura keeps the pipeline in one editable place and shows the result as you go.

The interesting idea is that a pipeline is a chain of stages, and you can stop the chain anywhere. The Alt+\ binding runs the pipe only up to the subcommand under the cursor, so you can see what the data looked like halfway through. A diff base can be set to any subcommand's output, so you can compare what one stage produced before and after an edit. The README says Rura caches subcommand output to keep this fast.

Commands run through a configurable shell: sh by default on Unix, powershell on Windows. Live modes re-execute the pipeline as you type, with a debounce delay that defaults to 500 ms. Tab completion borrows from your system's bash, zsh, or fish.

## Install

```
brew install rura
# Other routes from the README: cargo install rura, yay -S rura-bin (Arch), .deb/.rpm packages from GitHub Releases, nix-shell -p rura. No account or hardware needed.
```

## Try this

```
rura --file data.json
```
Opens the file as input data so you can build a pipeline against it and watch the output change as you type.

```
cat logs.txt | rura
```
Takes piped stdin as the input and lets you shape it interactively.

```
rura --command "grep error | sort"
```
Starts with that pipeline already in the input line, ready to edit and run.

## What's unique

Live partial-pipeline execution is the hook: run only up to the cursor's subcommand, and diff any stage's output across edits. Output caching and a 'Live Until Cursor' mode are less common in pipeline tools.

## Caveats

The brief could not confirm release dates or recent activity, and on Linux the Ctrl+q clipboard copy may be lost on exit unless a clipboard manager is running.

## Links

- [GitHub homepage and README](https://github.com/tlipinski/rura)
- [Releases (pre-compiled binaries)](https://github.com/tlipinski/rura/releases)
