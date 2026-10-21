---
name: regipy
title: regipy
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, file-formats, forensics, python, registry, windows]
homepage: https://github.com/mkorman90/regipy
scout_score: 5
status: draft
---

# regipy

**TLDR;** Parses offline Windows registry hive files from the command line, dumping them to JSON, diffing them, and running forensic plugins without needing Windows.

Regipy is a Python library with a set of command-line tools for reading Windows registry hives: the binary REGF files such as SYSTEM, NTUSER.DAT and amcache.hve. You point it at a hive file, optionally with its transaction logs, and it gives back JSON, a timeline, a CSV diff, a recovered hive, or plugin results.

The registry is one of the places Windows keeps a record of what a machine has done: which programs ran, what persists across logins, what the computer is called. Most developers never see it as a file format. Here it is just a structured binary file you can open on any machine and walk with calls like `get_key`, `iter_subkeys` and `recurse_subkeys`.

A plugin system sits on top. Regipy detects the hive type, then runs the relevant plugins to pull out artifacts such as amcache, shimcache, computer name, BAM, and Run-key persistence entries. Transaction-log handling is the other notable piece: a hive that was not cleanly closed can hold changes only in its logs, and the tools can apply those logs to produce a recovered hive before you compare or dump anything.

The parser is pure Python by default, built on the construct library. There is also an alpha Rust backend, regipy-rs, with the same API under `regipy.registry_rs`.

## Install

```
brew install regipy
# Needs Python. You also need a registry hive file to parse (SYSTEM, NTUSER.DAT, etc.). The README's PyPI route is `pip install regipy[full]`, which needs compilation tools.
```

## Try this

```
regipy-parse-header ~/Documents/TestEvidence/Registry/SYSTEM
```
Prints the REGF header fields of the hive and warns if it is not clean and needs transaction logs applied.

```
regipy-plugins-run ~/Documents/TestEvidence/Registry/SYSTEM -o /tmp/plugins_output.json
```
Detects the hive type, runs the relevant plugins, and writes the extracted artifacts to JSON.

```
regipy-diff NTUSER.dat NTUSER_modified.dat -o /tmp/diff.csv
```
Compares two hives of the same type and writes the differences to a CSV file.

## What's unique

Beyond reading hives, it recovers dirty ones by applying transaction logs and ships forensic plugins that run based on detected hive type. The alpha Rust backend claims 1:1 parity with the Python parser, a self-reported figure.

## Caveats

You need hive files to look at, ideally from a test image or your own machine, and the [full] pip extra can be slow to install; the Rust backend is alpha and its benchmark claims are the project's own.

## Links

- [Homepage / GitHub repository](https://github.com/mkorman90/regipy)
- [Plugins documentation](https://github.com/mkorman90/regipy/blob/HEAD/docs/PLUGINS.md)
- [regipy-rs on PyPI (Rust backend)](https://pypi.org/project/regipy-rs/)
