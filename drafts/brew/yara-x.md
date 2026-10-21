---
name: yara-x
title: YARA-X
source: brew
category: take-things-apart
commitment: quick
tags: [malware, pattern-matching, quick, reverse-engineering, rust]
homepage: https://virustotal.github.io/yara-x/
scout_score: 6
status: draft
---

# YARA-X

**TLDR;** VirusTotal's Rust rewrite of YARA: write rules from text or byte patterns plus a condition, then see which files match.

YARA-X is a pattern-matching tool for malware researchers. You describe a malware family, or anything else you want to find, as a rule. The rule has a strings section of named patterns, written as hex byte sequences or quoted text, and a condition that combines them with boolean operators. Run the rules against files and the output is which rules matched.

The README's own example matches any file containing one of three patterns and reports it as `silent_banker`. Patterns can use wildcards, case-insensitive strings and regular expressions. That small vocabulary is how analysts write down what a piece of malware looks like, and how those descriptions get shared and run at scale.

It exists to replace YARA, the older tool, as the default for this work. The README says the new version is faster, safer and more user-friendly. YARA is still maintained, but new large features and modules will go to YARA-X. The homepage says it is 99% rule compatible, so most existing YARA rule sets should run unchanged. There are also C/C++, Python and Go APIs.

The idea underneath is signature matching: reducing a family of binaries to a few telltale byte sequences and a logical test. Reading and writing rules is a good way to see how files are recognised without being run.

## Install

```
brew install yara-x
# the installed executable is named yr
```

## Try this

```
yr --help
```
Lists the subcommands the yr binary offers, since the pages read did not document its usage.

## What's unique

It is a drop-in-compatible rewrite of YARA, and the README says it is the same engine VirusTotal runs in production, scanning billions of files with tens of thousands of rules.

## Caveats

The pages read had no install steps or command examples, the README's rule example is YARA syntax not checked against the yr binary, and compatibility is 99%, so a few rules may behave differently.

## Links

- [Homepage](https://virustotal.github.io/yara-x/)
- [GitHub repository](https://github.com/VirusTotal/yara-x)
- [Getting started docs](https://virustotal.github.io/yara-x/docs/intro/getting-started/)
- [YARA-X vs YARA](https://virustotal.github.io/yara-x/docs/intro/yara-x-vs-yara/)
