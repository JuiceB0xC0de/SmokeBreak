---
name: ledger
title: ledger
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [accounting, afternoon, cli, double-entry, plain-text]
homepage: https://ledger-cli.org/
scout_score: 5
status: draft
---

# ledger

**TLDR;** A command-line double-entry accounting tool that reads a plain-text journal you write by hand and turns it into balances, registers and reports.

Ledger reads a text file of transactions that you type yourself, in an editor, and answers questions about it from the command line. There is no database and no GUI. The journal is the source of truth, and the program only reads it and reports.

The idea underneath it is double-entry bookkeeping. Every transaction moves an amount from one account to another, and the postings in each transaction must sum to zero. That one constraint catches mistakes and lets you model money, but also time, commodities and anything else you want to count.

Because the data is plain text, it works with version control, grep and diff, and it outlasts any app. The tool is also a door into a whole small ecosystem of plain-text accounting, with related tools that read similar formats.

The brief for this entry was empty, so the details of the journal syntax and report commands are best taken from the project's own documentation.

## Install

```
brew install ledger
```

## Try this

```
ledger --help
```
Prints the list of options and commands, a first look at what reports it can produce.

## What's unique

Your books are a text file you can read, edit and diff, and the program just queries them. It is one of the originals of the plain-text accounting approach.

## Caveats

It needs you to learn the journal format and to enter transactions yourself, and the brief gave no status or maintenance details.

## Links

- [Homepage](https://ledger-cli.org/)
