---
name: umple
title: Umple
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, code-generation, java, language, modeling, uml]
homepage: https://cruise.umple.org/umple/
scout_score: 5
status: draft
---

# Umple

**TLDR;** Umple is a modeling language that adds associations and state machines to Java, Python, C++ and PHP, then generates the boilerplate code and UML-style diagrams for you.

Umple takes text you write, such as classes with attributes, associations and state machines, and compiles it into code in a host language. Java, C++ and PHP are the mature targets, and Python is in beta per the README. It also produces diagrams, metrics and other artifacts from the same text. The graphical editor maps diagram elements back to the Umple source, so you can edit either side.

The idea underneath is that the model is the thing you read and edit, and the generated code is disposable. A line like `* -- 1 Student;` declares an association, and the compiler fills in the constructors, accessors and link management. The homepage says this generated boilerplate never has to be inspected or maintained, because it has been tested.

Umple dates from 2007 and has been on GitHub since 2015. The compiler is written in Umple itself, which makes it self-hosted. Umple can also be embedded in host-language code and the reverse. The homepage pitches it as a way to cut boilerplate, and as a way to check AI-generated models, since you can read the Umple text and diagrams.

The project's name is a pun: 'Simple', 'UML Programming Language' and 'Ample'.

## Install

```
brew install umple
Requires Java (the formula pulls in openjdk). To try it with no install, use UmpleOnline in the browser at https://try.umple.org.
```

## Try this

```
umple --help
```
Prints the compiler's command-line options so you can see how to point it at an Umple file and pick a target language.

## What's unique

Most code generators treat the output as the thing you keep. Umple reverses that: you edit the model, and the generated code is treated as disposable. It is also compiled by itself.

## Caveats

Much of the code is research-derived, so expect academic rough edges. The Python generator is beta, and some subprojects are in early development.

## Links

- [Umple homepage](https://cruise.umple.org/umple/)
- [User manual](https://manual.umple.org)
- [UmpleOnline (browser version)](https://try.umple.org)
- [Download page](https://umple.org/dl)
- [GitHub repository](https://github.com/umple/umple)
