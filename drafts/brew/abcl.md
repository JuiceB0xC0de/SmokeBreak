---
name: abcl
title: ABCL (Armed Bear Common Lisp)
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, common-lisp, jvm, language, lisp, repl]
homepage: https://abcl.org/
scout_score: 5
status: draft
---

# ABCL (Armed Bear Common Lisp)

**TLDR;** A full ANSI Common Lisp that compiles to Java bytecode, giving you a Lisp REPL with direct access to the Java ecosystem.

Armed Bear Common Lisp is an implementation of ANSI Common Lisp that runs on the Java Virtual Machine. It has an interpreter and a compiler, and the compiler turns Lisp code into Java byte code. You start it and land in a Lisp REPL where you type forms and get results.

According to the homepage, it began as a scripting language for the J editor. It has since grown into what the README calls "a conforming implementation of ANSI X3J13 Common Lisp that runs in a Java virtual machine." The README treats any non-conforming behavior as a bug.

The interesting part is the host. Because Lisp compiles to JVM byte code, Lisp can call Java libraries and Java programs can embed Lisp. ABCL works as a JSR-223 scripting engine, and it has APIs for Java-to-Lisp integration, so you can write parts of a Java application in Lisp. That puts an old, dynamic, interactive language inside one of the most widely deployed runtimes.

It also works with the usual Common Lisp tooling. The README describes installing Quicklisp with a provided script and starting a Swank server so Emacs SLIME can connect.

## Install

```
brew install abcl
# pulls in openjdk and rlwrap as dependencies; the README says Java 8, 11 and 17 are strongly supported
```

## Try this

```
abcl
```
Opens the interactive REPL with a CL-USER(1): prompt, where you can type Lisp forms and see results.

```
abcl --help
```
Lists the command-line options for the launcher.

## What's unique

It is a full Common Lisp that lives on the JVM, so Lisp code can use Java libraries and be embedded in Java applications. The README reports Maxima's test suite passes on it.

## Caveats

The README says 1.9.2 fails about 63 of 21,902 ANSI tests and that "ABCL has many deficiencies, both known and unknown"; the project looks quiet, with the README footer dated June 2023.

## Links

- [Homepage](https://abcl.org/)
- [User Manual (PDF, 1.9.2)](https://abcl.org/releases/1.9.2/abcl-1.9.2.pdf)
- [Source on GitHub](https://github.com/armedbear/abcl)
