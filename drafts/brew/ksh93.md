---
name: ksh93
title: ksh93
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, language, shell, unix]
homepage: https://github.com/ksh93/ksh
scout_score: 6
status: draft
---

# ksh93

**TLDR;** A maintained fork of KornShell 93, the AT&T shell that shaped bash and POSIX sh, patched to be the least buggy ksh93 yet.

ksh93u+m is a Unix shell and scripting language. It runs interactive commands and scripts, with built-in utilities, arrays, arithmetic, job control and line editing. The Homebrew package installs `ksh`, `ksh93`, the restricted variants `rksh` and `rksh93`, and `shcomp`.

The project exists because of a failed rewrite. According to the README, an attempt to refactor ksh93 into ksh2020 (2017 to 2020) was abandoned with many critical bugs. This fork starts again from the last stable AT&T release, 93u+ of 2012-08-01. It backports the bug fixes documented in the old AST issue tracker and adds patches from OpenSUSE, Red Hat, Solaris and the community. Its stated aim: "the least buggy version of ksh93 ever released."

The idea underneath is that a shell is a language with its own history. Many features people use in bash and zsh trace back to ksh. Running the original, in a maintained form, shows where they came from and where the lineages diverged. The maintainers are also willing to break old behaviour: "No 100% bug compatibility. Broken and undocumented behaviour gets fixed."

The build is driven by a POSIX shell script, `bin/package`, and features are chosen at compile time by editing `src/cmd/ksh93/SHOPT.sh`. That makes the source tree worth a look in itself.

## Install

```
brew install ksh93
```

## Try this

```
ksh93 --help
```
Prints the shell's usage and option summary.

```
shcomp --help
```
Shows usage for the script compiler that ships alongside ksh.

```
rksh93 --help
```
Shows usage for the restricted variant of the shell.

## What's unique

It is a revival of the last stable AT&T ksh93, carrying fixes from an abandoned rewrite and from distro patch sets. Each pull request is squashed into one self-documenting commit.

## Caveats

The README calls the project active but gives no release or commit dates in what was fetched, and its build and test instructions assume compiling from source rather than the brew package.

## Links

- [Project homepage and README](https://github.com/ksh93/ksh)
- [NEWS (user-visible fixes)](https://github.com/ksh93/ksh/blame/dev/NEWS)
- [Issue tracker](https://github.com/ksh93/ksh/issues)
- [Original ksh93 site (AT&T)](http://www.kornshell.com/)
