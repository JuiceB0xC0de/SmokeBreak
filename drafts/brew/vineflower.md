---
name: vineflower
title: Vineflower
source: brew
category: take-things-apart
commitment: quick
tags: [bytecode, decompiler, java, jvm, quick, reverse-engineering]
homepage: https://vineflower.org/
scout_score: 5
status: draft
---

# Vineflower

**TLDR;** A Java decompiler that turns compiled JVM bytecode back into readable source, from a jar, a folder, or a single class file.

Vineflower reads compiled JVM bytecode and writes Java source back out. Feed it a jar, a zip, a folder, or one class file. It writes to a folder, zip, or jar, or prints to the console if you give no destination. The README says it also handles other JVM languages, and supports newer Java features such as records, sealed classes, switch expressions and pattern matching.

Its stated aim is to be "as accurate as possible, while not sacrificing the readability of the generated code." The README lists clean code generation with automatic formatting and multithreaded decompilation as features. It does not explain how the decompilation works internally.

The project is a fork of forks. It descends from JetBrains' Fernflower, through MinecraftForge's ForgeFlower and FabricMC's fork, and is a direct continuation of Quiltflower. That lineage is a reminder that a compiled program is not a sealed box: bytecode keeps a lot of structure, and a decompiler rebuilds loops, branches and classes from it.

A good way in is to decompile a jar you already have and read what comes out, then compare with the project's output-comparison page, which shows its results next to other decompilers. It can also be used as a library, and there is an IntelliJ IDEA plugin that swaps it in for Fernflower.

## Install

```
brew install vineflower
Requires a Java runtime (Homebrew pulls in openjdk). The README says running the jar needs Java 17 or newer.
```

## Try this

```
vineflower --help
```
Prints the command-line options the installed launcher accepts.

```
java -jar vineflower.jar <source> <destination>
```
Decompiles a jar, zip, folder, or class file into the destination folder, zip, or jar. This is the README's form for the raw jar, not the brew launcher.

```
java -jar vineflower.jar <source>
```
Leaves out the destination, so the decompiled source prints to the console.

## What's unique

It is the latest in a Fernflower fork lineage, and it publishes a side-by-side output comparison against other decompilers. It ships as a plain jar with no install step beyond a Java runtime.

## Caveats

Needs Java 17 or newer to run, and the README calls it a work-in-progress project; the brief could not confirm a recent release date.

## Links

- [Homepage](https://vineflower.org/)
- [GitHub repository](https://github.com/Vineflower/vineflower)
- [Output comparison](https://vineflower.org/output-comparison/)
