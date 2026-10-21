---
name: uni
title: uni
source: brew
category: fundamentals
commitment: quick
tags: [cli, emoji, quick, text, unicode]
homepage: https://github.com/arp242/uni
scout_score: 6
status: draft
---

# uni

**TLDR;** A command-line Unicode database: look up any character by name, codepoint, category or emoji keyword and see its bytes, entity and name.

uni queries the Unicode database from the terminal. Give it text, codepoints, name words, categories, blocks, ranges or emoji keywords, and it prints a table of matching characters with codepoint, UTF-8 bytes, HTML entity and name. It has four main commands: identify (what is in this string, like a Unicode-aware hexdump), search (find codepoints by name), print (list codepoints by category, block or range) and emoji. Output can be a table, JSON, or a custom `-format` template.

The author calls the emoji command "the real reason I wrote this". It matches CLDR keywords as well as names, which matters: searching `smile` by name finds one emoji, while the keyword data finds many more. You can narrow by group, skin tone and gender variants.

The idea underneath is that text is not what it looks like. A string is a list of codepoints, which become bytes, and each codepoint belongs to a category and a block. Looking at a few strings through `identify` is a quick way to see how invisible characters, lookalikes and combining marks work. uni reads its own copy of the Unicode data rather than the Go standard library's, because that one is Unicode 13 and fails on newer codepoints.

## Install

```
brew install uni
```

## Try this

```
uni identify €
```
Prints the codepoint, decimal value, UTF-8 bytes, HTML entity and name of the euro sign.

```
uni s globe earth
```
Searches character names for codepoints containing both words.

```
uni e g:cat-face grin
```
Searches emoji by keyword within the cat-face group.

## What's unique

The emoji search uses CLDR keywords, groups, skin tones and gender variants, not just names. A WebAssembly build also lets you try it in a browser first.

## Caveats

The README still says Unicode 15.1, but the latest release notes say Unicode 18.0, so the README is out of date.

## Links

- [GitHub repository (homepage)](https://github.com/arp242/uni)
- [Run in the browser (WebAssembly build)](https://arp242.github.io/uni-wasm/)
- [Releases](https://github.com/arp242/uni/releases)
- [Packages (Repology)](https://repology.org/project/uni/versions)
