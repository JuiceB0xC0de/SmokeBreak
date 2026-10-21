---
name: rakudo
title: Rakudo
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, language, perl, raku]
homepage: https://rakudo.org
scout_score: 6
status: draft
---

# Rakudo

**TLDR;** Rakudo is the main compiler for Raku, the language formerly known as Perl 6, with a name that means 'Way of the Camel'.

Rakudo compiles Raku source and runs it on one of three backends: MoarVM, the JVM, or JavaScript. Its homepage calls it "the most mature, production-ready implementation of the Raku language," and the README says it is currently the primary implementation. Each backend supports a somewhat different feature set.

The Homebrew install gives you `raku` and `rakudo`, plus the older `perl6` name, which is a reminder of the language's history. It also installs a family of debug wrappers: `-debug`, `-gdb-m`, `-lldb-m` and `-valgrind-m` variants. A language compiler that ships its own gdb, lldb and valgrind launchers is unusual, and it makes the runtime itself easy to poke at.

The name is Japanese: Rakuda-do (駱駝道), 'Way of the Camel', with a pun on rakudo (楽土), 'paradise'. The project's own motto is "Programming should be `-Ofun`."

The repository holds only the compiler, with no modules or documentation. For a fuller distribution, the README points to Rakudo Star. Rakudo itself is written in NQP and built on MoarVM, which are the two dependencies Homebrew pulls in.

## Install

```
brew install rakudo
```

## Try this

```
raku --help
```
Lists the command-line options of the Raku compiler.

```
rakudo --help
```
Shows the same compiler under its implementation name, so you can see the aliases are the same program.

```
zef install Linenoise
```
Installs the Linenoise module, which the README recommends for history and tab completion in the interactive rakudo executable. Needs the zef module installer, which the brief does not say is bundled.

## What's unique

It is a language compiler that ships gdb, lldb and valgrind launchers for each backend, and a single prefix can hold several backends side by side.

## Caveats

Only the bare compiler is included, so modules and docs need Rakudo Star or zef, and each backend supports a different feature set.

## Links

- [Rakudo homepage](https://rakudo.org)
- [Rakudo GitHub repository and README](https://github.com/rakudo/rakudo)
- [Rakudo Star distribution downloads](http://rakudo.org/downloads/star)
