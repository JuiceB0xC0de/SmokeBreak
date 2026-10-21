---
name: regldg
title: regldg
source: brew
category: languages-and-oddities
commitment: quick
tags: [grammar, language, quick, regex, wordlist]
homepage: https://regldg.com/
scout_score: 6
status: draft
---

# regldg

**TLDR;** Runs regular expressions backwards: give it a pattern and it prints every string that matches, turning a regex into a word list.

Most people use a regex to ask whether a string matches. regldg flips that. You hand it a pattern and it enumerates every string the pattern describes. The homepage puts it plainly: "In regldg, you give it a pattern, and it will create all the strings of text which match it."

The author wrote it to build a password list. He knew a password started with "omu" and was 7 characters long, and he had only a very old computer. A pattern that fixes the prefix and the length gives a small, finite list to try. That origin explains why it is a dictionary generator and not a general string toy.

The idea underneath is that a regex defines a grammar, and the words matching it are that grammar's language. Normally you only ever test membership in that language. Here you walk the whole thing. It is a quick way to feel how pattern size turns into output size, and why a pattern like a* is awkward: the language is infinite, and the author deliberately left such cases unimplemented.

It supports a subset of Perl's regex syntax, with deliberate changes to avoid ambiguity. Character codes are written as \o40, \x20, or \z32, so that \1 is always a backreference. The homepage says uniqueness in the output is not guaranteed, so duplicates can appear, for example from a{2,3}a{3,2}.

## Install

```
brew install regldg
```

## Try this

```
regldg --help
```
Prints the program's usage text, so you can see how it takes a pattern.

```
man perlrequick
```
Opens Perl's quick regex tutorial, which the homepage suggests for learning the pattern syntax regldg accepts a subset of.

## What's unique

It inverts the usual regex direction, enumerating every string a pattern matches instead of testing one. The author also changed some Perl syntax on purpose to remove ambiguity.

## Caveats

The homepage gives no release date or repository, so maintenance is unknown, and it lacks Perl's named character classes, non-capturing groups, and zero-width assertions.

## Links

- [regldg homepage](https://regldg.com/)
