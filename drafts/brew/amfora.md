---
name: amfora
title: Amfora
source: brew
category: languages-and-oddities
commitment: quick
tags: [browser, gemini, go, protocol, quick, tui]
homepage: https://github.com/makew0rld/amfora
scout_score: 5
status: draft
---

# Amfora

**TLDR;** A terminal browser for Gemini, a small text-first protocol that sits beside the Web, with tabs, bookmarks, feeds and certificate handling.

Amfora fetches gemini:// addresses and draws the pages in your terminal, with styled headings, links, tabs, bookmarks and history. It also handles Gemini's input prompts, client certificates, and trust-on-first-use (TOFU) certificate checks. Pages can be downloaded, and non-text files can be handed to other applications.

Gemini is a separate internet protocol from the Web, not a layer on top of HTTP. The idea underneath Amfora is that a protocol kept deliberately small makes a complete client feasible for one person to build and polish. The README states the aim plainly: "Amfora aims to be the best looking Gemini client with the most features... all in the terminal." It claims to fully pass Sean Conman's client torture test and the Egsam one.

It is written in Go, using cview (a fork of tview) over tcell for the interface, and the author's fork of go-gemini for the protocol. It supports RSS, Atom and JSON Feed, and you can subscribe to a page and be notified when it changes. It is Gemini only; the README points to Bombadillo for Gopher and other protocols.

The project is in maintenance mode. The author links a 2023 blog post explaining why. A client for a small protocol does not need constant change, so that is not necessarily a problem.

## Install

```
brew install amfora
```

## Try this

```
amfora
```
Opens the browser in your terminal so you can type a gemini:// address and start following links.

```
amfora -v
```
Prints the installed version; for a source build, the exact commit it was built from.

```
amfora --help
```
Lists the command-line options.

## What's unique

It aims to be the most polished Gemini client in a terminal, with tabs, theming and feed subscriptions, rather than a bare-bones viewer.

## Caveats

It is in maintenance mode, so expect bug fixes but few new features, and on Windows some colours may not display correctly.

## Links

- [GitHub repository (homepage)](https://github.com/makew0rld/amfora)
- [Project wiki (usage and configuration)](https://github.com/makeworld-the-better-one/amfora/wiki)
- [Releases](https://github.com/makeworld-the-better-one/amfora/releases)
- [Author's blog post on maintenance mode](https://www.makeworld.space/2023/08/bye_gemini.html)
