---
name: scriptisto
title: scriptisto
source: brew
category: languages-and-oddities
commitment: quick
tags: [cli, compiled-languages, quick, scripting, shebang]
homepage: https://github.com/igor-petruk/scriptisto
scout_score: 5
status: draft
---

# scriptisto

**TLDR;** A shebang interpreter that lets you run single-file scripts in compiled languages like C, Rust, Go or COBOL, building and caching the binary on first run.

Scriptisto turns a source file into something you can execute directly. You put `#!/usr/bin/env scriptisto` on the first line, then add a comment block between `scriptisto-begin` and `scriptisto-end` markers that holds the build instructions, such as the source file name and the compile command. Run the file and scriptisto builds it, caches the result, and runs the binary.

The README describes the goal as writing one-file scripts in languages that need compilation, dependency fetching or preprocessing, which would otherwise need a separate build setup. Later runs skip the build. If the script has not changed, scriptisto hands off to the cached binary, and the README claims under 1 ms of overhead. Builds can also run inside Docker, so the host does not need the compiler installed.

The idea underneath is that a shebang is just a convention: the kernel runs whatever program the first line names and passes it the file. Nothing says that program has to be an interpreter. Scriptisto uses that to put a compile-and-cache step in front of the run, which is a good way to see what an interpreter actually does. It ships templates for languages including Rust, Go, C, Fortran, COBOL and C#.

## Install

```
brew install scriptisto
# Toolchains are only needed for the languages you use. The C demo needs clang, GLib and pkg-config. Docker is only needed if you choose Docker builds.
```

## Try this

```
scriptisto --help
```
Lists the subcommands, including the ones for working with language templates.

```
chmod +x ./script.c
```
Marks the README's C demo file as executable so the shebang line can take effect.

```
./script.c
```
The first run compiles the C file with the command in its comment block, then prints 'Hello, C! Current user: username'. Later runs reuse the cached binary.

## What's unique

Build instructions live inside the script as comments, and the compiled result is cached, so a compiled-language file behaves like a plain script. Templates cover unusual languages such as COBOL and Fortran.

## Caveats

The README's C demo is slightly confusing about file names (script.c versus the ./script output), the first build of heavier templates like Rust can take a while with no output because build logs are suppressed by default, and the C demo needs clang, GLib and pkg-config.

## Links

- [Homepage / README (GitHub)](https://github.com/igor-petruk/scriptisto)
- [Releases](https://github.com/igor-petruk/scriptisto/releases)
- [Crates.io](https://crates.io/crates/scriptisto)
- [Wiki](https://github.com/igor-petruk/scriptisto/wiki)
