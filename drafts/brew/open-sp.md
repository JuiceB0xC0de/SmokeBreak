---
name: open-sp
title: OpenSP
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, dsssl, markup, parser, sgml]
homepage: https://openjade.sourceforge.net/
scout_score: 5
status: draft
---

# OpenSP

**TLDR;** OpenSP is James Clark's SGML parser suite, the old pre-XML markup toolkit, installed as onsgmls, osx and a few other small tools.

OpenSP is the parsing half of the OpenJade project. The homepage describes OpenJade as a community effort to maintain Jade, James Clark's implementation of DSSSL, "as well as the related SP suite of SGML/XML processing tools." OpenSP is that SP suite. The page names 1.5.1 as the latest stable release.

SGML is the standard generalized markup language, the older and far more elaborate ancestor of XML and HTML. DSSSL, the Document Style Semantics and Specification Language, is an ISO standard for formatting SGML and XML documents. The homepage calls it a stylesheet language for that purpose. Jade implements it, and SP does the parsing underneath.

The formula installs six executables: onsgmls, osgmlnorm, ospam, ospcat, ospent and osx. The homepage does not say what each one reads or writes, so this entry does not guess beyond the names. The name onsgmls suggests a parser that checks and reports on SGML documents, and osx suggests conversion to XML, but those are inferences. The --help output is the place to confirm.

The door here is history. Before XML simplified things, SGML was how serious documentation was marked up, and many of XML's rules exist as reactions to it. Running a real SGML parser shows what was cut and why.

## Install

```
brew install open-sp
```

## Try this

```
onsgmls --help
```
Prints the usage and options of the SGML parser, the best starting point for learning what it accepts.

```
osx --help
```
Prints the usage of the osx tool, so you can see what it reads and writes.

```
ospcat --help
```
Prints the usage of ospcat, another tool in the suite.

## What's unique

It is a working parser from the original SGML and DSSSL era, written by the person behind Jade. Few current tools let you run real SGML rather than XML.

## Caveats

The homepage is the OpenJade page rather than an OpenSP one, gives no release dates, and does not document the individual commands, so expect to learn them from the help output.

## Links

- [OpenJade distribution homepage](https://openjade.sourceforge.net/)
