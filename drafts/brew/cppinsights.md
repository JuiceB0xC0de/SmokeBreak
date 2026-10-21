---
name: cppinsights
title: C++ Insights
source: brew
category: take-things-apart
commitment: quick
tags: [c++, clang, compilers, learning, quick, source-to-source]
homepage: https://cppinsights.io/
scout_score: 7
status: draft
---

# C++ Insights

**TLDR;** Rewrites your C++ the way Clang sees it, with lambdas, implicit conversions and deduced types spelled out as ordinary C++ you can read.

C++ Insights is a Clang-based tool that does a source-to-source transformation. You give it a C++ file and it prints another C++ file, one where the work the compiler normally does silently is written out. The README's examples include compiler-generated special member functions, lambdas, range-based for-loops, structured bindings, the implicit upcast from Derived to Base, and the types hidden behind auto and decltype.

The author, Andreas Fertig, built it because AST dumps and assembly listings are not in the language he writes. Showing a student an AST and saying "this is all there was" was unsatisfying. So the output stays in C++: a defaulted special member function appears as a commented-out default, and an implicit upcast appears as a static_cast.

The idea underneath is that much of C++ is things the compiler does on your behalf. In the project's words: "It's about the magic the compiler does for us to make things work." A lambda turns out to be a small class with an operator(). A range-based for turns out to be iterator calls. Seeing that written out makes the rules easier to remember than reading the standard.

The tool parses with Clang and uses Clang's AST to decide what to rewrite, so it is only as accurate as Clang's understanding. The author says plainly: "I do not claim to get all the things right." The output is meant to compile but is not guaranteed to. There is also a web version at cppinsights.io with Source, Insight and Console panes, so you can try it without installing anything.

## Install

```
brew install cppinsights
# pulls in llvm@21 as a dependency. The README describes the Homebrew route as macOS-focused; elsewhere you build from source with CMake, Ninja and a Clang installation, or use the web version.
```

## Try this

```
insights <YOUR_CPP_FILE> -- -std=c++17
```
Prints your file rewritten with the compiler's hidden work made explicit. Clang options go after the -- separator.

```
insights <YOUR_CPP_FILE> -- -std=c++17 `./scripts/getinclude.py`
```
Does the same but passes in system include paths collected from your compiler, for when the hard-coded ones don't match your setup. The script is in the source repository.

```
insights --help
```
Lists the available options.

## What's unique

The output is C++ rather than an AST dump or assembly, so you read the compiler's work in the language you wrote. It is also available as a web page with no install.

## Caveats

Output depends on Clang's AST and is not always compilable, C++20 support was described as still in progress, and I could not confirm recent project activity.

## Links

- [Homepage (online tool)](https://cppinsights.io/)
- [GitHub repository and README](https://github.com/andreasfertig/cppinsights)
