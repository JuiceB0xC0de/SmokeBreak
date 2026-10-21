---
name: peekaboo
title: Peekaboo
source: brew
category: take-things-apart
commitment: afternoon
tags: [accessibility, afternoon, automation, gui, macos, mcp]
homepage: https://peekaboo.sh/
scout_score: 5
status: draft
---

# Peekaboo

**TLDR;** A macOS command-line tool that reads any app's accessibility tree as a list of clickable element IDs, then clicks and types against them.

Peekaboo captures a screen, window, or app and returns two things: an image, and a structured map of the interface. The `see` command walks the accessibility tree and lists each element with an ID, role, label, frame, and available actions. Other commands, such as `click`, `type`, and `press`, then act on those elements by name or ID.

The idea underneath is that macOS apps already describe themselves to assistive technology. Buttons, text fields, and menus are exposed as a tree of objects, which is how screen readers work. Peekaboo treats that tree as an API for any app, so automation does not have to guess at pixels. The docs say to prefer a semantic action such as `menu click` when one exists.

Targeted input can be pinned to one window by ID and, by default, is delivered in the background, so the app does not need to be frontmost. The project describes itself as a toolkit "for humans and agents". It also includes a natural-language `agent` command and an MCP server that exposes the same tools to clients such as Codex, Claude Code, and Cursor.

Even if you never automate anything, `see --json` on an app you use every day is a quick way to see how its interface looks from the accessibility side.

## Install

```
brew install openclaw/tap/peekaboo
# Requires macOS 15 or later. Grant Screen Recording and Accessibility permissions, then verify with: peekaboo permissions status
# The agent command needs a configured model provider; settings live under ~/.peekaboo.
```

## Try this

```
peekaboo permissions status
```
Shows which macOS permissions Peekaboo has; re-run until Screen Recording and Accessibility show as granted.

```
peekaboo see --app Finder --json
```
Prints a structured map of Finder's UI with element IDs, roles, labels, and actions.

```
peekaboo see --no-elements --mode screen --path /tmp/peekaboo-screen.png
```
Takes a whole-screen screenshot and writes it as a PNG to /tmp.

## What's unique

It is built around the accessibility tree instead of screenshot guessing, so later commands act on element IDs. The same tool set is reachable from the shell, a built-in agent, and MCP clients.

## Caveats

macOS 15 or later only; it needs Screen Recording and Accessibility grants, some actions need extra permissions, and the docs flag drag, scroll, and key chords as having caveats.

## Links

- [Peekaboo documentation (homepage)](https://peekaboo.sh/)
- [Quickstart](https://peekaboo.sh/quickstart)
- [GitHub repository](https://github.com/openclaw/Peekaboo)
- [Latest release](https://github.com/openclaw/Peekaboo/releases/latest)
