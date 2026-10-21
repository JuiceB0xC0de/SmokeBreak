---
name: jasmin
title: Jasmin
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, assembler, bytecode, java, jvm, old]
homepage: https://jasmin.sourceforge.net/
scout_score: 6
status: draft
---

# Jasmin

**TLDR;** Jasmin is an assembler for the JVM: you write bytecode mnemonics by hand and it emits a real .class file Java can run.

Jasmin reads plain text files written in an assembler-like syntax, with directives that start with a dot, JVM opcode mnemonics, and labels, and turns them into binary Java .class files. The .class directive at the top of the source names the class and decides where the output lands.

It was written by Jon Meyer as a companion to his O'Reilly book 'Java Virtual Machine', so readers could try JVM features directly. The homepage says that since then it has become "the de-facto standard assembly format for Java" and is used in compiler classes around the world.

The interesting part is how literal it is. Jasmin maps almost one-to-one onto class-file structure and, in its own words, "does little compile-time processing or checking of the input code." It does not check that referenced classes exist or that descriptors are well formed. That means you can hand-write bytecode a Java compiler would never produce and watch what the verifier and runtime do with it.

Writing in it exposes the machine under Java: an operand stack, numbered local variables, exception tables, and names in class-file form, like java/lang/String and java/io/PrintStream/println(Ljava/lang/String;)V as a single token. It is a small, old tool, and that is part of the point: the format is simple enough to hold in your head.

## Install

```
brew install jasmin
# needs a Java runtime; Homebrew pulls in openjdk
```

## Try this

```
jasmin --help
```
Shows the options the installed wrapper accepts.

```
java -jar jasmin.jar myfile.j
```
Assembles myfile.j into a .class file, placed in the directory implied by its .class directive.

```
java -jar jasmin.jar -d /tmp myfile.j
```
Writes the output class file under /tmp, for example /tmp/mypackage/MyClass.class, instead of the current directory.

## What's unique

It is the original Java assembler, thin and deliberately unchecked, so you can write bytecode a compiler would refuse to emit and see what the JVM does with it.

## Caveats

The documentation dates from 1996 and the homepage from 2005, so recent maintenance is unconfirmed, and mistakes in class references or descriptors only show up at runtime or in the verifier.

## Links

- [Jasmin homepage](https://jasmin.sourceforge.net/)
- [Jasmin User Guide (July 1996)](https://jasmin.sourceforge.net/guide.html)
