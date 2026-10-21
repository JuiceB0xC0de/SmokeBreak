---
name: chaiscript
title: ChaiScript
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c++, embedded, language, library, scripting]
homepage: https://chaiscript.com/
scout_score: 6
status: draft
---

# ChaiScript

**TLDR;** A header-only scripting language you embed inside a C++ program, so scripts can call your C++ functions and hand typed values back.

ChaiScript is a scripting language modelled loosely on ECMAScript, built to live inside a C++ application. The host program creates a `chaiscript::ChaiScript` engine, registers its own functions with it, and then runs script source with `eval(string)` for a line at a time or `eval_file(fname)` for a whole file. Results can come back as real C++ types, for example `chai.eval<double>(...)`.

The README describes it as 'one of the only embedded scripting language designed from the ground up to directly target C++'. Instead of bridging through a C API, it is typed against the host program. It keeps type safety between C++ and scripts, and supports callbacks, overloaded functions, class methods and STL containers.

The library is header-only. You include `<chaiscript/chaiscript.hpp>` and there is no separate library to build or link. The standard library loads from a loadable module by default, or can be compiled into your code.

The idea underneath is a useful one: let a compiled program expose a small, safe surface and let someone else drive it with a script, without recompiling. Reading how ChaiScript maps C++ functions and types into a dynamic language is a good way into how embedding works. The project also publishes a formal EBNF grammar, which makes it a small, readable example of a language definition.

## Install

```
brew install chaiscript

Homebrew lists a `chai` executable, but the README does not document a standalone interpreter. The documented route is vcpkg: `git clone https://github.com/Microsoft/vcpkg.git`, `./bootstrap-vcpkg.sh`, `./vcpkg integrate install`, `vcpkg install chaiscript`. You need a C++ compiler; the README says C++17.
```

## Try this

```
chai --help
```
Shows what the installed interpreter accepts. The README does not document this executable, so treat it as exploration.

```
chai.add(chaiscript::fun(&my_function), "my_function_name");
```
In your C++ code, registers a C++ function so scripts can call it as my_function_name.

```
vcpkg install chaiscript
```
Installs ChaiScript through vcpkg, the README's documented route, so you can include the headers in a project.

## What's unique

It is header-only, needs no preprocessor or external tools, and is typed directly against the host C++ program rather than going through a C API.

## Caveats

The homepage says C++14 while the README says C++17, the CI badges point to Travis and AppVeyor, and the copyright notice stops at 2017, so how actively it is maintained is unclear.

## Links

- [ChaiScript homepage](https://chaiscript.com/)
- [GitHub repository and README](https://github.com/ChaiScript/ChaiScript)
- [Formal EBNF grammar](https://github.com/ChaiScript/ChaiScript/blob/master/grammar/chaiscript.ebnf)
