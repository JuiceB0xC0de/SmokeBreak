---
name: cdsclient
title: cdsclient
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, astronomy, catalogues, cli, network, science]
homepage: https://cdsarc.cds.unistra.fr/doc/cdsclient.html
scout_score: 5
status: draft
---

# cdsclient

**TLDR;** Command-line clients for the CDS astronomy archives in Strasbourg: pipe in sky coordinates, get back stars and sources from professional surveys.

cdsclient is a package of C and shell programs that query astronomical databases hosted at CDS (Strasbourg) or its mirrors. You give it sky positions or catalogue names, and it returns matching rows as ASCII, HTML, TSV, XML, VOTable or FITS. The generic tool is `vizquery`, which asks VizieR over HTTP. `find_cats` batch-matches a list of positions against several surveys at once.

Most of the executables are per-survey commands: `findgsc`, `findpmm`, `find2mass`, `findwise`, `finducac3` and dozens more. The README says these exist because they connect straight to one very large survey (107 or more rows) and so run faster than the generic `vizquery`, which "has to locate and transport the data via data-base queries". You feed a file of centres on stdin, set a radius in arcminutes, and get back the objects inside it.

The idea underneath is that professional sky surveys are public, and a catalogue of hundreds of millions of stars can be treated like a Unix filter. Coordinates go in, rows come out, with no web form or API script in between. A few tools also cover bibliography: `simbib` searches SIMBAD references, and `catcat` prints a catalogue's ReadMe so you can learn what the columns mean.

The package is old. The documentation page is dated 2009 and its program list runs to about 2015, so some of the surveys may no longer be served. The clients still show how astronomers query these archives.

## Install

```
brew install cdsclient
# Needs network access to CDS servers: port 1660 by default. If it is blocked, set CDSCLIENT=http to use port 80. No account or API key is mentioned.
```

## Try this

```
findgsc -help
```
Lists the basic options for the Guide Star Catalog query program. The README says most programs in the package accept -help.

```
findgsc - -r 5 < mycenters
```
Reads sky positions from the file mycenters and prints GSC stars within 5 arcminutes of each one.

```
simbib 1990 white dwarf X-ray
```
Retrieves SIMBAD bibliographic references from 1990 onward that match white, dwarf and X-ray.

## What's unique

It is a Unix-filter front door to professional astronomy archives, with one small command per survey. Coordinates go in on stdin and matches come out, with no web forms.

## Caveats

The documentation is dated 2009 with a program list to about 2015, many surveys are historical and may no longer be served, and the README mentions only Unix and Linux.

## Links

- [cdsclient documentation (homepage)](https://cdsarc.cds.unistra.fr/doc/cdsclient.html)
- [cdsclient source tarball](http://cdsarc.cds.unistra.fr/ftp/pub/sw/cdsclient.tar.gz)
