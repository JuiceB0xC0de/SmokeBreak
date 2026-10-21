---
name: cfr-decompiler
title: CFR
source: brew
category: take-things-apart
commitment: quick
tags: [decompiler, java, jvm, quick, reverse-engineering]
homepage: https://www.benf.org/other/cfr/
scout_score: 7
status: draft
---

# CFR

**TLDR;** CFR turns compiled Java .class files and jars back into readable Java source, by recognising the patterns compilers leave behind.

CFR is a Java decompiler. Give it a .class file, a fully qualified class name on your classpath, or a whole jar, and it prints Java source to the terminal. With `--outputdir` it writes the files to a directory instead. The author says it handles much of Java 9, 12 and 14, and makes a decent attempt at class files from other JVM languages.

The author's stated reason for building it is that it is a satisfying way to take programs apart. It is written entirely in Java 6, so it runs on almost any JVM.

The idea underneath is that a compiler is a set of habits. javac, ECJ and Kotlin each turn string concatenation, enums, lambdas, switch-on-string and try-with-resources into recognisable bytecode shapes. CFR works by spotting those shapes and reversing them, so the output reads like the original source rather than raw bytecode. The site collects the author's observations on how each compiler does this, and they are worth reading even if you never run the tool.

The author has also said CFR avoids relying on type tables, since an obfuscator can fake those. Flags such as `--antiobf` and `--aggressivesizethreshold` switch on extra recovery passes.

## Install

```
brew install cfr-decompiler
# needs a Java runtime; the formula depends on openjdk@21
```

## Try this

```
cfr-decompiler --help
```
Lists every argument CFR accepts, including the recovery and anti-obfuscation options.

```
cfr-decompiler SomeLibrary.jar --outputdir /tmp/putithere
```
Decompiles every class in the jar and writes the Java source files into /tmp/putithere instead of the terminal.

## What's unique

It decompiles from the compiler's side, recognising the idioms of javac, ECJ and Kotlin, including records, sealed classes and pattern switches, so output looks like source someone wrote.

## Caveats

The author calls it a work in progress with 'a lot of things missing', output is not guaranteed to match the original source, and the latest release (0.152) dates from December 2021, though the homepage hints at new work in 2026.

## Links

- [CFR homepage (benf.org)](https://www.benf.org/other/cfr/)
- [GitHub repository (README)](https://github.com/leibnitz27/cfr)
- [FAQ](https://www.benf.org/other/cfr/faq.html)
