---
name: yara
title: YARA
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, malware, pattern-matching, reverse-engineering, security]
homepage: https://virustotal.github.io/yara/
scout_score: 5
status: draft
---

# YARA

**TLDR;** A small rule language for describing files by their strings and a boolean condition, then scanning anything to see which rules match.

YARA lets you write a rule that describes a thing you want to find in a file. A rule has an optional meta section, a strings section that names patterns ($a, $b, $c) as hex byte sequences or quoted text, and a condition that is a boolean expression over those names, such as `$a or $b or $c`. Point the `yara` command at files and it reports which rules matched. The README's example rule, which matches any of two hex patterns or one text string, is labelled silent_banker.

It was built for malware researchers, in the project's words 'aimed at (but not limited to) helping malware researchers to identify and classify malware samples.' The homepage also calls it 'The pattern matching swiss knife for malware researchers (and everyone else).' Richer rules can use wildcards, case-insensitive strings, regular expressions and other operators, covered in the documentation.

The idea underneath is that classification can be written down as a small declarative text file that a person can read. That is why the rule format spread: the homepage lists dozens of organisations that use it. Learning to write rules is a gentle way into thinking about what makes a binary recognisable, which strings survive, and what a family of samples has in common.

There is also `yarac`, which compiles rules ahead of time. YARA can be driven from Python through the separate yara-python extension.

## Install

```
brew install yara
```

## Try this

```
yara --help
```
Lists the command-line options for scanning files with a rules file.

```
yarac --help
```
Shows how to compile a rules file into a binary form that can be reused.

## What's unique

The rule language is the real product: small, readable and declarative, and adopted widely enough that security vendors and sandboxes share rules written in it.

## Caveats

The GitHub README says the project is in maintenance mode and points to YARA-X as the stable successor, so new development is happening there.

## Links

- [Homepage](https://virustotal.github.io/yara/)
- [Documentation](https://yara.readthedocs.org/)
- [GitHub repository](https://github.com/VirusTotal/yara)
- [YARA-X is stable (maintenance-mode successor)](https://virustotal.github.io/yara-x/blog/yara-x-is-stable/)
