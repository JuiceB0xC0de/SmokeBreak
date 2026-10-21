---
name: logtalk
title: Logtalk
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, language, logic-programming, object-oriented, prolog]
homepage: https://logtalk.org/
scout_score: 6
status: draft
---

# Logtalk

**TLDR;** Logtalk adds objects, protocols, and hot-patchable components to Prolog by compiling down to the Prolog system you already have.

Logtalk is a declarative object-oriented logic programming language. It extends Prolog with prototypes, classes, protocols (interfaces), and categories, which are components that can be used to patch objects at runtime. It uses standard Prolog syntax plus a few added operators and directives, so the learning path is short if you already know Prolog.

It works as a transcompiler. You write Logtalk source, and it is compiled into code for a standards-compliant Prolog system, which the README says can be most modern ones. The Homebrew install ships a launcher for each supported backend, such as `swilgt`, `gplgt`, and `yaplgt`. The formula depends on GNU Prolog, so `gplgt` should work out of the box.

The README frames the goal as bringing Prolog up to 'programming in the large': code encapsulation and reuse, while keeping Prolog's declarative features. The homepage puts it as 'Logic Programming meets Software Engineering'. The idea underneath is that a logic language can have the structuring tools of mainstream OO languages without giving up its own way of computing.

The distribution also bundles libraries, a handbook, API docs, and many examples. There are developer tools too, including documentation generators (`lgt2html`, `lgt2md`, `lgt2pdf`, and others) and a test runner, `logtalk_tester`.

## Install

```
brew install logtalk
# Homebrew sets LOGTALKHOME=$HOMEBREW_PREFIX/share/logtalk and LOGTALKUSER=$HOME/logtalk
# Needs a Prolog backend; the formula pulls in gnu-prolog (use gplgt). Others, such as SWI-Prolog, are installed separately.
```

## Try this

```
gplgt --help
```
Shows the options for the GNU Prolog launcher, which starts Logtalk on the backend Homebrew installs for you.

```
swilgt --help
```
Shows the options for the SWI-Prolog launcher, if you have installed SWI-Prolog as a backend.

```
apropos logtalk
```
Lists the man pages for Logtalk's shell scripts, which is a quick way to see what the toolchain includes.

## What's unique

It is a layer over existing Prolog systems rather than a new Prolog, so you keep your backend and gain objects, protocols, and categories on top. The tool suite is unusually large for a niche language and works across backends.

## Caveats

It needs a Prolog backend, some features like high-level multi-threading work only on selected backends, and the community is small next to mainstream languages.

## Links

- [Homepage](https://logtalk.org/)
- [Logtalk Handbook (online HTML)](https://logtalk.org/docs/handbook/index.html)
- [Learn X in Y minutes: Logtalk](https://learnxinyminutes.com/docs/logtalk/)
