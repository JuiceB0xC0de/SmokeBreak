---
name: frege
title: Frege
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, functional, haskell, jvm, language]
homepage: https://github.com/Frege/frege/
scout_score: 6
status: draft
---

# Frege

**TLDR;** A lazy, purely functional language in the spirit of Haskell that compiles to Java and runs on the JVM, with access to any Java library.

Frege is described by its README as "a Haskell for the JVM." It compiles Frege source to Java, producing a `.java` and a `.class` file per module, and runs on the Java Virtual Machine. The compiler is `fregec`. Frege code can call Java libraries, and Java code can call Frege functions. The README says the standard library covers almost all of Haskell 2010, and that most idiomatic Haskell runs unmodified or with small, obvious changes.

The project is aimed at two audiences. Java programmers get a way to learn the pure functional style. Haskell programmers get a way to use their skills on the JVM while keeping Java's libraries. The README says Frege keeps Haskell's guarantees, such as purity, thread safety and lazy evaluation, even when it calls into Java.

The idea underneath is purity carried in the types. A strong static type system with global type inference tracks which functions are pure. `main` is typed `IO ()`, and anything that calls an IO function must itself be IO, so impurity propagates up the call chain. The README's Hello World shows this as islands of purity in a sea of imperative code. Because pure functions are stateless, the README suggests a compiler could cache them or apply optimizations like precalculation, deferred execution and common subexpression elimination.

To call Java from Frege, you declare the Java types in Frege terms, which is where the type system meets the outside world. Most of the compiler, standard library, REPL and documentation tool are written in Frege itself, which the README offers as evidence of stability. The language is named after Gottlob Frege, who published ideas on higher-order functions and partial application.

## Install

```
brew install frege
Requires a JDK (the formula pulls in openjdk); the README says JDK 7 or later. To try it without installing anything, use the online REPL at http://try.fregelang.org/
```

## Try this

```
fregec --help
```
Prints the compiler's options, a first look at how Frege source becomes Java.

## What's unique

It brings Haskell's purity and laziness to the JVM, with typed access to Java libraries, and the compiler is largely written in Frege itself.

## Caveats

Documentation is described as provisional, some differences from Haskell remain, and the project appears quiet since about 2022, though that was not confirmed.

## Links

- [Project homepage (GitHub)](https://github.com/Frege/frege/)
- [Frege Wiki, including Getting Started](https://github.com/Frege/frege/wiki/_pages)
- [Language reference (PDF)](http://www.frege-lang.org/doc/Language.pdf)
- [Online REPL](http://try.fregelang.org/)
