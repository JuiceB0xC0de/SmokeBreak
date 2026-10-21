---
name: metashell
title: Metashell
source: brew
category: languages-and-oddities
commitment: quick
tags: [clang, cpp, metaprogramming, quick, repl, templates]
homepage: http://metashell.org
scout_score: 6
status: draft
---

# Metashell

**TLDR;** An interactive shell for C++ template metaprogramming: type compile-time code at a prompt and see what Clang makes of it, no source file needed.

C++ templates can compute things at compile time. They are a language inside the language, and a famously awkward one. The usual way to see what a template metaprogram produces is to write a source file and coax the compiler into printing the answer, often through a deliberate error message. Metashell replaces that ritual with a prompt.

It works in the spirit of the Python, Haskell (ghci) and Erlang shells. You type a metaprogram, and it evaluates it using Clang. The project's own words: "Metashell provides an interactive shell similar to the Python, Haskell and Erlang shells for template metaprogramming. It uses Clang to evaluate the metaprograms."

The homepage argues that beginners have to learn tricks just to see the result of a simple metaprogram, and that debugging is hard because compilers are not built to expose intermediate results. A REPL shortens the loop between a guess and an answer. That makes it a handy way to learn how compile-time computation in C++ actually behaves.

The Homebrew formula also installs a full LLVM/Clang toolchain, including the templight family of tools (templight, templight++, templight-cl, templight_metashell). The brief does not describe how they fit together, but they appear to be bundled with the shell as its Clang-based backend.

## Install

```
brew install metashell
# On macOS, Xcode with the Command Line Developer Tools must be installed. The formula pulls in a full LLVM/Clang distribution, so the download is large.
```

## Try this

```
metashell --help
```
Lists the shell's command-line options so you can see how to start a session.

## What's unique

It is a REPL for C++ template metaprogramming, a narrow niche where the compiler is driven interactively to evaluate metafunctions and show their results.

## Caveats

The project looks quiet: the newest installers listed are version 4.0.0 for distributions from around 2018, and the CI badges point to the retired Travis service.

## Links

- [Homepage and docs](http://metashell.org)
- [Online demo](http://metashell.org/about/demo)
- [GitHub repository](https://github.com/metashell/metashell)
- [Binary installers](http://metashell.org/getting_metashell/installers/)
