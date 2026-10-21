---
name: moreutils
title: moreutils
source: brew
category: languages-and-oddities
commitment: quick
tags: [cli, pipelines, quick, shell, unix]
homepage: https://joeyh.name/code/moreutils/
scout_score: 6
status: draft
---

# moreutils

**TLDR;** Fifteen small Unix tools that fill gaps in the shell, like sponge, ts and vidir, which you will want in your pipelines once you know they exist.

moreutils is a set of small command-line programs, each doing one narrow job in a pipeline. `sponge` soaks up all of stdin before writing anything, `ts` timestamps each line, `vidir` opens a directory listing in your editor so you can rename files by editing text, and `vipe` lets you edit data in the middle of a pipe. The rest are `chronic`, `combine`, `errno`, `ifdata`, `ifne`, `isutf8`, `lckdo`, `mispipe`, `parallel`, `pee` and `zrun`. They install as separate executables, so they slot into existing shell habits.

The author's view is that the most basic tools fall through the cracks and go unnoticed by the people who could use them. In the project's words: "moreutils is a collection of the unix tools that nobody thought to write long ago when unix was young." The collection exists "to stop these programs from falling through the cracks."

`sponge` is the page's own example, and it calls it probably the most general-purpose tool in the set. A normal shell pipeline that reads and writes the same file will truncate it before the reader finishes. Because `sponge` reads everything first, you can rewrite a file in place at the end of the pipeline. Seeing why that works is a small lesson in how pipes and redirection actually behave.

The project page also keeps a visible list of rejected and under-consideration tools, with reasons. It is a small, opinionated piece of curation, and reading it shows what the author thinks does and does not belong in a shell toolbox.

## Install

```
brew install moreutils
```

## Try this

```
sed "s/root/toor/" /etc/passwd | grep -v joey | sponge /etc/passwd
```
The page's own sponge example: sponge reads all of stdin before writing, so the pipeline can safely rewrite /etc/passwd in place. Try it on a copy of a file, not the real one.

```
sponge --help
```
Shows the usage for the collection's most general-purpose tool.

```
vidir --help
```
Shows how to use vidir, which opens a directory listing in your editor so renaming files becomes text editing.

## What's unique

It is less a single clever tool than a deliberate curation project, with a public list of tools that were rejected or are still under consideration, and the reasons why.

## Caveats

The page says the collection is closed to new tool suggestions and asks for a new maintainer; it shows no dates, so how recently it was updated is unclear.

## Links

- [moreutils homepage](https://joeyh.name/code/moreutils/)
- [git repository (clone address from the page)](git://git.joeyh.name/moreutils)
