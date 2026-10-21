---
name: difftastic
title: difftastic
source: brew
category: take-things-apart
commitment: quick
tags: [cli, diff, parsing, quick, syntax, tree-sitter]
homepage: https://difftastic.wilfred.me.uk/
scout_score: 5
status: draft
---

# difftastic

**TLDR;** A diff tool that parses code into syntax trees and shows what actually changed, so reformatting and wrapping stop looking like rewrites.

Difftastic installs one executable, `difft`. Give it two files and it parses each with tree-sitter into a syntax tree, then compares the trees instead of the lines. It handles over 30 programming languages plus formats like HCL, HTML, JSON and YAML. Unrecognised extensions fall back to a line-oriented diff with word highlighting.

The problem it targets is that line diffs mislead. A reformatter that splits an expression across several lines, or a wrapper added around an existing expression, produces a noisy diff that hides the real change. In the README's words: "Difftastic is not line-oriented. If you reformat your code and it's now split over multiple lines, difftastic will show you what's actually changed."

The idea underneath is that comparing two trees can be treated as a graph problem. The comparison becomes a shortest-path search, solved with Dijkstra's algorithm, over the possible ways to turn one tree into the other. The author's blog post and the manual's internals section describe the design.

One design choice stands out. When it hits parse errors, it falls back to a line diff by default, to avoid claiming two syntactically different files are the same. You can loosen that with the `DFT_PARSE_ERROR_LIMIT` environment variable. It can also take a single file containing git merge conflict markers, rebuild the two sides and diff those.

## Install

```
brew install difftastic
```

## Try this

```
difft foo1.c foo2.c
```
Diffs two C files structurally and prints the changes with real line numbers from both files.

```
difft --check-only --exit-code before.js after.js
```
Checks whether the two files have the same syntax tree without printing a diff. Exit code 0 means no syntactic changes, 1 means changes were found.

```
difft file_with_conflicts.js
```
Takes one file containing merge conflict markers, builds the two conflicting versions and diffs them (needs version 0.50 or later).

## What's unique

It treats diffing as a shortest-path search over syntax trees, and it prefers a plain line diff to the risk of calling different files equal after a parse error. It can also diff conflict-marked files directly.

## Caveats

The README says it scales poorly on files with many changes and can use a lot of memory, it is order-sensitive so set(1, 2) and set(2, 1) show as changed, and it is not a patch generator or a merge tool.

## Links

- [Homepage](https://difftastic.wilfred.me.uk/)
- [Manual](https://difftastic.wilfred.me.uk/introduction.html)
- [GitHub repository](https://github.com/Wilfred/difftastic)
- [Author's design blog post](https://www.wilfred.me.uk/blog/2022/09/06/difftastic-the-fantastic-diff/)
