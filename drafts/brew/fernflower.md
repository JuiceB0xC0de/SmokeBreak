---
name: fernflower
title: Fernflower
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, bytecode, decompiler, java, jetbrains, reverse-engineering]
homepage: https://github.com/JetBrains/fernflower
scout_score: 6
status: draft
---

# Fernflower

**TLDR;** JetBrains' Java decompiler: feed it .class files or jars and it writes back readable Java source, with a renamer for obfuscated code.

Fernflower takes compiled Java bytecode (.class files, .zip or .jar archives, or directories scanned recursively) and writes reconstructed Java source into a destination directory. You can also pass library jars so that classes your code depends on resolve properly without being decompiled themselves. It is the same engine bundled in IntelliJ IDEA, which shows source when you debug or open a class file.

The README is confident about it: "Fernflower is the first actually working analytical decompiler for Java and probably for a high-level programming language in general." The README does not explain the internal algorithm, so the interesting part is the surface. Bytecode keeps far less than source does, so decompiling is a series of guesses about what the author wrote. The long list of -option=value flags, mostly 0/1 toggles, exposes those guesses: hide bridge methods, decompile enumerations, turn lambdas into anonymous classes, keep generic signatures.

The renamer is the unusual feature. The README notes that "Some obfuscators give classes and their member elements short, meaningless and above all ambiguous names," and recompiling such code produces many conflicts. With ren=1, Fernflower renames elements that are reserved words or shorter than three characters to names like class_<n>, method_<n> and field_<n>. You can plug in your own renamer by implementing IMemberIdentifierRenamer and passing it with urc.

The project has been maintained by JetBrains since 2014. Its original author, Stiver, has passed away, and the README includes a note on the correct spelling: Fernflower, not FernFlower.

## Install

```
brew install fernflower
Requires a Java runtime (the formula depends on openjdk). No account or hardware needed.
```

## Try this

```
fernflower --help
```
Runs the installed executable. The README documents the underlying usage as java -jar fernflower.jar [-<option>=<value>]* [<source>]+ <destination>, and it is not confirmed that the brew wrapper takes the same arguments.

```
java -jar fernflower.jar -dgs=1 c:\Temp\binary\library.jar c:\Temp\binary\Boot.class c:\Temp\source\
```
README example: decompiles a jar and a single class together with generic signatures turned on, writing the source to the last argument. Adjust the paths for your system.

```
java -jar fernflower.jar -hes=0 -hdc=0 c:\Temp\binary\ -e=c:\Java\rt.jar c:\Temp\source\
```
README example: decompiles a directory of classes, keeps empty super calls and default constructors visible, and uses a library jar for context.

## What's unique

The renamer is a first-class, pluggable feature aimed at obfuscated bytecode, and the option list covers modern Java constructs such as records and pattern switches. It is also the decompiler inside IntelliJ IDEA.

## Caveats

The README assumes you are a Java developer and says most options are aimed at professional reverse engineers. Its examples use Windows paths and an rt.jar that modern JDKs no longer ship. How the Homebrew executable wraps the jar is not documented.

## Links

- [Homepage / GitHub repository](https://github.com/JetBrains/fernflower)
- [Releases (IntelliJ repository)](https://www.jetbrains.com/intellij-repository/releases)
- [Issue tracker (YouTrack, subsystem Java. Decompiler. Engine)](https://youtrack.jetbrains.com/newIssue?project=IDEA&clearDraft=true&c=Subsystem%20Java.%20Decompiler.%20Engine)
- [IntelliJ Community repository (where contributions go)](https://github.com/JetBrains/intellij-community)
