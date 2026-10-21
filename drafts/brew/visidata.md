---
name: visidata
title: VisiData
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [csv, data, python, quick, spreadsheet, tui]
homepage: https://www.visidata.org/
scout_score: 7
status: draft
---

# VisiData

**TLDR;** A terminal spreadsheet that opens CSV, JSON, SQLite, Excel and more as an interactive grid, with histograms, scatterplots and Python per row.

VisiData opens tabular data in an interactive grid in the terminal. Point it at a file with `vd <input>`, or pipe the output of another command into it with `<command> | vd`. It reads a long list of formats, including CSV, TSV, JSON and JSON-Lines, SQLite, Excel, HDF5, HTML, YAML, Markdown, and git repositories according to the homepage. Python can be computed for each row.

The homepage describes it as an open-source data multitool that combines "the clarity of a spreadsheet, the efficiency of the terminal, and the power of Python" in a lightweight utility that can handle millions of rows. Its own one-line pitch is "an interactive multitool for tabular data."

The idea underneath is that a lot of things are tables if you look at them the right way: a directory listing, command output, an API response, a database. Once they are in a grid, the same few moves apply everywhere: sort, filter, pivot, summarise a column as an instant histogram, or draw a scatterplot in the terminal. The homepage also mentions saved sessions that can be replayed, and a batch mode (`vd -b input.csv`) for scripted pipelines.

The README says hundreds of commands and options exist beyond what it lists. Press Ctrl+H inside vd for the quick reference, and Ctrl+Q quits.

## Install

```
brew install visidata
# Some formats need extra Python packages (e.g. openpyxl and lxml for Excel). If vd says 'package X not installed', check that vd and the package share an environment (`which vd`).
```

## Try this

```
vd <input>
```
Opens a file, such as a CSV or JSON file, as an interactive grid you can move around in.

```
<command> | vd
```
Pipes another command's output into the grid so you can sort and explore it.

```
vd --help
```
Lists the command-line options; inside the app, Ctrl+H opens the quick reference.

## What's unique

It covers a very wide range of formats and data shapes in one terminal tool, with built-in plotting and Python-per-row computation. Its depth is discoverable from inside the app.

## Caveats

Windows is not supported natively and needs WSL or MSYS2, and some formats need extra optional Python packages.

## Links

- [Homepage](https://www.visidata.org/)
- [Documentation](https://visidata.org/docs)
- [Quick reference (also Ctrl+H inside vd)](https://visidata.org/man)
- [Intro to VisiData tutorial by Jeremy Singer-Vine](https://jsvine.github.io/intro-to-visidata/)
