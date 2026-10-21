---
name: radamsa
title: Radamsa
source: brew
category: take-things-apart
commitment: quick
tags: [fuzzing, quick, security, testing, unix-filter]
homepage: https://gitlab.com/akihe/radamsa
scout_score: 7
status: draft
---

# Radamsa

**TLDR;** A fuzzer that works like cat: pipe in sample data, get back subtly broken variants, and watch what falls over when you feed them to a program.

Radamsa is a general-purpose, black-box fuzzer shipped as a single binary with no runtime dependencies. You give it sample data on stdin or as files, and it writes mutated copies to stdout, to numbered files, or over TCP. It needs no knowledge of the target program or the data format. The README describes it as the cat tool, which "manages to break the data in often interesting ways as it flows through."

Inside, it applies a mix of heuristics and change patterns, varying between runs from a single small change to many, including bit flips and more advanced mutations. By default the seed comes from /dev/urandom. Pass a fixed seed with --seed and the same output comes back, which is what makes a crash reproducible.

The idea underneath is that fuzzing has two halves: generating odd inputs, and noticing what the target did with them. Radamsa handles the first half. The second is left to a few lines of shell, for example a loop that flags a crash when the exit status is above 127. That split is why it is easy to script and drop into regression tests. The README credits it with CVEs in libarchive, libtiff, Chromium, Firefox and others.

Try it on something harmless first. A calculator or a decompressor fed thousands of mangled inputs shows how many ways a program can be surprised.

## Install

```
brew install radamsa
# Building from source instead needs gcc or clang, make, git and wget; compiling can take several GB of memory.
# Fuzzed data can hang, reboot or corrupt things, so run it against targets in a VM, sandbox or disposable system.
```

## Try this

```
echo "HAL 9000" | radamsa
```
Prints one mutated version of the line; run it again and the result changes.

```
echo "Fuzztron 2000" | radamsa --seed 4
```
A fixed seed gives the same output every time. The README's example produces Fuzztron 4294967296.

```
echo "100 * (1 + (2 / 3))" | radamsa -n 10000 | bc
```
Feeds 10000 mangled expressions to the bc calculator so you can watch for errors, hangs and crashes.

## What's unique

It needs no instrumentation or format description, yet behaves like a plain Unix filter, so a basic fuzzing loop is one line of shell.

## Caveats

The README warns that fuzzed data can cause reboots, hangs and data loss and sums it up as "Not safe when used as prescribed"; I could not confirm when it was last updated, and the README may be dated.

## Links

- [Project homepage (GitLab)](https://gitlab.com/akihe/radamsa)
- [README (raw)](https://gitlab.com/akihe/radamsa/-/raw/master/README.md)
- [Issue tracker (new issue)](https://gitlab.com/akihe/radamsa/issues/new)
