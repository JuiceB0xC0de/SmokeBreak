---
name: recutils
title: recutils
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, csv, database, gnu, plain-text, query-language]
homepage: https://www.gnu.org/software/recutils/
scout_score: 6
status: draft
---

# recutils

**TLDR;** GNU recutils turns plain text files into typed, queryable databases you can still edit by hand in any editor.

GNU Recutils is a set of tools and a C library for working with what it calls recfiles: "human-editable, plain text databases." A recfile is a sequence of records, and each record holds "an arbitrary number of named fields." There is no server and no binary store. The data is a text file, so any editor can change it and ordinary tools like diff and version control can track it.

On top of that plain text sits much of what you would expect from a real database. Fields can have types, such as integer, real and date, or user-defined types based on regular expressions. Constraints can mark fields as mandatory or unique. The tools support joins, grouping, sorting and aggregate functions, and individual fields can be encrypted with a password using AES.

The package installs a small family of commands: recsel, recins, recdel and recset for selecting, inserting, deleting and changing records, recinf for describing a file, recfix for checking it, and recfmt for report templates. csv2rec and rec2csv convert to and from CSV. Editor support exists for Vim and Emacs.

The idea underneath is that a database does not have to hide its data. If the file format is simple enough to read and write by hand, you can keep structure and validation without giving up the text file. It is a good door into thinking about what a small personal database could look like.

## Install

```
brew install recutils
```

## Try this

```
recsel --help
```
Lists the options for the query tool, the main way to select records from a recfile.

```
recinf --help
```
Shows how to ask for a description of the record types in a recfile.

```
csv2rec --help
```
Shows how to convert a CSV file into recfile format, a quick way to get existing data into it.

## What's unique

Most databases want a server or a binary store. This one keeps the data as hand-editable text and still offers typed fields, constraints, joins, aggregates and field-level encryption.

## Caveats

The pages the brief draws on contain no command examples, so you will be working from the manual and --help output, and the homepage still mentions freenode IRC, which may be out of date.

## Links

- [GNU Recutils homepage](https://www.gnu.org/software/recutils/)
- [GNU Recutils Manual (download index)](https://www.gnu.org/software/recutils/manual/)
