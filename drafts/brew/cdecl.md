---
name: cdecl
title: cdecl
source: brew
category: languages-and-oddities
commitment: quick
tags: [c, c++, declarations, old-school, parsing, preprocessor, quick]
homepage: https://github.com/paul-j-lucas/cdecl
scout_score: 6
status: draft
---

# cdecl

**TLDR;** Turns English like "pointer to const pointer to const char" into a C or C++ declaration, and explains declarations back in English.

cdecl is a command-line translator for C and C++ declarations and casts. Type `declare p as pointer to const pointer to const char` and it prints `const char *const *p;`. Give it `int *const (*p)[4]` with `explain` and it answers "declare p as pointer to array 4 of constant pointer to integer". It runs as an interactive prompt, or reads from the command line or standard input.

The reason it exists is the declaration syntax itself. C declarations mirror how a variable is used, which makes them hard to read. The README quotes Dennis Ritchie saying he is "still uncertain" about that design, and Bjarne Stroustrup calling it "an experiment that failed". cdecl is the tool for the gibberish those choices produce.

The idea underneath is that C declarations are a small grammar you can learn to parse by hand, and a tool that does it for you shows the rules at work. The code is built on a flex lexer and a bison parser. This version covers standards from K&R C through C23 and C++98 through C++26.

It also has a mode for debugging preprocessor macros. Define a macro inside the session, run `expand` on a use of it, and cdecl shows each substitution step. That goes beyond declaration translation, and it is useful for token-pasting tricks like `A ## B`.

## Install

```
brew install cdecl
# installs two executables: cdecl and c++decl
```

## Try this

```
explain int *const (*p)[4]
```
At the cdecl prompt, prints "declare p as pointer to array 4 of constant pointer to integer".

```
declare p as pointer to const pointer to const char
```
Prints the C declaration `const char *const *p;`.

```
cdecl --help
```
Lists the command-line options and how to run it non-interactively.

## What's unique

It claims to be the most complete and current take on the classic English-to-C-declaration tool, covering many language standards. It also adds a step-by-step macro expander.

## Caveats

Unix-like systems only, with no native Windows support, and the code has an unusual licensing history: the 1980s original never had a license, and 3.0 and later are GPL v3.

## Links

- [GitHub repository and README](https://github.com/paul-j-lucas/cdecl)
- [Released versions (includes configure and generated parser)](https://github.com/paul-j-lucas/cdecl/releases)
- [README-2.5.txt (David Conrad's comments on licensing)](https://github.com/paul-j-lucas/cdecl/blob/master/README-2.5.txt)
