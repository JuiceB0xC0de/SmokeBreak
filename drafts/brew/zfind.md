---
name: zfind
title: zfind
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [archives, cli, find, go, quick, sql]
homepage: https://github.com/laktak/zfind
scout_score: 5
status: draft
---

# zfind

**TLDR;** A file finder where you write the filter as a SQL WHERE clause, and it searches inside tar, zip, 7z and rar archives as if they were folders.

zfind is a small Go program that does one job: you hand it a filter written the way you would write the WHERE half of a SQL query, and it prints the files that match. Each file, and each entry inside a supported archive, is treated like a row with properties such as name, path, size, date, time, ext, type and archive. So `size between 1M and 1G` or `ext in ("jpg","jpeg")` mean what you would expect.

The stated reason it exists is simple. In the README's words, "if you know SQL, you don't have to learn or remember any new syntax just for this tool." The find command's own expression language is something many people re-learn every time, and zfind swaps it for a syntax a lot of developers already know. It also supports LIKE with % wildcards and RLIKE for regular expressions.

The archive part is what makes it more than a syntax swap. zfind reads tar (including gz, bz2 and xz), zip, 7z and rar directly, so one query can cover loose files and files buried inside old backups, without extracting anything. A query like `date<"2010" and archive="tar"` goes looking inside tarballs.

It deliberately does not do find-style actions. Output can be a plain list, a long listing with -l, or CSV, or NUL-separated with -0, and you pipe that into xargs or whatever else you like.

## Install

```
brew install zfind
```

## Try this

```
zfind 'size<10k'
```
Lists files under 10KB in the current path, including entries inside any archives it meets.

```
zfind 'date<"2010" and archive="tar"'
```
Finds files last modified before 2010 that live inside tar archives.

```
zfind --no-archive 'name like "%.txt"' -0 | xargs -0 -L1 echo
```
Skips archives, emits NUL-separated paths of .txt files and hands each one to echo via xargs, the README's pattern for acting on results.

## What's unique

Archive contents show up as ordinary rows under the same WHERE syntax, so one query spans loose files and files inside tar, zip, 7z and rar. Plain find cannot do that.

## Caveats

Searching inside archives means reading them, which is slow on large files, and even 'not archive' in a query still opens them; some README examples also have stray quote typos, so copy from the working ones.

## Links

- [Homepage (GitHub repo)](https://github.com/laktak/zfind)
- [Releases](https://github.com/laktak/zfind/releases)
- [Go package docs for filter](https://pkg.go.dev/github.com/laktak/zfind/filter)
