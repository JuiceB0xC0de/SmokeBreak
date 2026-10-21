---
name: wllvm
title: wllvm
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, bitcode, compilers, llvm, python, static-analysis]
homepage: https://pypi.org/project/wllvm/
scout_score: 5
status: draft
---

# wllvm

**TLDR;** Compiler wrappers that build an ordinary C or C++ project as usual, then hand you the whole program as one LLVM bitcode file for analysis.

WLLVM is a set of Python wrappers that stand in for gcc or g++ in a normal build. Set `CC=wllvm` and run `./configure` or `cmake` as usual. Each wrapper runs the real compiler, then also asks clang for LLVM bitcode for the same source file. The build still produces working binaries.

The trick is where the bitcode goes. The wrapper records the path of each bitcode file in a dedicated section of the object file. When the linker joins objects, those sections are concatenated. After the build, `extract-bc` reads the section from a finished executable, library, or archive. It links all the bitcode into one whole-program module, or a bitcode archive for static libraries.

The README says this two-phase design is needed to be a drop-in replacement in any build system. It says gcc's LTO with the gold plugin works in many cases but fails with static libraries. Keeping the linker out of the job lets unmodified build systems do their normal thing.

The payoff is that you can feed real programs to tools that work on LLVM IR, such as analyzers, verifiers, and optimizers. You don't have to rewrite the build for them. The README's examples include pkg-config, the Bullet physics library, and apache.

## Install

```
brew install wllvm
# needs python and a clang install; before use, set the required variable:
export LLVM_COMPILER=clang
```

## Try this

```
wllvm-sanity-checker
```
Checks your environment variable setup and points out likely configuration mistakes.

```
CC=wllvm ./configure
```
Configures a package with wllvm as its C compiler, so the build makes bitcode alongside normal objects.

```
extract-bc pkg-config
```
Pulls the embedded bitcode out of a built pkg-config executable and writes pkg-config.bc.

## What's unique

Instead of making the linker merge bitcode, it hides bitcode file paths inside object-file sections. Ordinary build systems work unchanged and still produce real binaries.

## Caveats

The README looks dated (it mentions August 2016 and Ubuntu 14.04/16.04 tutorials), supports only *nix, and says gllvm is faster if you don't need dragonegg; the Homebrew formula also installs wfortran, wllvm-as and wparse-args, which the README doesn't document.

## Links

- [PyPI page](https://pypi.org/project/wllvm/)
- [GitHub repository and README](https://github.com/travitch/whole-program-llvm)
- [Tutorial: building apache on Ubuntu 14.04](https://github.com/travitch/whole-program-llvm/blob/master/doc/tutorial.md)
