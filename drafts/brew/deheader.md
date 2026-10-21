---
name: deheader
title: deheader
source: brew
category: take-things-apart
commitment: quick
tags: [build, c, c++, includes, quick, static-analysis]
homepage: http://www.catb.org/~esr/deheader/
scout_score: 5
status: draft
---

# deheader

**TLDR;** Eric Raymond's tool finds unneeded #include lines in C and C++ by deleting each one and asking your real compiler whether the build still passes.

deheader takes C or C++ source files, or a directory it recurses through, and reports which #include lines can go. It also flags duplicate includes and standard headers that portability may require but that are missing. With -r it rewrites the sources to delete the unneeded includes. The exit status is 1 when removable includes are found, 2 when a file could not be compiled and analyzed, and 0 otherwise.

The homepage says the point is to find unneeded includes, which can substantially improve compilation time on large C++ projects. It also says the exercise sometimes exposes dependencies and cohesions developers did not know about.

The tool does not parse C. For each foo.c, foo.cc or foo.cpp, it removes an include, then runs the equivalent of `rm foo.o; make foo.o`. A zero exit status means that header was not needed. When it detects a CMakeLists.txt it runs `make clean` instead, since foo.o is a phony target there. Each trial works on a temporary backup of the source, restored afterward. Includes inside #if/#ifdef/#else/#endif blocks are left alone.

The idea underneath is to use the compiler as an oracle instead of reimplementing it. Because the build command is just a string you can override with -m, the approach works with any build system you can describe on a command line.

## Install

```
brew install deheader
# You need a working build of your own C/C++ project first (make by default, or a custom command via -m). The docs do not list a runtime, but the -i and -x options take Python regular expressions, so Python is probably needed.
```

## Try this

```
deheader --help
```
Prints the usage line and the options: -m, -b, -i, -q, -r, -v, -x, -V.

```
deheader -m "make CFLAGS='-Werror -Wfatal-errors' %s" -v -v -v .
```
Runs the analysis over the current directory with warnings made fatal, so headers that only declare prototypes are not wrongly marked unneeded. -v -v -v prints the commands actually run so you can check the override.

```
deheader -m 'ninja -C build' .
```
Uses a custom build command for targetless builders such as meson; %s is omitted so the command runs unchanged.

## What's unique

It brute-forces the answer by deleting each include and asking the real compiler whether the build survives, rather than analyzing the code itself. That makes it work with whatever build command you can write down.

## Caveats

With -r it rewrites your sources, so keep them under version control; it can also give false positives, and the docs warn that perverse C++ (overloads, template specializations spread across files) can change behavior silently.

## Links

- [Homepage and resource page](http://www.catb.org/~esr/deheader/)
- [Manual page (deheader.html)](http://www.catb.org/~esr/deheader/deheader.html)
- [Source repository (GitLab)](https://gitlab.com/esr/deheader)
