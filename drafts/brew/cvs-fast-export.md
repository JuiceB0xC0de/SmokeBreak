---
name: cvs-fast-export
title: cvs-fast-export
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, ancient, cvs, git, history, migration, version-control]
homepage: http://www.catb.org/~esr/cvs-fast-export/
scout_score: 5
status: draft
---

# cvs-fast-export

**TLDR;** Reads decades-old CVS or RCS history and rewrites it as a Git fast-import stream, rebuilding the changesets CVS never recorded.

cvs-fast-export reads RCS files, or a CVS repository's directories of `,v` master files, and writes a Git fast-import stream to standard output. CVS tracked history one file at a time and never recorded which changes belonged together. The tool has to infer that, then emit the result as ordered commits and tags that Git can ingest.

It groups per-file revisions into changesets in two ways. If the revisions share a commitid, they go together. If they do not, it matches on identical author, comment and date within a time-fuzz window, 300 seconds by default. Tags become lightweight Git tags, HEAD is renamed to master, and `.cvsignore` files become `.gitignore`. When history is ambiguous it warns rather than guessing. The man page's own words: "there be dragons."

The underlying idea is version-control archaeology. A history format from before Git carries assumptions that have to be reconstructed, such as clock skew, vendor branches and missing metadata. The author, Eric S. Raymond, treats this tool as the first stage of a conversion. The man page says it is best used with reposurgeon, because plain conversions contain fossils that reposurgeon is good at cleaning up.

Two companions ship with it. `cvssync` mirrors the master files from a remote CVS host, and `cvsconvert` runs a trial conversion and checks it against the original. It can also emit a DOT graph of the commit DAG for graphviz.

## Install

```
brew install cvs-fast-export
```

## Try this

```
cvssync anonymous@cvs.savannah.gnu.org:/sources/groff groff
```
Mirrors the groff CVS master files from a remote host into a local directory named groff.

```
find groff | cvs-fast-export >groff.fi
```
Converts the fetched groff masters into a fast-import stream in groff.fi.

```
cvs-fast-export --help
```
Lists the options, including the author map and the graph output.

## What's unique

It groups changesets only by commitid or by matching metadata within a time window, and warns about ambiguity instead of guessing. It is designed to hand off to reposurgeon.

## Caveats

Vendor branches can produce wrong output, history from CVS older than 1.12 can be misordered by clock skew, memory use grows with repository size, and nothing in the docs mentions Windows support.

## Links

- [Homepage (resource page for 2.6)](http://www.catb.org/~esr/cvs-fast-export/)
- [Man page / documentation](http://www.catb.org/~esr/cvs-fast-export/cvs-fast-export.html)
- [Source repository on GitLab](https://gitlab.com/esr/cvs-fast-export)
