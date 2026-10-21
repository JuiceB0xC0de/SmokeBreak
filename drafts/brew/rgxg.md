---
name: rgxg
title: rgxg
source: brew
category: languages-and-oddities
commitment: quick
tags: [c-library, cidr, generator, quick, regex]
homepage: https://rgxg.github.io
scout_score: 5
status: draft
---

# rgxg

**TLDR;** Writes the regular expression for you: give it a numeric range or a CIDR block and it prints a pattern matching exactly that set.

rgxg (ReGular eXpression Generator) is a C library with a small command-line front end. Instead of matching text against a pattern, it goes the other way. You describe a set, such as a number range like 0 to 31 or 00 to FF, or a network block like 192.168.0.0/24 or 2001:db8:aaaa::/64, and it produces an (extended) regular expression that matches exactly that set.

The reason is plain: these patterns are tedious and error-prone to write by hand. A regex for "0 to 31" or "any address in this /24" has to spell out digit-by-digit alternatives, and one slip lets bad input through. Generating the pattern from the specification turns a fiddly puzzle into a lookup.

The idea underneath is that a regular expression is just a compact description of a finite set, and for sets with structure, such as ranges and prefixes, a program can derive that description mechanically. It is a small door into how regexes encode numbers and addresses. Because it is also a library, other C programs can call it directly rather than shelling out.

The README does not document the input syntax or show sample output, so expect to learn it from the tool's own help.

## Install

```
brew install rgxg
```

## Try this

```
rgxg --help
```
Lists the available commands and options, since the README does not document the input syntax.

## What's unique

Most regex tools go from pattern to matches. rgxg runs the other way, writing a pattern from a numeric range or network block, and it ships as a C library as well as a shell tool.

## Caveats

The last stable release, 0.1.2, is from April 2020, and the README does not document input syntax, output format, or the library API.

## Links

- [Homepage](https://rgxg.github.io)
- [GitHub repository and README](https://github.com/rgxg/rgxg)
- [Issue tracker](https://github.com/rgxg/rgxg/issues)
