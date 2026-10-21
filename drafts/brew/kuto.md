---
name: kuto
title: kuto
source: brew
category: take-things-apart
commitment: quick
tags: [bundler, code-splitting, esm, javascript, node, quick]
homepage: https://github.com/samthor/kuto
scout_score: 6
status: draft
---

# kuto

**TLDR;** Kuto splits a finished JavaScript bundle into a main file plus cached chunks, so returning visitors only download the code that changed.

Kuto takes a large ES module bundle and splits it into two parts: a small 'main' file and a 'corpus' directory of static chunks. It parses the input with acorn and works statement by statement, moving large statements that have no side-effects into the corpus. Those chunks never change once shipped, so browsers can cache them indefinitely, and Chromium can also cache the bytecode for files it has seen before.

The interesting part is what happens on the next build. Run Kuto again on a rebuilt bundle with the old output still in place, and it reuses existing corpus files where it can and deletes the ones no longer needed. The README puts the goal this way: "It reduces your download size by re-using code you've already shipped." The author's phrase for it is "Think of it as doing code-splitting 'last', rather than first."

The tool began as a way to learn about side-effects. The author wanted something that could report on them, and that became the `kuto info` command. The idea underneath is worth a look: deciding what is safe to move in a JavaScript file comes down to knowing which statements can run in any order without changing the program.

Note that this does not unpack minified apps back into readable source. It splits bundles rather than reversing them, and it works best on output from another bundler.

## Install

```
brew install kuto
# requires Node 16+; esbuild is optional and, if installed, lets split and info compile TS and similar files
```

## Try this

```
npx kuto
```
Prints usage information, which is the README's suggested first step for learning the tool.

```
kuto split yourbundle.js out/
```
Splits a JS bundle into a main file and a corpus of chunks written to out/.

```
kuto --help
```
Lists the available commands and flags.

## What's unique

Most code-splitting happens before bundling, by hand or by config. Kuto does it after the bundle exists, and reuses chunks from earlier deploys automatically.

## Caveats

It works best on large (over 1mb) single ESM bundles, gives little benefit on IIFE or webpack output, and needs the previous output kept around (or pointed to with -c) to reuse anything.

## Links

- [Homepage / GitHub repo](https://github.com/samthor/kuto)
- [Author's blog post on Kuto](https://samthor.au/2024/kuto/)
- [Theo.gg video about Kuto](https://www.youtube.com/watch?v=_sxwQBWJQHA)
