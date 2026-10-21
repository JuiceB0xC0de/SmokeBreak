---
name: eiffelstudio
title: EiffelStudio
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, design-by-contract, eiffel, gui, ide, language, object-oriented]
homepage: https://www.eiffel.com
scout_score: 6
status: draft
---

# EiffelStudio

**TLDR;** A full IDE for Eiffel, the object-oriented language where preconditions, postconditions and invariants are part of the code itself.

EiffelStudio is the development environment for Eiffel, published by Eiffel Software. Eiffel is built around Design by Contract: each routine states what it requires (preconditions) and what it guarantees (postconditions), and each class states what must always hold (invariants). These are written in the language and checked automatically, and violations are reported at the point of failure.

The site's argument is that most tooling optimizes for writing code quickly and leaves assumptions implicit, then relies on testing to catch problems late. In its words: "Testing validates samples of behavior. It does not define what must never happen." The project is pitched as a way to make correctness "explicit, executable, and continuously enforced."

The homepage also mentions automatic testing that needs no test cases or oracles, and SCOOP for concurrency. The pages read do not explain how either works, and the testing claim is a vendor claim, so treat it as something to check yourself.

Homebrew installs several executables: ec, ecb, estudio, compile_all, finish_freezing, iron, syntax_updater and vision2_demo. The pages read do not describe them, so the names are all this entry can offer. The GTK3 dependencies suggest estudio is the graphical IDE and vision2_demo a toolkit demo, but that is a guess from the names.

## Install

```
brew install eiffelstudio
# pulls in GTK+3 and related libraries for the graphical IDE
```

## Try this

```
ec --help
```
Prints usage for ec, which is listed as an installed executable; its role is not explained in the pages read.

```
estudio --help
```
Shows options for the estudio executable, which is likely the graphical IDE.

## What's unique

Design by Contract is built into the language and, per the site, into the IDE's navigation and testing, rather than added through a library or a linter.

## Caveats

The vendor sells it commercially with Purchase and Enterprise tiers, the homepage is mostly marketing, and licensing terms and platform support were not verified; the Homebrew formula lists GPL-2.0-only.

## Links

- [Homepage](https://www.eiffel.com)
- [Downloads and product overview](https://www.eiffel.com/downloads/)
