---
name: ghidra
title: Ghidra
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, decompiler, disassembler, gui, java, python, reverse-engineering]
homepage: https://github.com/NationalSecurityAgency/ghidra
scout_score: 5
status: draft
---

# Ghidra

**TLDR;** A reverse engineering framework from the NSA that disassembles and decompiles compiled programs across many processor architectures, with a GUI and scripting in Java or Python.

Ghidra takes a compiled executable, in a wide range of file formats and for many instruction sets, and turns it back into something a person can read. It disassembles, decompiles, graphs, and lets you annotate as you go. It runs on Windows, macOS, and Linux, and it can also run headless for automated analysis.

The README says it was built "to solve scaling and teaming problems on complex SRE efforts, and to provide a customizable and extensible SRE research platform." The NSA Research Directorate created and maintains it, and the README says the agency has used it to analyse malicious code and to understand potential vulnerabilities in networks and systems.

The door it opens is the idea that a binary is not opaque. Once you can see the machine code lifted into readable pseudo-code, you can ask what a program does without the source. Scripts and extensions can be written in Java or Python, so you can automate the questions you keep asking. A separate PyGhidra launcher exists for Python-driven use.

## Install

```
brew install ghidra
Requires a JDK; the formula pulls in openjdk@21. The README's own notes for the pre-built release name JDK 25, so check the Getting Started document if the launcher complains about the Java version.
```

## Try this

```
ghidraRun
```
Launches the Ghidra GUI, where you create a project and import a binary to analyse.

```
pyghidraRun
```
Launches Ghidra through PyGhidra, the Python-based launcher.

```
ghidraRun --help
```
Prints whatever launch options the launcher offers.

## What's unique

It is a full-featured decompiler and disassembler that is open source under Apache-2.0, with scripting in both Java and Python and a headless mode alongside the GUI.

## Caveats

The README opens with a warning that certain versions have known security vulnerabilities, so read the Security Advisories before using it on anything sensitive.

## Links

- [GitHub repository (homepage)](https://github.com/NationalSecurityAgency/ghidra)
- [Releases (pre-built zip downloads)](https://github.com/NationalSecurityAgency/ghidra/releases)
- [Security Advisories](https://github.com/NationalSecurityAgency/ghidra/security/advisories)
- [Getting Started doc](https://github.com/NationalSecurityAgency/ghidra/blob/master/GhidraDocs/GettingStarted.md)
