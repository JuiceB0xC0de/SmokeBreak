---
name: csmith
title: Csmith
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, compilers, fuzzing, generative, testing]
homepage: https://github.com/csmith-project/csmith
scout_score: 8
status: draft
---

# Csmith

**TLDR;** Csmith writes random C programs that avoid undefined behavior, so you can compile them with different compilers and treat any disagreement as a bug.

Run `csmith` and it prints one randomly generated C program to standard output. Redirect it to a file, compile it, run it. The program computes something opaque and prints a result. That result is not interesting on its own. It becomes interesting when you compile the same file with a second compiler and the two binaries disagree.

That is differential testing, and it is the idea underneath the tool. There is no expected answer to check against. If gcc and clang are both correct and the program is well defined, they must produce the same output. A mismatch points to a bug in one compiler, or, as the README puts it, in the unlikely case, in Csmith itself.

The hard part is the guarantee. In the README's words, Csmith outputs C programs free of undefined behaviors ("believe us, that's not trivial"). Without that, a mismatch could just mean the program was allowed to do anything. The project was built as research on finding bugs in C compilers, and the PLDI 2011 paper linked below describes the work.

The README also suggests it for anyone who needs a pile of C test programs and does not want to write them by hand. The package installs two Perl scripts alongside `csmith`, `compiler_test.pl` and `launchn.pl`, though the brief does not describe what they do.

## Install

```
brew install csmith
# Brew recommends setting CSMITH_PATH:
export CSMITH_PATH=$HOMEBREW_CELLAR/csmith/2.3.0/include/csmith-2.3.0
# Compiling generated programs needs a C compiler (gcc or clang) and Csmith's include directory on the include path via -I.
```

## Try this

```
csmith > random1.c
```
Generates one random C program and writes it to random1.c.

```
gcc random1.c -I$HOME/csmith/include -o random1
```
Compiles the generated program with gcc, using Csmith's include directory. Adjust the -I path to wherever your install keeps its headers.

```
csmith -h
```
Lists the command line options for customizing what gets generated.

## What's unique

It needs no expected answers. It generates valid C that avoids undefined behavior and uses disagreement between compilers as the bug signal.

## Caveats

The README says the project is maintained on the authors' discretionary time and replies may be slow. Generated programs can loop forever, so run them under a timeout.

## Links

- [Csmith GitHub repository and README](https://github.com/csmith-project/csmith)
- [Using Csmith for compiler testing (slightly outdated guide)](http://embed.cs.utah.edu/csmith/using.html)
- [Finding and Understanding Bugs in C Compilers (PLDI 2011 paper)](https://www.cs.utah.edu/~regehr/papers/pldi11-preprint.pdf)
